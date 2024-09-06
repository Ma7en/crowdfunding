from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.


def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, "projects/project_detail.html", {"project": project})


def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "add_project.html", {"form": form})


def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_detail", project_id=project_id)
    else:
        form = ProjectForm(instance=project)
    return render(request, "edit_project.html", {"form": form, "project": project})
