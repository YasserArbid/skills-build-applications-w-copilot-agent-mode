from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Models for each collection
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(email='tony@marvel.com', name='Iron Man', team='Marvel'),
            User(email='steve@marvel.com', name='Captain America', team='Marvel'),
            User(email='bruce@marvel.com', name='Hulk', team='Marvel'),
            User(email='clark@dc.com', name='Superman', team='DC'),
            User(email='diana@dc.com', name='Wonder Woman', team='DC'),
            User(email='barry@dc.com', name='Flash', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user_email='tony@marvel.com', type='Running', duration=30),
            Activity(user_email='steve@marvel.com', type='Cycling', duration=45),
            Activity(user_email='clark@dc.com', type='Swimming', duration=60),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Workouts
        workouts = [
            Workout(name='Push Ups', difficulty='Easy'),
            Workout(name='Pull Ups', difficulty='Medium'),
            Workout(name='Squats', difficulty='Hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
