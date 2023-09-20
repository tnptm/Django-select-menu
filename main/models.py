from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    """
    Projects table to database which has name and user fields for data including primary key field.
    """
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        """
        This function explain what field(s) will describe the data rows the best way
        """
        return self.name
    
    class Meta:
        """
        On admin page the name of class is properly referred with verbose_name
        """
        verbose_name = "Project"

