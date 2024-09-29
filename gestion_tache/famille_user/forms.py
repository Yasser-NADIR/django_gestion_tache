from django import forms
from .models import FUser

class FUserForm(forms.ModelForm):
    class Meta:
        model = FUser
        fields = ['libelle_famille', 'coefficient', 'remarques']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['libelle_famille'].widget.attrs.update({'class': 'form-control'})
        self.fields['coefficient'].widget.attrs.update({'class': 'form-control'})
        self.fields['remarques'].widget.attrs.update({'class': 'form-control'})