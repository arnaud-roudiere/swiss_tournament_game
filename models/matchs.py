from datetime import datetime


class Matchs:
    def __init__(self, liste_de_paires, debut_tour):
        self.liste_de_paires = liste_de_paires
        self.debut_tour = debut_tour

    def debut_tour():
        debut_tour = datetime.now().strftime("%I%p %M:%S")
        return debut_tour

    def fin_tour():
        fin_tour = datetime.now().strftime("%I%p %M:%S")
        return fin_tour

    def resultats_matchs(liste_de_paires, debut_tour):

        tuple_match = []

        for tour, joueurs in enumerate(liste_de_paires):
            tour += 1
            print(f"Résultat du match nº {tour} entre"
                  f" {joueurs[0]} et {joueurs[1]}")

            resultat_correct = True

            while resultat_correct is True:
                nom_joueur_1 = joueurs[0]
                resultat_joueur_1 = input("Tapez le score du premier joueur")
                resultats_acceptes = ['0', '0,5', '1']
                if resultat_joueur_1 not in resultats_acceptes:
                    print('Résultat incorrect. Tapez au choix 0 0,5 ou 1')
                else:
                    resultat_correct = False

            resultat_correct = True
            while resultat_correct is True:
                nom_joueur_2 = joueurs[1]
                resultat_joueur_2 = input("Tapez le score du second joueur")
                resultats_acceptes = ['0', '0,5', '1']
                if resultat_joueur_2 not in resultats_acceptes:
                    print('Résultat incorrect. Tapez au choix 0 0,5 ou 1')
                else:
                    resultat_correct = False

            liste_joueur_1_resultat = [nom_joueur_1, resultat_joueur_1]
            liste_joueur_2_resultat = [nom_joueur_2, resultat_joueur_2]

            tour = "Round " + str(tour)

            fin_tour = datetime.now().strftime("%I%p %M:%S")

            resultat_match = (tour, liste_joueur_1_resultat,
                              liste_joueur_2_resultat,
                              debut_tour, fin_tour)
            print('--- Résultat du match :', resultat_match)
            tuple_match.append(resultat_match)

        tuple_match = tuple(tuple_match)
        return tuple_match

    def tri_joueurs(tuple_match, liste_joueurs):
        liste_joueurs_tri = []
        for joueur in tuple_match:
            liste_joueurs_tri.append(joueur[1])
            liste_joueurs_tri.append(joueur[2])

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

    def paires_joueurs(liste_joueurs_classement, liste_de_paires):

        liste_paire_joueurs = []
        sous_liste_paire = []

        while len(liste_joueurs_classement) > 0:
            for i in liste_de_paires:
                sous_liste_paire.append(liste_joueurs_classement[0][0])
                if liste_joueurs_classement[0][0] in i and \
                        liste_joueurs_classement[1][0] in i:
                    sous_liste_paire.append(liste_joueurs_classement[2][0])
                    liste_joueurs_classement = liste_joueurs_classement[0:2]\
                                               + liste_joueurs_classement[3:]
                else:
                    sous_liste_paire.append(liste_joueurs_classement[1][0])
                    liste_joueurs_classement = [liste_joueurs_classement[0]] +\
                                                liste_joueurs_classement[2:]
                liste_joueurs_classement = liste_joueurs_classement[1:]
                liste_paire_joueurs.append(sous_liste_paire)
                sous_liste_paire = []

        return (liste_paire_joueurs)
