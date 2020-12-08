from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Forum
from .forms import Former
# Create your views here.


def final(request):
    return render(request, 'base.html')


def index(request):
    questions = Forum.objects.all()
    context = {'question': questions}
    return render(request, 'index.html', context)


def createt(request):
    form = Former(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'create_ques',{'form':form})


def editt(request,id):
    question = Forum.objects.get(id=id)
    form = Former(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'edit_form.html',{'form':form})

def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            redirect('final')
    else:
        form = AuthenticationForm()

    return render(request,'login.html', {'form':form})


def logoutuser(request):
    logout(request)
    return redirect('final')


def account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('final')
    else:
        form = UserCreationForm()
    return render(request,'account.html',{'form':form})

def resource(request):
    return render(request, 'resource.html')
