from django.core.management.base import BaseCommand
from hw2app.models import ClientModel

class Command(BaseCommand):
    help = 'Add new client'
    def handle(self, *args, **kwargs):
        user = ClientModel(name='Serj',
                           email='serj@example.com',
                           phone=89994445777,
                           address='SPb Nevskiy')
        user.save()
        self.stdout.write(f'{user}')

