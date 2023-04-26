from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    @property
    def segidores(self):
        return self.siguiendo_a_set.all().count()

    def __str__(self) -> str:
        return self.username


class Perfil(models.Model):
    avatar = models.ImageField(default='rhan.jpg')
    apodo = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.apodo