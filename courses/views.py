from django.shortcuts import render

# Create your views here.
def courses(request):
    return render(request,'courses/allcourse.html')

def python(request):
    return render(request,'courses/python.html')