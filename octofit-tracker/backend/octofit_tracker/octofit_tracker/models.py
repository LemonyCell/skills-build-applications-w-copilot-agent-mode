from djongo import models


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=24, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in km
    calories = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} - {self.duration} mins"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    user_name = models.CharField(max_length=100)
    team_id = models.CharField(max_length=24, null=True, blank=True)
    team_name = models.CharField(max_length=100, null=True, blank=True)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_points']

    def __str__(self):
        return f"{self.user_name} - {self.total_points} points"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)  # beginner, intermediate, advanced
    duration = models.IntegerField()  # in minutes
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
