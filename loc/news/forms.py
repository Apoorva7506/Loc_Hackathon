from django import forms
from .models import Comments, News

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)