from django.contrib.auth.models import AbstractUser
from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    sponsors = models.ManyToManyField(
        to=Sponsor,
        related_name="teams"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Player(AbstractUser):
    team = models.ForeignKey(
        to=Team,
        on_delete=models.CASCADE,
        related_name="players"
    )
    position = models.CharField(max_length=255)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MatchStatistics(models.Model):
    player = models.ForeignKey(
        to=Player,
        on_delete=models.CASCADE,
        related_name="matches_statistics"
    )
    minutes_played = models.PositiveSmallIntegerField()
    goals = models.PositiveSmallIntegerField()
    assists = models.PositiveSmallIntegerField()
    played_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-played_at"]
        verbose_name_plural = "matches statistics"

    def __str__(self):
        return (f"Statistics of {self.player.first_name} {self.player.last_name}: "
                f"played {self.minutes_played} minutes, scored {self.goals}, assisted {self.assists}.\n"
                f"Match played at {self.played_at}.")
