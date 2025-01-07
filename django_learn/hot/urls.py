from django.urls import path
from hot import views


urlpatterns = [
    path('',views.index),
    path('about/', views.about)
]
