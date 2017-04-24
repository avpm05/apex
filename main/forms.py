from django import forms

class SendOrder(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
