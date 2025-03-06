from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest  # Specify the model to tie the form to
        fields = (
            'name', 'email', 'message')  # List the fields that should appear in the form
