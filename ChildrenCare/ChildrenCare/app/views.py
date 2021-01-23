from django.shortcuts import render
from django.views.generic import TemplateView


from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'data': [
               {
                    'name': 'Cedrik',
                    'nachname': 'Walter'
                },         {
                    'name': 'Cedrik',
                    'nachname': 'Walter'
                },         {
                    'name': 'Cedrik',
                    'nachname': 'Walter'
                },         {
                    'name': 'Cedrik',
                    'nachname': 'Walter'
                },         {
                    'name': 'Cedrik',
                    'nachname': 'Walter'
                } 
               
                
            ]
        }

        return render(request, 'data.html', context)