from django import forms

class LinkForm(forms.Form):
    longurl = forms.URLField(label='long Url', max_length=1000)