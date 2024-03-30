from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.show_comments, name='index'),
    path('addcomment/', views.post_comment, name='post_comment'),
    path('likes/', views.like_post, name='like')
]