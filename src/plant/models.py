from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Plant(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField(default="")  # Setting the default value to an empty string.
    image_url = models.URLField(default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.scientific_name