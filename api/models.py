from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField(blank=True)
    github = models.URLField(blank=True)
    live = models.URLField(blank=True)

    def __str__(self):
        return self.title
class Skill(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.title