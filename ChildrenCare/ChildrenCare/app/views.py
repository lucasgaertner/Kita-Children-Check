from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class AboutPageView(TemplateView):
    template_name = "about.html"

class UploadDataPageView(TemplateView):
    template_name = "data.html"

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

        return render(request, 'index.html', context)