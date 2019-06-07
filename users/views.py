from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, User
from .forms import StudentCreateForm, Login, RegisterForm, StudentEditForm
from django.contrib import auth, messages


# Create your views here.
def home(*args, **kwargs):
    return HttpResponse("Hello World")


def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)


def login(request):
    form = Login(request.POST or None)
    if form.is_valid():
        user = auth.authenticate(email=request.POST.get('email'),
                                 password=request.POST.get('password'))
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You have successfully logged in")
            return HttpResponseRedirect('/users/')
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


def student_list(request):
    kids = Student.objects.all()
    context = {'kids': kids}
    return render(request, 'students/student_list.html', context)


def student_details(request, id):
    kid = get_object_or_404(Student, id=id)
    context = {'kid': kid}
    return render(request, 'students/student_details.html', context)


def student_edit(request, id):
    kid = get_object_or_404(Student, id=id)
    form = StudentEditForm(request.POST or None, instance=kid)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/student_list')
    context = {'kid': kid,
               'form': form}
    return render(request, 'students/student_edit.html', context)
