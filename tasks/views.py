from django.shortcuts import render, redirect
from tasks.models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.filter(completed=False)
    completed_tasks_list = []
    completed_tasks = Task.objects.filter(completed=True)
    
    for task in range(5):
        completed_tasks_list.append(completed_tasks[(len(completed_tasks)-1)-task])
    
    return render(request, 'list_tasks.html', {
        "tasks": tasks,
        "completed_tasks": completed_tasks_list
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

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/tasks/')

def update_task(request, task_id):
    if request.method == 'GET':
        task = Task.objects.filter(id=task_id)
        return render(request, 'update_task.html',{
            'id': task[0].id,
            'title': task[0].title,
            'description': task[0].description
        })
    else:
        new_title = request.POST['title']
        new_description = request.POST['description']
        
        task = Task.objects.get(id=task_id)
        task.title = new_title
        task.description = new_description
        task.save()
        
        return redirect('/tasks/')
