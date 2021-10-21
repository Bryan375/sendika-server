from django.db import models

# Create your models here.
class MLModel(models.Model):
    smile_name = models.CharField(max_length=120)
    #predicted_result = models.FloatField()
    
    
    def __str__(self):
        return self.smile_name
    