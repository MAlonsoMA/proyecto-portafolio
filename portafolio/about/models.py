from django.db import models

# Create your models here.
class Training(models.Model):
    title= models.CharField(max_length=150, verbose_name='Título')
    obtained_title= models.CharField(max_length=150, verbose_name='Título obtenido')
    description=models.TextField(verbose_name='Descripción')
    date_of_realization=models.DateField(verbose_name="Fecha de realización")
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha modificación')

    class Meta:
        verbose_name='formacion'
        verbose_name_plural='formaciones'
        ordering=['-date_of_realization']

    def __str__(self):
        return self.title
    

class Skill(models.Model):
    title= models.CharField(max_length=150, verbose_name='Título')
    image=models.ImageField(upload_to='skills',verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha modificación')

    class Meta:
        verbose_name='conocimiento'
        verbose_name_plural='conocimientos'
        ordering=['-created']

    def __str__(self):
        return self.title