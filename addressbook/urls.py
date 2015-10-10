from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import contacts.views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', contacts.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^new$', contacts.views.CreateContactView.as_view(),
        name='contacts-new',),
)
