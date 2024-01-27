from django.contrib import admin
from . models import Product
from . models import MainCategory
from . models import SubCategory
# Register your models here.
@admin.register(Product)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','description','product_image','prodfile']

@admin.register(MainCategory)

class MainCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title','description',]


@admin.register(SubCategory)

class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title','description','mcategory']
