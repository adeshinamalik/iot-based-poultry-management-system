from django.urls import path
from autopoultryweb import views

urlpatterns = [
	path('home', views.index),
]
