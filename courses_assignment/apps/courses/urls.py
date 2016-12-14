from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^courses$', views.courses),
	url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name='check-course'),
	url(r'^courses/delete/(?P<id>\d+)$', views.delete, name='delete-course')
]