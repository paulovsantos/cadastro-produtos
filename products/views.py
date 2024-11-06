from django.shortcuts import render
from products.models import Product


# Create your views here.

def product_view(request):
    products = Product.objects.all()
    #return HttpResponse('Hello world!')
    return render(
        request=request,
        template_name='products.html',
        context={'products': products},
    )

