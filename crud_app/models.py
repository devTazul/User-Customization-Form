from django.db import models


# Create your models here.
class Students(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=20)
    Gender = models.CharField(max_length=8)
    Section = models.CharField(max_length=10)
    Roll_Number = models.IntegerField()
    Address = models.TextField(max_length=50)
    Phone = models.IntegerField()

    def __str__(self):
        return self.Name
