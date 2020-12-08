from django import forms

from .models import Forum


class Former(forms.ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'