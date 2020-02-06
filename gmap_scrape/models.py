from django.db import models

# Create your models here.
class Scrape(models.Model):
    #ドル
    dollar = models.FloatField(blank=False)
    
def __str__(self):
    return self.title