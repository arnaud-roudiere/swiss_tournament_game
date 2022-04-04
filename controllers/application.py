from models.joueurs import Paires_Joueurs
from models.matchs import Matchs
from models.save import Save

from views.base import View


class Application:

    def __init__(self, Tournament):
        self.Tournament = Tournament

    def MenuManager(self):
        return View.menu_principal()

    def TournamentManager(self):

        choix = self.MenuManager()

        if choix == '1':
            """Accéder aux tournois précédents """
            return Save.load_tournament(self)
        else:
            """Créer un nouveau tournoi """
            return View.creation_tournoi(self)

    def Creation_joueurs(self, details_tournoi):
        details_tournoi = details_tournoi
        return View.creation_players(self, details_tournoi)

    def Creation_paires(self, liste_joueurs, details_tournoi):
        details_tournoi = details_tournoi
        liste_joueurs = liste_joueurs
        return Paires_Joueurs.paires_joueurs(self,
                                             liste_joueurs,
                                             details_tournoi)

    def Deroulement_tours(self, liste_de_paires,
                          liste_joueurs,
                          details_tournoi):

        details_tournoi = details_tournoi
        liste_de_paires = liste_de_paires
        liste_joueurs = liste_joueurs

        nombre_de_tours: int = 4
        liste_de_tours = []

        for i in range(nombre_de_tours):
            tour_actuel = i + 1
            liste_de_tours.append(tour_actuel)

            print("*******************************")
            print(f"Début du tour nº {tour_actuel}")
            print("-------------------------------")

            # Début du tour
            debut_tour = Matchs.debut_tour()

            # Resultats_matchs
            tuple_match = Matchs.resultats_matchs(liste_de_paires,
                                                  debut_tour)

            # Trier les joueurs
            liste_joueurs_classement = Matchs.tri_joueurs(tuple_match,
                                                          liste_joueurs)

            # Refaire des paires de joueurs
            liste_paire_joueurs = \
                Matchs.paires_joueurs(liste_joueurs_classement,
                                      liste_de_paires)
            liste_de_paires = liste_paire_joueurs

        Save.save_joueurs(liste_joueurs_classement,
                          details_tournoi,
                          liste_de_tours,
                          tuple_match,
                          liste_joueurs)

        return self.fin_tournoi()

    def fin_tournoi(self):
        entree = True
        reponses = ["1", "2"]
        while entree is True:
            choix_fin = input("Souhaitez-vous revenir "
                              "sur le menu ou bien quitter"
                              " l'application?\n1/Revenir au menu"
                              " \n2/Quitter \nTapez votre option (1 ou 2)")
            if choix_fin not in reponses:
                return print("La réponse est incorrecte, veuillez réessayer")
            elif choix_fin == '2':
                print('**************** Tournoi terminé *********************')
                quit()
            else:
                return self.TournamentManager()

    def run(self):
        self.TournamentManager()
