from django.core.management.base import BaseCommand
from accounts.models import Task

class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **options):
        Task.objects.create(title='Task 1', description='Sample task 1', status=1)
        Task.objects.create(title='Task 2', description='Sample task 2', status=2)
        Task.objects.create(title='Task 3', description='Sample task 3', status=3)

        self.stdout.write(self.style.SUCCESS('Successfully seeded test data.'))