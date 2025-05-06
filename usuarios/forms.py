from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea, min_length=10)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre.lower() == "admin":
            raise forms.ValidationError("¡¡ Esta es una alerta personalizada !!")
        return nombre


