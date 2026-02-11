from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team_id', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'activity_type', 'duration', 'calories', 'date')
    search_fields = ('user_id', 'activity_type')
    list_filter = ('activity_type', 'date')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'team_name', 'total_points', 'rank', 'updated_at')
    search_fields = ('user_name', 'team_name')
    list_filter = ('updated_at',)
    ordering = ('-total_points',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'duration', 'category', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('difficulty', 'category', 'created_at')
