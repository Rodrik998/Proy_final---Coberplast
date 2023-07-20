from django.db import models

from admin_settings.models import Category, SubCategory

class Product(models.Model):
    name = models.CharField(max_length=50)
    SKU = models.CharField(max_length=20)
    price = models.FloatField()
    product_image = models.ImageField(upload_to='poroduct_image', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)

    class Meta:
            verbose_name = 'Producto'
            verbose_name_plural = 'Productos'


class ExtraImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='extra_images')
    image = models.ImageField(upload_to='product/extra-images/')

    def __str__(self):
        return f'{self.product.name} - {str(self.id)}'
    
    class Meta:
            verbose_name = 'Imagen extra de producto'
            verbose_name_plural = 'Imagenes extra de producto'