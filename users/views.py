from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentCreateForm


# Create your views here.
def home(*args, **kwargs):
    return HttpResponse("Hello World")


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
