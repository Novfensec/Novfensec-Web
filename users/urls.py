from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles,name="profiles"),
    path('change', views.change, name="change")
    # path('deleteComment', views.deleteComment, name="deleteComment"),
    # path('<str:slug>/', views.blogPost,name="blogpost")
]