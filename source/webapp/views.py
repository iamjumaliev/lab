from django.shortcuts import render, get_object_or_404
from webapp.models import Product
from webapp.forms import SearchForm


def index_view(request):
    products = Product.objects.filter(amount__gt=0)
    form = SearchForm()
    return render(request, 'index.html', context={
        'products': products,
        'form': form
    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })

def search(request, *args, **kwargs):
    name = request.GET.get('search_name')
    products = Product.objects.all().filter(amount__gt=0).filter(name__icontains=name)
    form = SearchForm()
    return render(request, 'index.html', context={
        'products': products,
        'form': form
    })

# Create your views here.
