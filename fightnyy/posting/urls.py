from django.contrib import admin
from django.urls import path,include
from posting import views
urlpatterns = [
    path('create/',views.create,name='create'),
    path('',views.post,name='post'),
    path('detail<int:blog_id>/',views.detail,name='detail'),
    path('new/',views.new,name='new'),
]
