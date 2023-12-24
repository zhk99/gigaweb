from django import forms
from .models import Task


class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        # especificar tarea
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'important': ' Marcar Como Imporante:',
              
        }
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'description': forms.Textarea(attrs={'class':'form-control'}),
        'important': forms.CheckboxInput(attrs={'class': 'form-check-input justify-content-between"'}),
    



        }