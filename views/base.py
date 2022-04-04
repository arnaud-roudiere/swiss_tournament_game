import sys


liste_joueurs = {}
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
        """Création du tournoi

        Returns:
            str: on va créer un tournoi

        """

        print("*--------------- Création d'un tournoi --------------- *")

        """
        print(f"Entrez les données du tournoi:")
        nom_du_tournoi = input("Tapez le nom du tournoi")
        lieu = input("Tapez le lieu")
        date_debut = input("Tapez la date de début du tournoi")
        date_fin = input("Tapez la date de fin du tournoi")
        tournees = input("Tapez le nombre de matchs")
        # Par défaut 4
        joueurs = input("Entrez le nombre de joueurs")
        # Par défaut 8
        controle_temps = True
        while controle_temps is True:
            controle_du_temps   = input("Choisissez entre un mode de contrôle
         du temps entre bullet(1), blitz(2) ou un coup rapide(3)")
            reponses_attendues = ['1','2','3']
            if controle_du_temps not in reponses_attendues:
                print('Réponse incorrecte. Veuillez retenter."
            else:
                controle_temps = False
        description = input("Entrez la description du tournoi")

        details_tournoi[nom_du_tournoi] = (lieu , date_debut ,
         date_fin , nombre_de_tours , tournees , joueurs ,
          controle_du_temps , description)
        """
        details_tournoi['tournoi_test'] = ('Londres', "01/01/1999",
                                           "02/01/1999", 4, 'tournées',
                                           "momo, popo, lolo", 'blitz',
                                           'Description:Un tournoi test')
        return self.Creation_joueurs(details_tournoi)

    def creation_players(self, details_tournoi):
        details_tournoi = details_tournoi
        """ On va demander aux organisateurs d'entrer
        les informations des 8 joueurs"""

        joueur: int

        """
        for joueur in range(0, NOMBRE_DE_JOUEURS):
            joueur += 1
            print(f"Entrez les données du joueur nº {joueur}")
            nom_de_famille      = input("Tapez le nom du joueur")
            prénom              = input("Tapez le prénom du joueur")
            date_de_naissance   = input("Tapez la date de naissance du joueur")
            sexe                = input("Tapez le sexe du joueur")
            controle_reponse = True
            while controle_reponse is True:
                classement   = input("Tapez le classement du
                                    joueur (nombre positif)")
                if int(classement) > 0:
                    controle_reponse = False
                else:
                    print('Réponse incorrecte. Veuillez retenter."
            liste_joueurs[joueur] = (nom_de_famille, prénom,
             date_de_naissance, sexe, classement)
        """
        liste_joueurs = {'1': ('Jean', 'Dupont', '110', 'M', 1),
                         '2': ('Romain', 'Sanchez', '110', 'M', 4),
                         '3': ('Didier', 'Lefevre', '110', 'M', 3),
                         '4': ('Patrick', 'Poularde', '110', 'M', 2),
                         '5': ('Jeanne', 'Dupuis', '110', 'M', 5),
                         '6': ('Lucienne', 'LaFete', '110', 'M', 7),
                         '7': ('Alice', 'Silvestre', '110', 'M', 8),
                         '8': ('Alexandre', 'Perez', '110', 'M', 6)}
        return self.Creation_paires(liste_joueurs, details_tournoi)
