from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm
from .models import ToDoList
from .forms import ListForm
from django.http import HttpResponseRedirect

def about(request):
    return render(request, "about.html", {})    

def addressbook(request):
    return render(request, "addressbook.html", {})    

def add_address(request):
    return render(request, "add_address.html", {})          

def contact(request):
    return render(request, "contact.html", {}) 

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Login was a Success'))
            return redirect('home')
        else:
            messages.success(request, ('Login Failed, please try again'))
            return redirect('login')
    else:
        return render(request, "login.html", {}) 


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = ToDoList.objects.all
            messages.success(request, ('To-Do items was added!'))
            return render(request, "home.html", {'all_items' : all_items})

    else:
        all_items = ToDoList.objects.all
        return render(request, "home.html", {'all_items' : all_items})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered'))
            return redirect('home')
    else:
        form = SignUpForm()   
    context = {'form': form}
    return render(request, "register.html", context) 

def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have edited your profile'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)   
    context = {'form': form}
    return render(request, 'edit_profile.html', context)

def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have edited your password!'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)   
    context = {'form': form}
    return render(request, 'change_password.html', context)

def delete(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('item has been deleted'))
    return redirect('home')

def cross_off(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.completed = True
    item.save()
    #messages.success(request, ('item has been crossed off'))
    return redirect('home')

def uncross(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.completed = False
    item.save()
    #messages.success(request, ('item has been uncrossed'))
    return redirect('home')

def edit_list(request, list_id):
    if request.method == 'POST':
        item = ToDoList.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('To-Do items was edited!'))
            return redirect('home')


    else:
        item = ToDoList.objects.get(pk=list_id)
        return render(request, "edit_list.html", {'item' : item})
            
