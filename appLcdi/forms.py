from django.forms import ModelForm, Textarea
from django import forms
from appLcdi.models import Tweet

class FormTweet(ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'

        widgets = {
            'postTweet': Textarea(attrs={'class': 'form-control', 'maxlength': '140','placeholder':'Masukan tweet tidak lebih dari 140 karakter'}),
        }