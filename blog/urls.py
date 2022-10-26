from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.blog,name="blog"),
    path('search', views.search,name="search"),
    path('postComment', views.postComment, name="postComment"),
    path('deleteComment', views.deleteComment, name="deleteComment"),
    path('users/administrator/dashboard/new', views.BlogDashboard, name="AdminBlogDashboard"),
    # path('users/administrator/dashboard/edit/<str:slug>', views.EditBlogPost, name="EditBlogPost"),
    path('<str:slug>/', views.blogPost,name="blogpost")
]