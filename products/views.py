from django.shortcuts import get_object_or_404, redirect, render
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


""" class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product_view")
 """    
 

def del_product(request, id):
    product = get_object_or_404(Product, id=id)
    
    product.delete()
    
    return redirect('product_view')

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    
    product.title = request.POST.get('title', product.title)
    product.category = request.POST.get('category', product.category)
    product.brand = request.POST.get('brand', product.brand)
    product.description = request.POST.get('description', product.description)
    product.price = request.POST.get('price', product.price)


    product.save()
    
    return redirect('product_view')
    

# Exibe os dados dos produtos cadastrados.
def product_view(request):
    products = Product.objects.all()  # Busca todos os produtos
    return render(
        request=request,
        template_name='products.html',
        context={'products': products},
     )