from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    STATUS_CHOICES = [
        ('open', 'Открыт'),
        ('closed', 'Закрыт'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects', verbose_name='Автор')
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    github_url = models.URLField('Ссылка на GitHub', max_length=200, blank=True, null=True)
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='open')
    image = models.ImageField('Обложка проекта', upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='participated_projects', blank=True)

    favorited_by = models.ManyToManyField(
        User,
        related_name='favorite_projects',
        blank=True
    )

    def __str__(self):
        return self.name
