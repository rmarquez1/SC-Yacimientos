from django.conf.urls import patterns, url

from AnarWeb.apps.yacimientos import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
)