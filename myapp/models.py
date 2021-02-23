from django.db import models

# Create your models here.
class items(models.Model):
    def __str__(self):
        return self.item_name
    item_name=models.CharField(max_length=100)
    item_desc=models.CharField(max_length=100)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=100,default="this is a  image")



    