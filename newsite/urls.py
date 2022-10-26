from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('robots.txt', views.robots,name="robots.txt"),
    path('portfolio/', views.portfolio,name="portfolio"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('codepen/', views.codepen,name="codepen"),
    path('github/', views.github,name="github"),
    path('channel/', views.channel,name="channel"),
    path('stackoverflow/', views.stackoverflow,name="stackoverflow"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout")
]