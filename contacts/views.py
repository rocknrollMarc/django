from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse

from contacts.models import Contact

class ListContactView(ListView):

    model = Contact
    template_name = 'contact_list.html'

    def get_success_url(self):
        return reverse('contacts-list')

class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contacts.html'

    def get_success_url(self):
        return reverse('contacts-list')


class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')
