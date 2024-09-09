from django.urls import path
from django.contrib.auth.decorators import login_required
from projects.views import (
    project_detail,
    project_list,
    CreateProject,
    edit_project,
    delete,
    CategoryView,
    TagView,
)

urlpatterns = [
    path("", project_list, name="project_list"),
    path("<int:id>", project_detail, name="project_detail"),
    path("<int:id>/delete", delete, name="project_delete"),
    path("create", login_required(CreateProject.as_view()), name="project_create"),
    path("<int:id>/edit", edit_project, name="edit_project"),
    path("category/<str:category>", CategoryView.as_view(), name="category"),
    path("tags/<str:tag>", TagView.as_view(), name="tag"),
    path("<int:id>/donate", edit_project, name="donate"),
]
