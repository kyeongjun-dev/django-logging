from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('debug/', views.debug),
    path('info/', views.info),
    path('error/', views.error),
]