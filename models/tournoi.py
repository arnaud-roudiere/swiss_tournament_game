from datetime import datetime


class Tournament:
    def __init__(
            self,
            nom_du_tournoi: str = None,
            lieu: str = None,
            date_debut: datetime = None,
            date_fin: datetime = None,
            joueurs: int = 8,
            nombre_de_tours: int = 4,
            tournees: int = 4,
            controle_du_temps: str = None,
            description: str = None

    ):
        self.nom_du_tournoi = str(nom_du_tournoi)
        self.lieu = str(lieu)
        self.date_debut = str(date_debut)
        self.date_fin = str(date_fin)
        self.joueurs = joueurs
        self.nombre_de_tours: nombre_de_tours
        self.tournees = tournees
        self.controle_du_temps = controle_du_temps
        self.description = description

    def __str__(self):
        return self.nom_du_tournoi
