from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.IntegerField(blank=True)

class Topics(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=150, blank=True)
    parent_topic = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True
    )    

class Notes(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    topic = models.ForeignKey(
        Topics,
        on_delete = models.CASCADE,
    )
    parent_note = models.ForeignKey(
        'self',
        on_delete = models.CASCADE,
        null=True
    )
    related_note = models.ManyToManyField(
        'self',
    )

class Vocab(models.Model):
    word = models.CharField(max_length=50)
    part_of_speech = models.CharField(max_length=20, blank=True)
    definition = models.CharField(max_length=100, blank=True)
    topic = models.ForeignKey(
        Topics,
        on_delete = models.CASCADE
    )
