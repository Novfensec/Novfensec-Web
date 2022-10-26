from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login

# Create your views here.
def profiles(request):
    if request.user.is_active:
        return render(request, "users/userProfiles.html")
    else:
        context={'error':'404'}
        return render(request,'newsite/error.html', context)

def change(request):
    if request.user.is_active:
        if request.method=='POST':
            username=request.POST.get('updateusername')
            email=request.POST.get('updateemail')
            firstName=request.POST.get('updatefname')
            lastName=request.POST.get('updatelname')
            oldpassword=request.POST.get('updatepass1')
            newpassword=request.POST.get('updatepass2')
            user=User.objects.get(username=request.user.username)
            if check_password(oldpassword,request.user.password):
                user.username=username
                user.email=email
                user.first_name=firstName
                user.last_name=lastName
                if newpassword:
                    user.set_password(newpassword)
                    user.save()
                    myuser=authenticate(username= username, password= newpassword)
                    login(request, myuser)
                else:
                    user.save()
    return redirect(request.META.get("HTTP_REFERER"))