from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
