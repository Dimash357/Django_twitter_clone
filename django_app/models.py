from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    # user = models.IntegerField(
    #     verbose_name="user",
    #     default=0,
    #     editable=True,
    #     blank=True
    # )
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=True,
        db_index=True,

        max_length=150
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f"Post: {self.title} {self.description[:30]} [{self.pk}]"


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images')
    first = models.ImageField(upload_to='profile_images', default='')
    second = models.ImageField(upload_to='profile_images', default='')
    third = models.ImageField(upload_to='profile_images', default='')
    forth = models.ImageField(upload_to='profile_images', default='')
    description = models.TextField(default='')
    city = models.TextField(default='')

    def __str__(self):
        return f'{self.user.username}'
