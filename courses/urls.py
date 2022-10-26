from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses,name="courses"),
    path('python/', views.python,name="python"),
    path('javascript/', views.python,name="javascript"),
    path('design/', views.python,name="design"),
    path('design/bootstrap/', views.python,name="bootstrap")
]