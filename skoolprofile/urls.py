from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.school_list, name='school_list'),
]