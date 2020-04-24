from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    image = models.ImageField(upload_to="pics", default="default.png")

    def get_absolute_url(self):
        return reverse('page',)