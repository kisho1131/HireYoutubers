from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Youtuber(models.Model):
    crew_choices = {
        ('Solo', 'Solo'),
        ('Small', 'Small'),
        ('Large', 'Large'),
    }

    camera_choices = {
        ('canon', 'canon'),
        ('Nikon', 'Nikon'),
        ('Sony', 'Sony'),
        ('Red Camera', 'Red Camera'),
        ('Fuji', 'Fuji'),
        ('Panasonic', 'Panasonic'),
        ('others', 'others'),
    }

    category_choices = {
        ('Programing', 'Programing'),
        ('Mobile_Review', 'Mobile Review'),
        ('Motivation', 'Motivation'),
        ('Documantry', 'Documentary'),
        ('Movie', 'Movie'),
        ('Comedy', 'Comedy'),
        ('Tutorials', 'Tutorials'),
        ('Music', 'Music & Songs'),
    }
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = 'media/youtuber/%Y/%m')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices = crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255)
    subs_count = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    category = models.CharField(choices=category_choices, max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name + " " 
