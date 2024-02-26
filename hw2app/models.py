from django.db import models
from django.urls import reverse

# Create your models here.
class ClientModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    createdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Клиент создан: {self.name}'

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    createdate = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/', default='path/to/default/image.jpg')

    def __str__(self):
        return f'Заведен новый продукт: {self.name}'

class OrderModel(models.Model):
    customer = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel)
    date_order = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_products_list(self):
        return ", ".join([str(product.name) for product in self.products.all()])
    def __str__(self):
        return f'{self.date_order}'



