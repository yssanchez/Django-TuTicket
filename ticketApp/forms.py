from django import forms
from ticketApp.models import Show

class FormVenta(forms.Form):
    LARGO_CODIGO= 9
    VALIDADOR_CODIGO= 37

    id_show = forms.CharField()
    cliente = forms.CharField()
    email = forms.CharField(required=False)
    entradas = forms.IntegerField (min_value=1, max_value=10)
    codigo = forms.CharField(required=False)

    id_show.widget.attrs['class'] = 'form-control'
    cliente.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    entradas.widget.attrs['class'] = 'form-control'
    codigo.widget.attrs['class'] = 'form-control'

    def clean_entradas(self):
        id_show = self.cleaned_data['id_show']
        entradas = self.cleaned_data['entradas']

        show = Show.objects.get(id = id_show)
        tickets_disponibles = show.tickets_disponibles

        if (entradas > tickets_disponibles):
            raise forms.ValidationError("No hay entradas disponibles")
        return entradas
    
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if codigo == "" : return codigo

        codigoErroneo = False
        if (len(codigo)!=self.LARGO_CODIGO): codigoErroneo = True
        if not codigo.isnumeric(): codigoErroneo = True

        suma = 0
        for c in codigo:
            suma += int (c)

        if suma != self.VALIDADOR_CODIGO : codigoErroneo = True
        if (codigoErroneo):
            raise forms.ValidationError("Código incorrecto")

        return codigo    
