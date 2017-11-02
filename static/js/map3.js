'use strict';
(function(){
    // 党建
    $.getJSON('/getthreeindexs', {areaName: ''}, function (data) {
        $('#weimin-index').html(data.all);
        $('#dangjian-index').html(data.inprocess);
        $('#yuqing-index').html(data.done);
    });
    $.getJSON('/getmapdata', {areaName: ''}, function (data) {
        var chart = echarts.init(document.getElementById('map'));
        var option = {
            tooltip: {
                trigger: 'item',
                formatter: '{b}:{c}'
            },
            grid: {
                top: 0,
                bottom: 0,
                containLabel: true,
                height: '120%',
            },
            visualMap: {
                min: 0,
                max: data.maxvalue,
                left: 'left',
                top: 'bottom',
                show: false,
                text: ['高','低'],           // 文本，默认为数值文本
                calculable: true,
                inRange: {
                    color: ['#ffffff', '#ef001e']
                }
            },
            series: [
                {
                    name: '中国',
                    type: 'map',
                    map: 'china',
                    selectedMode : 'multiple',
                    zoom: 1.1,
                    // itemStyle: {
                    //     normal: {
                    //         areaColor: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    //             offset: 0, color: '#c10b00'
                    //         }, {
                    //             offset: 1, color: '#c1ac2f'
                    //         }], false),
                    //         color: '#fff',
                    //         // shadowOffsetX: 0,
                    //         // shadowOffsetY: 0,
                    //         // shadowBlur: 8,
                    //         // borderWidth: 0,
                    //         // shadowColor: 'rgba(16, 101, 184, 1)'
                    //     },
                    //     emphasis:{
                    //         show: true,
                    //         areaColor: '#0e27ff',
                    //         color: '#fff',
                    //         // shadowOffsetX: 0,
                    //         // shadowOffsetY: 0,
                    //         // shadowBlur: 8,
                    //         // borderWidth: 0,
                    //         // shadowColor: 'rgba(16, 101, 184, 1)'
                    //     }
                    // },
                    label: {
                        normal: {
                            show: false,
                            textStyle: {
                                color: '#fff'
                            },
                        },
                        emphasis:{
                            show: true,
                            textStyle: {
                                color: '#fff'
                            },
                        }
                    },
                    data: data.result
                }
            ]
        };
        chart.setOption(option);
    });

})()
