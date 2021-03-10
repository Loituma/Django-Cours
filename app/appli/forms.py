from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label='Nom')
    contact_email = forms.EmailField(required=True, label='Email')
    contact_subject = forms.CharField(required=True, label='Sujet')
    contact_message = forms.CharField(widget=forms.Textarea, required=True, label='Message')