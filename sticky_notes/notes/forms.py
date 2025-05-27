from django import forms
from .models import Notes


class StickyNote(forms.ModelForm):
    """
    Form for creating and updating note objects.

    Fields:
    - title: CharField for the post title.
    - body: TextField for the post content.

    """
    class Meta:
        """
        Metaform  class:
        - Defines the model to use (Notes) and the fields to include in the
        form.
        :param forms.ModelForm: Django's ModelForm class.
        """
        model = Notes
        fields = ['title', 'body']