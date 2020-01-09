import logging
from datetime import datetime
from typing import Union

import sleeper_wrapper as sleeper

YEAR = datetime.now().year
LOG = logging.getLogger("NFLLunch.sleeper_helper")
SEASON_TYPES = ['pre', 'regular', 'post']


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
            for d, v in self.__get_all_players().items()
            if v['position'] == 'DEF'
        }

    def __get_all_offensive_players(self):
        """
            Return all offensive NFL players
        """
        return {
            d: v
            for d, v in self.__get_all_players().items()
            if v['position'] != 'DEF'
        }

    def id_from_player_name(self, full_name: str) -> Union[str, None]:
        """
            Return the ID of a given player
        """
        full_name = full_name.title()
        for player_id, v in self.__get_all_offensive_players().items():
            try:
                if v['full_name'] == full_name:
                    return player_id
            except KeyError:
                logging.info(
                    f"KeyError: No 'full_name' for player {player_id}"
                )
                continue
        return None

    def id_from_defense_name(self, def_name: str) -> Union[str, None]:
        """
            Return the ID of a given team's defense.
        """
        def_name = def_name.lower()
        for def_id, v in self.__get_all_deffensive_players().items():
            del v['fantasy_positions']
            del v['active']
            if def_name in [t.lower() for t in list(v.values())]:
                return def_id
        return None

    def player_week_stats(
        self, player_id: Union[str, int], season_type: str,
        week: Union[str, int]
    ) -> dict:
        """
            Return stats for a given player
        """
        if season_type not in SEASON_TYPES:
            logging.warning(
                (
                    f"'{season_type}' is not a valid season type. "
                    f"Valid options are: {', '.join(SEASON_TYPES)}"
                )
            )
            return None
        return self.client.Stats().get_week_stats(season_type, YEAR, week)[
            str(player_id)
        ]

    def player_season_stats(
        self, player_id: Union[str, int], season_type: str
    ) -> dict:
        """
            Return stats for a given player
        """
        if season_type not in SEASON_TYPES:
            logging.warning(
                (
                    f"'{season_type}' is not a valid season type. "
                    f"Valid options are: {', '.join(SEASON_TYPES)}"
                )
            )
            return None
        return self.client.Stats().get_all_stats(season_type, YEAR)[
            str(player_id)
        ]

    def player_week_projection(
        self, player_id: Union[str, int], season_type: str,
        week: Union[str, int], scoring_only: bool = False
    ) -> dict:
        """
            Returns the weekly projections for a player
        """
        if season_type not in SEASON_TYPES:
            logging.warning(
                (
                    f"'{season_type}' is not a valid season type. "
                    f"Valid options are: {', '.join(SEASON_TYPES)}"
                )
            )
        if scoring_only:
            return {
                k: v
                for k, v in self.client.Stats().get_week_projections(
                    season_type, YEAR, week
                )[str(player_id)].items()
                if k.startswith('pts')
            }
        return self.client.Stats().get_week_projections(
            season_type, YEAR, week
        )[str(player_id)]


def main() -> None:
    """
        For testing
    """
    pass
