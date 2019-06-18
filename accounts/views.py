from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404,get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .forms import Login, RegisterForm
from django.contrib import auth, messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    return HttpResponse("Hello World")


@login_required(login_url='/login/')
def users(request):
    users = get_list_or_404(User)
    context = {'users': users}
    return render(request, 'users.html', context)


def login(request):
    if request.user.is_active:
        return redirect('/accounts/users/')
    form = Login(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        user = auth.authenticate(email=request.POST.get('email'),
                                 password=request.POST.get('password'))
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You have successfully logged in")
            if next:
                return redirect(next)
            return HttpResponseRedirect('/')
        else:
            form.add_error(None, "Your email or password was not recognised")
            return render(request, 'login.html', {'form': form})
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout(request):
    django_logout(request)
    return redirect('/login/')


# @login_required(login_url='/login/')
def registration(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)
