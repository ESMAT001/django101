from uuid import uuid4
from django.db import models

def overwrite(instance,filename):
    
    newfile=f'student_{instance.id}/image.{filename.split(".")[-1]}'
    return newfile
# Create your models here.
class Students(models.Model):
   
    
    id = models.UUIDField(primary_key=True,default=uuid4,editable=True)
    name=models.CharField(max_length=200,null=False,blank=False)
    fname=models.CharField(max_length=200,null=False,blank=False)
    last_name=models.CharField(max_length=200,null=False,blank=False)
    date_of_birth=models.DateField(auto_now=False)
    email=models.EmailField(max_length=254,null=False,blank=False,unique=True)
    image=models.ImageField(upload_to=overwrite,blank=True )
    created_at=models.DateTimeField(auto_now=True)

    def delete(self):
        img=self.image.name
        self.image.storage.delete(img)
        self.image.storage.delete(img.split('/')[0])
        super().delete()


    class Meta:
        ordering=['created_at']


class City(models.Model):
    name = models.CharField(max_length=200)

class Person(models.Model):
    hometown = models.ForeignKey(
        City, 
        on_delete = models.SET_NULL,
        blank=True,
        null = True
    )

    def __str__(self):
        return f"Person: city: {self.hometown.name}"


class Book(models.Model):
    author = models.ForeignKey(Person, on_delete = models.CASCADE)


class Cover(models.Model):
    name = models.OneToOneField(Book, on_delete=models.CASCADE)