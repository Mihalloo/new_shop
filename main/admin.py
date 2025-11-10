from django.contrib import admin
from .models import Category, Product #.models - . значит импорт из этой же директории где файл админ импортировать данные из фала модели
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] #будут отображаться в админке
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated'] #будут отображаться в админке
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available'] # это параметр класса ModelAdmin, который позволяет редактировать поля прямо в списке объектов в админке Django (на странице списка, без захода внутрь каждой записи).
    prepopulated_fields = {'slug': ('name',)}