from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Forum
from .forms import UserCreationForm
# Create your views here.


def final(request):
    return render(request, 'base.html')


def account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
        context = {'form',form}
    return render(request,'account.html',{'form',form})


def index(request):
    questions = Forum.objects.all()
    context = {'question': questions}
    return render(request, 'index.html', context)


def createt(request):
    form = Forum(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'create_ques',{'form',form})


def editt(request,id):
    question = Forum.objects.get(id=id)
    form = Forum(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'edit_form.html',{'form',form})