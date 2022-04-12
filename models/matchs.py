class Match:
    def __init__(
            self,
            id: int = None,
            nom_joueur_1: str = None,
            nom_joueur_2: str = None,
            resultat_joueur_1: int = None,
            resultat_joueur_2: int = None):
        self.id = id,
        self.nom_joueur_1 = nom_joueur_1,
        self.nom_joueur_2 = nom_joueur_2,
        self.resultat_joueur_1 = resultat_joueur_1,
        self.resultat_joueur_2 = resultat_joueur_2

    def __str__(self):
        return self.id
