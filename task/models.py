from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    datecomplete = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__ (self):
        return self.title + '- by ' + self.user.username