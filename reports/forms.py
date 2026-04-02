from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['category', 'description', 'location', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe the issue (e.g., "Large pothole in front of a house")'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Street address or landmark'
            }),
        }
        labels = {
            'category': 'What is the issue?',
            'description': 'Brief description',
            'location': 'Where is the issue?',
            'photo': 'Add evidence (optional)',
        }