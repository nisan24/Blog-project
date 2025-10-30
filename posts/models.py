from django.db import models
from django.contrib.auth.models import User
from categorys.models import CategoryModel

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ManyToManyField(CategoryModel)
    created_at = models.DateTimeField(auto_now_add= True)
    
    
    def __str__(self):
        return self.title