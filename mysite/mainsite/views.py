from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from mainsite.forms import ContactForm
from .models import Contact

class IndexView(TemplateView):
    template_name = "index.html"

class ResourcesView(TemplateView):
    template_name = "resources.html"
    
class ContributeView(TemplateView):
    template_name = "Contribute.html"
    
class ClassesView(TemplateView):
    template_name = "classes.html"

class ThanksView(TemplateView):
    template_name = "thanks.html"

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    
    def form_valid(self, form):
        # Process the form data
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        body = form.cleaned_data['body']
        location = form.cleaned_data['location']
        
        # Create and save the Contact object
        p = Contact(first_name = first_name, last_name = last_name, email = email, body = body, location = location)
        p.save()
    
        # Redirect to the success URL
        return HttpResponseRedirect(reverse('mainsite:thanks'))