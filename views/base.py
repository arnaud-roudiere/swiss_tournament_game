import sys

from models.joueurs import Joueur
from models.tournoi import Tournament

details_tournoi = {}


class View:

    def choix_tournoi():
        print("*--------------- Menu Tournois Précédents --------------- *")
        menu = True
        while menu is True:
            choix_tournoi = input('1/Charger les tournois précédents '
                                  '\n2/Charger les tours'
                                  '\n3/Charger les matchs '
                                  '\n4/Charger les joueurs par '
                                  'ordre alphabétique '
                                  '\n5/Charger les joueurs par rang '
                                  '\nTapez votre option:')

            options = ["1", "2", "3", "4", "5"]

            if choix_tournoi not in options:
                print("Option non existante, "
                      "veillez en sélectionner une autre")

            else:
                menu = False

        return choix_tournoi

    def menu_principal():
        """Accès au menu principal

             Returns:
                 str: une option choisie dans le menu

             """
        menu = True
        while menu is True:
            print("*--------------- Menu principal --------------- *")

            choix = input('1/Accéder aux tournois précédents '
                          '\n2/Créer un nouveau tournoi '
                          '\n3/Quitter \nTapez votre option:')

            options = ["1", "2", "3"]

            if choix not in options:
                print("Option non existante, "
                      "veillez en sélectionner une autre")

            else:
                if choix == "3":
                    print("----------- Au revoir -----------")
                    sys.exit(0)
                else:
                    menu = False

        return choix

    def creation_tournoi(self):
        liste_joueurs = {}
        tournoi_actuel = Tournament

        """Création du tournoi

        Returns:
            str: on va créer un tournoi

        """

        print("*--------------- Création d'un tournoi --------------- *")

        print("Entrez les données du tournoi:")
        tournoi_actuel.nom_du_tournoi = input("Tapez le nom du tournoi")
        tournoi_actuel.lieu = input("Tapez le lieu")
        tournoi_actuel.date_debut = input("Tapez la date de début du tournoi")
        tournoi_actuel.date_fin = input("Tapez la date de fin du tournoi")
        tournoi_actuel.joueurs = 8
        tournoi_actuel.nombre_de_tours = 4
        tournoi_actuel.tournees = input("Tapez le nombre de matchs")
        controle_temps = True
        while controle_temps is True:
            tournoi_actuel.controle_du_temps = input("Choisissez entre un mode de contrôle\
         du temps entre 'bullet', 'blitz' ou 'coup rapide'")
            reponses_attendues = ['bullet', 'blitz', 'coup rapide']
            if tournoi_actuel.controle_du_temps not in reponses_attendues:
                print('Réponse incorrecte. Veuillez retenter.')
            else:
                controle_temps = False
        tournoi_actuel.description = input("Entrez la description du tournoi")

        details_tournoi[tournoi_actuel.nom_du_tournoi] = (
            tournoi_actuel.lieu, tournoi_actuel.date_debut,
            tournoi_actuel.date_fin,
            tournoi_actuel.joueurs,
            tournoi_actuel.nombre_de_tours,
            tournoi_actuel.tournees,
            tournoi_actuel.controle_du_temps,
            tournoi_actuel.description)

        joueur: int
        joueurs = 8
        NOMBRE_DE_JOUEURS = int(joueurs)
        details_joueur = Joueur()
        for details_joueur.id in range(0, NOMBRE_DE_JOUEURS):
            details_joueur.id += 1
            print(f"Entrez les données du joueur nº {details_joueur.id}")
            details_joueur.nom_de_famille = input("Tapez le nom du joueur")
            details_joueur.prénom = input("Tapez le prénom du joueur")
            details_joueur.date_de_naissance = \
                input("Tapez la date de naissance du joueur")
            details_joueur.sexe = input("Tapez le sexe du joueur")
            controle_reponse = True
            while controle_reponse is True:
                details_joueur.classement = \
                    int(input("Tapez le classement "
                              "du joueur (nombre positif)"))
                try:
                    if int(details_joueur.classement) > 0:
                        controle_reponse = False
                    else:
                        print('Réponse incorrecte. Veuillez retenter.')
                except ValueError:
                    print('Réponse incorrecte. Veuillez retenter.')
            details_joueur.points = 0
            liste_joueurs[details_joueur.id] = (
                details_joueur.nom_de_famille,
                details_joueur.prénom,
                details_joueur.date_de_naissance,
                details_joueur.sexe,
                details_joueur.classement,
                details_joueur.points)

        return self.Creation_paires(liste_joueurs, details_tournoi)

    def resultats_matchs(self, nom_joueur_1):

        nom_joueur_1 = nom_joueur_1

        resultat_correct = True
        while resultat_correct is True:

            resultat_joueur_1 = input(
                f"Tapez le score du joueur {nom_joueur_1} :")
            resultats_acceptes = ['0', '0,5', '1']
            if resultat_joueur_1 not in resultats_acceptes:
                print('Résultat incorrect. Tapez au choix 0 0,5 ou 1')
            else:
                resultat_correct = False

        return nom_joueur_1, resultat_joueur_1

    def question_quit(self):
        entree = True
        reponses = ["1", "2"]
        while entree is True:
            choix_fin = input("Souhaitez-vous revenir "
                              "sur le menu ou bien quitter"
                              " l'application?\n1/Revenir au menu"
                              " \n2/Quitter \nTapez votre option (1 ou 2)")
            if choix_fin not in reponses:
                return print(
                    "La réponse est incorrecte, veuillez réessayer")
            elif choix_fin == '2':
                print('**************** Tournoi terminé *********************')
                quit()
            else:
                return choix_fin
