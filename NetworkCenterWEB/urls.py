"""NetworkCenterWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^getHotMomentsFromGrid', views.getHotMomentsFromGrid, name='getHotMomentsFromGrid'),
    url(r'^getPlotMomentStatData', views.getPlotMomentStatData, name='getPlotMomentStatData'),
    url(r'^getPlotMomentTrendData', views.getPlotMomentTrendData, name='getPlotMomentTrendData'),
    url(r'^getActiveAndCommentDegree', views.getActiveAndCommentDegree, name='getActiveAndCommentDegree'),
    url(r'^getNewsData', views.getNewsData, name='getNewsData'),
    url(r'^getIhomeEmoSource', views.getIhomeEmoSource, name='getIhomeEmoSource'),
    url(r'^getHotEventsFromEventsTJ', views.getHotEventsFromEventsTJ, name='getHotEventsFromEventsTJ'),
    url(r'^getYuqingEmo', views.getYuqingEmo, name='getYuqingEmo'),
    url(r'^getthreeindexs', views.getthreeindexs, name='getthreeindexs'),
    url(r'^getmapdata', views.getmapdata, name='getmapdata'),
    url(r'^$', views.ncbig),
    url(r'^detail', views.detail),
    url(r'^run', views.page_not_found),
    url(r'^admin', views.page_not_found),
]
handler404 = views.page_not_found
handler500 = views.page_error
