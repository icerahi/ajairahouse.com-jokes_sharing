from django.db import models

# Create your models here.
class Fci_Troll(models.Model):
    title=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='fci_troll')
    on_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
