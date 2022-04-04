
class Paires_Joueurs:

    def __init__(self, liste_joueurs):
        self.liste_joueurs = liste_joueurs

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
