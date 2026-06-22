from django.db import models
from django.utils import timezone


# 1. Custom QuerySet para manejar operaciones en lote (e.g., Herramienta.objects.filter(...).delete())
class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return super().update(deleted_at=timezone.now(), is_deleted=True)

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(is_deleted=False)

    def dead(self):
        return self.filter(is_deleted=True)


# 2. Custom Manager para filtrar por defecto los registros activos
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        # Por defecto, todas las consultas excluirán los registros borrados
        return SoftDeleteQuerySet(self.model, using=self._db).alive()

    def all_with_deleted(self):
        # Método auxiliar por si necesitas consultar TODO (activos y eliminados)
        return SoftDeleteQuerySet(self.model, using=self._db)


# 3. Modelo Abstracto que encapsula la lógica de Soft Delete
class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False, db_index=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    # Reemplazamos el manager por defecto de Django
    objects = SoftDeleteManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """Borrado lógico para una instancia individual"""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])

    def restore(self):
        """Método para recuperar un registro eliminado"""
        self.is_deleted = False
        self.deleted_at = None
        self.save(update_fields=['is_deleted', 'deleted_at'])

    def hard_delete(self, *args, **kwargs):
        """Borrado físico real de la base de datos si es necesario"""
        super().delete(*args, **kwargs)

# Create your models here.
class Herramienta(SoftDeleteModel):
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