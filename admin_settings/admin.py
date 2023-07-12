from django.contrib import admin

from admin_settings.models import Category, SubCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'category']