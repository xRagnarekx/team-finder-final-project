from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'github_url', 'image']


labels = {
    'name': 'Название',
    'description': 'Описание',
    'github_url': 'Ссылка на GitHub',
    'image': 'Обложка проекта',
}
