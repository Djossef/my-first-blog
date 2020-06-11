from django import forms

from blog.models import Comment


class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=4000, widget=forms.TextInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = Comment
        fields = ('comment',)
