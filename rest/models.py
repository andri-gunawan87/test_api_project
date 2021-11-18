from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length = 60, blank = True)
    alias = models.CharField(max_length = 60, blank = True)
    
    def __str__(self):
        return self.name