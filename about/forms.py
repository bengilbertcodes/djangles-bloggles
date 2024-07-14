from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    A django form for submitting collaboration requests.

    Attributes:
        model (CollaborateRequest): The model that the form is based on.
        fields (tuple): The fields to include in the form. This includes 
                        'name', 'email', and 'message'.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')