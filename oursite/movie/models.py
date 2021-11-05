from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default='hollywood')
    duration = models.FloatField()
    rating = models.FloatField() 
    image = models.ImageField(upload_to = 'media', default='Image/None/img.jpg')

    def __str__(self):
        return self.title
