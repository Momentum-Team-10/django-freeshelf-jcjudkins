from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=800, null=True, blank=True)
    url = models.URLField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=False)

    def __repr__(self):
        return f"<Book title={self.title} author={self.author}>"

    def __str__(self):
        return self.title




