from django.conf.urls import url

from . import views

app_name = 'file_manager'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]