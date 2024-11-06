from django.contrib import admin
from products import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'price',)
    search_fields = ('title',)
    list_filter = ('category', 'brand',)
    
admin.site.register(models.Product, ProductAdmin)
    