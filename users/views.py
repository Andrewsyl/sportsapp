from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, User
from .forms import StudentCreateForm, Login, RegisterForm
from django.contrib import auth, messages


# Create your views here.
def home(*args, **kwargs):
    return HttpResponse("Hello World")


def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)


def stuff(request, *args, **kwargs):
    jim = 'Whataawa test'
    print(request.user)
    user = request.user
    return HttpResponse("Hello World")


def contact(request, *args, **kwargs):
    context = {
        'user': request.user,
        'my_list': [88, 23, 213, 1231]
    }
    return render(request, 'home.html', context)


def login(request):
    form = Login(request.POST or None)
    if form.is_valid():
        user = auth.authenticate(email=request.POST.get('email'),
                                 password=request.POST.get('password'))
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You have successfully logged in")
            return HttpResponseRedirect('/')
        else:
            form.add_error(None, "Your email or password was not recognised")
            return render(request, 'login.html', {'form': form})
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def registration(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/users/')
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)


def student_create(request):
    form = StudentCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentCreateForm()
    context = {
        'form': form
    }
    return render(request, 'students/student_form.html', context)


def student_details(request):
    kids = Student.objects.all()
    context = {'kids': kids}
    return render(request, 'students/details.html', context)
