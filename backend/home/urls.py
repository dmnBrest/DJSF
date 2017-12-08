from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ngtest$', views.ng_test, name='ng_test'),
]