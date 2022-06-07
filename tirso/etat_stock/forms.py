from dataclasses import field
from django import forms
from django.forms import ModelForm
from etat_stock.models import Excel

class ExcelForm(ModelForm):
    class Meta:
        model = Excel
        exclude =()

