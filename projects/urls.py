from django.urls import path
from . import views

urlpatterns = [
    path('', views.projindex,name="projects"),
    path('notepad/', views.notepad,name="notepadP"),
    #path('javascript/', views.python,name="javascript"),
    #path('design/', views.python,name="design"),
    #path('design/bootstrap/', views.python,name="bootstrap")
]