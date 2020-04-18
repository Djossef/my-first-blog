from django import forms
from .models import Signup


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "id": "youremail",
        "placeholder": "youremail@exemple.smthng",
        "class": "form-control"
    }), label="")

    class Meta:
        model = Signup
        fields = ('email',)
