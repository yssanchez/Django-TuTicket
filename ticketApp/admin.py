from django.contrib import admin
from ticketApp.models import Conciertos, Show, Ventas
# Register your models here.

class ConciertosForm(admin.ModelAdmin):
    list_display=['artista', 'lugar', 'fecha']

class ShowForm(admin.ModelAdmin):
    list_display=['concierto', 'fecha', 'hora', 'tickets_vendidos', 'precio']

class VentasForm(admin.ModelAdmin):
    list_display=['show', 'cliente', 'entradas', 'total_original', 'total_final']

admin.site.register(Conciertos, ConciertosForm)
admin.site.register(Show, ShowForm)
admin.site.register(Ventas, VentasForm)