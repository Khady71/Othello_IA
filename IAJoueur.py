import Plateau
import numpy as np
import copy
import math
import time

PlusInfini = float('inf')
MoinsInfini = float('-inf')


    
#Stratégie Position
def fonctionEvaluationPositionnel(tabOthello, pion):
    valeurStatiquePosition = [
                [500, -150, 30, 10, 10, 30, -150, 500],    
                [-150, -250, 0, 0, 0, 0, -250, -150],
                [30, 0, 1, 2, 2, 1, 0, 30],
                [10, 0, 2, 16, 16, 2, 0, 10],
                [10, 0, 2, 16, 16, 2, 0, 10],
                [30, 0, 1, 2, 2, 1, 0, 30],
                [-150, -250, 0, 0, 0, 0, -250, -150],
                [500, -150, 30, 10, 10, 30, -150, 500]
    ]
    newTabOthello = copy.deepcopy(tabOthello)
    sommeCoutsPionJoueur = 0
    sommeCoutsPionAdversaire = 0
    for case in Plateau.listeCasesJoueur(newTabOthello, pion):
        sommeCoutsPionJoueur=sommeCoutsPionJoueur+valeurStatiquePosition[case[0]][case[1]]
    for case in Plateau.listeCasesJoueur(newTabOthello, Plateau.autrePion(pion)):
        sommeCoutsPionAdversaire=sommeCoutsPionAdversaire+valeurStatiquePosition[case[0]][case[1]]
    return sommeCoutsPionJoueur - sommeCoutsPionAdversaire


#Stratégie : Absolu
def fonctionEvaluationAbsolu(tabOthello, pion):
    score = 0
    for i in range(0,8):
        for j in range(0,8): 
            if(tabOthello[i][j] == pion):
                score = score+1
            elif(tabOthello[i][j] == Plateau.autrePion(pion)):
                score = score-1
    return score

#Stratégie : Mobilité
def fonctionEvaluationMobilite(tabOthello, pion):
    score = 0
    mobiliteJoueur = len(Plateau.positionsJouables(tabOthello, pion))
    mobiliteAdversaire = len(Plateau.positionsJouables(tabOthello, Plateau.autrePion(pion)))

    coinsJoueur = Plateau.nbreCoins(tabOthello, pion)
    coinsAdversaire = Plateau.nbreCoins(tabOthello, Plateau.autrePion(pion))

    score = mobiliteJoueur - mobiliteAdversaire + (coinsJoueur - coinsAdversaire)
    return score

#Stratégie : Mixte
def fonctionEvaluationMixte(tabOthello, pion, nbreCoupJoues):
    score = 0

    if(nbreCoupJoues < 20):
        score = fonctionEvaluationPositionnel(tabOthello, pion)
    elif(20<=nbreCoupJoues<40):
        score = fonctionEvaluationMobilite(tabOthello,pion)
    else:
        score = fonctionEvaluationAbsolu(tabOthello, pion)

    return score





def minimax(profondeur, tabOthello, pion,player,nbreCoupJoues,strategie):
    copytab = copy.deepcopy(tabOthello)
    score = 0
    bestMove = None
    newTabOthello = tabOthello
    if((profondeur==0) or (Plateau.isGameOver(copytab))):
        if(strategie == 'mixte'):
            return fonctionEvaluationMixte(copytab,pion,nbreCoupJoues), bestMove
        elif(strategie == 'absolu'):
            return fonctionEvaluationAbsolu(copytab,pion), bestMove
        elif(strategie == 'mobilite'):
            return fonctionEvaluationMobilite(copytab,pion), bestMove
        else:
            return fonctionEvaluationPositionnel(copytab,pion), bestMove
    
        
    tabPositionsJouables = Plateau.positionsJouables(newTabOthello, pion)
    if(player == 'MAX'):
        # print('round : ', profondeur, pion, player)
        bestScore = MoinsInfini
        for positionJouable in tabPositionsJouables:
            curentTabOthello = copy.deepcopy(tabOthello)
            newTabOthello = Plateau.jouerUnPion(positionJouable[0], positionJouable[1],curentTabOthello,pion)
            score, _ = minimax(profondeur-1, newTabOthello, Plateau.autrePion(pion),'MIN',nbreCoupJoues,strategie)
            curentTabOthello = tabOthello
            if((score >= bestScore)):
                bestScore = score
                bestMove = positionJouable

    else:
        bestScore = PlusInfini
        # print('round : ', profondeur, pion, player)
        for positionJouable in tabPositionsJouables:
            curentTabOthello = copy.deepcopy(tabOthello)
            newTabOthello = Plateau.jouerUnPion(positionJouable[0], positionJouable[1],curentTabOthello,pion)  
            score, _ = minimax(profondeur-1, newTabOthello, Plateau.autrePion(pion), 'MAX',nbreCoupJoues,strategie)
            curentTabOthello = tabOthello
            if((score <= bestScore)):
                bestScore = score
                bestMove = positionJouable
    return bestScore,bestMove



tabOthello34 = np.array([
        [' ','x','x','o','x','x','o','x'],
        ['o','o','x','x','o','o','o','x'],
        ['o','o','x','x','x','x','o','x'],
        ['o','o','x','o','x','x','x','x'],
        ['x','x','x','o','o','x','x','x'],
        ['x','x','x','o','o','o','o','x'],
        ['o','o','x','x','o','x','o','x'],
        ['x','x','x','x','x','x','x','x']
])

# print(minimax(4, Plateau.createTable(),'x','MAX',0,'mixte'))



#Algorithme alpha beta
def alphabeta(profondeur, tabOthello, pion,player,alpha, beta, nbreCoupJoues,strategie):
    copytab = copy.deepcopy(tabOthello)
    score = 0
    bestMove = None
    newTabOthello = tabOthello
    if((profondeur==0) or (Plateau.isGameOver(copytab))):
        if(strategie == 'mixte'):
            return fonctionEvaluationMixte(copytab,pion,nbreCoupJoues), bestMove
        elif(strategie == 'absolu'):
            return fonctionEvaluationAbsolu(copytab,pion), bestMove
        elif(strategie == 'mobilite'):
            return fonctionEvaluationMobilite(copytab,pion), bestMove
        else:
            return fonctionEvaluationPositionnel(copytab,pion), bestMove
    
        
    tabPositionsJouables = Plateau.positionsJouables(newTabOthello, pion)
    if(player == 'MAX'):
        # print('round : ', profondeur, pion, player)
        bestScore = MoinsInfini
        for positionJouable in tabPositionsJouables:
            curentTabOthello = copy.deepcopy(tabOthello)
            newTabOthello = Plateau.jouerUnPion(positionJouable[0], positionJouable[1],curentTabOthello,pion)
            score, _ = alphabeta(profondeur-1, newTabOthello, Plateau.autrePion(pion),'MIN',alpha, beta, nbreCoupJoues,strategie)
            # print('score cote max ', score)
            curentTabOthello = tabOthello
            if((score >= alpha)):
                alpha = score
                bestMove = positionJouable
                if(beta <= alpha):
                    break  #Elagage
            

    else:
        bestScore = PlusInfini
        # print('round : ', profondeur, pion, player)
        for positionJouable in tabPositionsJouables:
            curentTabOthello = copy.deepcopy(tabOthello)
            newTabOthello = Plateau.jouerUnPion(positionJouable[0], positionJouable[1],curentTabOthello,pion)  
            score, _ = alphabeta(profondeur-1, newTabOthello, Plateau.autrePion(pion), 'MAX',alpha, beta,nbreCoupJoues,strategie)
            # print('score cote min ', score)
            curentTabOthello = tabOthello
            if((score <= beta)):
                beta = score
                bestMove = positionJouable
            if(beta<=alpha):
                break
            
    return bestScore,bestMove

# print(alphabeta(4, Plateau.createTable(),'x','MAX',-200, 200,0,'mixte'))


#Algorithme negamax
def negamax(profondeur, tabOthello, pion,alpha, beta, nbreCoupJoues, strategie):
    copytab = copy.deepcopy(tabOthello)
    score = 0
    bestMove = None
    newTabOthello = tabOthello
    if((profondeur==0) or (Plateau.isGameOver(copytab))):
        if(strategie == 'mixte'):
            return fonctionEvaluationMixte(copytab,pion,nbreCoupJoues), bestMove
        elif(strategie == 'absolu'):
            return fonctionEvaluationAbsolu(copytab,pion), bestMove
        elif(strategie == 'mobilite'):
            return fonctionEvaluationMobilite(copytab,pion), bestMove
        else:
            return fonctionEvaluationPositionnel(copytab,pion), bestMove
    
        
    tabPositionsJouables = Plateau.positionsJouables(newTabOthello, pion)
    
    bestScore = MoinsInfini
    for positionJouable in tabPositionsJouables:
        curentTabOthello = copy.deepcopy(tabOthello)
        newTabOthello = Plateau.jouerUnPion(positionJouable[0], positionJouable[1],curentTabOthello,pion)
        score, _ = negamax(profondeur-1, newTabOthello, Plateau.autrePion(pion),-alpha, -beta, nbreCoupJoues, strategie)
        curentTabOthello = tabOthello
        if((-score >= bestScore)):
            bestScore = -score
            bestMove = positionJouable
        alpha = max(alpha, score)
        if(beta <= alpha):
            break  #Elagage
        
        
    return bestScore,bestMove

# print(negamax(4, Plateau.createTable(), 'x',-200, 200,45,'position'))

# tabOthello = Plateau.createTable()


    







