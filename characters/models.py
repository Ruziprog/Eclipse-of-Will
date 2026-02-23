from django.db import models

class Characters(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name