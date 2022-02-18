from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name="profile",
        verbose_name="Профиль",
        on_delete=models.CASCADE,
    )
    github = models.URLField(
        max_length=200,
        null=True,
        blank=False,
        verbose_name="ссылка на github",
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=False,
        verbose_name="О себе",
    )
    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to="avatars/",
        null=True,
        blank=False,
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"{self.user.username}. {self.id}"
