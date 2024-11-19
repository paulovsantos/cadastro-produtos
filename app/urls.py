from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Página para listar os produtos
    path("products/", views.product_view, name="product_view"),
    # Página para processar a adição de um produto
    path("products/add/", views.add_product, name="add_product"),
     # Página para processar a atualização de um produto
    path('products/<int:id>/atualizar/', views.update_product, name="update_product"),
    # Página para processar a exclusão de um produto
    path("products/<int:id>/delete/", views.del_product, name="del_product"),
    # Página para processar a busca de um produto
    path("products/search", views.product_list, name="product_list")
]
