from django.db import models

# Create your models here.
class Logo(models.Model):
    image=models.ImageField(upload_to='logo/')


    def __str__(self):
        return self.image
