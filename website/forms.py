from django import forms
from .models import Snippet

class SnippetModelForm(forms.ModelForm):
    tag_list = forms.CharField(max_length=100, label="Теги", required=None, help_text="Теги должны разделяться запятой")

    class Meta:
        model = Snippet
        fields = ['title', 'code', 'description']
