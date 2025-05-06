from django import forms

class ConsultasForm(forms.Form):

    # Listado de campos + Validación predeterminada
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea, min_length=10)

    # Validación personalizada para el campo 'nombre'
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre.lower() == "admin":
            raise forms.ValidationError("Esta es una alerta para el campo nombre")
        return nombre









