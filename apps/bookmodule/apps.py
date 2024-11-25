from django.apps import AppConfig
from django.db import models


class BookmoduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bookmodule'

class Book(models.Model):
 title = models.CharField(max_length = 50)
 author = models.CharField(max_length = 50)
 price = models.FloatField(default = 0.0)
 edition = models.SmallIntegerField(default = 1)