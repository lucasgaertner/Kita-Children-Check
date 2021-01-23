from django.shortcuts import render
from django.views.generic import TemplateView


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