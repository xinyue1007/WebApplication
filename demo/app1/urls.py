
from . import views as app1_views
from django.conf.urls import url

urlpatterns = [
      #主页
      url(r'^$', app1_views.index, name='index'),
]