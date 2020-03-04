from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)

class Topic(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=150, blank=True)
    parent_topic = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class Note(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    topic = models.ForeignKey(
        Topic,
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
        Topic,
        on_delete = models.CASCADE
    )
