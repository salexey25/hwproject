from django.core.management.base import BaseCommand
from hw2app.models import ClientModel, ProductModel, OrderModel

class Command(BaseCommand):
    help = 'Add new order'

    def handle(self, *args, **options):
        # Создаем заказ с данными о клиенте и продуктах.
        client = ClientModel.objects.get(name='Kiril')
        product1 = ProductModel.objects.get(name='sofa')
        product2 = ProductModel.objects.get(name='armchair')

        # Создание нового заказа
        order = OrderModel(customer=client,
                           total_price=product1.price + product2.price
                           )

        order.save()

        order.products.add(product1, product2) # Добавление продуктов к заказу

        self.stdout.write(f'Успешно сделанный заказ ID {order.id}')



