from django.shortcuts import render
from django.views import generic
from . import models


class Index(generic.TemplateView):

    template_name='contacts/index.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_contacts']= models.Contact.objects.all().count()
        return context

class ContactListView(generic.ListView):
    model = models.Contact
    template_name='contacts/contact_list.html'

class ContactDetailView(generic.DetailView):
    model = models.Contact
    template_name='contact/contact_detail.html'
#def index(request):
    #"""
    #View function for home page of site.
    #"""
    # Generate counts of some of the main objects
    #num_contacts=models.Contact.objects.all().count()

    #return render(
    #    request,
    #    'contacts/index.html',
    #    context={'num_contacts':num_contacts},
    #)
#,'num_phone':num_phone
