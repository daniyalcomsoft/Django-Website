from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('PC','Pre-Construction'),
    ('GC','General Contracting'),
    ('CM','Construction Management'),
    ('DB','Design and Build'),


)

# class Category(models.Model):
#     CategoryID = models.AutoField(primary_key=True)
#     CategoryName = models.CharField(max_length=255, verbose_name="Category Name", blank=False)

#     def __str__(self):
#         return self.CategoryName
    
# class SubCategory(models.Model):
#     SubCategoryID = models.AutoField(primary_key=True)
#     SubCategoryName = models.CharField(max_length=255, verbose_name="Sub Category Name", blank=False)
#     Category = models.ForeignKey(Category, verbose_name="Category Name", on_delete=models.DO_NOTHING)

#     def __str__(self):
#         return self.SubCategoryName


class Product (models.Model):

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    title = models.CharField(max_length=100)
    description = models.TextField()
    composition = models.TextField(default='')        
    product_image = models.ImageField(upload_to = 'product')
    prodfile = models.FileField(upload_to = 'Files',null=True)
    def _str_(self):
        return self.title

class MainCategory (models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()


    def _str_(self):
        return self.title


class SubCategory (models.Model):
    
    title = models.CharField(max_length=100)
    mcategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    description = models.TextField()


    def __str__(self):
        return str(self.mcategory.title)
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
# class ContactEmail(models.Model):
#     ContactEmailID = models.AutoField(primary_key=True)
#     name = models.CharField(max_length==255, verbose_name='Name', null=False)
#     Email = models.EmailField()
#     subject = models.CharField(max_length=255, verbose_name='Subject Name')
#     message = models.TextField()

#     def __str__(self) -> str:
#         return self.name