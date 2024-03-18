# blog/urls.py
from django.urls import path
from . import views

app_name = 'signlanguagetochatgpt'
urlpatterns = [
    path('', views.home, name='home'),
    path('chatgpt/', views.chatgpt, name='chatgpt'),
    path('chatgpt/chat1', views.chat1, name='chat1'),
    path('signchatgpt/', views.signchatgpt, name='signchatgpt'),
    path('signchatgpt/chat', views.chat, name='chat'),
]
