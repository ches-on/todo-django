from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def index (request):
    mem = Task.objects.all()
    return render(request, 'index.html', {'mem':mem})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    x=request.POST["taskname"]
    y=request.POST["starttime"]
    z=request.POST["endtime"]
    w=request.POST["description"]
    mem= Task(taskname=x ,starttime=y, endtime=z, description=w )
    mem.save()
    return  redirect("/")

def delete(request,id):
    mem = Task.objects.get(id=id)
    mem.delete()
    return redirect("/")
    
def update(request, id):
    mem = Task.objects.get(id=id)
    return render(request,'update.html', {'mem':mem})

def uprec (request, id):
    w=request.POST["description"]
    x=request.POST["taskname"]
    y=request.POST["starttime"]
    z=request.POST["endtime"]
    mem = Task.objects.get(id =id)
    mem.taskname=x
    mem.starttime=y
    mem.endtime=z
    mem.description=w
    mem.save()
    return redirect("/")



