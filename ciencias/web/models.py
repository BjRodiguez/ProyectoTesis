from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Carreras(models.Model):
    titulo_carrera = models.CharField(max_length=200)
    descripcion = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()
    titulo_pensum = models.CharField(max_length=50)
    video = EmbedVideoField(blank=True)
    titulo_video = models.CharField(max_length=50,blank=True)
    descripcion_video = models.CharField(max_length=300)


    def __str__(self):
        return self.titulo_carrera

class Pensum(models.Model):
    carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    ano_pensum = models.CharField(max_length=200)
    materia1 = models.CharField(max_length=50, blank=True)
    materia2 = models.CharField(max_length=50, blank=True)
    materia3 = models.CharField(max_length=50, blank=True)
    materia4 = models.CharField(max_length=50, blank=True)
    materia5 = models.CharField(max_length=50, blank=True)
    materia6 = models.CharField(max_length=50, blank=True)
    materia7 = models.CharField(max_length=50, blank=True)
    materia8 = models.CharField(max_length=50, blank=True)
    materia9 = models.CharField(max_length=50, blank=True)
    materia10 = models.CharField(max_length=50, blank=True)
    materia11 = models.CharField(max_length=50, blank=True)
    materia12 = models.CharField(max_length=50, blank=True)
    materia13 = models.CharField(max_length=50, blank=True)
    materia14 = models.CharField(max_length=50, blank=True)
    materia15 = models.CharField(max_length=50, blank=True)
    materia16 = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = 'pensums'

    def __str__(self):
        return self.ano_pensum
