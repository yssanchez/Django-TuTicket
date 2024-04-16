from django.db import models

# Create your models here.

class Conciertos (models.Model):
    artista=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)
    fecha=models.DateField()
    duracion=models.PositiveIntegerField()
    imagen=models.ImageField(upload_to='conciertos')

    def __str__(self):
        return self.artista + "(" + str(self.lugar) + ")"

class Show(models.Model):
    concierto=models.ForeignKey(Conciertos, on_delete=models.CASCADE)
    fecha=models.DateField()
    hora=models.TimeField()
    precio=models.PositiveIntegerField()
    tickets_disponibles=models.PositiveIntegerField()
    tickets_vendidos=models.PositiveIntegerField()

    def __str__(self):
        return self.concierto.artista

class Ventas(models.Model):
    show=models.ForeignKey(Show, on_delete=models.CASCADE)
    cliente=models.CharField(max_length=50)
    email=models.CharField(max_length=50, blank= True)
    codigo=models.CharField(max_length= 50, blank=True)
    entradas=models.PositiveIntegerField()
    total_original=models.PositiveIntegerField(default=0)
    total_descuento=models.PositiveIntegerField(default=0)
    total_final=models.PositiveIntegerField(default=0)
    fecha=models.DateField()