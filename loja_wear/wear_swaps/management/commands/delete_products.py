from django.core.management.base import BaseCommand
from django.db import connection, transaction
from wear_swaps.models import Produto

class Command(BaseCommand):
    help = 'Delete selected products with foreign key constraints temporarily disabled'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Disable foreign key checks
            cursor.execute('PRAGMA foreign_keys = OFF;')
            self.stdout.write(self.style.SUCCESS('Foreign key checks disabled'))

            try:
                # Perform the deletion inside a transaction
                with transaction.atomic():
                    produtos = Produto.objects.all()  # Adjust this query as needed
                    produtos_count = produtos.count()
                    produtos.delete()
                    self.stdout.write(self.style.SUCCESS(f'{produtos_count} products deleted successfully'))

            finally:
                # Re-enable foreign key checks
                cursor.execute('PRAGMA foreign_keys = ON;')
                self.stdout.write(self.style.SUCCESS('Foreign key checks enabled'))
