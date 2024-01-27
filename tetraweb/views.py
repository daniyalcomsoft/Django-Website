from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customadminpanel.models import *
from customadminpanel.EmailBackEnd import EmailBackEnd
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage

# def CustomAdminPanel(request):
#     return render(request, 'customadminpanel/base.html')

# def Login(request):
#     return render(request, 'login.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user based on email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the desired page after successful login
            return redirect('hod_home')  # Change 'dashboard' to your desired URL name
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')

# def doLogin(request):
#     if request.method == "POST":
#         user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),password=request.POST.get('password'))
#         if user!=None:
#             login(request,user)
#             user_type = user.user_type
#             if user_type == '1':
#                 return redirect('hod_home')
#             elif user_type == '2':
#                 return HttpResponse('This is Staff Panel')
#             elif user_type == '3':
#                 return HttpResponse('This is Engineer Panel')
#             else:
#                 messages.error(request,'Email or Password are invalid!!!')
#                 return redirect('login')
#         else:
#             messages.error(request,'Email or Password are invalid!!!')
#             return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')

@login_required
def HOME(request):
    product_count = Product.objects.count()
    project_count = Project.objects.count()
    used_machine_count = UsedMachine.objects.count()

    context = {
        'product_count': product_count,
        'project_count': project_count,
        'used_machine_count': used_machine_count,
    }
    return render(request, 'home.html', context)

# @login_required(login_url='/')
# def PROFILE(request):
#     user = CustomUser.objects.get(id=request.user.id)
#     context ={
#         "user":user,
#     }
#     return render(request, 'profile.html', context)

# @login_required(login_url='/')
# def PROFILE_UPDATE(request):
#     if request.method == "POST":
#         profile_pic = request.FILES.get('profile_pic')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         password = request.POST.get('password')
#         try:
#             customuser = CustomUser.objects.get(id=request.user.id)
#             customuser.first_name = first_name
#             customuser.last_name = last_name
#             if password !=None and password != "":
#                 customuser.set_password(password)
#             if profile_pic != None and profile_pic != "":
#                 customuser.profile_pic = profile_pic
#             customuser.save()
#             messages.success(request, "your profile Updated Successfully!") 
#         except:
#             messages.error(request, "Failed to Update your profile")
#     return render(request, 'profile.html')

def Add_Category(request):
    if request.method == "POST":
        CategoryName = request.POST.get('CategoryName')
        cat = Category (
            CategoryName = CategoryName
        )
        cat.save()
        messages.success(request, 'Category has been added successfully')
        return redirect('view_category')
    return render(request, 'add_category.html')

def View_Category(request):
    cat = Category.objects.all()
    context = {
        'cat':cat
    }
    return render(request, 'view_category.html', context)

def Edit_Category(request, id):
    cat = Category.objects.get(CategoryID=id)
    context = {
        'cat': cat
    }
    return render(request, 'edit_category.html', context)

def Update_Category(request):
    if request.method == "POST":
        CategoryID = request.POST.get('CategoryID')
        CategoryName = request.POST.get('CategoryName')
        cat = Category.objects.get(CategoryID=CategoryID)
        cat.CategoryName = CategoryName
        cat.save()
        messages.success(request, "Category has been updated successfully!")
        return redirect('view_category')
    return render(request, 'edit_category.html')
def Delete_Category(request, id):
    cat = Category.objects.get(CategoryID=id)
    cat.delete()
    messages.success(request, "Category has been deleted successfully")
    return redirect('view_category')

def Add_SubCategory(request):
    category = Category.objects.all()
    if request.method == "POST":
        CategoryID = request.POST.get('CategoryID')
        SubCategoryName = request.POST.get('SubCategoryName')
        cat = Category.objects.get(CategoryID=CategoryID)
        subcat = SubCategory (
            SubCategoryName = SubCategoryName,
            Category = cat
        )
        subcat.save()
        messages.success(request, 'Sub Category Has been saved successfully!')
        return redirect('view_subcategory')
    context = {
        'category':category
    }
    return render(request, 'add_subcategory.html', context)

def View_SubCategory(request):
    subcat = SubCategory.objects.all()
    context = {
        'subcat': subcat
    }
    return render(request, 'view_subcategory.html', context)

def Edit_SubCategory(request, id):
    subcat = SubCategory.objects.get(SubCategoryID=id)
    cat = Category.objects.all()
    context = {
        'subcat':subcat, 'cat':cat
    }
    return render(request, 'edit_subcategory.html', context)

def Update_SubCategory(request):
    if request.method == "POST":
        CategoryID = request.POST.get('CategoryID')
        SubCategoryID = request.POST.get('SubCategoryID')
        SubCategoryName = request.POST.get('SubCategoryName')

        cat = Category.objects.get(CategoryID=CategoryID)
        subcat = SubCategory.objects.get(SubCategoryID=SubCategoryID)

        subcat.SubCategoryName = SubCategoryName
        subcat.Category = cat
        subcat.save()
        messages.success(request, 'SubCategory has been updated successfully!')
        return redirect('view_subcategory')
    return render(request, 'edit_subcategory.html')

def Delete_SubCategory(request, id):
    subcat = SubCategory.objects.get(SubCategoryID=id)
    subcat.delete()
    messages.success(request, 'Sub Cateogry has been deleted successfully')
    return redirect('view_subcategory')

def Add_Product(request):
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    if request.method == "POST":
        CategoryID = request.POST.get('CategoryID')
        SubCategoryID = request.POST.get('SubCategoryID')

        ProductName = request.POST.get('ProductName')
        Description = request.POST.get('Description')
        Composition = request.POST.get('Composition')
        ProductImage = request.FILES.get('ProductImage')
        ProductFile = request.FILES.get('ProductFile')
        cat = Category.objects.get(CategoryID=CategoryID)
        subcat = SubCategory.objects.get(SubCategoryID=SubCategoryID)
        prod = Product (
            ProductName = ProductName,
            Description = Description,
            Composition = Composition,
            ProductImage = ProductImage,
            ProductFile = ProductFile,
            Category = cat,
            SubCategory = subcat
        )
        prod.save()
        messages.success(request, 'Product has been saved successfully!')
        return redirect('view_product')
    context = {
        'cat': cat, 'subcat':subcat
    }
    return render(request, 'add_product.html', context)

def View_Product(request):
    prod = Product.objects.all()
    context = {
        'prod':prod
    }
    return render(request, 'view_product.html', context)

def View_Product(request):
    prod = Product.objects.all()
    context = {
        'prod': prod
    }
    return render(request, 'view_product.html', context)

def Edit_Product(request, id):
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    prod = Product.objects.get(ProductID=id)
    context = {
        'cat':cat, 'subcat':subcat, 'prod':prod
    }
    return render(request, 'edit_product.html', context)

def Update_Product(request):
    if request.method == "POST":
        CategoryID = request.POST.get('CategoryID')
        SubCategoryID = request.POST.get('SubCategoryID')
        ProductID = request.POST.get('ProductID')

        cat = Category.objects.get(CategoryID=CategoryID)
        subcat = SubCategory.objects.get(SubCategoryID=SubCategoryID)
        prod = Product.objects.get(ProductID=ProductID)

        ProductName = request.POST.get('ProductName')
        Description = request.POST.get('Description')
        Composition = request.POST.get('Composition')
        ProductImage = request.FILES.get('ProductImage')
        ProductFile = request.FILES.get('ProductFile')

        # Delete the old files (if needed)
        if prod.ProductImage:
            default_storage.delete(prod.ProductImage.path)
        if prod.ProductFile:
            default_storage.delete(prod.ProductFile.path)

        prod.ProductName = ProductName
        prod.Description = Description
        prod.Composition = Composition
        prod.ProductImage = ProductImage
        prod.ProductFile = ProductFile
        prod.Category = cat
        prod.SubCategory = subcat

        prod.save()
        messages.success(request, 'Product Has Been Updated Successfully')
        return redirect('view_product')
    return render(request, 'edit_product.html')

def Delete_Product(request, id):
    prod = Product.objects.get(ProductID=id)
    prod.delete()
    messages.success(request, "Product has been deleted successfully")
    return redirect('view_product')

def Add_ProductDetail(request):
    prod = Product.objects.all()
    if request.method == "POST":
        ProductID = request.POST.get('ProductID')

        Field1 = request.POST.get('Field1')
        Field2 = request.POST.get('Field2')
        Field3 = request.POST.get('Field3')
        Field4 = request.POST.get('Field4')
        Field5 = request.POST.get('Field5')
        Description = request.POST.get('Description')

        prod = Product.objects.get(ProductID=ProductID)
        prodetails = ProductDetail(
            Product = prod,
            Field1 = Field1,
            Field2 = Field2,
            Field3 = Field3,
            Field4 = Field4,
            Field5 = Field5,
            Description = Description
        )
        prodetails.save()
        messages.success(request, 'Product Detials has been saved against this prodcut')
        return redirect('view_productdetail')
    context = {
        'prod':prod
    }
    return render(request, 'add_productdetail.html', context)

def View_ProductDetail(request):
    prodetails = ProductDetail.objects.all()
    context = {
        'prodetails': prodetails
    }
    return render(request, 'view_productdetail.html', context)

def Edit_ProductDetail(request, id):
    prod = Product.objects.all()
    proddetails = ProductDetail.objects.get(ProductDetailID=id)
    context = {
        'prod':prod, 'proddetails':proddetails
    }
    return render(request, 'edit_productdetail.html', context)

def Update_ProductDetail(request):
    if request.method == "POST":
        ProductID = request.POST.get('ProductID')
        ProductDetailID = request.POST.get('ProductDetailID')
        prod = Product.objects.get(ProductID=ProductID)
        proddetail = ProductDetail.objects.get(ProductDetailID=ProductDetailID)

        Field1 = request.POST.get('Field1')
        Field2 = request.POST.get('Field2')
        Field3 = request.POST.get('Field3')
        Field4 = request.POST.get('Field4')
        Field5 = request.POST.get('Field5')
        Description = request.POST.get('Description')

        proddetail.Product = prod
        proddetail.Field1 = Field1
        proddetail.Field2 = Field2
        proddetail.Field3 = Field3
        proddetail.Field4 = Field4
        proddetail.Field5 = Field5
        proddetail.Description = Description
        proddetail.save()
        messages.success(request, 'Product Details has been updated successfuly!')
        return redirect('view_productdetail')
    return render(request, 'edit_productdetail.html')

def Delete_ProductDetail(request, id):
    proddetail = ProductDetail.objects.get(ProductDetailID=id)
    proddetail.delete()
    messages.success(request, 'Product Detail has been deleted successfully')
    return redirect('view_productdetail')



# last two models --------------------------------------------------------------------

def Add_SubProduct(request):
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    prod = Product.objects.all()
    if request.method == "POST":
        CategoryID = request.POST.get('CategoryID')
        SubCategoryID = request.POST.get('SubCategoryID')
        ProductID = request.POST.get('ProductID')

        SubProductName = request.POST.get('SubProductName')
        Description = request.POST.get('Description')
        Composition = request.POST.get('Composition')
        ProductImage = request.FILES.get('ProductImage')
        ProductFile = request.FILES.get('ProductFile')
        cat = Category.objects.get(CategoryID=CategoryID)
        subcat = SubCategory.objects.get(SubCategoryID=SubCategoryID)
        prod = Product.objects.get(ProductID=ProductID)
        subprod = SubProduct (
            SubProductName = SubProductName,
            Description = Description,
            Composition = Composition,
            ProductImage = ProductImage,
            ProductFile = ProductFile,
            Category = cat,
            SubCategory = subcat,
            Product = prod
        )
        subprod.save()
        messages.success(request, 'Sub Product has been saved successfully!')
        return redirect('view_subproduct')
    context = {
        'cat': cat, 'subcat':subcat, 'prod':prod,
    }
    return render(request, 'add_subproduct.html', context)

def View_SubProduct(request):
    subprod = SubProduct.objects.all()
    context = {
        'subprod':subprod
    }
    return render(request, 'view_subproduct.html', context)

def Edit_SubProduct(request, id):
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    prod = Product.objects.all()
    subprod = SubProduct.objects.get(SubProductID=id)
    context = {
        'cat':cat, 'subcat':subcat, 'prod':prod, 'subprod':subprod
    }
    return render(request, 'edit_subproduct.html', context)

def Update_SubProduct(request):
    if request.method == "POST":
        CategoryID = request.POST.get('CategoryID')
        SubCategoryID = request.POST.get('SubCategoryID')
        ProductID = request.POST.get('ProductID')
        SubProductID = request.POST.get('SubProductID')

        cat = Category.objects.get(CategoryID=CategoryID)
        subcat = SubCategory.objects.get(SubCategoryID=SubCategoryID)
        prod = Product.objects.get(ProductID=ProductID)
        subprod = SubProduct.objects.get(SubProductID=SubProductID)

        SubProductName = request.POST.get('SubProductName')
        Description = request.POST.get('Description')
        Composition = request.POST.get('Composition')
        ProductImage = request.FILES.get('ProductImage')
        ProductFile = request.FILES.get('ProductFile')

        # Delete the old files (if needed)
        if subprod.ProductImage:
            default_storage.delete(subprod.ProductImage.path)
        if subprod.ProductFile:
            default_storage.delete(subprod.ProductFile.path)

        subprod.SubProductName = SubProductName
        subprod.Description = Description
        subprod.Composition = Composition
        subprod.ProductImage = ProductImage
        subprod.ProductFile = ProductFile
        subprod.Category = cat
        subprod.SubCategory = subcat
        subprod.Product = prod

        subprod.save()
        messages.success(request, 'Sub Product Has Been Updated Successfully')
        return redirect('view_subproduct')
    return render(request, 'edit_subproduct.html')

def Delete_SubProduct(request, id):
    subprod = SubProduct.objects.get(SubProductID=id)
    subprod.delete()
    messages.success(request, 'Sub Product has been delete')
    return redirect('view_subproduct')


# sub product details --------------------------------------------------------------------------------------


def Add_SubProductDetail(request):
    subprod = SubProduct.objects.all()
    if request.method == "POST":
        SubProductID = request.POST.get('SubProductID')

        Field1 = request.POST.get('Field1')
        Field2 = request.POST.get('Field2')
        Field3 = request.POST.get('Field3')
        Field4 = request.POST.get('Field4')
        Field5 = request.POST.get('Field5')
        Description = request.POST.get('Description')

        subprod = SubProduct.objects.get(SubProductID=SubProductID)
        subprodetails = SubProductDetail(
            SubProduct = subprod,
            Field1 = Field1,
            Field2 = Field2,
            Field3 = Field3,
            Field4 = Field4,
            Field5 = Field5,
            Description = Description
        )
        subprodetails.save()
        messages.success(request, 'Sub Product Detials has been saved against this prodcut')
        return redirect('view_subproductdetail')
    context = {
        'subprod':subprod
    }
    return render(request, 'add_subproductdetail.html', context)

def View_SubProductDetail(request):
    subprodetails = SubProductDetail.objects.all()
    context = {
        'subprodetails': subprodetails
    }
    return render(request, 'view_subproductdetail.html', context)

def Edit_SubProductDetail(request, id):
    subprod = SubProduct.objects.all()
    subproddetails = SubProductDetail.objects.get(SubProductDetailID=id)
    context = {
        'subprod':subprod, 'subproddetails':subproddetails
    }
    return render(request, 'edit_subproductdetail.html', context)

def Update_SubProductDetail(request):
    if request.method == "POST":
        SubProductID = request.POST.get('SubProductID')
        SubProductDetailID = request.POST.get('SubProductDetailID')
        subprod = SubProduct.objects.get(SubProductID=SubProductID)
        sbproddetail = SubProductDetail.objects.get(SubProductDetailID=SubProductDetailID)

        Field1 = request.POST.get('Field1')
        Field2 = request.POST.get('Field2')
        Field3 = request.POST.get('Field3')
        Field4 = request.POST.get('Field4')
        Field5 = request.POST.get('Field5')
        Description = request.POST.get('Description')

        sbproddetail.SubProduct = subprod
        sbproddetail.Field1 = Field1
        sbproddetail.Field2 = Field2
        sbproddetail.Field3 = Field3
        sbproddetail.Field4 = Field4
        sbproddetail.Field5 = Field5
        sbproddetail.Description = Description
        sbproddetail.save()
        messages.success(request, 'Sub Product Details has been updated successfuly!')
        return redirect('view_subproductdetail')
    return render(request, 'edit_subproductdetail.html')

def Delete_SubProductDetail(request, id):
    subproddetail = SubProductDetail.objects.get(SubProductDetailID=id)
    subproddetail.delete()
    messages.success(request, 'Sub Product Detail has been deleted successfully')
    return redirect('view_subproductdetail')

def Add_Project(request):
    if request.method == "POST":
        ProjectName = request.POST.get('ProjectName')
        ProjectImage = request.FILES.get('ProjectImage')
        StartDate = request.POST.get('StartDate')
        EndDate = request.POST.get('EndDate')
        Description = request.POST.get('Description')
        pro = Project(
            ProjectName = ProjectName,
            ProjectImage = ProjectImage,
            StartDate = StartDate,
            EndDate = EndDate,
            Description = Description
        )
        pro.save()
        messages.success(request, 'Project Has been added successfully')
        return redirect('view_project')
    return render(request, 'add_project.html')

def View_Project(request):
    pro = Project.objects.all()
    context = {
        'pro': pro
    }
    return render(request, 'view_project.html', context)

def Edit_Project(request, id):
    pro = Project.objects.get(ProjectID=id)
    pro.StartDate = pro.StartDate.strftime('%Y-%m-%d')
    pro.EndDate = pro.EndDate.strftime('%Y-%m-%d')
    context = {
        'pro':pro
    }
    return render(request, 'edit_project.html', context)

def Update_Project(request):
    if request.method == "POST":
        ProjectID = request.POST.get('ProjectID')
        ProjectName = request.POST.get('ProjectName')
        ProjectImage = request.FILES.get('ProjectImage')
        StartDate = request.POST.get('StartDate')
        EndDate = request.POST.get('EndDate')
        Description = request.POST.get('Description')
        pro = Project.objects.get(ProjectID=ProjectID)
                # Delete the old files (if needed)
        if pro.ProjectImage:
            default_storage.delete(pro.ProjectImage.path)

        pro.ProjectName = ProjectName
        pro.ProjectImage = ProjectImage
        pro.StartDate = StartDate
        pro.EndDate = EndDate
        pro.Description = Description
        pro.save()
        messages.success(request, 'Project has been updated successfully')
        return redirect('view_project')
    return render(request, 'edit_project.html')

def Delete_Project(request, id):
    pro = Project.objects.get(ProjectID=id)
    pro.delete()
    messages.success(request, 'Project has been deleted successfully')
    return redirect('view_project')

def Add_Partners(request):
    if request.method == "POST":
        Image = request.FILES.get('Image')
        Link = request.POST.get('Link')
        
        if Image and Link:  # Check if both fields are provided
            partner = Partner(Image=Image, Link=Link)
            partner.save()
            messages.success(request, 'Partner has been added successfully')
            return redirect('view_partners')
        else:
            messages.error(request, 'Please provide both an image and a link.')
    
    return render(request, 'add_partners.html')

def View_Partners(request):
    part = Partner.objects.all()
    context = {
        'part':part
    }
    return render(request, 'view_partners.html', context)

def Edit_Partners(request, id):
    part = Partner.objects.get(PartnerID=id)
    context = {
        'part':part
    }
    return render(request, 'edit_partners.html', context)

def Update_Partners(request):
    if request.method == "POST":
        PartnerID = request.POST.get('PartnerID')
        Image = request.FILES.get('Image')
        Link = request.POST.get('Link')
        part = Partner.objects.get(PartnerID=PartnerID)
        if Image:
            part.Image = Image
        if Link:
            part.Link = Link
        part.save()
        messages.success(request, "Partner has been updated successfully!")
        return redirect('view_partners')
    return render(request, 'edit_partners.html')

def Delete_Partners(request, id):
    part = Partner.objects.get(PartnerID=id)
    part.delete()
    messages.success(request, 'Partner Has been deleted successfully')
    return redirect('view_partners')


def Add_Client(request):
    if request.method == "POST":
        Image = request.FILES.get('Image')
        Link = request.POST.get('Link')
        
        if Image and Link:  # Check if both fields are provided
            client = Client(Image=Image, Link=Link)
            client.save()
            messages.success(request, 'Client has been added successfully')
            return redirect('view_client')
        else:
            messages.error(request, 'Please provide both an image and a link.')
    
    return render(request, 'add_client.html')

def View_Client(request):
    clint = Client.objects.all()
    context = {
        'clint':clint
    }
    return render(request, 'view_client.html', context)

def Edit_Client(request, id):
    clint = Client.objects.get(PartnerID=id)
    context = {
        'clint':clint
    }
    return render(request, 'edit_client.html', context)

def Update_Client(request):
    if request.method == "POST":
        ClientID = request.POST.get('ClientID')
        Image = request.FILES.get('Image')
        Link = request.POST.get('Link')
        clint = Client.objects.get(ClientID=ClientID)
        if Image:
            clint.Image = Image
        if Link:
            clint.Link = Link
        clint.save()
        messages.success(request, "Client has been updated successfully!")
        return redirect('view_client')
    return render(request, 'edit_client.html')

def Delete_Client(request, id):
    clint = Client.objects.get(PartnerID=id)
    clint.delete()
    messages.success(request, 'Client Has been deleted successfully')
    return redirect('view_client')


def Add_UsedMachine(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Description = request.POST.get('Description')
        Image = request.FILES.get('Image')
        Ref = request.POST.get('Ref')
        Year = request.POST.get('Year')
        Brand = request.POST.get('Brand')
        Status = request.POST.get('Status')
        DeliveryTime = request.POST.get('DeliveryTime')
        NumberOfStation = request.POST.get('NumberOfStation')
        Output = request.POST.get('Output')

        usedmachine = UsedMachine(
            Name=Name,
            Description=Description,
            Image=Image,
            Ref=Ref,
            Year=Year,
            Brand=Brand,
            Status=Status,
            DeliveryTime=DeliveryTime,
            NumberOfStation=NumberOfStation,
            Output=Output
        )
        usedmachine.save()
        messages.success(request, 'Used Machine has been saved successfully!')
        return redirect('view_usedmachines')  # Adjust the URL name as per your project

    return render(request, 'add_usedmachines.html')  # Adjust the template name as per your project

def View_UsedMachine(request):
    umachine = UsedMachine.objects.all()
    context = {
        'umachine':umachine
    }
    return render(request, 'view_usedmachines.html', context)

def Edit_UsedMachine(request, id):
    umachine = UsedMachine.objects.get(UsedMachineID=id)
    context = {
        'umachine':umachine
    }
    return render(request, 'edit_usedmachines.html', context)

def Update_UsedMachine(request):

    if request.method == "POST":
        UsedMachineID = request.POST.get('UsedMachineID')
        Name = request.POST.get('Name')
        Description = request.POST.get('Description')
        Image = request.FILES.get('Image')

        Ref = request.POST.get('Ref')
        Year = request.POST.get('Year')
        Brand = request.POST.get('Brand')
        Status = request.POST.get('Status')
        DeliveryTime = request.POST.get('DeliveryTime')
        NumberOfStation = request.POST.get('NumberOfStation')
        Output = request.POST.get('Output')

        used_machine = UsedMachine.objects.get(UsedMachineID=UsedMachineID)

        used_machine.Name = Name
        used_machine.Description = Description

        if Image:
            used_machine.Image = Image

        used_machine.Ref = Ref
        used_machine.Year = Year
        used_machine.Brand = Brand
        used_machine.Status = Status
        used_machine.DeliveryTime = DeliveryTime
        used_machine.NumberOfStation = NumberOfStation
        used_machine.Output = Output

        used_machine.save()
        messages.success(request, 'Used Machine has been updated successfully!')
        return redirect('view_usedmachines')  # Adjust the URL name as per your project

    context = {
        'used_machine': used_machine
    }

    return render(request, 'edit_usedmachines.html', context)  # Adjust the template name as per your project

def Delete_UsedMachine(request, id):
    usedmachine = UsedMachine.objects.get(UsedMachineID=id)
    usedmachine.delete()
    messages.success(request, 'Used Machinery Has been deleted successfully')
    return redirect('view_usedmachines')






def Add_UsedMachineryImages(request):
    umachine = UsedMachine.objects.all()
    if request.method == "POST":
        UsedMachineID = request.POST.get('UsedMachineID')
        Image = request.FILES.get('Image')

        umachine = UsedMachine.objects.get(UsedMachineID=UsedMachineID)
        
        if Image and umachine:  # Check if both fields are provided
            umachinei = UsedMachineryImages(Image=Image, Name = umachine)
            umachinei.save()
            messages.success(request, 'Used Machinery has been added successfully')
            return redirect('view_usedmachineryimages')
        else:
            messages.error(request, 'Please provide image.')
    context = {
        'umachine':umachine
    }
    
    return render(request, 'add_usedmachineryimages.html', context)

def View_UsedMachineryImages(request):
    umachinei = UsedMachineryImages.objects.all()
    context = {
        'umachinei':umachinei
    }
    return render(request, 'view_usedmachineryimages.html', context)

def Edit_UsedMachineryImages(request, id):
    umachinei = UsedMachineryImages.objects.get(UMID=id)
    umachine = UsedMachine.objects.all()
    context = {
        'umachinei':umachinei, 'umachine':umachine
    }
    return render(request, 'edit_usedmachineryimages.html', context)

def Update_UsedMachineryImages(request):
    if request.method == "POST":
        UMID = request.POST.get('UMID')
        UsedMachineID = request.POST.get('UsedMachineID')
        Image = request.FILES.get('Image')
        Name = UsedMachine.objects.get(UsedMachineID=UsedMachineID)
        umachinei = UsedMachineryImages.objects.get(UMID=UMID)
        if Image and Name:
            umachinei.Image = Image
            umachinei.Name = Name
        umachinei.save()
        messages.success(request, "Used Machinery Images has been updated successfully!")
        return redirect('view_usedmachineryimages')
    return render(request, 'edit_usedmachineryimages.html')

def Delete_UsedMachineryImages(request, id):
    umachinei = UsedMachineryImages.objects.get(UMID=id)
    umachinei.delete()
    messages.success(request, 'Used Machinery Has been deleted successfully')
    return redirect('view_usedmachineryimages')

def Add_Sliders(request):
  if request.method == "POST":
    Image = request.FILES.get('Image')
    HeadOne = request.POST.get('HeadOne')
    HeadTwo = request.POST.get('HeadTwo')
    LinkOne = request.POST.get('LinkOne')
    LinkTwo = request.POST.get('LinkTwo')
 
    if Image and HeadOne and HeadTwo and LinkOne and LinkTwo: # Check if all fields are provided
      slider = Slider(Image=Image, HeadOne=HeadOne, HeadTwo=HeadTwo, LinkOne=LinkOne, LinkTwo=LinkTwo)
      slider.save()
      messages.success(request, 'Slider has been added successfully')
      return redirect('view_sliders')
    else:
      messages.error(request, 'Please provide all the required fields.')
   
  return render(request, 'add_sliders.html')

def View_Sliders(request):
  sliders = Slider.objects.all()
  context = {
    'sliders':sliders
  }
  return render(request, 'view_sliders.html', context)

def Edit_Sliders(request, id):
  sliders = Slider.objects.get(SiderID=id)
  context = {
    'sliders':sliders
  }
  return render(request, 'edit_sliders.html', context)

def Update_Sliders(request):
  if request.method == "POST":
    SiderID = request.POST.get('SiderID')
    Image = request.FILES.get('Image')
    HeadOne = request.POST.get('HeadOne')
    HeadTwo = request.POST.get('HeadTwo')
    LinkOne = request.POST.get('LinkOne')
    LinkTwo = request.POST.get('LinkTwo')
    slider = Slider.objects.get(SiderID=SiderID)
    if Image:
      slider.Image = Image
    if HeadOne:
      slider.HeadOne = HeadOne
    if HeadTwo:
      slider.HeadTwo = HeadTwo
    if LinkOne:
      slider.LinkOne = LinkOne
    if LinkTwo:
      slider.LinkTwo = LinkTwo
    slider.save()
    messages.success(request, "Slider has been updated successfully!")
    return redirect('view_sliders')
  return render(request, 'edit_sliders.html')

def Delete_Sliders(request, id):
  slider = Slider.objects.get(SiderID=id)
  slider.delete()
  messages.success(request, 'Slider Has been deleted successfully')
  return redirect('view_sliders')



