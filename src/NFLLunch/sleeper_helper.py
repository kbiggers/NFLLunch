from datetime import datetime
from typing import Union
import sleeper_wrapper as sleeper

YEAR = datetime.now().year
# helper = SleeperHelper(sleeper, 11)


class SleeperHelper:
    def __init__(
        self, sleeper, week, season=YEAR, season_type='regular'
    ) -> None:
        self.client = sleeper
        self.season = season
        self.season_type = season_type
        self.week = week
        self.all_players = self.client.Players().get_all_players()
        self.defenses = {
            d: v for d, v in self.all_players.items() if v['position'] == 'DEF'
        }
        self.players = {
            k: self.all_players[k]
            for k in set(self.all_players) - set(self.defenses)
        }

    def id_from_player_name(self, full_name: str) -> Union[str, None]:
        """
            Return the ID of a given player
        """
        full_name = full_name.title()
        for player_id, v in self.players.items():
            try:
                if v['full_name'] == full_name:
                    return player_id
            except KeyError:
                continue
        return None

    def id_from_defense_name(self, def_name: str) -> Union[str, None]:
        """
            Return the ID of a given team's defense.
        """
        def_name = def_name.lower()
        for def_id, v in self.defenses.items():
            try:
                del v['fantasy_positions']
                del v['active']
                if def_name in [t.lower() for t in list(v.values())]:
                    return def_id
            except KeyError:
                continue
        return None


def main() -> None:
    """
        For testing
    """
    pass
