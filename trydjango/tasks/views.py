from django.shortcuts import render, HttpResponseRedirect
from .forms import UserSignupForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.

def Home_View(request):
    return render(request, 'base.html')

# View Function for Login form
def Login_View(request):
    if request.method == 'POST':
        fm = AuthenticationForm(data = request.POST)
        if fm.is_valid():
            UserName= fm.cleaned_data['username']
            PassWord = fm.cleaned_data['password']
            user = authenticate(username =UserName, password = PassWord)
            if user is not None:
                login(request, user)
                # request.session.set_expiry(3000)
                return HttpResponseRedirect('/profile/')

    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form':fm})


def Signup_View(request):
    if request.method == 'POST':
        fmd = UserSignupForm(request.POST)

        if fmd.is_valid():
            fmd.save()
    else:
        fmd = UserSignupForm()
    return render(request, 'signup.html', {'form':fmd})



def Profile_View(request):
    
    if request.user.is_authenticated:
        form  = User.objects.all()
    
        return render(request, 'profile.html', {'form':form})
    else:
         return HttpResponseRedirect('/login/') 



def Delete_View(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        obj.delete()
        return HttpResponseRedirect('/profile/')


def Update_View(request, id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=User.objects.get(pk=id)
            form=UserSignupForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                # update_session_auth_hash(request, form.User)
                return HttpResponseRedirect('/profile/')
        else:
            pi=User.objects.get(pk=id)
            form=UserSignupForm(instance=pi)
    else:
        return HttpResponseRedirect('/login/')
    
    return render(request, "update.html", {"form":form})


def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

