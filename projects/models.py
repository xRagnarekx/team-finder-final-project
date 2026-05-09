from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

MAX_LENGTH_NAME = 200
MAX_LENGTH_URL = 200
MAX_LENGTH_STATUS = 10

STATUS_OPEN = 'open'
STATUS_CLOSED = 'closed'
STATUS_CHOICES = [
    (STATUS_OPEN, 'Открыт'),
    (STATUS_CLOSED, 'Закрыт'),
]


class Project(models.Model):
    name = models.CharField('Название', max_length=MAX_LENGTH_NAME)
    description = models.TextField('Описание')
    github_url = models.URLField('Ссылка на GitHub', max_length=MAX_LENGTH_URL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects', verbose_name='Автор')
    status = models.CharField('Статус', max_length=MAX_LENGTH_STATUS, choices=STATUS_CHOICES, default=STATUS_OPEN)
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
