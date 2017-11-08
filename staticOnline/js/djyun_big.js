/*
 * @Author: Jason
 * @Date:   2017-04-05 07:23:03
 * @Last Modified by:   anchen
 * @Last Modified time: 2017-06-07 20:03:33
 */

'use strict';

var typeArr = [
    "其他", "短消息", "经贸 商务", "国资 投资", "工业 科技", "工商 物价", "财政 税收", "交通", "邮政", "金融 证券",
    "市政 环卫", "农业", "林业", "文化 教育", "民族 宗教","体育", "国防 公安", "司法 法治", "反腐 ", "人事 档案",
    "医疗 卫生", "社保 扶贫", "影视 出版", "食品 药品", "安全 生产", "政治"];
var setInt; //工作流程图有关时间的setInterval对象
(function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['exports', 'jquery', 'echarts', 'mustache', 'mobiletest'], factory);
    } else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {
        // CommonJS
        factory(exports, require(['jquery', 'echarts', 'mustache', 'mobiletest']));
    } else {
        // Browser globals
        factory({}, root.$, root.echarts, root.Mustache, root.mobiletest);
    }
}(this, function(exports, $, echarts, Mustache, mobiletest) {
    var log = function(msg) {
        if (typeof console !== 'undefined') {
            console && console.error && console.error(msg);
        }
    }
    if (!echarts) {
        log('ECharts is not Loaded');
        return;
    }
    if (!echarts.registerMap) {
        log('ECharts Map is not loaded')
        return;
    }

    var ismobile = mobiletest();

    var dangjianChart, statChart, trendChart, emotionChart, hotChart;

    // 党建
    function activeTrend(){
        $.getJSON('/getActiveAndCommentDegree', {areaName: ''}, function (data) {
            dangjianChart = plotActivityTrend(data);
        });
    }
    activeTrend();
    setInterval(activeTrend, 60*60*1000);


    // 为民
    var momentDetailMap = {};
    plotMomentTab();
    function requestEfficiency(){
        $.getJSON('/getPlotMomentStatData', {size: 10}, function (data) {
            statChart = plotMomentStat(data.result);
        });
        $.getJSON('/getPlotMomentTrendData', {span: 12}, function (data) {
            trendChart = plotMomentTrend(data.result);
        });
    }
    requestEfficiency();
    setInterval(requestEfficiency, 60*60*1000);
    function requestHotMoment() {
        $.getJSON('/getHotMomentsFromGrid', {areaName: "", type: -1, size: 30}, function (data) {
            plotMomentYujing(data.result);
        });
    }
    requestHotMoment();
    setInterval(requestHotMoment, 60000);

    // 舆情
    innerOuterViewTab();
    function YuqingByHour(){
        $.getJSON('/getNewsData', {
            size: 4,
            imgurl: true,
            sort: 'hot',
            type: 8, // type=8: magic for TJController.java, line 481, commented by @ht, 2017-04-08
        }, function (data) {
            innerOuterViewList("ul#inner-view-list", data.result, false);
        });
        $.getJSON('/getNewsData', {
            size: 4,
            imgurl: true,
            sort: 'hot',
            type: 1, // type=8: magic for TJController.java, line 481, commented by @ht, 2017-04-08
        }, function (data) {
            innerOuterViewList("ul#outer-view-list", data.result, true);
        });
        $.getJSON('/getYuqingEmo', {loc: ""}, function (data) {
            emotionChart = plotEventEmotion(data.result);
        });
        // hotChart = initFocus();
        var my_demo_chart = echarts.init(document.getElementById('hot-info'));
        my_demo_chart.showLoading({
            text: '',
            color: '#1983DD',
            textColor: '#00FFFF',
            maskColor: 'rgba(17, 84, 143, 0.3)',
            zlevel: 0,
        });
        $.getJSON('/getHotEventsFromEventsTJ', {
            areaName: "",
            size: "8000",
        }, function (data) {
            hotChart = plotHotEvents(data.result, data.maxValue, my_demo_chart);
        });

    }
    YuqingByHour();
    setInterval(YuqingByHour, 60*60*1000);

    var tabToogleTimer1 = undefined;
    var tabToogleTimer2 = undefined;

    // 时钟，自动切换Tab页
    if (!ismobile) {
        registerTabTimer();
    }

    function stripDate(datestr) {
        return new Date(datestr).format('M-d');
    }

    // 注册时钟，自动切换Tab页
    function registerTabTimer() {
        function toogleViewTab1() {
            console.log('timer1');
            if ($("div#trend-tab").hasClass("active")) {
                $("div#type-tab").click();
            }
            else {
                $("div#trend-tab").click();
            }
        }

        function toogleViewTab2() {
            console.log('timer2');
            if ($("#inner-view-tab").hasClass("table-item-active")) {
                $("#outer-view-tab").click();
            }
            else {
                $("#inner-view-tab").click();
            }
        }

        if (!ismobile) {
            if (tabToogleTimer1 != undefined) {
                clearInterval(tabToogleTimer1);
                tabToogleTimer1 = undefined;
            }
            tabToogleTimer1 = setInterval(toogleViewTab1, 20000);
            $(".toogle-tab-element").hover(function () {
                console.log("xxx" + tabToogleTimer1);
                clearInterval(tabToogleTimer1);
                tabToogleTimer1 = undefined;
            }, function () {
                if (tabToogleTimer1 != undefined) {
                    clearInterval(tabToogleTimer1);
                    tabToogleTimer1 = undefined;
                }
                tabToogleTimer1 = setInterval(toogleViewTab1, 20000);
                console.log("tttt" + tabToogleTimer1);
            });

            setTimeout(function () {
                if (tabToogleTimer2 != undefined) {
                    clearInterval(tabToogleTimer2);
                    tabToogleTimer2 = undefined;
                }
                tabToogleTimer2 = setInterval(toogleViewTab2, 20000);
                $(".toogle-tab-element").hover(function () {
                    clearInterval(tabToogleTimer2);
                    tabToogleTimer2 = undefined;
                }, function () {
                    if (tabToogleTimer2 != undefined) {
                        clearInterval(tabToogleTimer2);
                        tabToogleTimer2 = undefined;
                    }
                    tabToogleTimer2 = setInterval(toogleViewTab2, 20000);
                });
            }, 3000);
        }
    }

    // 党建活跃度和凝聚力
    function plotActivityTrend(data) {

        // 归一化活动指数
        var y1min = Math.min.apply(null, data.data_y1) * 0.8,
            y1max = Math.max.apply(null, data.data_y1) * 1.2,
            diff = y1max - y1min;
        data.data_y1 = data.data_y1.map(function (x) {
            return Math.round((x - y1min) * 100 / diff);
        });

        //卷积？？？曲线平滑处理
        function conv1d(wnd, arr) {
            var result = [].concat(arr);
            $.each(arr, function(i, x) {
                var lower = Math.max(0, i-Math.floor(wnd/2)),
                    upper = Math.min(arr.length, i+Math.floor((wnd+1)/2));
                var sub = arr.slice(lower, i).concat(arr.slice(i, upper));
                result[i] = Math.round(sub.reduce(function (a, b) { return a + b; }, 0) / (upper - lower));
            });
            return result;
        }

        var chart = echarts.init(document.getElementById('active-join'));
        // 指定图表的配置项和数据
        chart.setOption({
            // backgroundColor: 'rgba(17,47,117,.5)',
            // title: {
            //     text: '党建活跃度和凝聚力',
            //     textStyle: {
            //       color: '#fff',
            //       fontSize: 20,
            //       fontWeight: 'normal'
            //     },
            //     textAlign: 'left',
            //     left: '36',
            //     top: '4%',
            // },
            legend: {
                icon: 'circle',
                x: 'left',
                itemWidth: 13,
                itemHeight: 13,
                padding: [10, 20, 10, 10],
                left: '60%',
                top: '4%',
                itemGap: 20,
                textStyle: {
                    color: '#fff',
                    fontSize: 12
                },
                data:['总体','校外']
            },
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#0775e4'
                    },
                    crossStyle: {
                        color: '#bbb'
                    }
                },
                confine: true,
                extraCssText: 'max-width: 230px; background:rgba(17, 47, 117, 0.8); border:1px solid #0775e4'
                // formatter: '{b}<br />三会一课数：{c}'
            },
            grid: {
                left: '2%',
                right: '5%',
                bottom: '3%',
                containLabel: true
            },
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data : data.data_x.map(stripDate),
                    axisLabel: {
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        },
                        interval: 4,
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#2e63cf'
                        }
                    },
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#052f5d'
                        },
                        width: 1
                    }
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    max: 100,
                    axisLabel: {
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        }
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#0775e4'
                        }
                    },
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#052f5d'
                        },
                        width: 1
                    }
                },
            ],
            series : [
                {
                    name: '总体',
                    type: 'line',
                    smooth: true,
                    // symbol: 'circle',
                    // symbolSize: 8,
                    // showSymbol: false,
                    lineStyle: {
                        normal: {
                            width: 1
                        }
                    },
                    areaStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(255, 217, 114,0.8)'
                            }, {
                                offset: 1,
                                color: 'rgba(255, 217, 114,0.2)'
                            }], false),
                            // shadowColor: 'rgba(0, 0, 0, 0.1)',
                            // shadowBlur: 10
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: '#FFC93E',
                            borderColor: '#FFC93E',
                            // borderWidth: 12

                        },
                    },
                    /*data: conv1d(4, data.data_y1).map(function (x) { return Math.min(x + 20, 90); }),*/
                    data: data.data_y1,
                },
                {
                    name: '校外',
                    type: 'line',
                    smooth: true,
                    // symbol: 'circle',
                    // symbolSize: 8,
                    // showSymbol: false,
                    lineStyle: {
                        normal: {
                            width: 1
                        },
                    },
                    areaStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(255, 100, 80, 0.9)'
                            }, {
                                offset: 1,
                                color: 'rgba(255, 100, 80, 0.3)'
                            }], false),
                            // shadowColor: 'rgba(0, 0, 0, 0.1)',
                            // shadowBlur: 10
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: '#F7494C',
                            borderColor: '#F7494C',
                            // borderWidth: 12
                        },
                    },
                    /*data: conv1d(7, data.data_y2).map(function (x) { return Math.min(x * 2 + 10, 90); }),*/
                    data:data.data_y2,
                }
            ]
        });
        return chart;
    }

    var momentYujingTimer = undefined;

    // 为民服务工作流预警
    function plotMomentYujing(data) {
        var tpl =
            '<li class="box item start_box box_orient box_pack {{icon}}" id="{{id}}_{{idx}}"> \
                <span class="vertical-line"></span> \
                <div class="item-msg-info start_box box_align"> \
                    <span class="quest-icon iconfont icon-alarm"></span> \
                    <p class="info-p ellipsis w338" title="{{message}}">{{message}}</p> \
                </div> \
                <div class="time-from start_box box_align box_pack"> \
                    <p class="time-label" ><span class="iconfont icon-clock-o"></span>{{createdtstr}}</p> \
                    <p class="from-label ellipsis"><span class="iconfont icon-map-marker"></span>{{atdepartment}}</p> \
                </div> \
            </li>';
        // <span class="quest-label">{{typestr}}</span> \

        var items = [];
        var cnt = 0;
        $.each(data, function (i, item) {
            // if (item.types == 0 || item.types == 1 || item.types == 16 || item.types == 25) {
            //     return true;
            // }
            // if (item.types == 4) {
            //     item.typestr = "科技";
            // }
            // else {
            //     item.typestr = typeArr[item.types].split(" ")[0];
            // }
            item.idx = cnt++;
            item.createdtstr = new Date(item.addtime * 1000).format('M-d hh:mm'); // item.createdt.slice(0, 10);
            item.icon = item.expire == 0 ? 'newest' : 'hardest';
            items.push(item);
        });
        animateList("ul#moment-yujing", tpl, items);
        updateWorkflow(items[0]);

        function animateList(targetDom, tpl, items) {
            var tpl = "{{#elements}}" + tpl + "{{/elements}}";
            var $list = $(targetDom);
            $list.html(Mustache.render(tpl, {elements: items}));
            $list.find("li:first").addClass("active");
            function renderList() {
                var $first = $list.find("li:first");
                var $last = $list.find("li:last");
                $first.removeClass("active");
                $last.css({
                    'margin-top': -70 + 'px',
                    'margin-bottom': '20px',
                }).prependTo($list);
                $list.find("li:first").addClass("active");
                $list.find("li:first").animate({
                        marginTop: 0 + 'px',
                    },
                    1500,
                    function () {}
                );
                var idx = parseInt($list.find("li:first").attr("id").split("_")[1]);
                updateWorkflow(items[idx]);
            }

            if (!ismobile) {
                if (momentYujingTimer != undefined) {
                    clearInterval(momentYujingTimer);
                    momentYujingTimer = undefined;
                }
                momentYujingTimer = setInterval(function () { renderList(); }, 12000);
                $list.hover(function (){
                    clearInterval(momentYujingTimer);
                    momentYujingTimer = undefined;
                    }, function (){
                    if (momentYujingTimer != undefined) {
                        clearInterval(momentYujingTimer);
                        momentYujingTimer = undefined;
                    }
                    momentYujingTimer = setInterval(function () { renderList(); }, 12000);
                });
            }
            else {
                $list.find("li").on("click", function (e) {
                    var item = $(e.currentTarget);
                    $list.find("li").removeClass("active");
                    item.addClass("active");
                    var idx = parseInt(item.attr("id").split("_")[1]);
                    updateWorkflow(items[idx]);
                });
            }
        }
    }

    // 更新工作流流程图
    function updateWorkflow(moment) {
        var tpl =
            '<p class="questions">{{message}}</p> \
            <div class="start_box box_align box_pack"> \
                <p class="font16">{{createdtstr}}</p> \
                <div class="font16 start_box box-pack"><p>等级：</p><p class="hot-font font14">{{hotstr}}</p></div> \
                <p class="font16">部门：{{atdepartment}}</p> \
            </div>';
        // moment.hotstr = new Date(moment.addtime * 1000).format('M-d hh:mm');
        var timestamp=new Date().getTime();
        moment.hotstr = timestamp - moment.addtime * 1000  > 2 * 60 * 60 * 24 * 1000 ? '高' : '低';
        // moment.hotstr = moment.hot > 2 ? '高' : '低';
        $("div#moment-info").html(Mustache.render(tpl, moment));
        drawWorkflowChart(moment);
    }

    function drawWorkflowChart(moment)
    {
        if(setInt)
        {
            window.clearInterval(window.clearInterval(setInt));
        }
        if(moment.accept == 0)
        {
            var tpl = '<li class="item not-accept" >\
                <span class="status success"></span>\
            <p class="step">问题提出</p>\
            </li>\
            <li class="item not-accept" >\
            <span class="status wrong arrow animating"></span>\
            <p class="step">未受理</p>\
            </li>\
            <li class="item not-accept" >\
            <span class="status "></span>\
            <p class="step">未解决</p>\
            </li>'
            $("#flow_detail").html(tpl);
        }
        else if(moment.accept == 1)
        {
            var fromdate = new Date(moment.createdtfix * 1000);
            var now = new Date();
            var sec = Math.round((now.getTime() - fromdate.getTime())/1000);
            var type = getTimeType(sec);
            var classarray = new Array();
            var unsolvedclassarray = new Array();
            var parray = new Array();
            var arrowarray = new Array();
            var nodeindexarray = ["first","","last"];
            for(var i = 0;i<=3;i++)
            {
                if(i<type)
                {
                    classarray.push("wrong");
                    unsolvedclassarray.push("wrong");
                    parray.push("");
                    arrowarray.push("arrow");
                }
                else if(i == type)
                {
                    classarray.push("");
                    unsolvedclassarray.push("wrong animating");
                    parray.push("");
                    arrowarray.push("arrow");
                }
                else
                {
                    classarray.push("");
                    unsolvedclassarray.push("");
                    parray.push("unreach");
                    arrowarray.push("");
                }
            }
            //noinspection JSAnnotator   自动修改，后添加的
            function renderFlowGraph1(data) {
                var rendered = '<li class="item accept">\
                        <span class="status success"></span>\
                    <p class="step">问题提出</p>\
                    </li>\
                    <li class="item accept">\
                        <span class="status success arrow "></span>\
                        <p class="step" >已受理</p>\
                    </li>';
                rendered += '<li class="item crossing accept">\
                    <span class="status '+ unsolvedclassarray[0] +  ' arrow "></span>\
                    <p class="step" >' + data.dept_name_0 + '</p>\
                <ul class="minor-ul">';
                for(var i = 1;i<=3;i++)
                {

                    rendered += ' <li class="item branch-item '+  nodeindexarray[i-1] +  '">';
                    rendered += '<span class="status '+ unsolvedclassarray[i] +' '+ arrowarray[i] +  ' "></span>';
                    if(i == 1)
                    {
                        rendered += '<p style="position: relative;left: -20px;" class="step '+  parray[i] +' " >'+ data["dept_name_" + i] + '</p></li>';
                    }
                    else if(i == 2)
                    {
                        rendered += '<p style="position: relative;top: 40px;" class="step '+  parray[i] +' " >'+ data["dept_name_" + i] + '</p></li>';
                    }
                    else {
                        rendered += '<p class="step '+  parray[i] +' " >'+ data["dept_name_" + i] + '</p></li>';
                    }
                }
                rendered += ' </ul>\
                    </li>';
                rendered += '<li class="item time">\
                        <p class="step" id="timespan" >'+ changeSecondToTimespan(sec) +'</p>\
                        </li>';
                rendered += ' <li class="item">\
                        <span class="status"></span>\
                        <p class="step" >未解决</p>\
                    </li>';
                $("#flow_detail").html(rendered);
                setInt = setInterval(function()
                {
                    show(++sec);
                }, 1000);
            }
            if (momentDetailMap[moment.id] == undefined) {
                $.getJSON('/api/getMomentDetailFromDeptById?creat_id='+ moment.createby +"&solve_id=" +  moment.acceptby, {}, function (data) {
                    momentDetailMap[moment.id] = data;
                    renderFlowGraph1(momentDetailMap[moment.id]);
                });
            }
            else {
                renderFlowGraph1(momentDetailMap[moment.id]);
            }
        }
        else if(moment.accept == 2)
        {
            var fromdate = new Date(moment.createdt);
            var todate = new Date(moment.finishdt);
            var sec = Math.round((todate.getTime() - fromdate.getTime())/1000);
            var type = getTimeType(sec);
            var classarray = new Array();
            var unsolvedclassarray = new Array();
            var parray = new Array();
            var arrowarray = new Array();
            var nodeindexarray = ["first","","last"];
            for(var i = 0;i<=3;i++)
            {
                if(i<type)
                {
                    classarray.push("wrong");
                    unsolvedclassarray.push("wrong");
                    parray.push("");
                    arrowarray.push("arrow");
                }
                else if(i == type)
                {
                    classarray.push("");
                    unsolvedclassarray.push("wrong ");
                    parray.push("");
                    arrowarray.push("arrow");
                }
                else
                {
                    classarray.push("");
                    unsolvedclassarray.push("");
                    parray.push("unreach");
                    arrowarray.push("");
                }
            }
            //noinspection JSAnnotator
            function renderFlowGraph2(data) {
                var rendered = '<li class="item">\
                        <span class="status success"></span>\
                    <p class="step">问题提出</p>\
                    </li>\
                    <li class="item">\
                        <span class="status success arrow "></span>\
                        <p class="step" >已受理</p>\
                    </li>';
                rendered += '<li class="item crossing">\
                    <span class="status '+ unsolvedclassarray[0] +  ' arrow "></span>\
                    <p class="step" >' + data.dept_name_0 + '</p>\
                <ul class="minor-ul">';
                for(var i = 1;i<=3;i++)
                {
                    rendered += ' <li class="item branch-item '+  nodeindexarray[i-1] +  '">';
                    rendered += '<span class="status '+ unsolvedclassarray[i] +' '+ arrowarray[i] +  ' "></span>';
                    if(i == 1)
                    {
                        rendered += '<p style="position: relative;left: -30px;" class="step '+  parray[i] +' " >'+ data["dept_name_" + i] + '</p></li>';
                    }
                    else if(i == 2)
                    {
                        rendered += '<p style="position: relative;top: 40px;" class="step '+  parray[i] +' " >'+ data["dept_name_" + i] + '</p></li>';
                    }
                    else {
                        rendered += '<p class="step '+  parray[i] +' " >'+ data["dept_name_" + i] + '</p></li>';
                    }
                }
                rendered += ' </ul>\
                    </li>';
                rendered += '<li class="item time">\
                        <p class="step" id="timespan" >'+ changeSecondToTimespan(sec) +'</p>\
                        </li>';
                rendered += ' <li class="item">\
                        <span class="status success animating"></span>';
                rendered += '<p class="step" >已解决</p><p class="stars">';
                for(var i=5;i>0;i--)
                {
                    if(i-type > 0)
                    {
                        rendered += '<span class="start-yes"></span>';
                    }
                    else
                    {
                        rendered += '<span class="start-no"></span>'
                    }
                }
                rendered += '</p></li>';
                $("#flow_detail").html(rendered);
            }
            if (momentDetailMap[moment.id] == undefined) {
                $.getJSON('/api/getMomentDetailFromDeptById?creat_id='+ moment.createby +"&solve_id=" +  moment.acceptby, {}, function (data) {
                    momentDetailMap[moment.id] = data;
                    renderFlowGraph2(momentDetailMap[moment.id]);
                });
            }
            else {
                renderFlowGraph2(momentDetailMap[moment.id]);
            }
        }
    }

    //判断事件解决的事件区间，分为一天内，1~3天，3~5天，5天以上,传入间隔秒数
    function getTimeType(second) {
        var durarray = [1,3,5];
        var type = 3;
        for(var i = 0;i<durarray.length;i++)
        {
            if(second < 60*60*24*durarray[i])
            {
                type = i;
                break;
            }
        }
        return type;
    }

    function  changeSecondToTimespan(second) {
        var result = "";
        var timestr = ["天","时","分","秒"];
        var timediv = [60*60*24,60*60,60,1];
        var count = 0;
        while (count < timestr.length)
        {
            if(Math.floor(second/timediv[count])!=0)
            {
                result += Math.floor(second/timediv[count]) + timestr[count];
            }
            second = second % timediv[count];
            count++;
        }
        return result;
    }
    //时间增长前端变换函数
    function show(dur)
    {
        $("#timespan").html(changeSecondToTimespan(dur));
    }

    // 为民服务 tab。
    function plotMomentTab() {
        $("div#trend-tab").on('click', function (e) {
            $("div#type-tab").removeClass("active");
            $("div#trend-tab").addClass("active");
            // $("div#moment-stat").fadeOut(function () {
            //     $("div#moment-stat2").fadeIn("slow", function () {
            //         trendChart.resize();
            //     });
            // });
            // $("div#moment-stat").css('opacity', '0');
            // $("div#moment-stat2").css('opacity', '1');
            $("div#moment-stat").css('z-index', '50');
            $("div#moment-stat").css('visibility', 'hidden');
            $("div#moment-stat2").css('z-index', '100');
            $("div#moment-stat2").css('visibility', 'visible');
        });
        $("div#type-tab").on('click', function (e) {
            $("div#trend-tab").removeClass("active");
            $("div#type-tab").addClass("active");
            // $("div#moment-stat2").fadeOut(function () {
            //     $("div#moment-stat").fadeIn("slow", function () {
            //         statChart.resize();
            //     });
            // });
            // $("div#moment-stat2").css('opacity', '0');
            // $("div#moment-stat").css('opacity', '1');
            $("div#moment-stat2").css('z-index', '50');
            $("div#moment-stat2").css('visibility', 'hidden');
            $("div#moment-stat").css('z-index', '100');
            $("div#moment-stat").css('visibility', 'visible');
        });
    }
    //移动端tab切换
    function mobileMenuTab() {
        $('#menu-tab a').on('click', function(e){
            var index = $(this).index();
            var cont = $(".body .wrapper");

            e.preventDefault();                 /*取消默认点击*/
            $("#menu-tab .item").removeClass("active");
            $(this).addClass("active");

            cont.eq(index).fadeIn(function () {
                switch (index) {
                    case 0: // 为民
                        statChart.resize();
                        trendChart.resize();
                        break;
                    case 1: // 党建
                        dangjianChart.resize();
                        break;
                    case 2: // 舆情
                        hotChart.resize();
                        emotionChart.resize();
                        break;
                }
            }).siblings(".wrapper").fadeOut();
        });
    }
    mobileMenuTab();

    // 服务为民效率统计类型
    function plotMomentStat(data) {
        var chart = echarts.init(document.getElementById('moment-stat'));
        //var datearr = ["1天内","2~3天","4~7天","更长"];

        //var series = [];
        // var mytypearr = [];
        // $.each(data.type, function (i, t) {
        //     mytypearr.push(typeArr[t].split(' ')[0]);
        // });
        // 将大于7天的都合并为“更长”, modified by @ht, 2017-04-08
        // for (var i = 0; i < data[3].length; ++i) {
        //     data[3][i] = data[3][i] + data[4][i] + data[5][i];
        // }
        // $.each(datearr, function (i, date) {
        //     series.push({
        //         name: dataarr,
        //         type:'bar',
        //         barWidth: '40%',
        //         stack: '时间',
        //         data: data,
        //     });
        // });

        chart.setOption({
            // backgroundColor: 'rgba(17,47,117,.5)',
            // title: {
            //     text: '为民效率',
            //     textStyle: {
            //       color: '#fff',
            //       fontSize: 20,
            //       fontWeight: 'normal'
            //     },
            //     textAlign: 'left',
            //     left: '36',
            //     top: '4%'
            // },
            tooltip: {
                trigger: 'axis',
                axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                    type : 'shadow',        // 默认为直线，可选为：'line' | 'shadow'
                    label: {
                        backgroundColor: '#0775e4'
                    },
                    crossStyle: {
                        color: '#bbb'
                    }
                },
                confine: true,
                extraCssText: 'max-width: 230px; background:rgba(17, 47, 117, 0.8); border:1px solid #0775e4'
            },
            // legend: {
            //     left: '15%',
            //     top: '16%',
            //     textStyle: {
            //         color: '#fff',
            //         fontSize: 12
            //     },
            //     itemGap: 12,
            //     data: datearr
            // },
            grid: {
                top: '28%',
                left: '2%',
                right: '5%',
                bottom:  '16%',
                containLabel: true
            },
            color: [
                '#1E98FF',
                '#195aa2',
                '#c85933'],
            xAxis : [
                {
                    // name: '类型',
                    type : 'category',
                    boundaryGap : true,
                    data : data['datax'],
                    axisLabel: {
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        },
                        interval: 0,
                        rotate: 45,
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#2e63cf'
                        }
                    },
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#052f5d'
                        },
                        width: 1
                    },

                },
            ],
            yAxis : [
                {
                    name: '数量',
                    type: 'value',
                    axisLabel: {
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        }
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#0775e4'
                        }
                    },
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#052f5d'
                        },
                        width: 1
                    }
                }
            ],
            series : [{data: data['datay'], type:'bar', barWidth: '40%'}]
        });
        return chart;
    }

    // 服务为民效率趋势
    function plotMomentTrend(data) {
        var chart = echarts.init(document.getElementById('moment-stat2'));
        chart.setOption({
            // backgroundColor: 'rgba(17,47,117,.5)',
            // title : {
            //     text: '为民效率',
            //     textStyle: {
            //       color: '#fff',
            //       fontSize: 20,
            //       fontWeight: 'normal'
            //     },
            //     textAlign: 'left',
            //     left: '36',
            //     top: '4%'
            // },
            grid: {
                top: '28%',
                left: '2%',
                right: '5%',
                bottom: '3%',
                containLabel: true
            },
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    animation: false,
                    label: {
                        backgroundColor: '#0775e4'
                    },
                    crossStyle: {
                        color: '#bbb'
                    }
                },
                confine: true,
                extraCssText: 'max-width: 230px; background:rgba(17, 47, 117, 0.8); border:1px solid #0775e4'
            },
            // legend: {
            //     icon: 'circle',
            //     left: '15%',
            //     top: '16%',
            //     textStyle: {
            //         color: '#fff',
            //         fontSize: 12
            //     },
            //     itemGap: 12,
            //     data:['问题数', '未解决', '平均时长'],
            // },
            // color: ['#90dcdd', '#d87a80', 'red'],
            // color: ['#d3b334',
            //     '#f15a2a',
            //     '#ff1c43'],
            xAxis: [
                {
                    // name: '类型',
                    type : 'category',
                    boundaryGap : true,
                    data: data.datax,
                    axisLabel: {
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        },
                        interval: 0,
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#2e63cf'
                        }
                    },
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#052f5d'
                        },
                        width: 1
                    }
                }
            ],
            yAxis: [
                {
                    name: '数量',
                    type: 'value',
                    // max: 100,
                    axisLabel: {
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        }
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#0775e4'
                        }
                    },
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#052f5d'
                        },
                        width: 1
                    }
                },
                // {
                //     name: '处理时长（天）',
                //     type: 'value',
                //     // max: 10,
                //     axisLabel: {
                //         textStyle: {
                //             color: '#fff',
                //             fontSize: 12
                //         }
                //     },
                //     axisLine: {
                //         lineStyle: {
                //             color: '#0775e4'
                //         }
                //     },
                //     splitLine: {
                //         show: true,
                //         lineStyle: {
                //             color: '#052f5d'
                //         },
                //         width: 1
                //     }
                // },
            ],
            series: [
                {
                    name: '问题数',
                    type: 'line',
                    smooth: true,
                    // symbol: 'circle',
                    // showSymbol: false,
                    lineStyle: {
                        normal: {
                            width: 1
                        }
                    },
                    areaStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(30, 152, 255, 0.9)'
                            }, {
                                offset: 1,
                                color: 'rgba(30, 152, 255, 0.3)'
                            }], false),
                            // shadowColor: 'rgba(0, 0, 0, 0.1)',
                            // shadowBlur: 10
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: '#1e98ff',
                            borderColor: '#1e98ff',
                            // borderWidth: 12

                        }
                    },
                    data: data.datay,
                },
                // {
                //     name:'未解决',
                //     type: 'line',
                //     smooth: true,
                //     // symbol: 'circle',
                //     // showSymbol: false,
                //     lineStyle: {
                //         normal: {
                //             width: 1
                //         }
                //     },
                //     areaStyle: {
                //         normal: {
                //             color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                //                 offset: 0,
                //                 color: 'rgba(255, 84, 33, 0.9)'
                //             }, {
                //                 offset: 1,
                //                 color: 'rgba(255, 84, 33, 0.3)'
                //             }], false),
                //             // shadowColor: 'rgba(0, 0, 0, 0.1)',
                //             // shadowBlur: 10
                //         }
                //     },
                //     itemStyle: {
                //         normal: {
                //             color: '#FF5421',
                //             borderColor: '#FF941E',
                //         }
                //     },
                //     data: data.unsolvedcount,
                // },
                // {
                //     name:'平均时长',
                //     type: 'line',
                //     yAxisIndex: 1,
                //     lineStyle: {
                //         normal: {
                //             color: '#FFC11E',
                //             width: 1
                //         }
                //     },
                //     itemStyle: {
                //         normal: {
                //             color: '#FFC11E',
                //             borderColor: '#FFC11E',
                //             borderWidth: 9
                //         }
                //     },
                //     data: data.avetime.map(function (x) { return (x-1).toFixed(2); }),
                // }
            ]
        });
        return chart;
    }

    // 津内视角、津外视角
    function innerOuterViewTab() {
        $("#inner-view-tab").on('click', function (e) {
            $("#inner-view-tab").addClass("table-item-active");
            $("#outer-view-tab").removeClass("table-item-active");
            // $("#outer-view-div").fadeOut(function () {
            //     $("#inner-view-div").fadeIn("slow");
            // });
            $("#outer-view-div").css("opacity", "0");
            $("#inner-view-div").css("opacity", "1");
        });
        $("#outer-view-tab").on('click', function (e) {
            $("#outer-view-tab").addClass("table-item-active");
            $("#inner-view-tab").removeClass("table-item-active");
            // $("#inner-view-div").fadeOut(function() {
            //     $("#outer-view-div").fadeIn("slow");
            // });
            $("#inner-view-div").css("opacity", "0");
            $("#outer-view-div").css("opacity", "1");
        });
    }

    // 津内视角、津外视角
    // outerTJ: true：津外，false：津内。
    function innerOuterViewList(targetList, data, outerTJ) {
        var tpl = '{{#events}} \
            <li class="item box clearfix"> \
                <div class="item-img"> \
                    <img width="62" height="45" src="{{imgurl}}" alt="无图片"> \
                </div> \
                <div class="item-content"> \
                    <div class="content-top "> \
                        <span class="view-type attr-block">{{typestr}}</span> \
                        <span class="view-pos  attr-block">{{eventLoc}}</span> \
                        <p class="title" title="{{description}}">{{description}}</p> \
                    </div> \
                    <div class="content-bt clearfix"> \
                        <span class="time left"><i class="iconfont icon-clock-o"></i>{{timestr}}</span> \
                        {{#outerTJ}}<!--<span class="relevancy">相关度：{{relativity}}%</span>-->{{/outerTJ}}\
                        <span class="from"><i class="iconfont icon-resource"></i>来源：{{src}}</span> \
                    </div> \
                </div> \
            </li> \
        {{/events}}';

        var cnt = 0, items = [];

        $.each(data, function (i, d) {
            if(d.description.indexOf('大脑体积') != -1 || d.description.indexOf('全县组织工作会议召开') != -1) {
                return true;
            }
            d.timestr = d.time.split("T")[0];
            // d.typestr = typeArr[parseInt(d.eventType)];
            if (d.src == '新闻')
                d.es_type = 0;
            else
                d.es_type = 1;
            var eventType = parseInt(d.eventType)
            if (eventType == 1 || eventType == 25) {
                d.typestr = typeArr[eventType];
                d.typecolor = "#FF7920!important";
            }
            else if (eventType == 4) {
                d.typestr = "科技";
                d.typecolor = "#60A3F5!important";
            }
            else {
                d.typestr = typeArr[eventType].split(" ")[0];
                d.typecolor = "#87A5B5!important";
            }
            d.relativity = Math.floor(d.relativity * (90-60) / 100 + 60),
                items.push(d);
            if(cnt++ > 2) {
                return false;
            }
        });

        // 处理相关度
        if (outerTJ) {
            var minbound = 100, maxbound = 0;
            $.each(items, function (i, d) {
                minbound = Math.min(minbound, d.relativity);
                maxbound = Math.max(maxbound, d.relativity);
            });
            $.each(items, function (i, d) {
                d.relativity = Math.round((d.relativity - minbound) * (90 - 55) / (maxbound - minbound) + 55);
            });
        }

        $(targetList).html(Mustache.render(tpl, {events: items, outerTJ: outerTJ}));
    }

    // 舆论情绪
    function plotEventEmotion(data) {
        var chart = echarts.init(document.getElementById('discuss-emotion'));

        var datelist = [];
        var pos = [];
        var neg = [];
        var influence = [];

        $.each(data, function (i, item) {
            datelist.push(new Date(item.time).format('yyyy-MM-dd'));
            console.log(item)
            console.log(item.time)
            console.log(new Date(item.time).format('yyyy-MM-dd'))
            pos.push(item.positive);
            neg.push(item.negative);
            influence.push(item.neutral);
        })

        // 指定图表的配置项和数据
        chart.setOption({
            // backgroundColor: 'rgba(17,47,117,.5)',
            legend: {
                icon: 'circle',
                x: 'left',
                itemWidth: 13,
                itemHeight: 13,
                padding: [10, 20, 10, 10],
                left: '30%',
                top: '5%',
                textStyle: {
                    color: '#fff',
                    fontSize: 12
                },
                data:['高兴','生气','悲伤']
            },
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#0775e4'
                    },
                    crossStyle: {
                        color: '#bbb'
                    }
                },
                confine: true,
                extraCssText: 'max-width: 230px; background:rgba(17, 47, 117, 0.8); border:1px solid #0775e4',
                formatter: '2017-{b}<br> \
                    <span style="display:inline-block;margin-right:5px;border-radius:10px;width:9px;height:9px;background-color:#1e98ff"> \
                    </span>{a0} : {c0}<br> \
                    <span style="display:inline-block;margin-right:5px;border-radius:10px;width:9px;height:9px;background-color:#FF5421"> \
                    </span>{a1} : {c1}<br> \
                    <span style="display:inline-block;margin-right:5px;border-radius:10px;width:9px;height:9px;background-color:#FFC11E"> \
                    </span>{a2} : {c2}</div>',
            },
            grid: {
                left: '2%',
                right: '5%',
                bottom: '3%',
                containLabel: true
            },
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data : datelist.map(stripDate),
                    axisLabel: {
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        },
                        interval: 1,
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#2e63cf'
                        }
                    },
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#052f5d'
                        },
                        width: 1
                    }
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    max: 10,
                    axisLabel: {
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        }
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#0775e4'
                        }
                    },
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: '#052f5d'
                        },
                        width: 1
                    }
                },
            ],
            series : [
                {
                    name: '高兴',
                    type: 'line',
                    smooth: true,
                    // symbol: 'circle',
                    // showSymbol: false,
                    lineStyle: {
                        normal: {
                            width: 1
                        }
                    },
                    areaStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(30, 152, 255, 0.9)'
                            }, {
                                offset: 1,
                                color: 'rgba(30, 152, 255, 0.3)'
                            }], false),
                            // shadowColor: 'rgba(0, 0, 0, 0.1)',
                            // shadowBlur: 10
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: '#1e98ff',
                            borderColor: '#1e98ff',
                            // borderWidth: 12

                        }
                    },
                    data: neg
                },
                {
                    name: '生气',
                    type: 'line',
                    smooth: true,
                    // symbol: 'circle',
                    // showSymbol: false,
                    lineStyle: {
                        normal: {
                            width: 1
                        }
                    },
                    areaStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(255, 84, 33, 0.9)'
                            }, {
                                offset: 1,
                                color: 'rgba(255, 84, 33, 0.3)'
                            }], false),
                            // shadowColor: 'rgba(0, 0, 0, 0.1)',
                            // shadowBlur: 10
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: '#FF5421',
                            borderColor: '#FF941E',
                        }
                    },
                    data: pos
                },
                {
                    name: '悲伤',
                    type: 'line',
                    lineStyle: {
                        normal: {
                            color: '#FFC11E',
                            width: 1
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: '#FFC11E',
                            borderColor: '#FFC11E',
                            borderWidth: 9
                        }
                    },
                    data: influence
                }
            ]
        });
        return chart;
    }

    // 社会舆情
    function plotHotEvents(data, dataMaxValue, my_demo_chart) {
    // function initFocus(){

            var datelist = [];
            var pos = [];
            var neg = [];
            var influence = [];
            var maxValue = dataMaxValue;

            $.each(data, function (i, item) {
                datelist.push(new Date(item.time).format('yyyy-MM-dd'));
                console.log(item)
                console.log(item.time)
                console.log(new Date(item.time).format('yyyy-MM-dd'))
                pos.push(item.positive);
                neg.push(item.negative);
                influence.push(item.neutral);
            })

            var focusOption = {
                // backgroundColor: 'rgba(17,47,117,.5)',
                legend: {
                    icon: 'circle',
                    x: 'left',
                    itemWidth: 13,
                    itemHeight: 13,
                    padding: [10, 20, 10, 10],
                    left: '30%',
                    top: '5%',
                    textStyle: {
                        color: '#fff',
                        fontSize: 12
                    },
                    // data:['正面','负面','中性']
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        label: {
                            backgroundColor: '#0775e4'
                        },
                        crossStyle: {
                            color: '#bbb'
                        }
                    },
                    confine: true,
                    extraCssText: 'max-width: 230px; background:rgba(17, 47, 117, 0.8); border:1px solid #0775e4',
                    formatter: '2017-{b}<br> \
                    <span style="display:inline-block;margin-right:5px;border-radius:10px;width:9px;height:9px;background-color:#1e98ff"> \
                    </span>{a0} : {c0}</div>',
                },
                grid: {
                    left: '2%',
                    right: '5%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: [
                    {
                        type: 'category',
                        boundaryGap: false,
                        data: datelist.map(stripDate),
                        axisLabel: {
                            textStyle: {
                                color: '#fff',
                                fontSize: 12
                            },
                            interval: 1,
                        },
                        axisLine: {
                            lineStyle: {
                                color: '#2e63cf'
                            }
                        },
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: '#052f5d'
                            },
                            width: 1
                        }
                    }
                ],
                yAxis: [
                    {
                        type: 'value',
                        max: maxValue,
                        axisLabel: {
                            textStyle: {
                                color: '#fff',
                                fontSize: 12
                            }
                        },
                        axisLine: {
                            lineStyle: {
                                color: '#0775e4'
                            }
                        },
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: '#052f5d'
                            },
                            width: 1
                        }
                    },
                ],
                series: [
                    {
                        name: '舆论',
                        type: 'line',
                        smooth: true,
                        // symbol: 'circle',
                        // showSymbol: false,
                        lineStyle: {
                            normal: {
                                width: 1
                            }
                        },
                        areaStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                    offset: 0,
                                    color: 'rgba(30, 152, 255, 0.9)'
                                }, {
                                    offset: 1,
                                    color: 'rgba(30, 152, 255, 0.3)'
                                }], false),
                                // shadowColor: 'rgba(0, 0, 0, 0.1)',
                                // shadowBlur: 10
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#1e98ff',
                                borderColor: '#1e98ff',
                                // borderWidth: 12

                            }
                        },
                        data: influence
                    }
                ]
            };

            my_demo_chart.hideLoading();
            my_demo_chart.setOption(focusOption);

            return my_demo_chart;
        };


}));
