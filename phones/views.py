from django.shortcuts import render, redirect
from work_with_database.phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_all = list()
    sort_param = request.GET.get('sort', None)

    if sort_param is not None:
        if sort_param == 'name':
            phones_all = list(Phone.objects.all().order_by('name'))
        if sort_param == 'min_price':
            phones_all = list(Phone.objects.all().order_by('price'))
        if sort_param == 'max_price':
            phones_all = list(Phone.objects.all().order_by('-price'))
    else:
        phones_all = list(Phone.objects.all())

    context = {
        "phones": phones_all
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # phone = Phone.objects.get(slug=slug)
    phone = 'iphone'
    context = {
        "phone": phone
    }
    return render(request, template, context)
