from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')

    class Meta:
        ordering = ['-priority', '-created_date']
