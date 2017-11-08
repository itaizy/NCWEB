/**
 * Created by ACT on 7/8/2017.
 */
require.config({
    baseUrl: "/static",
    paths: {
        'main': 'src/js/main',

        'jquery': 'node_modules/jquery/dist/jquery.min',
        'bootstrap': 'node_modules/bootstrap/dist/js/bootstrap.min',

        'validate': 'vendor/js/jquery-validation/1.11.1/jquery.validate.min',
        'validate_zh': 'vendor/js/jquery-validation/1.11.1/messages_bs_zh',
        'datetimepicker': 'vendor/js/bootstrap-datetimepicker/bootstrap-datetimepicker.min',
        'datetimepicker.zh-CN': 'vendor/js/bootstrap-datetimepicker/locales/bootstrap-datetimepicker.zh-CN',
        'switch': 'vendor/js/bootstrap-switch/bootstrap-switch.min',
        'notify': 'vendor/js/common/bootstrap-notify.min',
        'tooltip': 'vendor/js/common/jquery.tooltip',
        'raphael': 'vendor/js/common/raphael.min',
        'highcharts': 'vendor/js/common/highcharts.min',
        'higstock': 'vendor/js/common/highstock.min',
        'map': 'vendor/js/common/map.min',
        'date.format': 'vendor/js/common/date.format',
        'exporting': 'vendor/js/common/exporting.min',
        'echarts': 'vendor/js/common/echarts-3.5.2.min',
        'webui-popover': 'vendor/js/common/jquery.webui-popover.min',
        'datatables': 'vendor/js/common/jquery.dataTables.min',
        'fancybox': 'vendor/js/common/jquery.fancybox.pack.min',
        'contextmenu': 'vendor/js/common/jquery.contextmenu.min',
        'pjax': 'vendor/js/common/jquery.pjax.min',
        'nav2': 'vendor/js/common/jquery.nav2',
        'MarkerClusterer': 'vendor/js/common/MarkerClusterer.min',
        'TextIconOverlay': 'vendor/js/common/TextIconOverlay.min',
        'jqcloud': 'vendor/js/common/jqcloud-1.0.4.min',
        'jsapi': 'vendor/js/common/jsapi.min',
        'google': 'vendor/js/common/google.min',
        // 'gmap' : 'gmap.min',
        'chinamap': 'vendor/js/common/china',
        'wordcloud': 'vendor/js/common/wordcloud',
        'd3': 'vendor/js/common/d3.min',
        'd3.cloud': 'vendor/js/common/d3.layout.cloud',
        'sankey': 'vendor/js/common/sankey',
        'underscore': 'vendor/js/common/underscore-min',
        'mustache': 'vendor/js/common/mustache.min',
        'streamgraph': 'vendor/js/common/streamgraph.min',

        'Blob': 'vendor/js/excel/Blob',
        'Export2Excel': 'vendor/js/excel/Export2Excel',
        'FileSaver': 'vendor/js/excel/FileSaver',
        'xlsx': 'vendor/js/excel/xlsx',
        'jszip': 'vendor/js/excel/jszip',

        'index_build': 'src/js/index_build',
        'index_build1': 'src/js/index_build1',
        'demo': 'src/js/demo1',
        'neo4j':'src/js/neo4jGraph',
        'tjneo':'src/js/tjneo4j',
        'monitor': 'src/js/monitor',
        'ihome': 'src/js/ihome',
        'getgmap': 'src/js/getgmap',
        'bmap': 'src/js/bmap',
        'tjbmap':'src/js/tjbmap',
        'util': 'src/js/util',
        'weiboUtils': 'src/js/weiboUtils',
        'highstock': 'src/js/highstock',
        'jquery-ui-1.9.2.custom.min': 'src/js/jquery-ui-1.9.2.custom.min',
        'jquery.vticker.min':'src/js/jquery.vticker.min',
        // 'mapfiles' : '../mapfiles/api-3/8/2/main',

        'EventStatistics': 'src/js/EventStatistics',
        'jquery.tabslet.min':'vendor/js/common/jquery.tabslet.min',
        'browser-sync-client.2.13.0':'vendor/js/common/browser-sync-client.2.13.0',
        'BreakingNews':'vendor/js/common/BreakingNews',
        'laydate':'vendor/js/laydate/laydate',
        'djyun':'src/js/djyun',
        'djyun_big':'src/js/djyun_big',
        'djyun_big_map':'src/js/djyun_big_map',
        'mobiletest': 'src/js/mobiletest',
        'index_static': 'dist/js/index_static'
    },
    shim: {
        'bootstrap': ['jquery'],
        'highstock': ['jquery'],
        'validate': ['jquery'],
        'validate_zh': ['validate'],
        'datetimepicker': ['jquery'],
        'raphael': ['jquery'],
        'datetimepicker.zh-CN': ['datetimepicker'],
        'map': ['jquery', 'raphael', 'tooltip'],
        'google': ['jsapi'],
        'datatables': ['jquery'],
        'fancybox': ['jquery'],
        'contextmenu': ['jquery'],
        'jqcloud': ['jquery'],
        'd3.cloud': ['d3'],
        'sankey': ['d3'],
        'tjbmap': ['TextIconOverlay', 'MarkerClusterer'],
        // highchart err 16
        // 'demo': ['echarts', 'highstock', 'map', 'jqcloud', 'd3.cloud', 'sankey', 'weiboUtils', 'date.format'],
        'demo': ['echarts', 'map', 'jqcloud', 'd3.cloud', 'sankey', 'weiboUtils', 'date.format'],
        'neo4j':['echarts'],
        'tjneo':['echarts'],
        'monitor': ['echarts', 'highcharts', 'd3.cloud', 'date.format', 'TextIconOverlay', 'MarkerClusterer'],
        'bmap': ['TextIconOverlay', 'MarkerClusterer'],
        'ihome': ['datatables'],
        'EventStatistics': ['highcharts'],
        'mustache': {
            exports: 'Mustache'
        },
        'xlsx': {
            deps: ['jszip']
        },
        'Export2Excel': ['Blob', 'FileSaver','xlsx'],
        'jquery.vticker.min':['jquery'],
        'jquery.tabslet.min':['jquery'],
        'browser-sync-client.2.13.0':['jquery'],
        'BreakingNews':['jquery'],
        'nav2':['jquery','chinamap'],
        'tooltip':['jquery'],
        'djyun':['jquery'],
        'mobiletest': {
            exports: 'mobiletest',
        },
        'highcharts': {
            exports: "Highcharts",
            deps: ["jquery"],
        },
        // 'laydate':['jquery'],
        // 'djyun':['jquery','jquery.tabslet.min','browser-sync-client.2.13.0','BreakingNews']
    },
    waitSeconds: 0
});
require(['jquery', 'bootstrap', 'underscore'], function ($) {
    return {};
});