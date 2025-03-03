from django.db import models

class UnderstatPlayer(models.Model):
    player_id = models.CharField(max_length=20, primary_key=True)
    player_name = models.CharField(max_length=255)
    games = models.IntegerField()
    time = models.IntegerField(help_text="Playing time in minutes")
    goals = models.IntegerField()
    xG = models.FloatField(help_text="Expected Goals")
    assists = models.IntegerField()
    xA = models.FloatField(help_text="Expected Assists")
    shots = models.IntegerField()
    key_passes = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    position = models.CharField(max_length=2)
    team_title = models.CharField(max_length=255)
    npg = models.IntegerField(help_text="Non-Penalty Goals")
    npxG = models.FloatField(help_text="Non-Penalty Expected Goals")
    xGChain = models.FloatField(help_text="Expected Goals Chain")
    xGBuildup = models.FloatField(help_text="Expected Goals Buildup")

    def __str__(self):
        return f"{self.player_name} - {self.team_title}"

    class Meta:
        verbose_name = "UnderstatPlayer"
        verbose_name_plural = "UnderstatPlayers"
        ordering = ["-goals", "player_name"]