from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name =  models.CharField(max_length= 250)
    role = models.CharField(max_length=250)
    fb_link = models.CharField(max_length=250)
    linkedIn_link  = models.CharField(max_length=250)
    photo = models.ImageField(upload_to = 'media/Team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " +self.last_name

class Slider(models.Model):
    headline = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    button_url = models.URLField(default=True)

    def __str__(self):
        return self.headline
