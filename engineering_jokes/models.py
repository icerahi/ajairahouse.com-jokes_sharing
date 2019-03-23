from django.db import models

# Create your models here.
class Engineering_Jokes(models.Model):
    title=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='engineering_jokes')
    on_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
