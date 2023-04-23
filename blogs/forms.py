from django import forms
from .models import BlockPost


class NewPost(forms.ModelForm):
    class Meta:
        model = BlockPost
        fields = ['title', 'text']
        labels = {'title': 'Title:', 'text': 'Text:'}


class EditPost(forms.ModelForm):
    class Meta:
        model = BlockPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Text:'}
