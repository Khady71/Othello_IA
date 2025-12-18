import JeuOthello
import time


def strategie(option):
    if(option == 1 ):
        return 'position'
    elif(option==2):
        return 'mobilite'
    elif(option ==3):
        return 'absolu'
    else:
        return 'mixte'
    

def menuPrincipal():
    print("********* Bienvenue dans le jeu d'Othello ! **********")
    print("**************** [1] Joueur VS Joueur ****************")
    print("***************** [2] Joueur VS IA *******************")
    print("******************* [3] IA vs IA *********************")

    print("*************** Choisir une option : *****************")
    option =  int(input("**************** => Option choisie : "))
    if(option == 1):
        print("********** Lancement de Joueur vs Joueur ***********%n")
        print('Veuillez saisir la position souhaitee sous ce format x y')
        time.sleep(4)
        JeuOthello.jeuOthelloHumainVSHumain()
    elif(option == 2):
        print("************ Lancement de Joueur vs IA *************%n")
        print("********** Lancement de Joueur vs Joueur ***********%n")
        print('Veuillez saisir la position souhaitee sous ce format x y')
        time.sleep(4)
        JeuOthello.jeuOthelloHumainVsIA('negamax', 'mixte')
    elif(option == 3):
        print("*****************************************************") 
        print("************** Lancement de IA vs IA ***************\n")
        print("**Voici les numéros associés à chaque stratégie****")
        print("**************** [1] Position ****************")
        print("***************** [2] Mobilite *******************")
        print("******************* [3] Absolu *********************")
        print("******************* [4] Mixte *********************")
        option1 = input("Veuillez choisir une stratégie pour IA numero 1 \n")
        option2 = input("Veuillez choisir une stratégie pour IA numero 2 \n")

        time.sleep(2)
        JeuOthello.jeuOthelloIAVsIA('alphaBeta', strategie(option1),strategie(option2))
        
    elif(option == 4):
        print("******** Lancement des stats pour IA vs IA *********%n")
    else :
        JeuOthello.jeuOthelloHumainVsIA('alphaBeta', 'mixte')


menuPrincipal()
         
