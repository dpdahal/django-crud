from django.db import models


# Create your models here.

class User(models.Model):
    gender_filed = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    language_filed = [
        ('nepali', 'Nepali'),
        ('english', 'English'),
        ('chinese', 'Chinese')
    ]
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    gender = models.CharField(choices=gender_filed, max_length=10)
    language = models.CharField(choices=language_filed, max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_gallery', blank=True, null=True)

    def get_language(self):
        lang = self.language
        lang_object = lang.split(',')
        return lang_object
