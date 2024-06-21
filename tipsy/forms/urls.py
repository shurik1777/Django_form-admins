from django.urls import path
from . import views

urlpatterns = [
    path('pre/', views.new_page, name='new_page'),
    path('users/', views.users, name='users'),
]
