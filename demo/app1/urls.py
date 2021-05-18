
from . import views as app1_views
from django.conf.urls import url
app_name = 'app1'
urlpatterns = [
      #主页
      url(r'^$', app1_views.index, name='index'),
      #显示所有主题
      url(r'^topics/$', app1_views.topics, name='topics'),
      #特定主题的详细页面w
      url(r'^topics/(?P<topic_id>\d+)/$', app1_views.topic, name='topic'),
]