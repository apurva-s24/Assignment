from django import forms
from .models import User


class UserEntry(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'start_date', 'end_date', 'value']

