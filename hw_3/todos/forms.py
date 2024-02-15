from django import forms
from django.forms import DateInput

class CreateTodoForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, min_length=0, max_length=2000, required=False)
    due_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)
    status = forms.BooleanField(required=False, help_text='Check if completed')
