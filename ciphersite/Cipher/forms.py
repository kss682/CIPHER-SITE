from django import forms

class Encrypt(forms.Form):
    Etext   =   forms.CharField(max_length = 200)
    Ekey    =   forms.IntegerField()
