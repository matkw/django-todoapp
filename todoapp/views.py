from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from todoapp.models import Task


def index(request):
    task_list = Task.objects.order_by('-added_time')
    context = {
        "task_list": task_list,
    }
    return render(request, 'todoapp/index.html', context)


@csrf_exempt
def add_task(request):
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        now = timezone.now()
        task = Task(name=task_name, added_time=now)
        task.save()
        response = redirect('/todoapp/')
        return response


@csrf_exempt
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        response = redirect('/todoapp/')
        return response
    return render(request, 'index.html', {})


@csrf_exempt
def clear_task_list(request):
    if request.method == "POST":
        Task.objects.all().delete()
        response = redirect('/todoapp/')
        return response
    return render(request, 'index.html', {})
