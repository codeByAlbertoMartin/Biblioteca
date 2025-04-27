from django import forms # type: ignore

class ContactForm(forms.Form):
    
    nombre= forms.CharField(
        label="Nombre",
        max_length=140
    )

    email = forms.EmailField(label="Email")

    comentario = forms.CharField(
        label="Comentario",
        max_length=1000,
        widget=forms.Textarea)
    
    #SON LAS VALIDACIONES QUE SE REALIZAN PARA COMPROBAR EN LA VISTA LA PARTE DE FORMULARIO.IS_VALID()
    #este metodo siempre se llama con clean_(nombre del campo)
    def clean_comentario(self):
        comentario = self.cleaned_data.get("comentario")
        if(len(comentario)<5):
            raise forms.ValidationError("El comentario debe tener al menos 5 caracteres")
        return comentario
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if(len(nombre)<5):
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre