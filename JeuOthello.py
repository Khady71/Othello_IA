import Plateau
import IAJoueur
import time

Profondeur_Maximal = 6


def wait(seconds):
    time.sleep(seconds)


def jeuOthelloHumainVSHumain():
    print('Bienvenue sur le jeu Othello, J1-->o J2-->x')
    tabOthello = Plateau.createTable()
    numJoueur = 1
    cptJeu = 0
    while(Plateau.isGameOver(tabOthello) == False):
        cptJeu = cptJeu + 1
        if(numJoueur == 1):
            Plateau.afficher_tab_othello(tabOthello)
            if(Plateau.canPlay(tabOthello,'o')):
                positions = input('J1,sur quelle position voulez-vous jouer?', )
                iligne = int(positions.split()[0])
                icolonne = int(positions.split()[1])
                print('Position choisie : ',iligne, icolonne)
                if(Plateau.isPositionJouable(iligne,icolonne,tabOthello,'o')):
                    tabOthello = Plateau.jouerUnPion(iligne, icolonne,tabOthello,'o')
                    numJoueur = 2
                else:
                    print('Vous ne pouvez pas jouer sur cette position, veuillez reessayer')
                    numJoueur = 1
            else:
                print('Vous ne pouvez pas jouer sur ce tour')
                numJoueur = 2
        if(numJoueur == 2):
            Plateau.afficher_tab_othello(tabOthello)
            if(Plateau.canPlay(tabOthello,'x')):
                positions = input('J2,sur quelle position voulez-vous jouer?', )
                iligne = int(positions.split()[0])
                icolonne = int(positions.split()[1])
                print('Position choisie : ',iligne, icolonne)
                if(Plateau.isPositionJouable(iligne,icolonne,tabOthello,'x')):
                    tabOthello = Plateau.jouerUnPion(iligne, icolonne,tabOthello,'x')
                    numJoueur = 1
                else:
                    print('Vous ne pouvez pas jouer sur cette position, veuillez reessayer')
                    numJoueur = 2
            else:
                print('Vous ne pouvez pas jouer sur ce tour')
                numJoueur = 1

    if(Plateau.isGameOver(tabOthello)):
        print(Plateau.whoWins(tabOthello))



def jeuOthelloHumainVsIA(strategie, algo):
    print('Bienvenue sur le jeu Othello, IA-->o J2-->x')
    tabOthello = Plateau.createTable()
    # print(tabOthello)
    nbreCoupJoues = 0
    numJoueur = 1
    newtabOthello = tabOthello
    while(Plateau.isGameOver(newtabOthello) == False):
        nbreCoupJoues = nbreCoupJoues+1
        if(numJoueur == 1):
            Plateau.afficher_tab_othello(newtabOthello)
            if(Plateau.canPlay(newtabOthello,'o')):
                if(algo == 'negamax'):
                    bestscore, bestMove = IAJoueur.negamax(Profondeur_Maximal, newtabOthello, 'o',-200, 200, nbreCoupJoues, strategie)
                elif(algo == 'alphaBeta'):
                    bestscore, bestMove = IAJoueur.alphabeta(Profondeur_Maximal, newtabOthello, 'o',-200, 200, nbreCoupJoues,strategie)
                else:
                    bestscore, bestMove = IAJoueur.minimax(Profondeur_Maximal, newtabOthello, 'o', 'MAX', nbreCoupJoues,strategie)
                if(bestMove == None):     #Cas où l'IA retourne None pour ne pas arreter le jeu
                    print("L IA n'a pas trouvé une position à jouer")
                    numJoueur = 2
                else:
                    iligne = bestMove[0]
                    icolonne = bestMove[1]
                    print('Position choisie par IA: ',iligne, icolonne)
                    if(Plateau.isPositionJouable(iligne,icolonne,newtabOthello,'o')):
                        newtabOthello = Plateau.jouerUnPion(iligne, icolonne,newtabOthello,'o')
                        wait(3)
                        numJoueur = 2
                    else:
                        print('Vous ne pouvez pas jouer sur cette position, veuillez reessayer')
                        numJoueur = 1
            else:
                print('Vous ne pouvez pas jouer sur ce tour')
                numJoueur = 2
        if(numJoueur == 2):
            Plateau.afficher_tab_othello(newtabOthello)
            if(Plateau.canPlay(newtabOthello,'x')):
                positions = input('J2,sur quelle position voulez-vous jouer?', )
                iligne = int(positions.split()[0])
                icolonne = int(positions.split()[1])
                print('Position choisie par Humain: ',iligne, icolonne)
                if(Plateau.isPositionJouable(iligne,icolonne,newtabOthello,'x')):
                    newtabOthello = Plateau.jouerUnPion(iligne, icolonne,newtabOthello,'x')
                    wait(3)
                    numJoueur = 1
                else:
                    print('Vous ne pouvez pas jouer sur cette position, veuillez reessayer')
                    numJoueur = 2
            else:
                print('Vous ne pouvez pas jouer sur ce tour')
                numJoueur = 1

    if(Plateau.isGameOver(newtabOthello)):
        print(Plateau.whoWins(newtabOthello))





def jeuOthelloIAVsIA(algo, strategie1, strategie2):
    print('Jeu Othello : IA VS IA , IA num 1-->x IA num 2-->o %n')
    tabOthello = Plateau.createTable()
    # print(tabOthello)
    nbreCoupJoues = 0
    numJoueur = 1
    newtabOthello = tabOthello
    while(Plateau.isGameOver(newtabOthello) == False):
        nbreCoupJoues = nbreCoupJoues+1
        if(numJoueur == 1):
            Plateau.afficher_tab_othello(newtabOthello)
            if(Plateau.canPlay(newtabOthello,'x')):
                if(algo == 'negamax'):
                    bestscore, bestMove = IAJoueur.negamax(Profondeur_Maximal, newtabOthello, 'x',-200, 200, nbreCoupJoues, strategie1)
                elif(algo == 'alphaBeta'):
                    bestscore, bestMove = IAJoueur.alphabeta(Profondeur_Maximal, newtabOthello, 'x','MAX',-200, 200, nbreCoupJoues,strategie1)
                else:
                    bestscore, bestMove = IAJoueur.minimax(Profondeur_Maximal, newtabOthello, 'x', 'MAX', nbreCoupJoues,strategie1)
                if(bestMove == None):     #Cas où l'IA retourne None pour ne pas arreter le jeu
                    print("L IA num 1 n'a pas trouvé une position à jouer")
                    numJoueur = 2
                else :
                    iligne = bestMove[0]
                    icolonne = bestMove[1]
                    print('Position choisie par IA num 1: ',iligne, icolonne)
                    if(Plateau.isPositionJouable(iligne,icolonne,newtabOthello,'x')):
                        newtabOthello = Plateau.jouerUnPion(iligne, icolonne,newtabOthello,'x')
                        # wait(3)
                        numJoueur = 2
                    else:
                        print('Vous ne pouvez pas jouer sur cette position, veuillez reessayer')
                        numJoueur = 1
            else:
                print('Vous ne pouvez pas jouer sur ce tour')
                numJoueur = 2
        if(numJoueur == 2):
            Plateau.afficher_tab_othello(newtabOthello)
            if(Plateau.canPlay(newtabOthello,'o')):
                if(algo == 'negamax'):
                    bestscore, bestMove = IAJoueur.negamax(Profondeur_Maximal, newtabOthello, 'o',-200, 200, nbreCoupJoues, strategie2)
                elif(algo == 'alphaBeta'):
                    bestscore, bestMove = IAJoueur.alphabeta(Profondeur_Maximal, newtabOthello, 'o','MAX',-200, 200, nbreCoupJoues,strategie2)
                else:
                    bestscore, bestMove = IAJoueur.minimax(Profondeur_Maximal, newtabOthello, 'o', 'MAX', nbreCoupJoues,strategie2)
                if(bestMove == None):  #Cas où l'IA retourne None pour ne pas arreter le jeu
                    print("L IA num 2 n'a pas trouvé une position à jouer")
                    numJoueur = 1
                else:
                    iligne = bestMove[0]
                    icolonne = bestMove[1]
                    print('Position choisie par IA num 2: ',iligne, icolonne)
                    if(Plateau.isPositionJouable(iligne,icolonne,newtabOthello,'o')):
                        newtabOthello = Plateau.jouerUnPion(iligne, icolonne,newtabOthello,'o')
                        # wait(5)
                        numJoueur = 1
                    else:
                        print('Vous ne pouvez pas jouer sur cette position, veuillez reessayer')
                        numJoueur = 2
            else:
                print('Vous ne pouvez pas jouer sur ce tour')
                numJoueur = 1

    if(Plateau.isGameOver(newtabOthello)):
        print(Plateau.whoWins(newtabOthello))


# jeuOthelloIAVsIA('negamax','absolu','position')

def statsNumeriqueIAVSIA():
    tabResultat = []
    algoTab = ['alphaBeta','negamax']
    strategieTab = ['mixte','absolu','mobilite','position']
    print("Algorithmes   Stratégies   Temps d'exécution")
    for algo in algoTab:
        for strategie in strategieTab:
            print(algo, ' ', strategie, ' ', end='')
            debut = time.time()
            temps_execution = jeuOthelloIAVsIA(algo, strategie, strategie)
            fin = time.time()
            temps_execution = fin - debut
            tabResultat.append((algo, strategie, temps_execution))
            print(temps_execution)
    return tabResultat


# print(statsNumeriqueIAVSIA())

