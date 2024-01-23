from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username}')
            return redirect('user-login')
    else:
        form =CreateUserForm()
    context={
        'form':form,
    }
    return render(request,'register.html',context)

@login_required(login_url='user-login')
def profile(request):
    return render(request,'profile.html')


@login_required(login_url='user-login')
def profile_update(request):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save and profile_form.save()
            return render(request,'profile.html')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request,'profile_update.html',context)