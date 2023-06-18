from django.shortcuts import render, HttpResponse
from home.models import task

# Create your views here.

def home(request):
    context={'sucess':False}
    if request.method == "POST":
        title =request.POST['title']
        desc = request.POST['desc']
        ins = task(taskTitle=title, taskDesc=desc)
        ins.save()
        context={'sucess':True}
    return render(request, 'index.html', context)
def tasks(request):
    allTasks = task.objects.all()
    # for item in allTasks:
    #     print(item.taskTitle) 
    context = {'tasks':allTasks}
    return render(request, 'tasks.html',context)