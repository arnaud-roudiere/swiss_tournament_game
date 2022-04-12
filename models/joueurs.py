from datetime import datetime


class Joueur:
    def __init__(
            self,
            id: int = None,
            nom_de_famille: str = None,
            prénom: str = None,
            date_de_naissance: datetime = None,
            sexe: str = None,
            classement: int = None,
            points: int = None

    ):
        self.id = id,
        self.nom_de_famille = nom_de_famille,
        self.prénom = prénom,
        self.date_de_naissance = date_de_naissance,
        self.sexe = sexe,
        self.classement = classement
        self.points = points

    def __str__(self):
        return self.prénom
