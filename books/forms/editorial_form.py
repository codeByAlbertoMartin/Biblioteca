from django import forms # type: ignore
from django.forms import ModelForm # type: ignore
from books.models import Editorial

class EditorialCreate(forms.Form):
    nombre = forms.CharField(max_length=200, required=False)
    direccion = forms.CharField(max_length=300, required=False)
    ciudad = forms.CharField(max_length=100, required=False)
    pais = forms.CharField(max_length=100, required=False)
    codigo_postal = forms.CharField(max_length=20, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    sitio_web = forms.URLField(required=False)
    fecha_fundacion = forms.DateField(widget=forms.SelectDateWidget)

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if(len(nombre)<5):
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre
    
class EditorialModelFormCreate(ModelForm):
    class Meta:
        model= Editorial
        fields = ["nombre", "direccion",
                  "ciudad", "pais",
                  "codigo_postal", "telefono", "email",
                  "sitio_web", "fecha_fundacion"]
