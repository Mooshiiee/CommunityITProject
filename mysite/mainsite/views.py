from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ResourcesView(TemplateView):
    template_name = "resources.html"
    
class ContributeView(TemplateView):
    template_name = "Contribute.html"
    
class ClassesView(TemplateView):
    template_name = "classes.html"

class ContactView(TemplateView):
    template_name = "contact.html"