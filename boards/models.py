from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name="topics", on_delete=models.CASCADE)
    creation = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name="topics", on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.CharField(max_length=4000)
    created_by = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    creation = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.message
