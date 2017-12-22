from django.db import models

# Create your models here.
class Santa(models.Model):
    santa_name = models.TextField(max_length=40)
    santa_photo_url = models.TextField(max_length=200)

class Kid(models.Model):
    kid_name = models.TextField(max_length=40)
    kid_photo = models.TextField(max_length=200)