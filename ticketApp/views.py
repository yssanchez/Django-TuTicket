from django.shortcuts import render
from django.shortcuts import render, redirect
from ticketApp.models import Show, Conciertos, Ventas
from ticketApp.forms import FormVenta
import datetime

# Create your views here.

def index(request):
    shows = Show.objects.all();
    data = {'shows': shows}
    return render (request, 'index.html', data)

def ticket(request, id):
    venta = Ventas.objects.get(id=id);
    data = {'venta' : venta}
    return render (request, 'ticket.html', data)

def comprar(request, id):
    DESCUENTO = 20
    form = FormVenta()
    form.fields['id_show'].initial= id
    if request.method == 'POST':
        form = FormVenta(request.POST)
        if form.is_valid():
            show = Show.objects.get(id = id)

            cantidad = form.cleaned_data['entradas']
            show.tickets_disponibles -= cantidad
            show.tickets_vendidos += cantidad
            show.save()

            venta = Ventas()
            venta.show = funcion
            venta.cliente = form.cleaned_data['cliente']
            venta.entradas = form.cleaned_data['entradas']
            venta.codigo = form.cleaned_data['codigo']
            venta.email = form.cleaned_data['email']
            venta.fecha = datetime.datetime.now()

            descuento = DESCUENTO if venta.codigo != "" else 0

            valor_entrada= show.precio
            total_original =venta.entradas * valor_entrada
            total_descuento = total_original * descuento / 100
            total_final = total_original - total_descuento

            venta.total_original = total_original
            venta.total_descuento = total_descuento
            venta.total_final = total_final
            venta.save()

        return redirect('/ticket/' + str(venta.id))
        
    show = Show.objects.get(id=id)
    data = {
        'show' : show,
        'form' : form
    }
    return render (request, 'comprar.html', data)
    
    