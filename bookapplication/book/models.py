from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

