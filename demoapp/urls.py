from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.hello),
    path('emp',views.emp),
    path('api', views.ChartData.as_view()),
    path('new', views.HomeView.as_view()),
    path('coursera',views.coursera,name="coursera")

]