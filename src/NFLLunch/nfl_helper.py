#
# Wrapper for nflhelper library
#
from datetime import datetime
from typing import Any, List

import nflgame

CURRENT_YEAR = datetime.today().year


class Team:
    """
    Class representation of a team containing all games and players in a given season
    """

    def __init__(
        self, name: str, games: List[Any] = None, players: List[Any] = None
    ) -> None:
        self.name = name
        self.__games = games
        self.__players = players

    def set_players(self, players: List[Any]) -> None:
        self.__players = players

    def set_games(self, games: List[Any]) -> None:
        self.__games = games

    def get_players(self):
        return self.__players

    def get_games(self):
        return self.__games


class NFLGameHelper:
    """
    Wrapper for the nflgame client with specific functionality for NFLLunch
    """

    def __init__(self, nflgame_client):
        self.__client = nflgame_client

    def get_all_team_games(self, team: str, year: int = CURRENT_YEAR) -> List[Any]:
        """Return a list of Game objects for a given team and a given year."""
        return self.__client.games(year, home=team, away=team)

    def get_all_team_players(self, team: str) -> List:
        """Return a list of Player objects for a given team"""
        return [
            player for player in self.__client.players.values() if player.team == team
        ]

    def get_all_teams(self):
        return {team[0]: team for team in self.__client.teams}


def populate_team_data(team: str) -> Team:
    """
    This is for demo purposes only, it will be removed later on and the
        nflgame import will be removed as well
    """
    helper = NFLGameHelper(nflgame_client=nflgame)
    t = Team(team)
    t.set_players(helper.get_all_team_players(team))
    t.set_games(helper.get_all_team_games(team))

    return t


def main():
    """
    Also for demo purposes, will be removed later on
    """
    team = populate_team_data('MIN')
    players = team.get_players()
    games = team.get_games()

    for player in players:
        print(f"{team.name}: {player.position} {player.name}")

    for game in games:
        print(
            f"Week: {game.schedule['week']}, "
            f"Time: {game.schedule['time']}, "
            f"Home: {game.home}, "
            f"Away: {game.away}")


main()
