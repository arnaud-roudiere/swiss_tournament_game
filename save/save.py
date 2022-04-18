import json

from tinydb import TinyDB
from views.base import View


class Save:

    def load_tournament(self):
        choix_tournoi = View.choix_tournoi()
        try:
            with open('swiss_tournament_db.json') as f:
                data = json.load(f)

            """'1/Charger les tournois précédents '
                2/Charger les tours'
                3/Charger les matchs '
                4/Charger les joueurs par ordre alphabétique '
                5/Charger les joueurs par rang '
                Tapez votre option:')"""

            if choix_tournoi == '1':
                print('----------------\n')
                print('La liste des tournois :\n')
                for i in data['liste_tournois']:
                    print(i, '-->', data['liste_tournois'][i])
                print('----------------')

            elif choix_tournoi == '2':
                print('La liste des tours :', data['liste_tours'])

            elif choix_tournoi == '3':
                print('La liste des matchs:')
                for i in data['liste_matchs_tournoi']:
                    print(i, '-->', data['liste_matchs_tournoi'][i])

            elif choix_tournoi == '4':
                print('La liste des joueurs par ordre alphabétique :')
                for i in data['joueurs_alphabetique']:
                    print(i, '-->', data['joueurs_alphabetique'][i])

            elif choix_tournoi == '5':
                print('La liste des joueurs par rang :')
                for i in data['joueurs_classement']:
                    print(i, '-->', data['joueurs_classement'][i])

        except IOError:
            print("*********** \nFichier inexistant\n***********")

        return self.fin_tournoi()

    def save_joueurs(liste_joueurs_classement,
                     details_tournoi, liste_de_tours,
                     tuple_match, liste_joueurs):

        db = TinyDB('swiss_tournament_db.json')

        joueurs_alphabetique = db.table('joueurs_alphabetique')
        joueurs_classement = db.table('joueurs_classement')
        liste_tournois = db.table('liste_tournois')
        liste_tours = db.table('liste_tours')
        liste_matchs_tournoi = db.table('liste_matchs_tournoi')

        details_tournoi = details_tournoi
        liste_de_tours = liste_de_tours
        tuple_match = tuple_match

        # ------> liste joueurs par classement
        liste_des_joueurs = []
        for i, j in enumerate(liste_joueurs_classement):
            joueur = liste_joueurs[i][1][0]
            liste_des_joueurs.append(joueur)
            joueurs_classement.insert({liste_joueurs[i][1][0]: [j[0], j[1]]})

        liste_des_joueurs.sort()

        # ------> liste joueurs par ordre alphabetique
        for i, j in enumerate(liste_des_joueurs):
            joueurs_alphabetique.insert({i+1: j})

        # ------> liste des tournois
        nom_tournoi = {(next(iter(details_tournoi))):
                       details_tournoi.get(next(iter(details_tournoi)))[7]}
        liste_tournois.insert(nom_tournoi)

        # ------> liste des tours
        for i, j in enumerate(liste_de_tours):
            liste_tours.insert({'Tour :': j})

        # ------> liste des matchs
            """ on crée in dictionnaire avec le numéro
            de tour + les joueurs et leurs résultats """
        for i, j in enumerate(liste_de_tours):
            matchs_resultats = [tuple_match[i][2][:2]]\
                               + [tuple_match[i][3][:2]]
            liste_matchs_tournoi.insert({j: matchs_resultats})

    def run(self):
        return self.load_tournament()
