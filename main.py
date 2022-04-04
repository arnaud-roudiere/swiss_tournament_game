"""Entry point."""

from controllers.application import Application
from models.tournoi import Tournament


def main():

    tournament = Tournament()
    game = Application(tournament)
    game.run()


if __name__ == "__main__":
    main()
