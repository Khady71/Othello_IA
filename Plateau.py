import numpy as np
import copy

def createTable():
    #initialise le plateau de jeu 
    tabOthello = np.array([
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','x','o',' ',' ',' '],
        [' ',' ',' ','o','x',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ']
    ])
    return tabOthello


def autrePion(pion):
    #Retourne le pion contraire 
    if(pion == 'o'):
        return 'x'
    else:
        return 'o'
    
def nbPionsARetourner(iligne, icolonne,tab,pion,direction):
    #Compte le nbre de pions à retourner apres un coup pour une direction donnée. Les directions sont les ensembles : gauche, droite, haut, bas
    i, j = direction
    newItemp = i
    newJtemp = j
    nbcases=0
    cpt = 2
    while((0<iligne+newItemp<8) and (0<icolonne+newJtemp<8) and (tab[iligne+newItemp,icolonne+newJtemp] == autrePion(pion))):
        newItemp = i*cpt
        newJtemp = j*cpt
        cpt+=1 
        nbcases+=1
    
    if((0<iligne+newItemp<8) and (0<icolonne+newJtemp<8) and (tab[iligne+newItemp,icolonne+newJtemp] == pion)):
        return nbcases
    else:
        return 0


    
def isPositionJouable(iligne, icolonne,tab,pion):  
    #Teste si un coup est possible  
    directions = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]
    if(tab[iligne,icolonne] != ' '):
        return False
    cpt = 0
    while(cpt < len(directions)):
        nb = nbPionsARetourner(iligne, icolonne,tab,pion,directions[cpt])
        if(nb > 0):
            return True
        else:
           cpt = cpt+1
    return False
        
        

def positionsPionsARetourner(iligne, icolonne,tab,pion):
    #Retourne un tableau contenant les positions des pions à retourner
    directions = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]
    tabPositions = []
    for direction in directions:
        nbPions = nbPionsARetourner(iligne,icolonne,tab,pion,direction) 
        if (nbPions > 0):
            for i in range (1, nbPions+1):
                newligne = iligne+direction[0]*i
                newcolonne = icolonne+direction[1]*i
                if((0<=newligne<8) and (0<=newcolonne<8)):
                    tabPositions.extend((newligne, newcolonne))
    return tabPositions



def isGameOver(tab):
    #Teste si le jeu est terminé c'est à dire personne ne peut plus jouer ou le plateau est complètement rempli
    for i in range(0,8):
        for j in range(0,8): 
            if(tab[i][j] == ' '):
                if((isPositionJouable(i, j, tab,'x')) or (isPositionJouable(i, j, tab,'o'))):
                    # print(i, j)
                    return False
    return True


def isPlateauFull(tab):
    #Teste si le plateau est complètement rempli
    for i in range(0,8):
        for j in range(0,8): 
            if(tab[i][j] == ' '):
                return False
    return True



def canPlay(tab, pion):
    #Teste si un joueur peut encore jouer sur le plateau
    for i in range(0,8):
        for j in range(0,8): 
            if(tab[i][j] == ' '):
                if(isPositionJouable(i, j, tab,pion)):
                    return True
    return False





def whoWins(tab):
    #Determine quel joueur a gagné
    cptJ1 = 0
    cptJ2 = 0
    for i in range(0,8):
        for j in range(0,8): 
            if(tab[i][j] == 'o'):
                cptJ1 = cptJ1+1
            elif(tab[i][j] == 'x'):
                cptJ2 = cptJ2+2
            else:
                pass
    if(cptJ1 > cptJ2):
        print('Le joueur avec les pions o a gagne avec un nbre de pions total égale à : ',cptJ1)
    elif(cptJ2 > cptJ1):
        print('Le joueur avec les pions x a gagne avec un nbre de pions total égale à : ',cptJ2)
    else:
        print('Match nul')



def afficher_tab_othello(tab):
    # Afficher les numéros de colonnes
    print("    " + " ".join(map(str, range(tab.shape[1]))))

    # Afficher les numéros de lignes et le contenu du tableau
    for i, ligne in enumerate(tab):
        print(f"{i} | {' '.join(map(str, ligne))}")

afficher_tab_othello(createTable())


def jouerUnPion(iligne, icolonne,tab,pion):
    #Permet de jouer un coup
    tabIni = copy.deepcopy(tab)
    tabIni2 = copy.deepcopy(tab) 
    if(isPositionJouable):
        tabPionsARetourner = positionsPionsARetourner(iligne, icolonne,tabIni,pion)
        # print(tabPionsARetourner)
        tabIni[iligne, icolonne] = pion
        for i in range (0,len(tabPionsARetourner),2):
            tabIni[tabPionsARetourner[i],tabPionsARetourner[i+1]] = pion
        return tabIni
    else:
        print('Vous ne pouvez pas jouer sur cette position')
        return tabIni2




def casesVidesJouables(tabOthello):
    #Regroupe dans un tableau les positions dans le tableau encore jouables
    directions = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)] 
    newIligne=0
    newIcolonne=0
    tabPositionsVides = []
    for iligne in range (0,8):
        for icolonne in range(0,8):
            if(tabOthello[iligne,icolonne] != ' '):
                # print(tabOthello[iligne, icolonne]+ ' ' + str(iligne) + ' '+ str(icolonne)+' ')
                for direction in directions:
                    newIligne = iligne+direction[0]
                    newIcolonne = icolonne+direction[1]
                    # print(str(newIligne) +' '+str(newIcolonne)+ '\n')
                    if((0<=newIligne<8) and (0<=newIcolonne<8)):
                        if(tabOthello[newIligne,newIcolonne] == ' '):
                            if((newIligne,newIcolonne) not in tabPositionsVides):
                                tabPositionsVides.append((newIligne,newIcolonne))
    
    return tabPositionsVides


def listeCasesJoueur(tabOthello, pion):
    #Retourne la liste des positions des pions d'un joueur
    listeCases = []
    for iligne in range (0,8):
        for icolonne in range(0,8):
            if(tabOthello[iligne,icolonne] == pion):
                listeCases.append((iligne,icolonne))
    return listeCases



def nbreCoins(tabOthello, pion):
    #Calcule le nombre de coins possédés par un joueur
    nbreCoins = 0

    #Coin supérieur gauche
    if(tabOthello[0][0] == pion):
        nbreCoins = nbreCoins+1
    
    #Coin supérieur droite
    if(tabOthello[0][7] == pion):
        nbreCoins = nbreCoins+1

     #Coin inférieur gauche
    if(tabOthello[7][0] == pion):
        nbreCoins = nbreCoins+1

     #Coin inferieur droite
    if(tabOthello[7][7] == pion):
        nbreCoins = nbreCoins+1

    return nbreCoins




def positionsJouables(tabOthello, pion):
    #Retourne la liste des positions jouables pour un joueur donné
    positionsJouables = []
    directions = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]
    nb = 0
    for position in casesVidesJouables(tabOthello):
        # print(casesVidesJouables(tabOthello))
        iligne, icolonne = position
        for direction in directions:    
            nb = nbPionsARetourner(iligne, icolonne,tabOthello,pion,direction)
            if(nb > 0):
                if((iligne, icolonne) not in positionsJouables):
                    positionsJouables.append((iligne, icolonne))
            # else:
            #     cpt = cpt+1
    return positionsJouables


def etendre(tabOthello, pion):
    #Retourne un tableau contitué de plateaux pouvant être généré par un coup d'un joueur donné
    tabOthelloPossibles = []
    tabOthelloInitial = copy.deepcopy(tabOthello)   #pour éviter que tabOthello soit modifié au cours de la boucle
    tabpositionsJouables = positionsJouables(tabOthelloInitial, pion)
    for positionJouable in tabpositionsJouables:
        tabOthelloPossibles.append(jouerUnPion(positionJouable[0], positionJouable[1],tabOthelloInitial,pion)) 

    return tabOthelloPossibles








