import logging
from datetime import datetime
from typing import Union
import sleeper_wrapper as sleeper

YEAR = datetime.now().year
LOG = logging.getLogger("NFLLunch.sleeper_helper")
# helper = SleeperHelper(sleeper, 11)


class SleeperHelper:
    def __init__(self, sleeper) -> None:
        self.client = sleeper

    def __get_all_players(self):
        """
            Return all NFL players and defenses
        """
        return self.client.Players().get_all_players()

    def __get_all_deffensive_players(self):
        """
            Return all defensive NFL players
        """
        return {
            d: v
            for d, v in self.__get_all_players.items()
            if v['position'] == 'DEF'
        }

    def __get_all_offensive_players(self):
        """
            Return all offensive NFL players
        """
        all_players = self.__get_all_players
        return {
            k: all_players[k]
            for k in set(all_players) - set(self.__get_all_deffensive_players)
        }

    def id_from_player_name(self, full_name: str) -> Union[str, None]:
        """
            Return the ID of a given player
        """
        full_name = full_name.title()
        for player_id, v in self.__get_all_offensive_players.items():
            try:
                if v['full_name'] == full_name:
                    return player_id
            except KeyError:
                logging.info(
                    "KeyError: No 'full_name' for player %s", player_id
                )
                continue
        return None

    def id_from_defense_name(self, def_name: str) -> Union[str, None]:
        """
            Return the ID of a given team's defense.
        """
        def_name = def_name.lower()
        for def_id, v in self.__get_all_deffensive_players.items():
            del v['fantasy_positions']
            del v['active']
            if def_name in [t.lower() for t in list(v.values())]:
                return def_id
        return None


def main() -> None:
    """
        For testing
    """
    pass
