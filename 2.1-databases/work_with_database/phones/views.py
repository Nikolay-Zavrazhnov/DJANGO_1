

from django.shortcuts import render, redirect
from django.core.management import call_command
import phones.models
from phones.models import Phone
from phones.management.commands.import_phones import Command

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    call_command('import_phones')

    sort = request.GET.get('sort', '')

    if sort == 'name':
        phones = Phone.objects.order_by("name")
    elif sort == 'min_price':
        phones = Phone.objects.order_by("price")
    elif sort == 'max_price':
        phones = Phone.objects.order_by("-price")
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
