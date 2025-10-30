from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length= 100)
    slug = models.SlugField(max_length= 255, unique= True)
    
    def __str__(self):
        return self.name