from django.db import models


# Create your models here.
class NewsApp(models.Model):
    title= models.CharField(max_length=255)
    decription=models.CharField(max_length=500)
    Author=models.CharField(max_length=255)
    pusbishedAt=models.CharField(max_length=255)

class Meta:
    db_table="NewsApp"
def __str__(self):
    return self.name