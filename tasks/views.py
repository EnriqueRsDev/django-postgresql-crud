from django.shortcuts import render, redirect
from tasks.models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {
        "tasks": tasks
    })

def create_task(request):
    title = request.POST['title']
    description = request.POST['description']
    
    # Creating an instance of the class Task
    task = Task(title=title, description=description)
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
