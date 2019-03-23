from django.db import models

# Create your models here.
class Programming_Jokes(models.Model):
    title=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='Programming_Jokes')
    on_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.title
