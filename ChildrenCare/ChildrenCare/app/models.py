from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=150)
    nachname = models.EmailField(blank=True)
    def __str__(self):
        return self.name