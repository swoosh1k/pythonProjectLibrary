from django import forms
from .models import *


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'age', 'price']





class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewBook
        fields = ['name','email', 'text']



