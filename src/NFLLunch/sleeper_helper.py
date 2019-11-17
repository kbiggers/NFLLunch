import sleeper_wrapper as sleeper
from datetime import datetime

YEAR = datetime.now().year


class SleeperHelper:
    def __init__(self, sleeper, season=YEAR, season_type='regular'):
        self.client = sleeper
        self.season = season
        self.season_type = season_type
        self.players = self.sleeper_client.get_all_players()

    def player_from_id(self, player):
        pass

    def get_stats(self, season=self.season: int,
        season_type=self.season_type: str, week: int
    ):
        """
        Return specified stat type
        """
        stats_client = self.client.Stats()
        season_stats = stats_client.get_all_stats(season_type, season)
        week_stats = stats_client.get_week_stats(season_type, season, week)
        return season_stats, week_stats

    def trending_players(self, hours: int = 24, results: int = 25, mode: str):
        valid_modes = ['add', 'drop']
        if mode not in valid_modes:
            return
        return self.client.Players().get_trending_players(
            sport='nfl',
            add_drop='mode',
            hours=hours,
            limit=limit
        )
        
