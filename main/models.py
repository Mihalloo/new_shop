from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True) #db_index=True - создать индекс для данного поля(для фильтрации товаров)
    slug = models.SlugField(max_length=100, unique=True) #models.SlugField - создается генерация urk на продукт

    class Meta:
        ordering = ('name',) # сортировка будет по name
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) #related_name='products' - отображение в админке. on_delete=models.CASCADE - если удалить категорию удаляться все продукты
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #upload_to='products/%Y/%m/%d' - дата когда был загружен файл. blank=True - поле может быть пустым без картинки
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) #decimal_places=2 - максимальное количество цифр после запятой
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name