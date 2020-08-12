from django.db import models
# Create your models here.

class NewsApp(models.Model):
    title= models.CharField(max_length=255)
    description=models.CharField(max_length=500)
    author=models.CharField(max_length=255)
    pusbishedAt=models.CharField(max_length=255)

    class Meta:
        db_table="NewsApp"
    def __str__(self):
        return self.name