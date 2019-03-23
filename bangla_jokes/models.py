from django.db import models


# Create your models here.
class Bangla_Jokes(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    picture=models.ImageField(upload_to='bangla_jokes/',blank=True,null=True)
    on_posted=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
