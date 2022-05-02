from datetime import datetime
from uuid import uuid4

from django.db import models

class User_test(models.Model):
    username = models.CharField(max_length=64,unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.CharField(max_length=128,unique=True)

class Project(models.Model):
    name = models.CharField(max_length=64)
    links_repo = models.CharField(max_length=128)
    user = models.ForeignKey(User_test,on_delete=models.CASCADE)

class ToDo_list(models.Model):
    project_name = models.OneToOneField(Project,on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateField(default=datetime.now)
    updated = models.DateField(default=datetime.now)
    user = models.OneToOneField(User_test,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
