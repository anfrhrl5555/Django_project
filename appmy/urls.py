from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('success/', views.success),
]
