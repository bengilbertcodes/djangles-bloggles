from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    A django form for submitting comments.

    Attributes:
        fields: only uses 'body'
    """
    class Meta:
        model = Comment
        fields = ('body',)