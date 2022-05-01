from django.db import models

class Zapchasti(models.Model):
    name = models.CharField('название', max_length=200)
    image = models.TextField('URL изоображения', max_length=5000)
    price = models.CharField('цена', max_length=200)
