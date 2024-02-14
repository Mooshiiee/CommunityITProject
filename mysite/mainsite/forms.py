from django import forms
from .models import Contact
#form fields are required by default

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'body', 'location']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 7, 'cols': 70,'style': "width:100%;"}),
        }