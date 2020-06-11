from django import forms
from .models import Signup, Like


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


class LikeForm(forms.ModelForm):
    likeField = forms.CharField(widget=forms.TextInput(attrs={
        "id": "likeme",
        "value": "done",
        "placeholder": "youremail@exemple.smthng",
        #"hidden": "hidden"
    }), label="")

    class Meta:
        model = Like
        fields = ('likeField',)
