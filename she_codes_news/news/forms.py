from cProfile import label
from tkinter import Widget
from django import forms
from django.forms import ModelForm, Textarea
from .models import NewsStory, StoryComments
from .models import Image

# class ImageForm(ModelForm):
#     class Meta: 
#         model = Image
#         fields = ("name", "img")

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        #if you don't want the user to change the publish date, you would remove it from this field. 
        fields = ['title', 'pub_date', 'image','content']
        labels = {
            'pub_date':"Publishing Date:",
            'image':"Image URL:",
            "content":"Your story:",
        }
        widgets = {
            'pub_date': forms.DateInput(
                format="%m/%d/%Y",
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": 'date'
                }
            ),
            'content': Textarea(),
        }

class CommentForm(ModelForm):
    class Meta:
        model = StoryComments
        fields = ['content']
        labels = {
            "content":""
        }
        widgets = {
            'content': Textarea(
                attrs={
                    'rows':2,
                    'cols':40,
                }
            )
        }

