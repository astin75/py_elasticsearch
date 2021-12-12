from django.db import models

# Create your models here.

class memberData(models.Model):
    name = models.CharField(max_length=10)
    memberNumber = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    major = models.CharField(max_length=10)

    def __str__(self):
        return self.name