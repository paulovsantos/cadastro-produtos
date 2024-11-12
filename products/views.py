from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from products.models import Product


def add_product(request):
# Pegando os dados do formulário
    new_product = Product()
    new_product.title = request.POST.get('title')
    new_product.category = request.POST.get('category')
    new_product.brand = request.POST.get('brand')
    new_product.description = request.POST.get('description')
    new_product.price = request.POST.get('price')
   
    new_product.save()
    
    return redirect('product_view')  # Redireciona para a view que exibe os produtos

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product_view")

# Exibe os dados dos produtos cadastrados.
def product_view(request):
    products = Product.objects.all()  # Busca todos os produtos
    return render(
        request=request,
        template_name='products.html',
        context={'products': products},
     )