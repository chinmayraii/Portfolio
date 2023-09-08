from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    hire_for=models.CharField(max_length=1000)
    message=models.TextField()
    def __str__(self) -> str:
        return self.name
