from django.http import HttpResponseRedirect
from django.shortcuts import render
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
    success_url = "/thanks"
    
    def submitData(request):
        # if this is a POST request we need to process the form data
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = ContactForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                first_name = form.cleaned_data[first_name]
                last_name = form.cleaned_data[last_name]
                email = form.cleaned_data[email]
                body = form.cleaned_data[body]
                location = form.cleaned_data[location]
                
                p = Contact(first_name,last_name,email,body,location)
                p.save()
                # redirect to a new URL:
                return HttpResponseRedirect("/thanks")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ContactForm()

        return render(request, "name.html", {"form": form})
