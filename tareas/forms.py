from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la tarea',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe la tarea con más detalle',
                'style': 'resize: vertical; min-height: 120px;',
            }),
            'completada': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }