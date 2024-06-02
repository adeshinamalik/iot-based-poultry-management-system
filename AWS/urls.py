from django.urls import path
from autopoultryweb import views

urlpatterns = [
	path('', views.index),
	path('home', views.index),
]
