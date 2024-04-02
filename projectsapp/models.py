from django.db import models

# Create your models here.
class Project(models.Model):
    month = models.CharField(max_length=20)
    assigned = models.IntegerField()
    completed = models.IntegerField()