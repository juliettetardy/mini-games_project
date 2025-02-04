class Islet :
    """
    Une classe qui permet de créer des îlots protecteurs.
    Ces îlots pretecteur sont réalisés de tels sorte à ce que les aliens puissent les détruire.

    Fonctions 
    ---------
        multiply_islet :
            
    """
    def __init__ (self, x, y, side, canevas) :
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle-ci.
        Entrée(s): 
            x : coordonées en abscisse d'un cube de l'îlot
            y : coordonées en ordonnée d'une cube de l'îlot
            side : longueur d'un côté d'une cube de l'îlot
            canevas : canevas du jeu sur lequel les îlots vont être placés
        
        Sortie(s): None

        """
        self.x = x
        self.y = y
        self.side = side
        self.canevas = canevas

    def multiply_islet (self) :
        """ 
        Fonction qui multiplie le nombre de cubes pour former un îlot à plusieurs cubes. 
        Entrée(s): None
        Sortie(s):
            list_cubes : 
                nombre de cubes qui composent l'îlot et leur placement.
                type = list

        """
        # Initilisation de la liste des cubes 
        list_cubes = []

        # Création de 8 colonnes
        for i in range (8) :

            # Création de 3 lignes
            for j in range (3) :

                # Création des cubes
                cube = self.canevas.create_rectangle (
                    self.x + (i) * self.side,
                    self.y + (j) * self.side, 
                    self.x + self.side + (i) * self.side, 
                    self.y + self.side + (j) * self.side,
                    width = 1, outline = 'black', fill = 'gray' )
                
                # Ajout des cubes
                list_cubes.append (cube)

        # Affichage des îlots
        return list_cubes
