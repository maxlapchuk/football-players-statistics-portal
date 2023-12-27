from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from players_results.models import Sponsor, Team, Player, MatchStatistics


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ["name", "country", ]
    search_fields = ["name", ]
    actions = None


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "country", ]
    search_fields = ["name", ]
    actions = None


@admin.register(MatchStatistics)
class MatchStatisticsAdmin(admin.ModelAdmin):
    list_display = [
        "player",
        "minutes_played",
        "goals",
        "assists",
        "played_at",
    ]
    search_fields = ["name", ]
    list_filter = ["player", "played_at"]
    actions = None


@admin.register(Player)
class PlayerAdmin(UserAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "team",
        "position"
    ]
    fieldsets = (
        ("Login info", {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Team and position", {"fields": ("team", "position")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        ("Date of joining", {"fields": ("date_joined", )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Team and position", {"fields": ("team", "position")}),
    )
    actions = None


admin.site.unregister(Group)
