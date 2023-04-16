from django.contrib import admin

# Register your models here.
from category_app import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Create)
