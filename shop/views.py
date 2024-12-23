from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products

def index(request):
    product_objects = Products.objects.all()
    
    #? Search functionality for products
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    
    #? Pagination functionality for viewing products in a page
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {'product_objects': product_objects})