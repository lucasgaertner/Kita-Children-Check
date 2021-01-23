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

@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://127.0.0.1:8000' # this can be current domain
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')