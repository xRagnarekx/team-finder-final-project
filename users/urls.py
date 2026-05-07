from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, reverse_lazy
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', views.register, name='register'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='users/change_password.html',
        success_url=reverse_lazy('users:edit_profile')
    ), name='change_password'),

    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('list/', views.user_list, name='list'),
    path('<int:pk>/', views.profile_detail, name='profile_detail'),
]
