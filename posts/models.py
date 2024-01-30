from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=1000000)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

class User(Post, models.Model):
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=50)
  email = models.EmailField()