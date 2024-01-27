from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


# class CustomUser(AbstractUser):
#     USER = (
#         (1,'ADMIN'),
#         (2, 'USER'),
#     )
#     user_type = models.CharField(choices=USER, max_length=50, default=1)
#     profile_pic = models.ImageField(upload_to='media/profile_pic')

#     def __str__(self):
#         return self.user_type




class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255, blank=False, verbose_name="Category Name")

    def __str__(self) -> str:
        return self.CategoryName
    
class SubCategory(models.Model):
    SubCategoryID = models.AutoField(primary_key=True)
    SubCategoryName = models.CharField(max_length=255, blank=False, verbose_name="Sub Category Name")
    Category = models.ForeignKey(Category, verbose_name='Category Name', on_delete=models.CASCADE)

    def __str__(self):
        return self.SubCategoryName

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255, blank=False, verbose_name="Product Name")
    Description = models.TextField(verbose_name="Product Description")
    Composition = models.TextField(verbose_name="Composition")
    ProductImage = models.ImageField(upload_to= 'media/product', null=True)
    ProductFile = models.FileField(upload_to='media/Files', null=True)
    Category = models.ForeignKey(Category, verbose_name='Category Name', on_delete=models.CASCADE)
    SubCategory = models.ForeignKey(SubCategory, verbose_name='Sub Category Name', on_delete=models.CASCADE)

    def __str__(self):
        return self.ProductName
    
class ProductDetail(models.Model):
    ProductDetailID = models.AutoField(primary_key=True)
    Product = models.ForeignKey(Product, verbose_name="Product Name", on_delete=models.CASCADE)
    Field1 = models.CharField(max_length=255, blank=True, verbose_name="Field1")
    Field2 = models.CharField(max_length=255, blank=True, verbose_name="Field2")
    Field3 = models.CharField(max_length=255, blank=True, verbose_name="Field3")
    Field4 = models.CharField(max_length=255, blank=True, verbose_name="Field4")
    Field5 = models.CharField(max_length=255, blank=True, verbose_name="Field5")
    Description = models.TextField(verbose_name='Description')

    def __str__(self) -> str:
        return self.Field1
    
class SubProduct(models.Model):
    SubProductID = models.AutoField(primary_key=True)
    SubProductName = models.CharField(max_length=255, verbose_name="Sub Product Name", blank=False)
    Description = models.TextField(verbose_name='Description')
    Composition = models.TextField(verbose_name='Composition')
    ProductImage = models.ImageField(upload_to='media/product', null=True)
    ProductFile = models.FileField(upload_to='media/Files', null=True)
    Category = models.ForeignKey(Category, verbose_name='Category Name', on_delete=models.CASCADE)
    SubCategory = models.ForeignKey(SubCategory, verbose_name='Sub Category Name', on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, verbose_name="Main Product Name", on_delete=models.CASCADE)

    def __str__(self):
        return self.SubProductName
    
class SubProductDetail(models.Model):
    SubProductDetailID = models.AutoField(primary_key=True)
    SubProduct = models.ForeignKey(SubProduct, verbose_name="Sub Product Name", on_delete=models.CASCADE)
    Field1 = models.CharField(max_length=255, blank=True, verbose_name="Field1")
    Field2 = models.CharField(max_length=255, blank=True, verbose_name="Field2")
    Field3 = models.CharField(max_length=255, blank=True, verbose_name="Field3")
    Field4 = models.CharField(max_length=255, blank=True, verbose_name="Field4")
    Field5 = models.CharField(max_length=255, blank=True, verbose_name="Field5")
    Description = models.TextField(verbose_name='Description')

    def __str__(self) -> str:
        return self.Field1

class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=255, verbose_name='Project Name', blank=False)
    ProjectImage = models.ImageField(upload_to='media/product', null=True)
    StartDate = models.DateField(verbose_name="Project Start Date", auto_now_add=False)
    EndDate = models.DateField(verbose_name="Project End Date", auto_now_add=False)
    Description = models.TextField()

    def __str__(self):
        return self.ProjectName
    

class Partner(models.Model):
    PartnerID = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='media/product', null=True)
    Link = models.URLField(max_length=5000)

    def __str__(self):
        return self.Link

class Client(models.Model):
    ClientID = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='media/product', null=True)
    Link = models.URLField(max_length=5000)

    def __str__(self) -> str:
        return self.Link


class UsedMachine(models.Model):
    UsedMachineID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=False, verbose_name="Machine Name")
    Description = models.TextField()
    Image = models.ImageField(upload_to='media/product', null=True)
    Ref = models.CharField(max_length=255, verbose_name="Reference No", blank=True)
    Year = models.CharField(max_length=255, verbose_name="Reference No", blank=True)
    Brand = models.CharField(max_length=255, verbose_name="Reference No", blank=True)
    Status = models.CharField(max_length=255, verbose_name="Reference No", blank=True)
    DeliveryTime = models.CharField(max_length=255, verbose_name="Reference No", blank=True)
    NumberOfStation = models.CharField(max_length=255, verbose_name="Reference No", blank=True)
    Output = models.CharField(max_length=255, verbose_name="Reference No", blank=True)

    def __str__(self):
        return self.Name
    
class UsedMachineryImages(models.Model):
    UMID = models.AutoField(primary_key=True)
    Name = models.ForeignKey(UsedMachine, verbose_name="Machine Name", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='media/product', null=True)



# class Product (models.Model):

#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     composition = models.TextField(default='')        
#     product_image = models.ImageField(upload_to = 'product')
#     prodfile = models.FileField(upload_to = 'Files',null=True)
#     def _str_(self):
#         return self.title


    
class Slider(models.Model):
    SiderID = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='media/product', null=True)
    HeadOne = models.CharField(max_length=255, verbose_name="Heading One")
    HeadTwo = models.CharField(max_length=255, verbose_name="Heading Two")
    LinkOne = models.URLField(max_length=5000)
    LinkTwo = models.URLField(max_length=5000)

    def __str__(self):
        return self.HeadOne