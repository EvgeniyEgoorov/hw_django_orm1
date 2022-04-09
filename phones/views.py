from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    raw_list = Phone.objects.all()
    sorting = request.GET.get('sort')
    if sorting:
        if sorting == 'name':
            sorted_list = raw_list.order_by('name')
        elif sorting == 'min_price':
            sorted_list = raw_list.order_by('price')
        elif sorting == 'max_price':
            sorted_list = raw_list.order_by('-price')
        elif sorting == 'release_date':
            sorted_list = raw_list.order_by('release_date')
    else:
        sorted_list = raw_list
    context = {'phones': sorted_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

