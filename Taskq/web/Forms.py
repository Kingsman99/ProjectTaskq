from .models import DataBase
from django import forms


class DataBaseForm(forms.ModelForm):
    class Meta:
        model = DataBase
        fields = ('name', 'detail')