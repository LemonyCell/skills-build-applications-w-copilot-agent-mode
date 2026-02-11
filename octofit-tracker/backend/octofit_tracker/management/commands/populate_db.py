from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db MongoDB database with test data.'

    def handle(self, *args, **options):
        User = get_user_model()
        user1, _ = User.objects.get_or_create(username='alice', email='alice@example.com')
        user1.set_password('password123')
        user1.save()
        user2, _ = User.objects.get_or_create(username='bob', email='bob@example.com')
        user2.set_password('password123')
        user2.save()
        self.stdout.write(self.style.SUCCESS('Test users created. Add more test data as needed.'))
