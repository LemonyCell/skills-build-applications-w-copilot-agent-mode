"""
Script to populate the octofit_db MongoDB database with test data using Django ORM.
"""
import os
import django

def setup_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
    django.setup()

def populate():
    # Import models after Django setup
    from django.contrib.auth import get_user_model
    from octofit_tracker import models

    User = get_user_model()

    # Create test users
    user1, _ = User.objects.get_or_create(username='alice', email='alice@example.com')
    user1.set_password('password123')
    user1.save()
    user2, _ = User.objects.get_or_create(username='bob', email='bob@example.com')
    user2.set_password('password123')
    user2.save()

    # Create test teams, activities, leaderboard, and workouts if models exist
    # Add your model population logic here as needed
    print('Test users created. Add more test data as needed.')

if __name__ == '__main__':
    setup_django()
    populate()
