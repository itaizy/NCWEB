/*
 * @Author: Jason
 * @Date:   2017-04-05 07:23:03
 * @Last Modified by:   anchen
 * @Last Modified time: 2017-06-07 20:03:33
 */

'use strict';

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
        factory({}, root.$, root.echarts, root.Mustache);
    }
}(this, function(exports, $, echarts, Mustache) {
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

    // 舆情
    function getdates(){
        $.getJSON('/getIhomeEmoSource', {
           emoclass: 1,
        }, function (data) {
            innerOuterViewList("ul#happy-view-list", data.result);
        });

        $.getJSON('/getIhomeEmoSource', {
            emoclass: 2,
        }, function (data) {
            innerOuterViewList("ul#angry-view-list", data.result);
        });

        $.getJSON('/getIhomeEmoSource', {
            emoclass: 3,
        }, function (data) {
            innerOuterViewList("ul#sad-view-list", data.result);
        });
    }
    getdates();
    setInterval(getdates, 60*60*1000)

    // 津内视角、津外视角
    // outerTJ: true：津外，false：津内。
    function innerOuterViewList(targetList, data) {
        var tpl = '{{#events}} \
            <li class="item box clearfix"> \
                <div class="item-img"> \
                    <img width="50" height="50" src="{{imgurl}}" alt="无图片"> \
                </div> \
                <div class="item-content"> \
                    <div class="content-top "> \
                        <span class="view-pos  attr-block">{{eventLoc}}</span> \
                        <p class="title" title="{{description}}">{{description}}</p> \
                    </div> \
                    <div class="content-bt clearfix"> \
                        <span class="time left"><i class="iconfont icon-clock-o"></i>{{timestr}}</span> \
                        <span class="from"><i class="iconfont icon-resource"></i>来源：{{src}}</span> \
                    </div> \
                </div> \
            </li> \
        {{/events}}';

        var items = [];

        $.each(data, function (i, d) {
            d.timestr = d.time.split("T")[0];
            // d.typestr = typeArr[parseInt(d.eventType)];
            items.push(d);
        });
        $(targetList).html(Mustache.render(tpl, {events: items}));
    }
}));
