from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content
