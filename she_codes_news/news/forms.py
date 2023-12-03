from django import forms
from django.forms import ModelForm
from .models import NewsStory
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
        widgets = {
            'pub_date': forms.DateInput(
                format="%m/%d/%Y",
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": 'date'
                }
            )
        }

