from django.db import models

class Destination(models.Model):
    name=models.CharField(max_length=64)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()