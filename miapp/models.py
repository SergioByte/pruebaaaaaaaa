from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(default='null', verbose_name="Miniatura", upload_to="articulos")
    publicado = models.BooleanField(verbose_name="¿Publicado?")
    ## auto no add true permite
   # registrar la fecha de creación del registro
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    #auto now true
    #ka fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now_add=True, verbose_name="Editado")
    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['titulo','publicado']
    ##mostrar letras mejores al momento de observar en la tabla de control principal
    def __str__(self):
            if self.publicado:
                publicado = "Publicado"
            else:
                publicado = "No Publicado / En Revisión"
            return f"{self.titulo}. Creado el: {self.creado}. {publicado}"
        


class Categoria(models.Model):
    nombre = models.CharField(max_length=110)
    descripcion = models.CharField(max_length=250)
    #models.datefield() para guardar la fecha manualmente
    creado = models.DateField()
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Autor(models.Model):
    nombre = models.CharField(max_length=110)
    apellido = models.CharField(max_length=110)
    sexo = models.CharField(max_length=20)
    fecha_nacimiento = models.DateTimeField(auto_now_add=False)
    pais = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)



