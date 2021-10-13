from django.db import models

# Create your models here.
class MLModel(models.Model):
    smile_name = models.TextField(max_length=120)
    result = models.FloatField()
    
    def __str__(self):
        return self.smile_name
    