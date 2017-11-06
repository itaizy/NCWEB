import logging

import os
import sys
import json
import random
import time
import requests
from datetime import datetime
from datetime import timedelta

from django.db.models import Q

from django.core import serializers

from django.core.paginator import Paginator
from django.db import connection
from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django import forms
from common.utils import json_response



# Create your views here.
from django.db.models import Count
from NetworkCenterWEB.models import IhomeComplain
from NetworkCenterWEB.models import IhomeDoing
from NetworkCenterWEB.models import MoodlensRealtime


#from common.utils import json_response
#from home.models import Protocol, Website, Device

logger = logging.getLogger(__name__)

#periodInt = 7;
intPeriod = 30;

intPeriod2 = 30;

intTimeNowBeforeOneWeek = int(time.time()) - intPeriod*60*60*24;
intTimeNowBeforeO2Week = int(time.time()) - intPeriod2*60*60*24;

def _update_one_week():
    intTimeNowBeforeOneWeek = int(time.time()) - intPeriod*60*60*24;

def _update_two_week():
    intTimeNowBeforeO2Week = int(time.time()) - intPeriod2*60*60*24;


#SQLMap = 'SELECT B.sourcearea FROM ihome_complain A, ihome_baseprofile B WHERE A.UID = B.UID and A.addtime > ' + str(intTimeNowBeforeOneWeek)
SQLMap = 'SELECT B.sourcearea FROM ihome_complain A, ihome_baseprofile B WHERE A.UID = B.UID'
SQLstat = 'SELECT atdepartment, count(*) as num from ihome_complain where addtime > ' + str(intTimeNowBeforeOneWeek) + ' group by atdepartment order by num desc limit 10;'
SQLtrend = 'SELECT id, (replytime - addtime) as kk from ihome_complain where replytime > addtime and addtime > ' + str(intTimeNowBeforeOneWeek) + ' order by kk desc;'
SQLsentiment = 'SELECT * from (select end as time, sentiment, count from moodlens_realtime order by end desc limit 45) aa order by time;'
SQLactive = 'select dateline,ip,replynum from ihome_doing where dateline > ' + str(intTimeNowBeforeO2Week);

def _my_execuse_query_sql(SQLMap):
    from django.db import connection, transaction
    cursor = connection.cursor()

    # 数据修改操作——提交要求
    #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    #transaction.commit_unless_managed()

    # 数据检索操作,不需要提交
    cursor.execute(SQLMap)
    row = cursor.fetchall()

    return row

def ncbig(request):
    '''
    默认html
    :param request:
    :return:
    '''
    return render_to_response('big.html')

def detail(request):
    '''
    默认html
    :param request:
    :return:
    '''
    return render_to_response('detail.html')

def _deleteAt(str):
    str = str.replace('&nbsp;','')
    if '</a>' in str and '<a' in str:
        left = str.index('<a')
        right = str.index('</a>')
        if left == -1 or right == -1:
            return str
        else:
            tmp = str[:left]
            return _deleteAt(tmp + str[right + 4:])
    return str

def getHotMomentsFromGrid(request):
    '''
    静态文件返回：近一周未解决诉求
    :param request:
    :return:
    '''

    querydata = IhomeComplain.objects.filter(isreply='0', addtime__gt=intTimeNowBeforeOneWeek).values("id", "message", "addtime", "expire", "atdepartment").order_by('-addtime')[0:10]

    #print('********************************************')
    res_list = []
    for one in querydata:
        if '</a>' in one['message']:
    #        print('~~~~~~~~~~~~~~~' + one['message'])
            one['message'] = _deleteAt(one['message'])
        res_list.append(one)
    #    print(one)
    #print('********************************************')






    # json_msg = {'result' : serializers.serialize("json", querydata)}

    # json_msg = serializers.serialize("json", querydata)

    json_msg = {'result' : res_list}

    # json_msg = {
    #     'result' : [
    #         {"id":"3062","pass":0,"accept":0,"createby":"146473","createdt":"2017-07-07 19:34:35","createdtfix":1499427275,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市","content":"发现废弃地毯后及时清理","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/5a648bd5a99c98ed405f8f86ad61747e.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/8ed5acd9a9f881c8436e7bda93579b3b.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/d5769bd5f1b8b89e64451223162bb91e.jpg.600x600.jpg\"]","sol_content":"经社区积极协调，漏水点找到并修好，恢复了地面。","sol_img_arr":"[]","flag":0},
    #         {"id":"3061","pass":0,"accept":0,"createby":"146476","createdt":"2017-07-07 19:19:07","createdtfix":1499426347,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市-新河里小区","content":"新兴里网格员巡视中发现废弃护栏！已清理","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/0eb91b8392551684939ed676f7eec518.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/37f44d40acd375e50a106939c4ffc372.jpeg.600x600.jpeg\"]","sol_content":"经社区积极协调，漏水点找到并修好，恢复了地面。","sol_img_arr":"[]","flag":0},
    #         {"id":"3060","pass":0,"accept":0,"createby":"146476","createdt":"2017-07-07 19:12:31","createdtfix":1499425951,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市-新河里小区","content":"新兴里网格员在巡视中发现楼门口房檐上有杂物！已清理","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/ea8bea73bb2b801b1f4272794e2ea9c5.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/d6bfac50e33f38461ad838a677918726.jpeg.600x600.jpeg\"]","sol_content":"经社区积极协调，漏水点找到并修好，恢复了地面。","sol_img_arr":"[]","flag":0},
    #         {"id":"102","pass":0,"accept":1,"createby":"37758","createdt":"2017-02-24 14:37:00","createdtfix":1487918220,"acceptby":"37759","acceptdt":"2017-03-15 20:57:54","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市和平区碧云里","content":"反映楼内邻居有杂物要求清理","types":10,"hot":0,"img_arr":"[]","sol_content":"null","sol_img_arr":"null","flag":1},
    #         {"id":"3059","pass":0,"accept":0,"createby":"146474","createdt":"2017-07-07 17:44:07","createdtfix":1499420647,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市","content":"朝阳里网格员在巡视当中，发现新河里44门前，有居民丢弃的旧家具。而后几名网格员冒着下午燃热酷暑，顶着烈日炎炎，衣服都被汗水打透了。一趟趟将旧家具清理到堆放点。","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/4f115ffeb06a9df94c98df69c09c6545.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/b433d4f8281b0800e6d5f55540595159.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/36ca9b43b09523d091c29702b8a334d3.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/2ad63d3e5500651adbbcc10a97c31268.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/b5f543d2e6a54ed5e20bda603235f55a.jpg.600x600.jpg\"]","sol_content":"经社区积极协调，漏水点找到并修好，恢复了地面。","sol_img_arr":"[]","flag":0},
    #         {"id":"103","pass":0,"accept":0,"createby":"37758","createdt":"2017-02-27 14:37:00","createdtfix":1488177420,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市和平区碧云里一号楼","content":"楼门内堆物","types":10,"hot":0,"img_arr":"[]","sol_content":"null","sol_img_arr":"null","flag":1},
    #         {"id":"91","pass":0,"accept":1,"createby":"37758","createdt":"2017-03-14 09:01:00","createdtfix":1489453260,"acceptby":"37759","acceptdt":"2017-03-15 21:00:07","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市和平区营口道116号","content":"居民到社区咨询如何办理低保","types":21,"hot":0,"img_arr":"[]","sol_content":"null","sol_img_arr":"null","flag":1},
    #         {"id":"89","pass":0,"accept":0,"createby":"37758","createdt":"2017-03-15 10:01:00","createdtfix":1489543260,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市和平区山东路123号","content":"居民反映地沟堵塞，影响正常生活","types":10,"hot":0,"img_arr":"[]","sol_content":"社区了解情况后，找到麻辣烫老板将情况说明，老板表示进行厨房改造，保证不影响居民生活","sol_img_arr":"[]","flag":1},
    #         {"id":"3058","pass":0,"accept":0,"createby":"146472","createdt":"2017-07-07 17:41:54","createdtfix":1499420514,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市","content":"在网格巡视中发现有居民的堆物  已清理完毕","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/b031249807193b5b7cc763ece2c73ae6.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/c15e85c7157605fcb305c117b7d74fcf.jpg.600x600.jpg\"]","sol_content":"经社区积极协调，漏水点找到并修好，恢复了地面。","sol_img_arr":"[]","flag":0},
    #         {"id":"3056","pass":0,"accept":0,"createby":"146472","createdt":"2017-07-07 17:37:48","createdtfix":1499420268,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市","content":"朝阳里社区网格员在巡视中发现废旧废旧木凳  现已清理","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/8175caa66a024d6e56c521892a7b75bc.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/26c6a00547b515c21aa4817061627e34.jpg.600x600.jpg\"]","sol_content":"已处理","sol_img_arr":"[]","flag":0},
    #         {"id":"3055","pass":0,"accept":0,"createby":"146157","createdt":"2017-07-07 17:27:26","createdtfix":1499419646,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市-绵阳道菜市场","content":"社区网格员巡视社区，发现地面有喷涂的小广告，网格员使用灰色喷漆进行覆盖。","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/ae7218fc3686cdfa5b79de5e0e018cf0.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/95af383f6eefc9c4ce9de184e4b73d48.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/c2f9e035ee98f4732576a66786696c1a.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/488a1377f7bdf7d3b1bceb6ad70f100d.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/dd46498a70294b5b43815e5a3d5a6619.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/480964f5e2983a87cb035dc3f51ce804.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/a7522638d6305f755dbc1cbcf55d6a30.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/fa16f64d13745003998f4b58cd31882d.jpeg.600x600.jpeg\"]","sol_content":"已处理","sol_img_arr":"[]","flag":0},
    #         {"id":"97","pass":0,"accept":1,"createby":"37758","createdt":"2017-03-15 14:36:00","createdtfix":1489559760,"acceptby":"37759","acceptdt":"2017-03-15 20:59:15","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市和平区哈尔滨道40号","content":"网格员在巡视中发现，哈尔滨道40号二楼居民装修，工程土堆放在楼下影响居民出行","types":10,"hot":0,"img_arr":"[]","sol_content":"卫生主任了解情况后，及时找到保洁队进行了清理，并告知租户不要在捡拾垃圾堆放。","sol_img_arr":"[]","flag":1},
    #         {"id":"3043","pass":0,"accept":0,"createby":"146260","createdt":"2017-07-07 16:09:02","createdtfix":1499414942,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市-麦购休闲广场","content":"网格员巡查时发现清河南里胡同口放无主床板，网格员及时联系保洁员处理。","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/57e013aa84423a6bd2e24aae58c5a398.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/b31043669e5aa2f38c96496cf9f04d1a.jpeg.600x600.jpeg\"]","sol_content":"已完成","sol_img_arr":"[]","flag":0},
    #         {"id":"95","pass":0,"accept":0,"createby":"37758","createdt":"2017-03-15 15:35:00","createdtfix":1489563300,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市和平区马场道20号","content":"马场道20号有枯枝，联系保洁队清理","types":10,"hot":0,"img_arr":"[]","sol_content":"卫生主任了解情况后，及时找到保洁队进行了清理，并告知租户不要在捡拾垃圾堆放。","sol_img_arr":"[]","flag":1},{"id":"96","pass":0,"accept":1,"createby":"37758","createdt":"2017-03-15 15:35:01","createdtfix":1489563301,"acceptby":"37759","acceptdt":"2017-03-15 20:59:11","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市和平区新三多里","content":"消杀公司要在居民家中布置粘蟑板，监控蟑螂情况，帮助联系居民，去家中布置。","types":10,"hot":0,"img_arr":"[]","sol_content":"卫生主任了解情况后，及时找到保洁队进行了清理，并告知租户不要在捡拾垃圾堆放。","sol_img_arr":"[]","flag":1},
    #         {"id":"3036","pass":0,"accept":0,"createby":"146272","createdt":"2017-07-07 14:45:43","createdtfix":1499409943,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"中国天津市和平区哈密道40号","content":"劝业场街新津社区网格员在巡视社区时发现沈阳道与辽宁路交口处有一个垃圾桶外溢并倒地，网格员及时联系保洁公司和保洁人员一起将垃圾桶扶起，已处理完毕。","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/34e8b05d5fc78e6d3f5a4a1180ca541e.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/338023bd27208af355e8215663b7ad47.jpg.600x600.jpg\"]","sol_content":"已处理","sol_img_arr":"[]","flag":0},
    #         {"id":"3033","pass":0,"accept":0,"createby":"111057","createdt":"2017-07-07 11:18:47","createdtfix":1499397527,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"中国天津市和平区鞍山道168号","content":"为大力培育和践行社会主义核心价值观，教育引导社区未成年人爱祖国、爱人民、爱劳动、爱学习、爱社会主义，充分发挥“快乐营地”以乐促智、以技促能、以读养德的功能，不断丰富社区未成年人暑假生活，促进未成年人健康成长全面发展，2017年7月7日上午，文化村社区暑期“快乐营地”正式开营。","types":1,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/ed73a13a8d3553f16e0a73c20fa8589e.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/8be920aec5815be9d9e1f78b8ec92c00.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/4e05e6ba46ed9b3e19bfb43707e2341f.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/c0a5349858db94f8924294fd710905dc.jpg.600x600.jpg\"]","sol_content":"已完成","sol_img_arr":"[]","flag":0},
    #         {"id":"3014","pass":0,"accept":0,"createby":"96311","createdt":"2017-07-06 10:11:22","createdtfix":1499307082,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市-复元里","content":"“三创”期间入户宣传，提升社区居民对“三创”工作的认知度。","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/06/ff1cfeeb7b8486bb2c0fe054f69e55c5.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/06/b83643449e69337e02dcc09ba57bcfa8.jpeg.600x600.jpeg\"]","sol_content":"已联系街保洁队清除","sol_img_arr":"[]","flag":0},
    #         {"id":"3011","pass":0,"accept":0,"createby":"107398","createdt":"2017-07-06 09:54:51","createdtfix":1499306091,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"中国天津市和平区哈密道138号","content":"&quot;监察机关对监察对象执法、廉政、效能情况进行监察，履行下列职责：\n\n&quot;（一）检查国家行政机关在遵守和执行法律、法规和人民政府的决定、命令中的问题；\n\n&quot;（二）受理对国家行政机关及其公务员和国家行政机关任命的其他人员违反行政纪律行为的控告、检举；\n\n&quot;（三）调查处理国家行政机关及其公务员和国家行政机关任命的其他人员违反行政纪律的行为；\n\n&quot;（四）受理国家行政机关公务员和国家行政机关任命的其他人员不服主管行政机关给予处分决定的申诉，以及法律、行政法规规定的其他由监察机关受理的申诉；\n\n&quot;（五）法律、行政法规规定由监察机关履行的其他职责。&quot;\n\n增加一款，作为第二款：&quot;监察机关按照国务院的规定，组织协调、检查指导政务公开工作和纠正损害群众利益的不正之风工作。&quot;","types":10,"hot":0,"img_arr":"[]","sol_content":"null","sol_img_arr":"null","flag":0},
    #         {"id":"2969","pass":0,"accept":0,"createby":"104299","createdt":"2017-07-05 15:17:08","createdtfix":1499239028,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市-粤园","content":"昆明路小学党员教师走进社区，帮助进行清整","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/05/1a50dd7d1247f03ce4a0e4fa40579092.jpeg.600x600.jpeg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/05/68338c37e70b17f39023a1b94e158e0d.jpeg.600x600.jpeg\"]","sol_content":"网格负责人已经告知卫生主任联系保洁队将同康里旧床垫子运走。","sol_img_arr":"[]","flag":0},
    #         {"id":"2955","pass":0,"accept":0,"createby":"108167","createdt":"2017-07-05 09:19:09","createdtfix":1499217549,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"中国天津市和平区气象台路37号-增1","content":"清晨在及时清理商户卷帘门上的残标 。","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/05/d548369ed4790b4f895e41b09430921c.jpg.600x600.jpg\"]","sol_content":"已完成","sol_img_arr":"[]","flag":0},
    #         {"id":"2896","pass":0,"accept":0,"createby":"146151","createdt":"2017-07-04 16:02:05","createdtfix":1499155325,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市","content":"南营门街街道干部及世昌里社区工作者清理世昌里社区某居民家垃圾堆物。","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/04/3fd6d521c724c1b540fbf8671e009524.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/04/eafc7ed3c6ae47153eecda8cae19e7b6.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/04/e59d868206ba796c74210dd651bed8e6.jpg.600x600.jpg\"]","sol_content":"已完成","sol_img_arr":"[]","flag":0}
    #     ]
    # }
    #json_msg = {"id":"3062","pass":0,"accept":0,"createby":"146473","createdt":"2017-07-07 19:34:35","createdtfix":1499427275,"acceptby":"0","acceptdt":"1970-01-01 08:00:00","finishby":"0","finishdt":"1970-01-01 08:00:00","location":"天津市","content":"发现废弃地毯后及时清理","types":10,"hot":0,"img_arr":"[\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/5a648bd5a99c98ed405f8f86ad61747e.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/8ed5acd9a9f881c8436e7bda93579b3b.jpg.600x600.jpg\",\"https://img.dangjianwang.com/img/sets/mobile/2017/07/07/d5769bd5f1b8b89e64451223162bb91e.jpg.600x600.jpg\"]","sol_content":"经社区积极协调，漏水点找到并修好，恢复了地面。","sol_img_arr":"[]","flag":0}

    return json_response(json_msg)


def getPlotMomentStatData(request):

    #print(SQLstat)

    _update_one_week();
    alllocal = _my_execuse_query_sql(SQLstat)

    datay = []
    datax = []

    for onelocal in alllocal:
        datay.append(onelocal[1])
        datax.append(onelocal[0])

    #print(localnum)
    json_msg = {'result' : {'datax' : datax, 'datay' : datay}}

    #print(json_msg)

    # json_msg = {
    #     "0":[5,4,2,3,6,4,2,1,6,2],
    #     "1":[3,4,1,2,4,6,5,2,3,3],
    #     "2":[1,3,5,5,5,3,2,4,2,4],
    #     "3":[2,3,5,2,5,1,2,4,6,5],
    #     "4":[4,2,4,2,5,2,4,3,2,1],
    #     "5":[4,12,7,4,6,3,4,2,1,6],
    #     "type":[10,21,17,5,11,20,13,7,18,24]
    # }
    return json_response(json_msg)

def getPlotMomentTrendData(request):

    _update_one_week();
    alllocal = _my_execuse_query_sql(SQLtrend)

    datainterval = [60*60*1, 60*60*3, 60*60*6, 60*60*12, 60*60*24, 60*60*24*3, 60*60*24*7]
    datax = ['1h', '3h', '6h', '12h', '1d', '3d', '7d']
    datay = [0,0,0,0,0,0,0]

    #print(alllocal)
    for onelocal in alllocal:


        if int(onelocal[1]) < 60*60*24*7:
            i = 1
            while i < 7 and int(onelocal[1]) < datainterval[i - 1]:
                i = i + 1
            datay[i - 1] = datay[i - 1] + 1


    #print(localnum)
    json_msg = {'result' : {'datax' : datax, 'datay' : datay}}

    #print(json_msg)

    return json_response(json_msg)

    # json_msg = {
    #     "avetime":[66.77854820526696,64.05162463076573,64.78414911659108,63.998574133900306,58.73345948241406,63.67083664975071,63.236569583943634,58.90132924859997,64.54492789956467,70.94874744102621,69.0330000720565,73.50048492766796],
    #     "unsolvedcount":[3,1,10,2,5,2,7,2,3,1,9,0],
    #     "count":[33,47,58,55,121,74,77,80,52,19,36,0],
    #     "datearray":["2017-06-28","2017-06-29","2017-06-30","2017-07-01","2017-07-02","2017-07-03","2017-07-04","2017-07-05","2017-07-06","2017-07-07","2017-07-08","2017-07-09"]
    # }
    # return json_response(json_msg)

def getActiveAndCommentDegree(request):
    json_msg = {
        "data_x":["2017-06-08","2017-06-09","2017-06-10","2017-06-11","2017-06-12","2017-06-13","2017-06-14","2017-06-15","2017-06-16","2017-06-17","2017-06-18","2017-06-19","2017-06-20","2017-06-21","2017-06-22","2017-06-23","2017-06-24","2017-06-25","2017-06-26","2017-06-27","2017-06-28","2017-06-29","2017-06-30","2017-07-01","2017-07-02","2017-07-03","2017-07-04","2017-07-05","2017-07-06","2017-07-07","2017-07-08"],
        "data_y1":[356,328,332,37,162,960,5068,2619,625,382,50,217,536,433,437,484,577,257,348,610,605,725,861,1056,460,526,759,809,590,363,278],
        "data_y2":[24,22,23,10,11,9,50,50,33,34,10,19,28,29,23,28,39,20,26,50,26,34,50,50,24,28,37,21,21,24,25]
    }

    d_x = set()
    d_y1 = {}
    d_y2 = {}

    _update_two_week();

    alllocal = _my_execuse_query_sql(SQLactive)
    #print(alllocal)
    for onelocal in alllocal:
        tmp_date = int(int(onelocal[0]/(60*60*24))*(60*60*24))
        if tmp_date not in d_x:
            d_x.add(tmp_date)
            d_y1[tmp_date] = int(onelocal[2]) + 1;
            if onelocal[1].startswith('192.168') or onelocal[1].startswith('10.0'):
                d_y2[tmp_date] = int(onelocal[2]) + 1;
            else:
                d_y2[tmp_date] = 0;
        else:
            d_y1[tmp_date] = d_y1[tmp_date] + int(onelocal[2]) + 1;
            if onelocal[1].startswith('192.168') or onelocal[1].startswith('10.0'):
                d_y2[tmp_date] = d_y2[tmp_date] + int(onelocal[2]) + 1;

    data_x = []
    data_y1 = []
    data_y2 = []
    #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    #print(d_x)
    x_list = list(d_x)
    x_list.sort()
    #print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    #print(x_list)
    for tmp in x_list:
        #print(tmp)
        tmp_time = time.localtime(tmp)
        data_x.append(time.strftime("%Y-%m-%d",tmp_time))
        data_y1.append(d_y1[tmp])
        data_y2.append(d_y2[tmp])

    #print(data_x)
    #print(data_y1)
    #print(data_y2)

    json_msg = {"data_x": data_x, "data_y1":data_y1, "data_y2":data_y2}

    return json_response(json_msg)

def getNewsData(request):

    querydata = IhomeDoing.objects.filter(dateline__gt=intTimeNowBeforeOneWeek).values("doid", "message", "dateline", "fromdevice").order_by('-replynum')[0:10]

    #print('********************************************')
    res_list = []
    for one in querydata:
        if '</a>' in one['message']:
            #        print('~~~~~~~~~~~~~~~' + one['message'])
            one['description'] = _deleteAt(one['message'])
            del one['message']
        else:
            one['description'] = one['message']
            del one['message']
        one['imgurl'] = "/static/images/hotnewslogo.png"
        one['src'] = 'ihome'
        one['time'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(one['dateline']))
        one['eventLoc'] = '北航'
        one['eventType'] = 1
        res_list.append(one)
    #    print(one)
    #print('********************************************')

    json_msg = {'result' : res_list}

    # json_msg = {
    #     'result' : [
    #         {"eventId":"bftjyw033308714","imgurl":"/static/images/hotnewslogo.png","emotion":"0","src":"微信","eventLoc":"北京市","relativity":59,"description":"习近平《在庆祝香港回归祖国二十周年大会暨香港特别行政区第五届政府就职典礼上的讲话》单行本出版 ","eventType":"25","time":"2017-07-07T19:57:00","hot":2291,"url":"http://news.enorth.com.cn/system/2017/07/07/033308714.shtml"},
    #         {"eventId":"bftjyw033304470","imgurl":"/static/images/hotnewslogo.png","emotion":"2","src":"新闻","eventLoc":"湖南省","relativity":56,"description":" 湖南宁乡县遭遇特大严重洪涝灾害 44人死亡失联 ","eventType":"24","time":"2017-07-07T11:18:00","hot":1449,"url":"http://news.enorth.com.cn/system/2017/07/07/033304470.shtml"},
    #         {"eventId":"hbqz1091574","imgurl":"/static/images/hotnewslogo.png","emotion":"0","src":"微信","eventLoc":"北京市","relativity":59,"description":"刘云山出席纪念全民族抗战爆发80周年仪式","eventType":"13","time":"2017-07-08T07:29:00","hot":1992,"url":"http://www.jcqzw.com/ssyw/201707/t20170708_1091574.shtml"},
    #         {"eventId":"bftjyw033309491","imgurl":"/static/images/hotnewslogo.png","emotion":"1","src":"微信","eventLoc":"广东省","relativity":53,"description":" 世界最长跨海大桥:港珠澳大桥主体工程全线贯通 ","eventType":"10","time":"2017-07-08T07:17:00","hot":1883,"url":"http://news.enorth.com.cn/system/2017/07/08/033309491.shtml"},
    #         {"eventId":"bftjyw033309531","imgurl":"/static/images/hotnewslogo.png","emotion":"1","src":"微博","eventLoc":"青海省","relativity":45,"description":" 可可西里申遗成功 入选世界自然遗产名录(组图) ","eventType":"13","time":"2017-07-08T07:41:00","hot":1772,"url":"http://news.enorth.com.cn/system/2017/07/08/033309531.shtml"}
    #     ]
    # }
    return json_response(json_msg)

def getIhomeEmoSource(request):

    startTime = int(time.time()) - 9*(24*60*60)
    emoclass = request.GET.get('emoclass');

    # querydata = MoodlensRealtime.objects.filter(end__gt=startTime).filter(sentiment=int(emoclass)).values("end", "weibos").order_by('-end')
    querydata = MoodlensRealtime.objects.filter(~Q(weibos= '')).filter(sentiment=int(emoclass)).values("end", "weibos").order_by('-end')[0:9]

    print(len(querydata))
    print(querydata)

    #print('********************************************')
    res_list = []
    for one in querydata:
        if '</a>' in one['weibos']:
            #        print('~~~~~~~~~~~~~~~' + one['message'])
            one['description'] = _deleteAt(one['weibos'])
            del one['weibos']
        else:
            one['description'] = one['weibos']
            del one['weibos']
        one['imgurl'] = "/static/images/emoicon" + emoclass + ".png"
        one['src'] = 'ihome'
        one['time'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(one['end']))
        one['eventLoc'] = '北航'
        res_list.append(one)

    json_msg = {'result' : res_list}

    return json_response(json_msg)

def getHotEventsFromEventsTJ(request):
    json_msg = {
        'result' : [
            {"negative":25,"neutral":69,"positive":1,"time":1498262400000},
            {"negative":14,"neutral":68,"positive":13,"time":1498348800000},
            {"negative":20,"neutral":68,"positive":12,"time":1498435200000},
            {"negative":24,"neutral":64,"positive":2,"time":1498521600000},
            {"negative":1,"neutral":64,"positive":24,"time":1498608000000},
            {"negative":15,"neutral":65,"positive":17,"time":1498694400000},
            {"negative":1,"neutral":41,"positive":24,"time":1498780800000},
            {"negative":2,"neutral":52,"positive":4,"time":1498867200000},
            {"negative":6,"neutral":42,"positive":23,"time":1498953600000},
            {"negative":24,"neutral":42,"positive":1,"time":1499040000000},
            {"negative":2,"neutral":42,"positive":4,"time":1499126400000},
            {"negative":2,"neutral":42,"positive":24,"time":1499212800000},
            {"negative":2,"neutral":41,"positive":4,"time":1499299200000},
            {"negative":8,"neutral":41,"positive":17,"time":1499385600000},
            {"negative":1,"neutral":41,"positive":4,"time":1499472000000}
        ]
    }

    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    oneMonthAgo = (str(datetime.now() - timedelta(20)))[:10]
    print(today)
    print(oneMonthAgo)
    url = "http://ring.act.buaa.edu.cn/api/minotor/histEsTableByTimeAndWords"
    para = {"from":oneMonthAgo, "to":today, "tableName":"crawler_all","field":"releasedate", "interval":"day", "words":"北航+北京航空航天大学"}
    header ={}
    r = requests.get(url,params=para,headers= header)
    r_json = r.json()
    print(r_json)
    maxv = 0;
    res = [];
    for k in sorted(r_json.keys()):
        tmpTime = time.strptime(k[:19], "%Y-%m-%dT%H:%M:%S")
        keyListOne = int(time.mktime(tmpTime))
        valueListOne = r_json[k]
        if maxv < valueListOne:
            maxv = valueListOne
        res.append({"negative":0,"neutral":valueListOne,"positive":0,"time":keyListOne*1000})
    maxv = maxv + maxv/20;

    print(res)
    print(maxv)
    json_msg = {'result': res, 'maxValue':maxv}

    return json_response(json_msg)
    # json_msg = {
    #     'result' : [
    #         {"emotion":"1","trend":"0 226 2230","ringId":"bftjyw033266676","location":"天津市","time":"2017-06-30T21:38:00.000Z","type":"4","hot":2230,"title":" 首届世界智能大会6月30日继续在津召开 怀进鹏出席 "},
    #         {"emotion":"1","trend":"37 185 1912","ringId":"rmwtj30408682","location":"天津市","time":"2017-07-02T01:23:00.000Z","type":"7","hot":1912,"title":"天津地铁5号线全线贯通?将在今年年底试运行"},
    #         {"emotion":"0","trend":"18 177 2219","ringId":"bftjyw033279308","location":"天津市","time":"2017-07-03T23:58:00.000Z","type":"25","hot":2219,"title":" 李鸿忠会见农民日报社采访组 "},
    #         {"emotion":"0","trend":"40 100 2135","ringId":"bftjyw033228487","location":"天津市","time":"2017-06-25T12:49:00.000Z","type":"25","hot":2135,"title":"肖怀远带领市人大机关党员干部参观\u201c利剑高悬 警钟长鸣\u201d警示教育主题展 重温入党誓词 不忘初心践行誓言 推动人大机关党建工作 "},
    #         {"emotion":"0","trend":"36 149 2231","ringId":"bftjyw033248076","location":"天津市","time":"2017-06-28T23:39:00.000Z","type":"4","hot":2231,"title":"李鸿忠王东峰怀进鹏与出席世界智能大会企业家代表恳谈 "},
    #         {"emotion":"0","trend":1999,"ringId":"bftjyw033266156","location":"天津市","time":"2017-06-30T13:22:00.000Z","type":"20","hot":1999,"title":"李鸿忠王东峰就天津市第三中心医院恶性伤医事件作出批示 "},
    #         {"emotion":"0","trend":"3 54 1347","ringId":"tjw1170134","location":"天津市","time":"2017-07-02T00:13:00.000Z","type":"13","hot":1347,"title":"2017天津中招招生计划出炉 普通高中招生计划53400个"},
    #         {"emotion":"1","trend":"24 34 1398","ringId":"bftjyw033228518","location":"天津市","time":"2017-06-25T12:49:00.000Z","type":"13","hot":1398,"title":"第三期澳门大学生来津学习交流结业 厚植优秀中华文化 担当津澳友谊使者 "},
    #         {"emotion":"0","trend":"37 138 1673","ringId":"bftjyw033267507","location":"天津市","time":"2017-07-01T01:51:00.000Z","type":"10","hot":1673,"title":"天津环境保护突出问题边督边改第二十三批公开信息 "},
    #         {"emotion":"0","trend":"17 39 1992","ringId":"hbqz1091575","location":"天津市","time":"2017-07-07T23:30:00.000Z","type":"25","hot":1992,"title":"李克强主持经济形势座谈会:更好完成全年目标"},
    #         {"emotion":"0","trend":"3 149 1993","ringId":"bftjyw033308338","location":"天津市","time":"2017-07-07T12:57:00.000Z","type":"25","hot":1993,"title":"王东峰会见法国留尼汪大区议会主席迪迪埃·罗伯特 "},
    #         {"emotion":"2","trend":"15 49 1553","ringId":"bftjyw033228609","location":"天津市","time":"2017-06-25T13:12:00.000Z","type":"10","hot":1553,"title":" 天津环境保护突出问题边督边改第十八批公开信息 "},
    #         {"emotion":"0","trend":"45 135 2231","ringId":"bftjyw033229503","location":"天津市","time":"2017-06-26T00:46:00.000Z","type":"25","hot":2231,"title":" 李鸿忠会见新加坡副总理尚达曼 "},
    #         {"emotion":"1","trend":"3 80 2299","ringId":"bftjyw033294275","location":"天津市","time":"2017-07-05T23:22:00.000Z","type":"25","hot":2299,"title":"李鸿忠：秉持共商共建共享理念 更好造福金砖各国人民 "},
    #         {"emotion":"1","trend":"19 118 2184","ringId":"bftjyw033293003","location":"天津市","time":"2017-07-05T13:42:00.000Z","type":"10","hot":2184,"title":"王东峰：深入推进城市综合整治 为全运会创造良好环境 "},
    #         {"emotion":"0","trend":"20 140 2197","ringId":"bftjyw033309822","location":"天津市","time":"2017-07-08T01:01:00.000Z","type":"25","hot":2197,"title":" 李鸿忠王东峰会见韩国SK集团会长崔泰源 "},
    #         {"emotion":"0","trend":"36 88 1670","ringId":"bfqxlm033229218","location":"天津市","time":"2017-06-26T00:26:00.000Z","type":"20","hot":1670,"title":" 天津：创新发展生物医药 推进\u201c健康天津\u201d建设  "},
    #         {"emotion":"0","trend":"3 200 1551","ringId":"TJWMS1170415","location":"天津市","time":"2017-07-03T00:50:00.000Z","type":"13","hot":1551,"title":"中考：市内六区考生普通高中志愿最少报两个区"},
    #         {"emotion":"0","trend":"34 222 1229","ringId":"rmwtj30411227","location":"天津市","time":"2017-07-03T00:27:00.000Z","type":"4","hot":1229,"title":"天津出商事制度改革\u201c大招\u201d?企业名称登记与设立登记合并受理"},
    #         {"emotion":"1","trend":"37 18 1223","ringId":"bfqxlm033259217","location":"津南区","time":"2017-06-30T00:22:00.000Z","type":"13","hot":1223,"title":" 津南区迎新合作社提高土地\u201c含金量\u201d  "},
    #         {"emotion":"0","trend":"2 26 1227","ringId":"bfqxlm033279255","location":"津南区","time":"2017-07-03T23:48:00.000Z","type":"17","hot":1227,"title":" 津南司法局开展\u201c绿色全运 法治同行\u201d宣传活动  "},
    #         {"emotion":"0","trend":"31 244 1923","ringId":"bfqxlm033259332","location":"蓟州区","time":"2017-06-30T00:23:00.000Z","type":"11","hot":1723,"title":" 蓟州区：大棚黄瓜清脆爽口 供不应求游客采摘忙  "},
    #         {"emotion":"0","trend":"38 117 1555","ringId":"bfqxlm033235008","location":"河西区","time":"2017-06-26T23:56:00.000Z","type":"25","hot":1555,"title":" 河西区委书记贾凤山到区委网信办调研网信工作  "},
    #         {"emotion":"0","trend":"1 73 2109","ringId":"bftjyw033247140","location":"宝坻区","time":"2017-06-28T13:15:00.000Z","type":"25","hot":2109,"title":" 李鸿忠到宝坻调研并为农村基层党员干部讲党课 "},
    #         {"emotion":"0","trend":"39 10 1126","ringId":"bfqxlm033310942","location":"武清区","time":"2017-07-08T08:00:00.000Z","type":"10","hot":1126,"title":" 武清召开创建全国文明城区社区物业管理推动会  "},
    #         {"emotion":"0","trend":1371,"ringId":"bfqxlm033240879","location":"武清区","time":"2017-06-28T00:17:00.000Z","type":"2","hot":1371,"title":" 武清举行投资环境恳谈会暨项目签约仪式  "},
    #         {"emotion":"0","trend":"9 79 1596","ringId":"bfqxlm033302267","location":"宝坻区","time":"2017-07-06T23:41:00.000Z","type":"1","hot":1596,"title":" 宝坻区基层党建工作重点任务推进会议召开  "},
    #         {"emotion":"1","trend":"2 207 1527","ringId":"rmwtj30408764","location":"宝坻区","time":"2017-07-02T01:39:00.000Z","type":"13","hot":1527,"title":"天津宝坻化育知行推新策?传统文化将走进中小学课堂"},
    #         {"emotion":"1","trend":"31 41 1452","ringId":"bfqxlm033241800","location":"静海区","time":"2017-06-28T01:40:00.000Z","type":"13","hot":1452,"title":" 静海镇春园里社区举办趣味比赛 丰富居民生活  "},
    #         {"emotion":"0","trend":"41 146 1534","ringId":"bfqxlm033279426","location":"东丽区","time":"2017-07-04T00:18:00.000Z","type":"10","hot":1534,"title":" 东丽区加快重点项目建设 展现靓丽市容环境  "},
    #         {"emotion":"0","trend":"47 42 1231","ringId":"bfqxlm033272102","location":"东丽区","time":"2017-07-02T23:58:00.000Z","type":"23","hot":1231,"title":" 东丽食品安全宣传周活动启动 现场解答群众咨询  "},
    #         {"emotion":"0","trend":"48 160 1889","ringId":"bfqxlm033286884","location":"宝坻区","time":"2017-07-05T00:09:00.000Z","type":"7","hot":1889,"title":" 宝坻区：重拳整治交通乱象 净化居民出行环境  "},
    #         {"emotion":"0","trend":"39 199 1392","ringId":"bfqxlm033259161","location":"东丽区","time":"2017-06-30T00:01:00.000Z","type":"25","hot":1392,"title":" 东丽区委部署第二轮巡察工作 抓住重点确保成效  "},
    #         {"emotion":"1","trend":"40 121 1661","ringId":"bfqxlm033287458","location":"东丽区","time":"2017-07-05T00:55:00.000Z","type":"13","hot":1661,"title":" 东丽区文化馆艺术培训班开班 丰富暑期文化生活  "},
    #         {"emotion":"0","trend":"48 171 1433","ringId":"bfqxlm033310996","location":"南开区","time":"2017-07-08T08:20:00.000Z","type":"13","hot":1433,"title":" 南开区成立天津市首个青少年法治教育实践基地  "},
    #         {"emotion":"1","trend":"24 88 1771","ringId":"bfqxlm033248135","location":"和平区","time":"2017-06-28T23:46:00.000Z","type":"2","hot":1771,"title":" 和平2017年招商大会举行 现场签约23个重点项目  "},
    #         {"emotion":"0","trend":"5 195 1792","ringId":"bfqxlm033272085","location":"和平区","time":"2017-07-02T23:54:00.000Z","type":"1","hot":1792,"title":" 和平区委常委会召开会议 服务群众全面从严治党  "},
    #         {"emotion":"0","trend":"33 146 1453","ringId":"bfqxlm033235029","location":"宁河区","time":"2017-06-27T00:05:00.000Z","type":"2","hot":1453,"title":" 宁河区政协经济委员会就电子商务发展进行调研  "},
    #         {"emotion":"0","trend":"19 154 1381","ringId":"bfqxlm033294463","location":"宁河区","time":"2017-07-06T00:02:00.000Z","type":"11","hot":1381,"title":" 宁河区：农夫樱桃正当时 八方来客采摘忙  "},
    #         {"emotion":"0","trend":"33 0 1549","ringId":"bfqxlm033229675","location":"南开区","time":"2017-06-26T01:17:00.000Z","type":"24","hot":1549,"title":" 南开区召开防汛工作紧急会议  "},
    #         {"emotion":"1","trend":"22 92 1771","ringId":"bfqxlm033242791","location":"南开区","time":"2017-06-28T03:05:00.000Z","type":"13","hot":1771,"title":" 南开区万兴街开展\u201c文明童行\u2014\u2014画最美南开\u201d活动  "},
    #         {"emotion":"0","trend":"0 209 1456","ringId":"bfqxlm033248199","location":"西青区","time":"2017-06-29T00:01:00.000Z","type":"24","hot":1456,"title":" 西青区部署消防安全工作 加强督查杜绝事故发生  "},
    #         {"emotion":"0","trend":"37 130 1222","ringId":"bfqxlm033302273","location":"西青区","time":"2017-07-06T23:42:00.000Z","type":"16","hot":1222,"title":" 西青公安创新警务模式 \u201c移动警务站\u201d便民惠民  "},
    #         {"emotion":"0","trend":"23 52 1779","ringId":"bfqxlm033279651","location":"河北区","time":"2017-07-04T00:46:00.000Z","type":"1","hot":1779,"title":" 河北区召开纪念建党96周年座谈会  "},
    #         {"emotion":"2","trend":"26 223 1769","ringId":"TJWMS1170230","location":"西青区","time":"2017-07-02T02:18:00.000Z","type":"18","hot":1769,"title":"西青区原区委书记周家彪接受组织审查"},
    #         {"emotion":"0","trend":"35 209 1771","ringId":"bfqxlm033294560","location":"西青区","time":"2017-07-06T00:19:00.000Z","type":"13","hot":1771,"title":" 西青举办第二届\u201c运河记忆\u201d非遗宣传展示活动  "},
    #         {"emotion":"1","trend":"37 76 1389","ringId":"bfqxlm033229612","location":"河东区","time":"2017-06-26T00:59:00.000Z","type":"10","hot":1389,"title":" 河东区危改广场改造完工 靓丽新颜迎市民  "},
    #         {"emotion":"0","trend":"32 53 1131","ringId":"bfqxlm033235425","location":"河北区","time":"2017-06-27T00:57:00.000Z","type":"20","hot":1131,"title":" 河北区家庭医生签约服务工作稳步推进  "},
    #         {"emotion":"0","trend":"48 230 1892","ringId":"bfqxlm033235312","location":"河东区","time":"2017-06-27T00:39:00.000Z","type":"7","hot":1892,"title":" 河东开展交通大整治 解决停车难停车乱问题  "},
    #         {"emotion":"2","trend":"4 163 1297","ringId":"bfqxlm033248279","location":"河东区","time":"2017-06-29T00:33:00.000Z","type":"10","hot":1297,"title":" 河东区新东方家园前违章建筑拆除  "},
    #         {"emotion":"0","trend":"19 152 1291","ringId":"bfqxlm033286956","location":"河东区","time":"2017-07-05T00:22:00.000Z","type":"7","hot":1291,"title":" 河东区10条道路实施沿街立面整修  "},
    #         {"emotion":"0","trend":"36 163 1522","ringId":"bfqxlm033295022","location":"河东区","time":"2017-07-06T00:54:00.000Z","type":"22","hot":1522,"title":" 河东\u201c巡更\u201d系统上线 加固食品安全\u201c防火墙\u201d  "},
    #         {"emotion":"0","trend":"19 5 1329","ringId":"bfqxlm033302486","location":"河东区","time":"2017-07-07T00:30:00.000Z","type":"10","hot":1329,"title":" 河东区时尚花园社区集中清理楼道堆物  "}
    #     ]
    # }
    # return json_response(json_msg)

def getYuqingEmo(resquest):
    json_msg = {
        'result' : [
            {"negative":25,"neutral":69,"positive":1,"time":1498262400000},
            {"negative":14,"neutral":68,"positive":13,"time":1498348800000},
            {"negative":20,"neutral":68,"positive":12,"time":1498435200000},
            {"negative":24,"neutral":64,"positive":2,"time":1498521600000},
            {"negative":1,"neutral":64,"positive":24,"time":1498608000000},
            {"negative":15,"neutral":65,"positive":17,"time":1498694400000},
            {"negative":1,"neutral":41,"positive":24,"time":1498780800000},
            {"negative":2,"neutral":52,"positive":4,"time":1498867200000},
            {"negative":6,"neutral":42,"positive":23,"time":1498953600000},
            {"negative":24,"neutral":42,"positive":1,"time":1499040000000},
            {"negative":2,"neutral":42,"positive":4,"time":1499126400000},
            {"negative":2,"neutral":42,"positive":24,"time":1499212800000},
            {"negative":2,"neutral":41,"positive":4,"time":1499299200000},
            {"negative":8,"neutral":41,"positive":17,"time":1499385600000},
            {"negative":1,"neutral":41,"positive":4,"time":1499472000000}
        ]
    }

    sentiment2res = {1: 'negative', 2:'neutral', 3:'positive'}
    resByKeyTime = {}
    sqlres = _my_execuse_query_sql(SQLsentiment);
    for onesqlres in sqlres:
        if onesqlres[0] not in resByKeyTime:
            resByKeyTime[onesqlres[0]] = {sentiment2res[int(onesqlres[1])]: onesqlres[2], "time": onesqlres[0] * 1000}
        else:
            resByKeyTime[onesqlres[0]][sentiment2res[int(onesqlres[1])]] = onesqlres[2]
    resByKeyTime = sorted(resByKeyTime.items(), key=lambda item:item[0])
    result = []
    for k,v in resByKeyTime:
        result.append(v)

    #print(result)
    json_msg = {'result' : result}

    return json_response(json_msg)

def getthreeindexs(request):
    _update_one_week();
    all = IhomeComplain.objects.filter(addtime__gt=intTimeNowBeforeOneWeek).count()
    inprocess = IhomeComplain.objects.filter(replytime=0, addtime__gt=intTimeNowBeforeOneWeek).count()
    json_msg = {'all' : all, 'inprocess':inprocess, 'done':all - inprocess}
    return json_response(json_msg)

def randomData():
    return random.uniform(10,80)

def getmapdata(request):

    localname = ['北京','天津','上海','重庆','河北','河南','云南','辽宁','黑龙江','湖南','安徽','山东','新疆','江苏','浙江','江西','湖北','广西','甘肃','山西','内蒙古','陕西','吉林','福建','贵州','广东','青海','西藏','四川','宁夏','海南','台湾','香港','澳门','南海诸岛']

    localnum = {'北京':0,'天津':0,'上海':0,'重庆':0,'河北':0,'河南':0,'云南':0,'辽宁':0,'黑龙江':0,'湖南':0,'安徽':0,'山东':0,'新疆':0,'江苏':0,'浙江':0,'江西':0,'湖北':0,'广西':0,'甘肃':0,'山西':0,'内蒙古':0,'陕西':0,'吉林':0,'福建':0,'贵州':0,'广东':0,'青海':0,'西藏':0,'四川':0,'宁夏':0,'海南':0,'台湾':0,'香港':0,'澳门':0,'南海诸岛':0}

    alllocal = _my_execuse_query_sql(SQLMap)
    for onelocal in alllocal:
        for onelocalname in localname:
            if onelocalname in onelocal:
                localnum[onelocalname] = localnum[onelocalname] + 1

    res = []
    maxvalue = 0
    for one in localnum:
        if maxvalue < localnum[one]:
            maxvalue = localnum[one]
        resone = {'name' : one, 'value': localnum[one]}
        res.append(resone)


    #print(localnum)
    json_msg = {'result' : res, 'maxvalue' : maxvalue}





    # json_msg = {
    #     'result' : [
    #         {'name': '北京','value': randomData() },
    #         {'name': '天津','value': randomData() },
    #         {'name': '上海','value': randomData() },
    #         {'name': '重庆','value': randomData() },
    #         {'name': '河北','value': randomData() },
    #         {'name': '河南','value': randomData() },
    #         {'name': '云南','value': randomData() },
    #         {'name': '辽宁','value': randomData() },
    #         {'name': '黑龙江','value': randomData() },
    #         {'name': '湖南','value': randomData() },
    #         {'name': '安徽','value': randomData() },
    #         {'name': '山东','value': randomData() },
    #         {'name': '新疆','value': randomData() },
    #         {'name': '江苏','value': randomData() },
    #         {'name': '浙江','value': randomData() },
    #         {'name': '江西','value': randomData() },
    #         {'name': '湖北','value': randomData() },
    #         {'name': '广西','value': randomData() },
    #         {'name': '甘肃','value': randomData() },
    #         {'name': '山西','value': randomData() },
    #         {'name': '内蒙古','value': randomData() },
    #         {'name': '陕西','value': randomData() },
    #         {'name': '吉林','value': randomData() },
    #         {'name': '福建','value': randomData() },
    #         {'name': '贵州','value': randomData() },
    #         {'name': '广东','value': randomData() },
    #         {'name': '青海','value': randomData() },
    #         {'name': '西藏','value': randomData() },
    #         {'name': '四川','value': randomData() },
    #         {'name': '宁夏','value': randomData() },
    #         {'name': '海南','value': randomData() },
    #         {'name': '台湾','value': randomData() },
    #         {'name': '香港','value': randomData() },
    #         {'name': '澳门','value': randomData() },
    #         {'name': '南海诸岛','value': '99' }
    #     ]
    # }
    return json_response(json_msg)
