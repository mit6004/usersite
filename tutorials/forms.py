from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django import forms
from tutorials.models import Comment, PublicVideo 

class CommentForm(ModelForm):
    fields=['text']
    # want to auto populate video and username fields
    
    class Meta:
        model=Comment

class PublicVideoForm(ModelForm):
    file=forms.FileField()
    class Meta:
        model=PublicVideo
        # author should be auto-assigned but pre-populated
        fields=['author','title', 'type', 'semester', 'file', 'description']
