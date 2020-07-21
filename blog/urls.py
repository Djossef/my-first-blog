from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<str:post_title>/', views.post_detail, name='post_detail'),
    path('Covid-19', views.covid_tracker, name='covid')
]
