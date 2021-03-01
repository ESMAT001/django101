from uuid import uuid4
from django.db import models


# Create your models here.
class students(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name=models.CharField(max_length=200,null=False,blank=False)
    fname=models.CharField(max_length=200,null=False,blank=False)
    last_name=models.CharField(max_length=200,null=False,blank=False)
    date_of_birth=models.DateField(auto_now=False)
    email=models.EmailField(max_length=254,null=False,blank=False)
    image=models.ImageField(null=False,blank=False,upload_to='student_images/%Y/%m/')
    created_at=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['created_at']