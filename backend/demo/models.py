from django.db import models

# Create your models here.
class Demo(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title

class MLHMember(models.Model):
    name = models.CharField(max_length=100, null=True, blank = True)
    avatar_url = models.CharField(max_length=1000, null=True, blank=True)
    member_url = models.CharField(max_length=1000,null=True, blank=True)

class Project(models.Model):
    name = models.CharField(max_length=100, null=True, blank = True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    avatar_url = models.CharField(max_length=1000, null=True, blank=True)
    project_url = models.CharField(max_length=1000,null=True, blank=True)
    commits_url = models.CharField(max_length=1000,null=True, blank=True)

class Commit(models.Model):
    author = models.CharField(max_length=100, null=True, blank = True)
    project = models.CharField(max_length=100, null=True, blank = True)
    description = models.CharField(max_length=10000,null=True, blank=True)
    commit_url = models.CharField(max_length=1000,null=True, blank=True)
