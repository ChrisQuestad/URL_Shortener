from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from .models import URL

# Form to create shortened url

class CreateURLView(View):
    form_class = CreateForm
    template_name = 'urls/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save()
            return redirect('shorten_url:detail', pk=model.pk)

        return render(request, self.template_name, {'form': form})

class DetailURLView(View):
    template_name = 'urls/detail.html'


class NewURLView(View):
    template_name = 'urls/newurl.html'
