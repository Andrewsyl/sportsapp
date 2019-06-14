from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, User, Club, Team
from .forms import StudentCreateForm, ClubCreateForm, Login, RegisterForm, StudentEditForm, TeamCreateForm, TeamEditForm
from django.contrib import auth, messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(*args, **kwargs):
    return HttpResponse("Hello World")


@login_required(login_url='/login/')
def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)


def login(request):
    if request.user.is_active:
        return redirect('/')
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
            return HttpResponseRedirect('/users/')
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
        return HttpResponseRedirect('/users/')
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)


@login_required(login_url='/login/')
def student_create(request):
    club = request.user.club
    teams = Team.objects.filter(club=club)
    form = StudentCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.club = club
        instance.save()
        return redirect('/student_list/')
    context = {
        'form': form,
        'teams': teams
    }
    return render(request, 'students/student_form.html', context)


@login_required(login_url='/login/')
def student_list(request):
    user = request.user
    kids = Student.objects.filter(club=user.club)
    context = {'kids': kids}
    return render(request, 'students/student_list.html', context)


@login_required(login_url='/login/')
def student_details(request, id):
    kid = get_object_or_404(Student, id=id)
    context = {'kid': kid}
    return render(request, 'students/student_details.html', context)


@login_required(login_url='/login/')
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('/student_list/')
    context = {
        'student': student
    }
    return render(request, "students/student_delete.html", context)


@login_required(login_url='/login/')
def student_edit(request, id):
    user = request.user
    kid = Student.objects.filter(club=user.club, id=id).first()
    form = StudentEditForm(request.POST or None, instance=kid)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/student_list')
    context = {'kid': kid,
               'form': form}
    return render(request, 'students/student_edit.html', context)


@login_required(login_url='/login/')
def club_create(request):
    try:
        club_instance = Club.objects.get(user=request.user)
    except Club.DoesNotExist:
        club_instance = Club(user=request.user)
    form = ClubCreateForm(request.POST or None, instance=club_instance)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.club = request.club
        instance.save()
        return redirect('/student_list/')
    context = {
        'form': form
    }
    return render(request, 'club_create.html', context)


@login_required(login_url='/login/')
def team_list(request):
    club = request.user.club
    teams = Team.objects.filter(club=club)
    context = {'teams': teams}
    return render(request, 'teams/team_list.html', context)


def team_details(request, id):
    club = request.user.club
    team = Team.objects.filter(club=club, id=id).first()
    kids = Student.objects.filter(team=team)
    context = {'team': team,
               'kids': kids}
    return render(request, 'teams/team_details.html', context)


@login_required(login_url='/login/')
def team_create(request):
    club = request.user.club
    form = TeamCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.club = club
        instance.save()
        return redirect('/team_list/')
    context = {
        'form': form
    }
    return render(request, 'teams/team_create.html', context)


@login_required(login_url='/login/')
def team_edit(request, id):
    club = request.user.club
    team = Team.objects.filter(club=club, id=id).first()
    form = TeamEditForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/team_list')
    context = {'team': team,
               'form': form}
    return render(request, 'students/student_edit.html', context)
