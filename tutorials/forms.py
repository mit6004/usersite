from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django import forms

class CommentForm(ModelForm):
    fields=['text']
    # want to auto populate video and username fields
    
    class Meta:
        model=Comment

