from django.db import models

# Create your models here.
class Funny_Videos(models.Model):
    title=models.CharField(max_length=200)
    video_embed_code=models.TextField('video_embed_code')
    on_posted=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
