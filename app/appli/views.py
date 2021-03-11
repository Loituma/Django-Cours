from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .forms import ContactForm
from .models import Contact
from datetime import datetime
from django.views.generic import CreateView

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'appli/index.html')

def about(request):
    return render(request, 'appli/about.html')

def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_namel = request.POST.get('contact_namel', '')
            contact_namef = request.POST.get('contact_namef', '')
            contact_email = request.POST.get('contact_email', '')
            contact_subject = request.POST.get('contact_subject', '')
            contact_message = request.POST.get('contact_message', '')
            contact_competence = ','.join(request.POST.getlist('contact_competence', ''))

            c = Contact(nom=contact_namel, prenom=contact_namef, mail=contact_email, titre=contact_subject, contenu=contact_message, competence=contact_competence, date=datetime.now())
            c.save()

        return redirect('contact')

    return render(request, 'appli/contact.html', {
        'form': form_class,
    })