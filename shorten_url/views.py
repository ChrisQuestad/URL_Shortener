from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from .models import URL
from .forms import CreateForm
from django.http import HttpResponseRedirect
import random
import string


class CreateURLView(View):
    form_class = CreateForm
    template_name = 'shorten_url/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save()
            allowed_chars = ''.join((string.ascii_letters, string.digits))
            model.code = ''.join(random.choice(allowed_chars) for _ in range(8))
            model.save()
            return HttpResponseRedirect(URL.url)
         # redirect('shorten_url:new_url', pk=model.pk)

        return render(request, self.template_name, {'form': form})

def detail(request, pk):
    shorten_url = URL.objects.get(pk=pk)
    return render(request, 'shorten_url/newurl.html',{'shorten_url':shorten_url})


# class NewURLView(View):
#     template_name = 'shorten_url/newurl.html'
