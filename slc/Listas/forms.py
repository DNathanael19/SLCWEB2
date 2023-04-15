from django import forms
from .models import Iten, Lista

class ListForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nome',)

class ListForm2(forms.ModelForm):
    class Meta:
        model = Iten
        fields = ('item',)

