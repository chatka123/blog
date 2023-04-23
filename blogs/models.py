from django.db import models
from django.contrib.auth.models import User


class BlockPost(models.Model):
    """Post which user wrote on his blog"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a string representation of the model"""
        return self.title


