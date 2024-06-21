from django.urls import path
from . import views

urlpatterns = [
    path('pre/', views.new_page, name='new_page'),
    path('users/', views.users, name='users'),
    path('', views.index_main, name='index_main'),
    path('about/', views.about_main, name='about_main'),
]
