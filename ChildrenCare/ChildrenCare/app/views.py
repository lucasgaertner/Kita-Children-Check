from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


import csv, io
from django.contrib import messages
from .models import Profile


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class AboutPageView(TemplateView):
    template_name = "about.html"

class UploadDataPageView(TemplateView):
    def get(self, request, **kwargs):
        # declaring template
        data = Profile.objects.all()
        # prompt is a context variable that can have different values      depending on their context
        prompt = {
            'order': 'Order of the CSV should be name, email, address,    phone, profile',
            'profiles': data    
                  }
        # GET request returns the value of the data with the specified key.
        if request.method == "GET":
            return render(request, "data.html", prompt)
    
    def post(self, request, **kwargs):
        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=';', quotechar="|"):
            _, created = Profile.objects.update_or_create(
                nachname=column[0],
                name=column[1],
            )
        context = {}
        return render(request, "data.html", context)

class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        profiles = Profile.objects.all()
        context = {"profiles": profiles}
        return render(request, 'index.html', context)