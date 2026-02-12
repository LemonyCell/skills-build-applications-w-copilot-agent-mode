from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team_id', 'created_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date', 'created_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'user_name', 'team_id', 'team_name', 'total_points', 'rank', 'updated_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration', 'category', 'created_at']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None
