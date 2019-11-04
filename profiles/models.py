from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=50, blank=False, null=True)
    contact = models.CharField(max_length=25)
    bio = models.TextField(max_length=250)
    links = models.CharField(max_length=255) 

    def __str__(self):
        return f"My name is{self.name}"

