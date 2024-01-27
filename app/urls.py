from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("services/", views.services,name="services"),
    path("solutions/", views.solutions,name="solutions"),
    # path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("product-details/<int:pk>", views.ProductDetails.as_view(),name="product-detail"),
    path('category/', views.All_Products, name='category'),
    path("categoryproduct/<int:pk>", views.ProductAgainstCategory.as_view(),name="categoryproduct"),

    path("sub-product-details/<int:pk>", views.SubProductDetails.as_view(),name="sub-product-detail"),
    path("product-sub-product/<int:pk>", views.SubProductAgainstProduct.as_view(),name="product-sub-product"),

    path("project-details/<int:pk>", views.ProjectDetails.as_view(),name="project-detail"),
    path('projects/', views.All_Projects, name='projects'),
    path('allmachines/', views.All_Machines, name='allmachines'),
    path('allcategories/', views.allcategories, name='allcategories'),

    path('solutiondesign/', views.SolutionDesign, name='solutiondesign'),
    path('solutionengineer/', views.SolutionEngineer, name='solutionengineer'),
    path('solutioninstallation/', views.SolutionInstallation, name='solutioninstallation'),
    path('solutionmantainence/', views.SolutionMantainence, name='solutionmantainence'),
    path('solutionfabrication/', views.SolutionFabrication, name='solutionfabrication'),

    path("umachine-details/<int:pk>", views.MachineDetails.as_view(),name="umachine-detail"),
    path('subcategory/<int:pk>', views.CategorySubCategory, name='subcategory'),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
