from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=150)
    nachname = models.CharField(max_length=150)
    def __str__(self):
        return self.name