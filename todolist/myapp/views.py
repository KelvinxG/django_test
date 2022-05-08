from django import http
from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import Todo
def index(request):
    todos= Todo.objects.all()
    if request.method=='POST':
        content=request.POST.get('content')
        todo=Todo(content=content)
        todo.save()
    return render(request,'app/index.html',{'todos':todos})

def delete_todo(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return http.HttpResponseRedirect('/')

def update_todo(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=='POST':
        content=request.POST.get('content')
        todo.content=content
        todo.save()
        return http.HttpResponseRedirect('/')
    return render(request,'app/update.html',{'todo':todo})