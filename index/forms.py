from django import forms

class PostForm(forms.Form):
    nimi = forms.CharField(max_length=50)
    postaus = forms.CharField(max_length=250)