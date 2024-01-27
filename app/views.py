from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
# from . models import Product 

from customadminpanel.models import *

from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.
def index(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    part = Partner.objects.all()
    products = Product.objects.all()
    pro = Project.objects.order_by('-EndDate')[:3]
    clint = Client.objects.all()
    umachine = UsedMachine.objects.all()
    sliders = Slider.objects.all()

    context = {
        'categories': categories,
        'subcategories': subcategories,
        'products': products,
        'pro':pro, 'part':part, 'clint':clint, 'umachine':umachine, 'sliders':sliders

    }
    return render(request,  "index.html", context)

def services(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    umachine = UsedMachine.objects.all()
    context = {
        'categories': categories,
        'subcategories': subcategories, 'umachine':umachine

    }
    return render(request, 'services.html', context)

def solutions(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    umachine = UsedMachine.objects.all()
    context = {
        'categories': categories,
        'subcategories': subcategories, 'umachine':umachine

    }
    return render(request, 'solutions.html', context)

def about(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    umachine = UsedMachine.objects.all()
    # product = Product.objects.all()

    context = {
        'categories': categories,
        'subcategories': subcategories, 'umachine':umachine
        # 'product': product
    }
    return render(request,  "about.html", context)

def contact(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    umachine = UsedMachine.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send an email
        recipient_list = ['info@tetratech.com.sa']
        send_mail(subject, message, email, recipient_list)
        messages.success(request, "Your Email Has Beend Send Successfully!, We will get you in touch soon!")
    context = {
        'categories': categories,
        'subcategories': subcategories, 'umachine':umachine

    }
    return render(request,  "contact.html", context)

# class CategoryView(View):
#     def get(self,request,val):
#         product = Product.objects.filter(category=val)
#         title = Product.objects.filter(category=val).values('title')

#         return render(request,"app/category.html",locals())


class ProductDetails(View):
    def get(self,request,pk):
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        umachine = UsedMachine.objects.all()

        product = Product.objects.get(pk=pk)
        proddetail = ProductDetail.objects.filter(Product=product)
        context = {
            'product':product, 'proddetail':proddetail, 'categories':categories, 'subcategories':subcategories, 'umachine':umachine
        }
        return render(request,"productdetail.html", context)
    
class MachineDetails(View):
    def get(self,request,pk):
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        umachine = UsedMachine.objects.all()

        umachine_details = UsedMachine.objects.get(pk=pk)
        uimage = UsedMachineryImages.objects.filter(Name=umachine_details)

        context = {
            'umachine_details':umachine_details, 'uimage':uimage, 'categories':categories, 'subcategories':subcategories, 'umachine':umachine
        }
        return render(request, 'machinedetails.html', context)
    
class ProjectDetails(View):
    def get(self,request,pk):
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        umachine = UsedMachine.objects.all()

        pro = Project.objects.get(pk=pk)
        context = {
            'pro':pro, 'categories':categories, 'subcategories':subcategories, 'umachine':umachine
        }
        return render(request,"projectdetail.html", context)
    
class SubProductDetails(View):
    def get(self,request,pk):
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        product = Product.objects.all()
        umachine = UsedMachine.objects.all()

        subproduct = SubProduct.objects.get(pk=pk)
        subproddetail = SubProductDetail.objects.filter(SubProduct=subproduct)
        context = {
            'product':product, 'subproddetail':subproddetail, 'categories':categories, 'subcategories':subcategories, 'subproduct':subproduct, 'umachine':umachine
        }
        return render(request,"subproductdetail.html", context)
    
def All_Products(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    umachine = UsedMachine.objects.all()
    prods = Product.objects.all()
    context = {
        'prods': prods, 'categories':categories, 'subcategories':subcategories, 'umachine':umachine
    }
    return render(request, 'category.html', context)

def All_Projects(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    umachine = UsedMachine.objects.all() 
    search_query = request.GET.get('q', '')  # Get the search query from the URL

    if search_query:
        # Filter projects based on the search query
        pro = Project.objects.filter(Q(ProjectName__icontains=search_query) | Q(Description__icontains=search_query))
    else:
        pro = Project.objects.all()
    context = {
        'pro': pro,  'categories':categories, 'subcategories':subcategories,  'umachine':umachine
    }
    return render(request, 'projects.html', context)

def All_Machines(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    pro = Project.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        umachine = UsedMachine.objects.filter(Q(Name__icontains=search_query) |  Q(Description__icontains=search_query))
    else:
        umachine = UsedMachine.objects.all()
    context = {
        'pro': pro,  'categories':categories, 'subcategories':subcategories,  'umachine':umachine
    }
    return render(request, 'allmachines.html', context)

class ProductAgainstCategory(View):
    def get(self, request, pk):
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        umachine = UsedMachine.objects.all()
        subcat = SubCategory.objects.get(pk=pk)

        # prod = Product.objects.filter(SubCategory=subcat)
        search_query = request.GET.get('q', '')
        # Filter products based on the search query
        prod = Product.objects.filter(
            Q(ProductName__icontains=search_query) |  
            Q(Description__icontains=search_query) 
        ).filter(SubCategory=subcat)
        context = {
            'subcat':subcat, 'prod':prod, 'categories':categories, 'subcategories':subcategories, 'umachine':umachine
        }
        return render(request, 'categoryproduct.html', context)

# class ProductAgainstCategory(View):
#     def get(self, request, pk):
#         categories = Category.objects.all()
#         subcategories = SubCategory.objects.all()
#         umachine = UsedMachine.objects.all()
#         subcat = SubCategory.objects.get(pk=pk)

#         # prod = Product.objects.filter(SubCategory=subcat)
#         search_query = request.GET.get('q', '')
#         # Filter products based on the search query
#         prod = Product.objects.filter(
#             Q(ProductName__icontains=search_query) |  # Search in product name
#             Q(Description__icontains=search_query)  # Search in product description
#         ).filter(SubCategory=subcat).first()
#         subproduct = SubProduct.objects.filter(Product=prod)
#         context = {
#             'subcat': subcat,
#             'prod': prod,
#             'categories': categories,
#             'subcategories': subcategories,
#             'umachine': umachine,
#             'subproduct': subproduct
#         }
#         return render(request, 'categoryproduct.html', context)


    
class SubProductAgainstProduct(View):
    def get(self, request, pk):
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        product = Product.objects.all()

        pro = Product.objects.get(pk=pk)
        search_query = request.GET.get('q', '')
        subproduct = SubProduct.objects.filter(
            Q(SubProductName__icontains=search_query) |  
            Q(Description__icontains=search_query)
        ).filter(Product=pro)
        context = {
            'subproduct':subproduct, 'product':product, 'categories':categories, 'subcategories':subcategories, 'pro':pro
        }
        return render(request, 'productsubproduct.html', context)
    
def allcategories(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {
        'categories':categories, 'subcategories':subcategories
    }
    return render(request, 'allcategories.html', context)
    
# def dynamic_nav_menu(request):
#     # Retrieve all categories and their subcategories
#     categories = Category.objects.all()
#     subcategories = SubCategory.objects.all()

#     context = {
#         'categories': categories,
#         'subcategories': subcategories,
#     }

#     return render(request, 'base.html', context)

def SolutionDesign(request):
    return render(request, 'solutiondesign.html')

def SolutionEngineer(request):
    return render(request, 'solutionengineer.html')

def SolutionFabrication(request):
    return render(request, 'solutionfabrication.html')

def SolutionInstallation(request):
    return render(request, 'solutioninstallation.html')

def SolutionMantainence(request):
    return render(request, 'solutionmantainence.html')


def CategorySubCategory(request, id):
    category = Category.objects.get(CategoryID=id)
    subcat = SubCategory.objects.filter(Category=category)
    context = {
        'category':category, 'subcat':subcat
    }
    return render(request, 'subcategory.html', context)