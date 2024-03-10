from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140) # types of data column can hold 
    text = models.TextField()
    published = models.DateField(auto_now_add=True)
    
    