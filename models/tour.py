from datetime import datetime


class Tour:
    def __init__(
            self,
            liste_de_paires: str = None,
            tour: int = None,
            debut_tour: datetime = None,
            fin_tour: datetime = None
    ):
        self.liste_de_paires = liste_de_paires,
        self.tour = tour,
        self.debut_tour = debut_tour,
        self.fin_tour = fin_tour

    def debut_tour():
        debut_tour = datetime.now().strftime("%I%p %M:%S")
        return debut_tour

    def fin_tour():
        fin_tour = datetime.now().strftime("%I%p %M:%S")
        return fin_tour
