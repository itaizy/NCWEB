'use strict';
(function(){
    var chart = echarts.init(document.getElementById('age'));
    var colorList = [
        {
            top: '#ffa452',
            middle: '#ff8944',
            bottom: '#ff652e'
        },
        {
            top: '#e6c6ff',
            middle: '#c57aff',
            bottom: '#a632ff'
        },
        {
            top: '#8ae7fe',
            middle: '#50c8e7',
            bottom: '#1bacd0'
        },
        {
            top: '#ffcb97',
            middle: '#ffab59',
            bottom: '#ff9630'
        },
        {
            top: '#8cbdff',
            middle: '#5ea2ff',
            bottom: '#2f87ff'
        },
        {
            top: '#ff7b74',
            middle: '#ff554d',
            bottom: '#ff3a30'
        },
    ];
    var timers = null;
    var colorListDefault = ['#4e301d','#290743','#094959','#3e2a08','#0b2850','#3a0606'];
    var ageArr = [], maxArr = [];

    //初始化党支部党员的模板字符串
    var dangStr = '<div class="left box number-board lace-corner">\
        <div id="branch_num" class="num"><%= dangcount %></div>\
        <div class="name">党委/党总支数</div>\
    </div>\
    <div class="right box number-board lace-corner">\
        <div id="member_num" class="num"><%= dangyuan %></div>\
        <div class="name">党员数</div>\
    </div>\
    <div class="middle box number-board lace-corner">\
        <div id="dept_num" class="num"><%= zhibu %></div>\
        <div class="name">党支部数</div>\
    </div>';
    var dangTpl = _.template(dangStr);

    //初始化男女性别的模板字符串
    var sexStr = '<div class="login-number">\
        <div class="bg">\
            <div class="bg-1"></div>\
            <div class="bg-2"></div>\
            <div class="bg-3"></div>\
        </div>\
        <div id="login_num" class="num">14284</div>\
        <div class="txt">\
            登录人数\
        </div>\
    </div>\
    <div class="sex">\
        <div class="man boy"></div>\
        <div class="ratio">\
            <div id="rate_man" class="percent"><%= femal%></div>\
            <div class="txt">男性比例</div>\
        </div>\
    </div>\
    <div class="sex">\
        <div class="man girl"></div>\
        <div class="ratio">\
            <div id="rate_woman" class="percent"><%= mal%></div>\
            <div class="txt">女性比例</div>\
        </div>\
    </div>';
    var sexTpl =  _.template(sexStr);

    //登录人数
    function setLogin() {
        $.ajax({
            url: '/IScreenshow/LoginStatus',
            type: 'post',
            dataType: 'jsonp',
            data: {},
        })
        .done(function(res) {
            if (res.code == 200) {
                $('#login_num').html(res.data);
            } else {
                alert(res.msg);
            }
        })
        .fail(function() {
            console.log("error");
        })
    }

    //党支部数据 男女比例 接口调用
    $.ajax({
        url: '/IScreenshow/GetBaseInfo',
        type: 'post',
        dataType: 'jsonp',
        data: {},
    })
    .done(function(res) {
        if (res.code == 200) {
            setLogin();
            ageArr = res.data.age;
            var max = Math.max.apply(Math, ageArr) + 1000;
            for (var i = 0; i < ageArr.length; i++) {
                maxArr.push(max);
            };
            // 指定图表的配置项和数据
            var option = {
                color: ['#3398DB'],
                title: {
                    text: '党员年龄分布',
                    textStyle: {
                      color: '#fff',
                      fontSize: 20,
                      textBaseline: 'middle'
                    },
                    left: '7%',
                    top: '3%'
                },
                tooltip : {
                    trigger: 'axis',
                    axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                        type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '12%',
                    containLabel: true,
                    show: false
                },
                xAxis : [
                    {
                        type : 'category',
                        nameTextStyle: {
                            color: '#fff'
                        },
                        nameRotate: 45,
                        data : ['18-30岁', '30-40岁', '40-50岁', '50-60岁', '60-70岁', '70岁以上'],
                        axisTick: {
                            alignWithLabel: true
                        },
                        axisLabel: {
                            rotate: 45,
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
                            show: false
                        }

                    }
                ],
                yAxis : [
                    {
                        type : 'value',
                        nameTextStyle: {
                            color: '#fff'
                        },
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
                            show: false
                        }
                    }
                ],
                series : [
                    {
                        name:'',
                        type:'bar',
                        barWidth: '14',
                        barGap: '-100%',
                        silent: true,
                        animation: false,
                        itemStyle: {
                            normal: {
                                color: function(params){
                                    return colorListDefault[params.dataIndex];
                                }
                            }
                        },
                        data: maxArr
                    },
                    {
                        name:'党员人数',
                        type:'bar',
                        barWidth: '14',
                        itemStyle: {
                            normal: {
                                color: function(params){
                                    return new echarts.graphic.LinearGradient(
                                        0, 0, 0, 1,
                                        [
                                            {offset: 0, color: colorList[params.dataIndex].top},
                                            {offset: 0.5, color: colorList[params.dataIndex].middle},
                                            {offset: 1, color: colorList[params.dataIndex].bottom}
                                        ]
                                    )
                                }
                            },
                            emphasis: {

                            }
                        },
                        data: ageArr
                    },
                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            chart.setOption(option);

            var dangHtml = dangTpl({dangcount: res.data.dept_num, dangyuan: res.data.member_num, zhibu: res.data.branch_num});
            $('.group-count').append(dangHtml);

            var sexHtml = sexTpl({femal: res.data.rate_man, mal: res.data.rate_woman});
            $('.sex-ratio').append(sexHtml);

        } else {
            alert(res.msg);
        }
    })
    .fail(function() {
        console.log('网络请求失败');
    })


})()