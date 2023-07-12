from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

class SubCategory(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')

    def __str__(self):
        return f'{self.category.name} - {self.name}'
    
    class Meta:
        verbose_name='Subcategoria'
        verbose_name_plural='Subcategorias'