from django.db import models

# Create your models here.
class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #podemos devolver los datos que necesitamos
    class Meta:
        db_table = '"apps"."herramienta"'
        
    def __str__(self):
        return self.nombre