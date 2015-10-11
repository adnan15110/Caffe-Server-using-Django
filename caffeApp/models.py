from django.db import models

# Create your models here.


class ClassifierResult(models.Model):
    model_name = models.CharField(max_length=50, default="none")
    predicted_class = models.CharField(max_length=20)
    image_loaction = models.CharField(max_length=100)
    all_results = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.predicted_class


class Image(models.Model):
    imagefile = models.FileField(upload_to='images')
