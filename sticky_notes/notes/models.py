from django.db import models


# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title