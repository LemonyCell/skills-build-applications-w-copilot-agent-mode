from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! The mightiest heroes on Earth'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League - Fighting for truth and justice'
        )

        self.stdout.write('Creating users...')
        users_data = [
            # Marvel superheroes
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': team_marvel},
            {'name': 'Steve Rogers', 'email': 'captain@marvel.com', 'team': team_marvel},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com', 'team': team_marvel},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'team': team_marvel},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'team': team_marvel},
            # DC superheroes
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': team_dc},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': team_dc},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'team': team_dc},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'team': team_dc},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'team': team_dc},
        ]

        users = []
        for user_data in users_data:
            user = User.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                team_id=str(user_data['team']._id)
            )
            users.append(user)
            self.stdout.write(f'  Created user: {user.name}')

        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Swimming', 'Cycling', 'Weightlifting', 'Yoga']
        for user in users:
            for i in range(random.randint(5, 10)):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = duration * random.randint(5, 12)
                
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_type,
                    duration=duration,
                    distance=round(random.uniform(2.0, 15.0), 2) if activity_type in ['Running', 'Cycling'] else None,
                    calories=calories,
                    date=datetime.now() - timedelta(days=random.randint(0, 30))
                )
        self.stdout.write(f'  Created {Activity.objects.count()} activities')

        self.stdout.write('Creating leaderboard entries...')
        for user in users:
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_points = sum([act.calories for act in user_activities])
            
            team = team_marvel if user.team_id == str(team_marvel._id) else team_dc
            
            Leaderboard.objects.create(
                user_id=str(user._id),
                user_name=user.name,
                team_id=user.team_id,
                team_name=team.name,
                total_points=total_points,
                rank=0
            )
        
        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_points')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(f'  Created {Leaderboard.objects.count()} leaderboard entries')

        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity workout for building strength and endurance',
                'difficulty': 'advanced',
                'duration': 60,
                'category': 'Strength Training'
            },
            {
                'name': 'Speedster Sprint Session',
                'description': 'Lightning-fast cardio workout to boost your speed',
                'difficulty': 'intermediate',
                'duration': 45,
                'category': 'Cardio'
            },
            {
                'name': 'Amazonian Warrior Workout',
                'description': 'Full-body combat training for warriors',
                'difficulty': 'advanced',
                'duration': 75,
                'category': 'Combat Training'
            },
            {
                'name': 'Beginner Hero Training',
                'description': 'Start your hero journey with this beginner-friendly workout',
                'difficulty': 'beginner',
                'duration': 30,
                'category': 'General Fitness'
            },
            {
                'name': 'Arc Reactor Core Workout',
                'description': 'Build a strong core like Iron Man',
                'difficulty': 'intermediate',
                'duration': 40,
                'category': 'Core Strength'
            },
            {
                'name': 'Kryptonian Power Training',
                'description': 'Unleash your inner strength with this power workout',
                'difficulty': 'advanced',
                'duration': 90,
                'category': 'Power Training'
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(f'  Created {Workout.objects.count()} workouts')

        self.stdout.write(self.style.SUCCESS('\nSuccessfully populated the database!'))
        self.stdout.write(f'  Teams: {Team.objects.count()}')
        self.stdout.write(f'  Users: {User.objects.count()}')
        self.stdout.write(f'  Activities: {Activity.objects.count()}')
        self.stdout.write(f'  Leaderboard: {Leaderboard.objects.count()}')
        self.stdout.write(f'  Workouts: {Workout.objects.count()}')
