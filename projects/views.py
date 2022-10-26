from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.
def projindex(request):
    return render(request,'projects/projects.html')

def notepad(request):
    zip_file = open(os.path.join('./projects/downloads/notepad.zip'), 'rb')
    return FileResponse(zip_file)
