from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import UserEditForm, CustomUserCreationForm, ProfileEditForm
from .models import Profile

User = get_user_model()


def paginate_queryset(request, queryset, per_page=12):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def user_list(request):
    sort_by = request.GET.get('sort_by', 'new')
    if sort_by == 'name':
        users = User.objects.exclude(id=request.user.id).order_by('first_name', 'last_name')
    else:
        users = User.objects.exclude(id=request.user.id).order_by('-date_joined')

    page_obj = paginate_queryset(request, users, 12)

    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
    }
    return render(request, 'users/participants.html', context)


def profile_detail(request, pk):
    user_profile = get_object_or_404(User, pk=pk)
    return render(request, 'users/user-details.html', {'profile': user_profile})


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:profile_detail', pk=request.user.pk)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/edit_profile.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('projects:index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})
