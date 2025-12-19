# Othello IA

Projet académique de développement d’une **intelligence artificielle pour le jeu Othello**, intégrant plusieurs algorithmes de recherche et stratégies d’évaluation.

---

## 📌 Présentation du projet

L’objectif de ce projet est de concevoir une IA capable de jouer au jeu **Othello (Reversi)** contre un joueur humain ou une autre IA. Le projet met en œuvre des algorithmes classiques de recherche dans les jeux à deux joueurs, combinés à différentes stratégies d’évaluation afin de comparer leurs performances.

Le jeu se déroule sur un plateau 8×8 et se joue en **mode console** (pas d’interface graphique).

Projet réalisé par  dans le cadre d’un TP de jeu et intelligence artificielle.

---

## 🎮 Règles du jeu (rappel)

* Jeu de stratégie à deux joueurs : **Noir** et **Blanc**
* Le joueur Noir commence
* À chaque coup, le joueur place un pion qui encadre un ou plusieurs pions adverses
* Les pions encadrés sont retournés
* La partie se termine lorsque plus aucun joueur ne peut jouer
* Le gagnant est celui qui possède le plus de pions à la fin

---

## 🧠 Stratégies implémentées

Le projet implémente plusieurs stratégies d’évaluation :

* **Stratégie positionnelle** :

  * Utilisation de matrices de valeurs tactiques
  * Importance des coins, de la stabilité et de la structure du plateau

* **Stratégie absolue** :

  * Basée uniquement sur la différence du nombre de pions

* **Stratégie de mobilité** :

  * Maximise les coups possibles du joueur
  * Réduit les options de l’adversaire

* **Stratégie mixte** :

  * Début de partie : positionnelle
  * Milieu de partie : mobilité
  * Fin de partie : absolue

---

## ⚙️ Algorithmes utilisés

Les algorithmes suivants ont été implémentés en **Python** :

* **Minimax**
* **Alpha-Beta** (optimisation de Minimax par élagage)
* **Negamax** (simplification de Minimax)

Chaque algorithme peut être combiné avec les différentes stratégies d’évaluation.

---

## 🗂️ Structure du projet

```text
.
├── Plateau.py        # Gestion du plateau et des règles du jeu
├── IAJoueur.py       # Algorithmes IA + fonctions d’évaluation
├── JeuOthello.py     # Modes de jeu (Humain vs Humain, Humain vs IA, IA vs IA)
├── Main.py           # Point d’entrée du programme
└── README.md
```

---

## ▶️ Modes de jeu disponibles

* **Humain vs Humain**
* **Humain vs IA**
* **IA vs IA** (utile pour comparer les performances)

L’utilisateur peut choisir :

* l’algorithme (Minimax, Alpha-Beta, Negamax)
* la stratégie d’évaluation

---

## 📊 Validation & performances

Une fonction de statistiques permet de mesurer les **temps d’exécution** des différentes combinaisons algorithme / stratégie.

### Résultats principaux :

* **Alpha-Beta** est nettement plus rapide que Negamax
* Les stratégies influencent fortement le temps de calcul
* La stratégie **mixte** est globalement la plus efficace
* Minimax est volontairement exclu des tests lourds à cause de son coût élevé

---



## 🏁 Conclusion

Ce projet démontre l’efficacité des algorithmes de recherche classiques appliqués aux jeux de stratégie. Il met en évidence l’impact crucial du choix de l’algorithme et de la stratégie d’évaluation sur les performances d’une IA.

Il constitue une base solide pour approfondir les domaines de l’**intelligence artificielle**, des **systèmes experts** et de la **recherche opérationnelle**.

---


---

> 📘 Projet académique – TP IA / Jeux à deux joueurs
