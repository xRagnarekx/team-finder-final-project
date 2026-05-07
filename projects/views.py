from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Project
from .forms import ProjectForm


def index(request):
    projects_list = Project.objects.all().order_by('-created_at')

    paginator = Paginator(projects_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'projects/project_list.html', context={'page_obj': page_obj})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project-details.html', {'project': project})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)

            project.owner = request.user

            project.save()

            return redirect('projects:project_detail', pk=project.pk)
    else:

        form = ProjectForm()

    return render(request, 'projects/create-project.html', {'form': form})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/create-project.html', {'form': form})


@login_required
def complete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)

    if request.method == 'POST':
        project.status = 'closed'
        project.save()
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)


@login_required
def favorite_projects(request):
    projects = request.user.favorite_projects.all()
    return render(request, 'projects/favorite_projects.html', {'projects': projects})


@login_required
def toggle_favorite(request, pk):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=pk)

        if request.user in project.favorited_by.all():
            project.favorited_by.remove(request.user)
            status = 'removed'
        else:
            project.favorited_by.add(request.user)
            status = 'added'

        return JsonResponse({'status': status})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def participate_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        if request.user in project.participants.all():
            project.participants.remove(request.user)
            return JsonResponse({'status': 'removed'})
        else:
            project.participants.add(request.user)
            return JsonResponse({'status': 'added'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
