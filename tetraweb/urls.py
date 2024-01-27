"""
URL configuration for tetraweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    

    # custom admin panel
    # path('customadminpanel/', views.CustomAdminPanel, name='customadminpanel'),
    path('login/', views.Login, name='login'),
    # path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('hod/home/', views.HOME, name='hod_home'),

    # path('profile', views.PROFILE, name='profile'),
    # path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    path('add/category/', views.Add_Category, name='add_category'),
    path('view/category/', views.View_Category, name='view_category'),
    path('edit/category/<str:id>', views.Edit_Category, name='edit_category'),
    path('update/category/', views.Update_Category, name='update_category'),
    path('delete/category/<str:id>', views.Delete_Category, name='delete_category'),

    path('add/subcategory/', views.Add_SubCategory, name='add_subcategory'),
    path('view/subcategory/', views.View_SubCategory, name='view_subcategory'),
    path('edit/subcategory/<str:id>', views.Edit_SubCategory, name='edit_subcategory'),
    path('update/subcategory/', views.Update_SubCategory, name='update_subcategory'),
    path('delete/subcategory/<str:id>', views.Delete_SubCategory, name='delete_subcategory'),

    path('add/product/', views.Add_Product, name='add_product'),
    path('view/product/', views.View_Product, name='view_product'),
    path('edit/product/<str:id>', views.Edit_Product, name='edit_product'),
    path('update/product/', views.Update_Product, name='update_product'),
    path('delete/product/<str:id>', views.Delete_Product, name='delete_product'),

    path('add/productdetail', views.Add_ProductDetail, name='add_productdetail'),
    path('view/productdetail', views.View_ProductDetail, name='view_productdetail'),
    path('edit/productdetail/<str:id>', views.Edit_ProductDetail, name='edit_productdetail'),
    path('upate/productdetail', views.Update_ProductDetail, name='update_productdetail'),
    path('delete/productdetail/<str:id>', views.Delete_ProductDetail, name='delete_productdetail'),

    path('add/subproduct/', views.Add_SubProduct, name='add_subproduct'),
    path('view/subproduct/', views.View_SubProduct, name='view_subproduct'),
    path('edit/subproduct/<str:id>', views.Edit_SubProduct, name='edit_subproduct'),
    path('update/subproduct/', views.Update_SubProduct, name='update_subproduct'),
    path('delete/subproduct/<str:id>', views.Delete_SubProduct, name='delete_subproduct'),

    path('add/subproductdetail', views.Add_SubProductDetail, name='add_subproductdetail'),
    path('view/subproductdetail', views.View_SubProductDetail, name='view_subproductdetail'),
    path('edit/subproductdetail/<str:id>', views.Edit_SubProductDetail, name='edit_subproductdetail'),
    path('upate/subproductdetail', views.Update_SubProductDetail, name='update_subproductdetail'),
    path('delete/subproductdetail/<str:id>', views.Delete_SubProductDetail, name='delete_subproductdetail'),

    path('add/project/', views.Add_Project, name='add_project'),
    path('view/project/', views.View_Project, name='view_project'),
    path('edit/project/<str:id>', views.Edit_Project, name='edit_project'),
    path('update/project/', views.Update_Project, name='update_project'),
    path('delete/project/<str:id>', views.Delete_Project, name='delete_project'),

    path('add/partners/', views.Add_Partners, name='add_partners'),
    path('view/partners/', views.View_Partners, name='view_partners'),
    path('edit/partners/<str:id>', views.Edit_Partners, name='edit_partners'),
    path('update/partners/', views.Update_Partners, name='update_partners'),
    path('delete/partners/<str:id>', views.Delete_Partners, name='delete_partners'),

    path('add/client/', views.Add_Client, name='add_client'),
    path('view/client/', views.View_Client, name='view_client'),
    path('edit/client/<str:id>', views.Edit_Client, name='edit_client'),
    path('update/client/', views.Update_Client, name='update_client'),
    path('delete/client/<str:id>', views.Delete_Client, name='delete_client'),

    path('add/usedmachineryimages/', views.Add_UsedMachineryImages, name='add_usedmachineryimages'),
    path('view/usedmachineryimages/', views.View_UsedMachineryImages, name='view_usedmachineryimages'),
    path('edit/usedmachineryimages/<str:id>', views.Edit_UsedMachineryImages, name='edit_usedmachineryimages'),
    path('update/usedmachineryimages/', views.Update_UsedMachineryImages, name='update_usedmachineryimages'),
    path('delete/usedmachineryimages/<str:id>', views.Delete_UsedMachineryImages, name='delete_usedmachineryimages'),

    path('add/usedmachine/', views.Add_UsedMachine, name='add_usedmachines'),
    path('view/usedmachine/', views.View_UsedMachine, name='view_usedmachines'),
    path('edit/usedmachine/<str:id>', views.Edit_UsedMachine, name='edit_usedmachines'),
    path('update/usedmachine/', views.Update_UsedMachine, name='update_usedmachines'),
    path('delete/usedmachine/<str:id>', views.Delete_UsedMachine, name='delete_usedmachines'),

    path('add/sliders/', views.Add_Sliders, name='add_sliders'),
    path('view/sliders/', views.View_Sliders, name='view_sliders'),
    path('edit/sliders/<str:id>', views.Edit_Sliders, name='edit_sliders'),
    path('update/sliders/', views.Update_Sliders, name='update_sliders'),
    path('delete/sliders/<str:id>', views.Delete_Sliders, name='delete_sliders'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
