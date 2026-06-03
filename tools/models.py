from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #podemos devolver los datos que necesitamos
    def __str__(self):
        return self.name
    
    