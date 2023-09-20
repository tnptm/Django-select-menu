from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
