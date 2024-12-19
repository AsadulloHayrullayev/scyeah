from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationUserForm,CustomAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request, user
            )
            return redirect('home')
    else:
        form = CustomUserCreationUserForm()
    return render(request,'accounts/register.html',{'form':form})


def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')   
            password = form.cleaned_data.get('password')  
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')           


def home(request):
    return render(request,'accounts/home.html')