from django.urls import path, include,re_path
from .import views
app_name ='blog'
urlpatterns = [
    path('index/', views.index),
    path('edit/', views.edit_page),
    re_path(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page' ),
]