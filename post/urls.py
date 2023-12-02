from django.urls import path
from .views import post, detail

urlpatterns = [
    path('', post, name='post'),
    path('detail/<str:pk>', detail, name='detail'),

]