from django import forms

class LinkForm(forms.Form):
    longurl = forms.URLField(max_length=1000, widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "https://" }
        )
    )