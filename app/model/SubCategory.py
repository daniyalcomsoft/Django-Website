# from django.db import models
# from .MainCategory import MainCategory
# from .SubCategory import SubCategory
# from django.conf import settings 
# from datetime import datetime,timezone
# from django.db.models.fields import CharField

# # Create your models here.


# class SubCategory (models.Model):
    
#     title = models.CharField(max_length=100)
#     mcategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE,parent_link=True)
#     description = models.TextField()

#     @staticmethod
#     def get_all_subcategories():
#         return SubCategory.objects.all()

#     def _str_(self):
#         return self.title