from django.db import models

# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=20)
    badge = models.CharField(max_length=20, default="New")

    def __str__(self):
        return self.title
