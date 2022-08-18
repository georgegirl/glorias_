from django.urls import path
from . import views

urlpatterns =[
    path('class_app/', views.home_hello),
    path('class-app/', views.run_page),
    path('another/', views.another_page),

]