from django.db import models
from django.test import TestCase

from .fields import VideoField


class VideoFieldModel(models.Model):
    video = VideoField()


class VideoFieldTestCase(TestCase):

    def test_model_instanciation(self):
        instance = VideoFieldModel.objects.create(video='movie.webm')

        self.assertEqual(instance.video, 'movie.webm')
