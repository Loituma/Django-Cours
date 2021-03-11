from django import forms

COMPETENCE_DEV = [
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('js', 'JavaScript'),
    ('php', 'PHP'),
    ('python', 'Python'),
    ('ruby', 'Ruby'),
    ('nodejs', 'Node.js'),
]

class ContactForm(forms.Form):
    contact_namel = forms.CharField(required=True, label='Nom')
    contact_namef = forms.CharField(required=True, label='Prenom')
    contact_email = forms.EmailField(required=True, label='Email')
    contact_subject = forms.CharField(required=True, label='Sujet')
    contact_message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
    contact_competence = forms.MultipleChoiceField(choices=COMPETENCE_DEV,widget=forms.CheckboxSelectMultiple(attrs={'class': 'browser-default'}),label = 'Competence')