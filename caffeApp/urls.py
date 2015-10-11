from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image_app$', views.image_app, name='image_app'),
    url(r'^image_upload$', views.list, name='image_list'),
]
