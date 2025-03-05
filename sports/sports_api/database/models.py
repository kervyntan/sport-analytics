import uuid
from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    public_id = models.CharField(max_length=50, null=True, editable=False) # Null if they don't provide id
    season = models.IntegerField(default=2025)
    team = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ["-date_created"]

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.id = uuid.uuid4()
            self.public_id = self.generate_unique_public_id(self.id)
        super().save(*args, **kwargs)

    @classmethod
    def prepare_for_bulk_create(cls, instances):
        for instance in instances:
            if not instance.id:
                instance.id = uuid.uuid4()
            if not instance.public_id:
                instance.public_id = cls.generate_static_public_id(instance.id)
        return instances

    @classmethod
    def prepare_for_bulk_create_dicts(cls, instances: dict):
        for instance in instances:
            if "id" not in instance.keys():
                instance["id"] = uuid.uuid4()
            if "public_id" not in instance.keys():
                instance["public_id"] = cls.generate_static_public_id(instance["id"])
        return instances

    @staticmethod
    def generate_static_public_id(id: uuid.UUID) -> str:
        return str(id.hex)[:8]

    def generate_unique_public_id(self, id: uuid.UUID) -> str:
        return str(id.hex)[:8]

    def soft_delete(self):

        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super().delete()

    def __str__(self):
        return self.public_id

class UnderstatPlayer(BaseModel):
    player_id = models.CharField(max_length=20, unique=True)
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


class UnderstatTeamResult(BaseModel):
    is_result = models.BooleanField()
    side = models.CharField(max_length=1)
    h_id = models.CharField(max_length=10)
    h_title = models.CharField(max_length=50)
    h_short_title = models.CharField(max_length=10)
    a_id = models.CharField(max_length=10)
    a_title = models.CharField(max_length=50)
    a_short_title = models.CharField(max_length=10)
    goals_a = models.IntegerField() 
    goals_h = models.IntegerField() 
    xG_a = models.IntegerField()
    xG_h = models.IntegerField()
    forecast_w = models.FloatField()
    forecast_d = models.FloatField()
    forecast_l = models.FloatField()
    datetime = models.DateTimeField()
    result = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.h_title} vs {self.a_title} - {self.result}"
    
class UnderstatTeamSituation(BaseModel):
    source = models.CharField(max_length=20)
    shots = models.IntegerField()
    goals = models.IntegerField()
    xG = models.FloatField()
    against_shots = models.IntegerField()
    against_goals = models.IntegerField()
    against_xG = models.FloatField()
    percent_shots_made = models.FloatField()
    percent_shots_made_across_all_goals = models.FloatField(null=True)
    percent_against_shots_made = models.FloatField()
    percent_against_shots_made_across_all_goals = models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.team}, {self.source}"
class UnderstatTeamFormationStats(BaseModel):
    source = models.CharField(max_length=20)
    time_spent = models.IntegerField()
    shots = models.IntegerField()
    goals = models.IntegerField()
    xG = models.FloatField()
    against_shots = models.IntegerField()
    against_goals = models.IntegerField()
    against_xG = models.FloatField()
    percent_shots_made = models.FloatField()
    percent_shots_made_across_all_goals = models.FloatField(null=True)
    percent_against_shots_made = models.FloatField()
    percent_against_shots_made_across_all_goals = models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.team}, {self.source}"
class UnderstatTeamTimingStats(BaseModel):
    source = models.CharField(max_length=20)
    shots = models.IntegerField()
    goals = models.IntegerField()
    xG = models.FloatField()
    against_shots = models.IntegerField()
    against_goals = models.IntegerField()
    against_xG = models.FloatField()
    percent_shots_made = models.FloatField()
    percent_shots_made_across_all_goals = models.FloatField(null=True)
    percent_against_shots_made = models.FloatField()
    percent_against_shots_made_across_all_goals = models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.team}, {self.source}"

class UnderstatTeamPlayerStats(BaseModel):
    player_name = models.CharField(max_length=100)
    lowercase_player_name = models.CharField(max_length=100)
    games = models.IntegerField()
    time = models.IntegerField()
    goals = models.IntegerField()
    xG = models.FloatField()
    assists = models.IntegerField()
    xA = models.FloatField()
    shots = models.IntegerField()
    key_passes = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    position = models.CharField(max_length=50)
    npg = models.IntegerField()  # Non-penalty goals
    npxG = models.FloatField()   # Non-penalty expected goals
    '''
    Find all the possessions each player is involved in.
    Find all the shots within those possessions.
    Sum their xG (you might take the highest xG per possession, or you might treat the shots as dependent events, whatever floats your boat).
    Assign that sum to each player, however involved they were.
    '''
    xGChain = models.FloatField()
    xGBuildup = models.FloatField()

    def __str__(self):
        return f"{self.player_name} - {self.team}"

