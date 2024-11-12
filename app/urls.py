from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Página para listar os produtos
    path('products/', views.product_view, name='product_view'),
    # Página para processar a adição de um produto
    path('products/add/', views.add_product, name='add_product'),
    # Página para processar a exclusão de um produto
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete-product'),

    

]
