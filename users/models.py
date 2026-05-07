from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
