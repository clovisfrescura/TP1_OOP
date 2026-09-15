# TP1 — Programmation orientée objet (OOP)

Ce dépôt contient les fichiers et exercices pour le TP1 de Programmation Orientée Objet.

## Description

Objectif : comprendre et implémenter des concepts OOP (classes, méthodes, héritage, encapsulation) à travers plusieurs scripts Python fournis.

## Prérequis

- Python 3.8+ recommandé
- Conda (ou Miniconda/Mamba) si vous souhaitez créer l'environnement via `environment.yml`

## Installation (avec Conda)

```bash
conda env create -f environment.yml -n tp1_oop
conda activate tp1_oop
```

Si vous n'utilisez pas Conda, installez les dépendances listées dans `environment.yml` manuellement.

## Exécution

- Lancer l'exercice principal :

```bash
python exercice1.py
```

- Les autres scripts utiles :
  - [critique.py](critique.py) : fonctions/logiciel pour l'analyse critique.
  - [dictionnaire.py](dictionnaire.py) : utilitaires de dictionnaire/structures de données.
  - [qualite.py](qualite.py) : métriques et vérifications de qualité.
  - [robots.py](robots.py) : classes et comportements de robots utilisés dans les exercices.

## Structure des fichiers

- [exercice1.py](exercice1.py) — point d'entrée pour l'exercice principal.
- [critique.py](critique.py) — module d'analyse critique.
- [dictionnaire.py](dictionnaire.py) — module utilitaire dictionnaire.
- [qualite.py](qualite.py) — module de métriques/qualité.
- [robots.py](robots.py) — classes de robots et exemples.
- [environment.yml](environment.yml) — environnement Conda pour reproduire les dépendances.

## Contribution

Vous pouvez modifier les scripts pour expérimenter ; soumettez des Pull Requests si vous voulez partager des améliorations.

## Auteur

TP fourni par l'équipe pédagogique.
