from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=200, blank=False, null = False)
    apellido = models.CharField('Apellido',max_length=220, blank=False, null = False)
    nacionalidad = models.CharField('Nacionalidad',max_length=100, blank=False,null = False)
    descripcion = models.TextField('Descripción',blank=False, null = False)  
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título',max_length=225, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank=False, null=False)
    autor_id= models.OneToOneField(Autor, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


    