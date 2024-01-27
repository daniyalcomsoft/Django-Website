from django.contrib import admin
from customadminpanel.models import *

from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class UserModel(UserAdmin):
#     list_display = ['username', 'user_type'] 

# admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(SubProduct)
admin.site.register(SubProductDetail)
admin.site.register(Project)
admin.site.register(Partner)