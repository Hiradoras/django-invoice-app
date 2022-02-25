from email.policy import default
from django.db import models
from django.forms import CharField
from datetime import datetime

class Receiver(models.Model):
    """
    Class for company that receives the invoice 
    """
    name = models.CharField(default = "",max_length=200)
    address = models.TextField()
    website = models.URLField(blank=True)
    created = models.DateTimeField(default=datetime.now)

    logo = models.ImageField(default="images/no_photo.png")

    # add later
    # logo

    def __str__(self):
        return (self.name)