from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=15)

    def __str__(self):
        return f"User: {self.username}"


class Project(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"Project: {self.name}"


class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Bug id: {self.id}"
