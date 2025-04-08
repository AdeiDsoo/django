from django import forms

class CreateAuto(forms.Form):
    marca=forms.CharField(max_length=20)
    modelo=forms.CharField(max_length=20)