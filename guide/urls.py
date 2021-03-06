from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/*$', views.news_show, name='news_show'),
    url(r'^videos/*$', views.videos_show, name='videos_show'),
    url(r'^find/*$', views.search, name='search'),
    url(r'^visit/*$', views.visit, name='visit'),
    url(r'^connect/*$', views.connect, name='connect'),
    url(r'^collections/*$', views.collections_list, name='collections_list'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/*$', views.collection, name='collection'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/photos/*$', views.object_photos, name='object_photos'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/list/*$', views.object_list, name='object_list'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/category/*$', views.object_cats, name='object_cats'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/category/(?P<category>[a-z0-9\-]+)/*$', views.object_category, name='object_category'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/tours$', views.tours, name='tours'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/tours/(?P<tour>[a-z0-9\-]+)/*$', views.tour, name='tour'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/o/(?P<object>[a-z0-9\-]+)/*$', views.object, name='object'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/c/(?P<category>[a-z0-9\-]+)/(?P<object>[a-z0-9\-]+)/*$', views.object_w_category, name='object_w_category'),
    url(r'^collections/(?P<collection>[a-z0-9\-]+)/t/(?P<tour>[a-z0-9\-]+)/(?P<object>[a-z0-9\-]+)/*$', views.object_w_tour, name='object_w_tour'),
    url(r'^q/(?P<object>[a-z0-9\-]+)', views.object_search, name='object_search'),
    url(r'^forceupdate$', views.update_data, name='force_update')
]
