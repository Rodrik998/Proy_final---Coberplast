from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    birth_date = models.DateField( auto_now=False, auto_now_add=False)