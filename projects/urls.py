from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_project, name='create_project'),
    path('favorites/', views.favorite_projects, name='favorite_projects'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('<int:pk>/complete/', views.complete_project, name='complete_project'),
    path('<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('<int:pk>/participate/', views.participate_project, name='participate'),
]
