from django.db import models

class Status(models.TextChoices):
    UNSTARTED = 'u', 'Not started yet'
    OMGOING = 'o', 'On going'
    FINISHED = 'f', 'Finished'

class Task(models.Model):
    name = models.CharField(verbose_name='Task name',max_length=255, unique=True)
    status = models.CharField(verbose_name='Task status', max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name