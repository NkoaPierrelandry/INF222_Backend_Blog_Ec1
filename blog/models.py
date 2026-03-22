from django.db import models

# Create your models here.

class Article(models.Model):
    
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    contenu = models.TextField()
    autor = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    category = models.CharField(max_length = 55)
    tags  = models.CharField(max_length=255)

    class Meta :
        ordering = ['-date']

    def __str__(self):
        return self.name
