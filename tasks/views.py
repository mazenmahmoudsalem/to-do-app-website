from django.shortcuts import render, redirect
from . import models


def home(request):
    tasks = models.task.objects.all()
    if request.GET.get("task"):
        task = models.task.objects.get(title=request.GET.get("task"))
        task.delete()
        return redirect("tasks:home")
    if request.GET.get("end"):
        task = models.task.objects.get(title=request.GET.get("end"))
        task.is_ended = True
        task.save()
    if request.GET.get("reset"):
        task = models.task.objects.get(title=request.GET.get("reset"))
        task.is_ended = False
        task.save()
    if request.GET.get("taskcreate"):
        task = models.task()
        task.title = request.GET.get("taskcreate")
        task.save()
    context = {"tasks": tasks}
    return render(request, "index.html", context)