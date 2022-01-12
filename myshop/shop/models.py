from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True) # Название продукта.
    slug = models.SlugField(max_length=200, db_index=True) #Алиас продукта(его URL)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #Изображение продукта.
    description = models.TextField(blank=True) #Необязательное описание для продукта.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField() #остатков данного продукта.python -m pip uninstall Pillow
    available = models.BooleanField(default=True) #доступен ли продукт или нет
    created = models.DateTimeField(auto_now_add=True) #дата когда был создан объект
    updated = models.DateTimeField(auto_now=True) #время последнего обновления
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])
