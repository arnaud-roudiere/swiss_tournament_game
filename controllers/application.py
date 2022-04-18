from models.matchs import Match
from models.tour import Tour


from save.save import Save

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

        return self.paires_joueurs(liste_joueurs, details_tournoi)

    def paires_joueurs(self, liste_joueurs, details_tournoi):
        details_tournoi = details_tournoi
        liste_joueurs = sorted(liste_joueurs.items(), key=lambda t: t[1][4])

        liste_joueurs_sup = liste_joueurs[:int(len(liste_joueurs) / 2)]

        liste_joueurs_inf = liste_joueurs[int(len(liste_joueurs) / 2):]

        liste_de_paires = []

        for i in range(len(liste_joueurs_sup)):
            paire_de_joueurs = []

            paire_de_joueurs.append(liste_joueurs_sup[i][0])
            paire_de_joueurs.append(liste_joueurs_inf[i][0])

            liste_de_paires.append(paire_de_joueurs)

        return self.Deroulement_tours(liste_de_paires,
                                      liste_joueurs,
                                      details_tournoi)

    def Deroulement_tours(self, liste_de_paires,
                          liste_joueurs,
                          details_tournoi):

        self.tour_en_cours = Tour()

        self.tour_en_cours.liste_de_paires = liste_de_paires

        details_tournoi = details_tournoi
        liste_de_paires = liste_de_paires
        liste_joueurs = liste_joueurs

        liste_de_paires_cumul = []

        nombre_de_tours: int = 4
        liste_de_tours = []
        resultats_precedents = {}

        stack = []

        for i in range(nombre_de_tours):
            self.tour_en_cours.liste_de_paires = liste_de_paires
            self.tour_en_cours.tour = i + 1
            print('TOUR nº', self.tour_en_cours.tour)
            liste_de_tours.append(self.tour_en_cours.tour)

            print("*******************************")
            print(f"Début du tour nº {self.tour_en_cours.tour}")
            print("-------------------------------")

            # ----> Début du tour
            self.tour_en_cours.debut_tour = Tour.debut_tour()

            # ----> Resultats_matchs
            tuple_match, resultats_precedents = self.resultats_matchs(
                self.tour_en_cours.liste_de_paires,
                self.tour_en_cours.debut_tour,
                resultats_precedents)

            # ----> Trier les joueurs
            liste_joueurs_classement = self.tri_joueurs(
                tuple_match,
                liste_joueurs,
                resultats_precedents)
            # ----> Refaire des paires de joueurs
            liste_paire_joueurs = self.paires_de_joueurs(
                liste_joueurs_classement,
                stack,
                details_tournoi[list(details_tournoi.keys())[0]][3])

            liste_de_paires = liste_paire_joueurs

            stack += liste_paire_joueurs

            liste_de_paires_cumul += liste_paire_joueurs

        # ----> Sauvegarde des différents éléments
        Save.save_joueurs(liste_joueurs_classement,
                          details_tournoi,
                          liste_de_tours,
                          tuple_match,
                          liste_joueurs)

        return self.fin_tournoi()

    def resultats_matchs(self,
                         liste_de_paires,
                         debut_du_tour,
                         resultats_precedents):

        resultats_precedents = resultats_precedents

        tuple_match = []

        match_en_cours = Match

        for match_en_cours.id, joueurs in enumerate(liste_de_paires):
            match_en_cours.id += 1
            print(f"Résultat du match nº {match_en_cours.id} entre"
                  f" {joueurs[0]} et {joueurs[1]}")

            match_en_cours.nom_joueur_1, \
                match_en_cours.resultat_joueur_1 = \
                View.resultats_matchs(self, joueurs[0])

            match_en_cours.nom_joueur_2, \
                match_en_cours.resultat_joueur_2 = \
                View.resultats_matchs(self, joueurs[1])

            liste_joueur_1_resultat = [match_en_cours.nom_joueur_1,
                                       match_en_cours.resultat_joueur_1]
            liste_joueur_2_resultat = [match_en_cours.nom_joueur_2,
                                       match_en_cours.resultat_joueur_2]

            if len(resultats_precedents) < 8:
                resultats_precedents.update({match_en_cours.nom_joueur_1:
                                            float(match_en_cours.
                                                  resultat_joueur_1)})
                resultats_precedents.update({match_en_cours.nom_joueur_2:
                                            float(match_en_cours.
                                                  resultat_joueur_2)})
            else:
                resultats_precedents.update({match_en_cours.nom_joueur_1:
                                            resultats_precedents[
                                                match_en_cours.nom_joueur_1] +
                                            float(match_en_cours.
                                                  resultat_joueur_1)})
                resultats_precedents.update({match_en_cours.nom_joueur_2:
                                            resultats_precedents[
                                                match_en_cours.nom_joueur_2] +
                                            float(match_en_cours.
                                                  resultat_joueur_2)})

            tour = "Tour nº" + str(self.tour_en_cours.tour)

            self.tour_en_cours.fin_tour = Tour.fin_tour()

            match_en_cours_id = 'Match nº ' + str(match_en_cours.id)

            resultat_match = (tour, match_en_cours_id, liste_joueur_1_resultat,
                              liste_joueur_2_resultat,
                              debut_du_tour, self.tour_en_cours.fin_tour)

            print('--- Résultat du match nº ',
                  match_en_cours.id,
                  ': ',
                  resultat_match)

            tuple_match.append(resultat_match)

        tuple_match = tuple(tuple_match)
        return tuple_match, resultats_precedents

    def tri_joueurs(self, tuple_match, liste_joueurs, resultats_precedents):

        tuple_match_pondere = []
        for i in tuple_match:
            tuple_match_pondere += [
                tuple((list(i[:2]) +
                       [[i[2][0], str(resultats_precedents[i[2][0]])]] +
                       [[i[3][0], str(resultats_precedents[i[3][0]])]] +
                       list(i[4:])))]
        tuple_match = tuple(tuple_match_pondere)

        liste_joueurs_tri = []
        for joueur in tuple_match:
            liste_joueurs_tri.append(joueur[2])
            liste_joueurs_tri.append(joueur[3])

        """ On trie avec le score du match"""

        liste_joueurs_tri.sort(key=lambda x: x[1], reverse=True)

        for i, j in enumerate(liste_joueurs_tri):
            for h in liste_joueurs:
                if j[0] == h[0]:
                    k = liste_joueurs[int(h[0]) - 1][1][4]
                    liste_joueurs_tri[i].append(k)

        liste_classement = []
        for i in liste_joueurs_tri:
            liste_classement.append(i[1])
        liste_joueurs_classement = []
        for i in liste_joueurs_tri:
            if liste_classement.count(i[1]) > 1:
                sub_liste_classement = []
                for j in liste_joueurs_tri:
                    if j[1] == i[1]:
                        sub_liste_classement.append(j)

                sub_liste_classement.sort(key=lambda x: x[2])
                for h in sub_liste_classement:
                    if h not in liste_joueurs_classement:
                        liste_joueurs_classement.append(h)
            else:
                liste_joueurs_classement.append(i)

        return liste_joueurs_classement

    def paires_de_joueurs(self,
                          liste_joueurs_classement,
                          stack,
                          nombre_de_tours):

        paire_1 = []
        liste_paire_joueurs = []
        nombre_de_tours = 4
        for i in range(nombre_de_tours):
            paire_1.append(liste_joueurs_classement[0][0])
            liste_joueurs_classement = liste_joueurs_classement[1:]
            if [paire_1[0], liste_joueurs_classement[0][0]] not in stack:
                paire_1.append(liste_joueurs_classement[0][0])
                liste_joueurs_classement = liste_joueurs_classement[1:]
                liste_paire_joueurs.append(paire_1)
                paire_1 = []
            else:
                if len(liste_joueurs_classement) > 1:
                    paire_1.append(liste_joueurs_classement[1][0])
                    liste_joueurs_classement = [liste_joueurs_classement[0]] +\
                        liste_joueurs_classement[2:]
                else:
                    paire_1.append(liste_joueurs_classement[0][0])
                    liste_joueurs_classement = liste_joueurs_classement[1:]
                liste_paire_joueurs.append(paire_1)
                paire_1 = []
        return liste_paire_joueurs

    def fin_tournoi(self):
        View.question_quit(self)
        return self.TournamentManager()

    def run(self):
        self.TournamentManager()
