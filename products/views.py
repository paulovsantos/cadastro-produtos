from django.forms import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product


def add_product(request):
    # Pegando os dados do formulário
    new_product = Product()
    new_product.title = request.POST.get("title")
    new_product.category = request.POST.get("category")
    new_product.brand = request.POST.get("brand")
    new_product.description = request.POST.get("description")
    new_product.price = request.POST.get("price")

    new_product.save()

    return redirect("product_view")  # Redireciona para a view que exibe os produtos


def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    product.title = request.POST.get("title", product.title)
    product.category = request.POST.get("category", product.category)
    product.brand = request.POST.get("brand", product.brand)
    product.description = request.POST.get("description", product.description)   
    product.price = request.POST.get("price", product.price)

    if request.method == "POST":
        product.save()

    return redirect("product_view")


def del_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()

    return redirect("product_view")

def product_list(request):
    
    template_name = "products.html"
    
    products = Product.objects.all()

    search = request.GET.get('search', '')  

    if search:
        products = products.filter(
            Q(title__icontains=search) |
            Q(category__icontains=search) |
            Q(brand__icontains=search)
        )
        
        if not products:
            
            no_results_message = "Product not found."
        else:
            no_results_message = None
        
    context = {
        'products': products,
        'search': search,  
        'no_results_message': no_results_message,
    }
    
    return render(request, template_name, context)


# Exibe os dados dos produtos cadastrados.
def product_view(request):
    products = Product.objects.all()  # Busca todos os produtos
    return render(
        request=request,
        template_name="products.html",
        context={"products": products},
    )
