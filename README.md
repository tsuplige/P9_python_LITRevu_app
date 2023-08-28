# P9_python_LITRevu_app

# LITRevu - Application Web Django


## Introduction

Bienvenue dans le README du projet LITRevu, une application web Django pour la publication et la demande de critiques de livres ou d'articles. Ce document vous guidera à travers le processus d'installation, les fonctionnalités de base, et fournira des informations essentielles pour contribuer au projet.

## Table des matières

1. [Installation](#installation)
2. [Fonctionnalités](#fonctionnalités)
3. [Cahier des charges](#cahier-des-charges)
4. [Veille technologique](#veille-technologique)
5. [Wireframes](#wireframes)
6. [Base de données](#base-de-données)
7. [Contribution](#contribution)
8. [Contact](#contact)

## Installation

Pour installer et exécuter cette application sur votre propre environnement de développement, suivez ces étapes :



1. Clonez le référentiel depuis GitHub :
   ```bash
   git clone https://github.com/tsuplige/P9_python_LITRevu_app.git
   
   cd P9_python_LITRevu_app
   ```

2. Créez un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   ```

3. Activez l'environnement virtuel :
   - Sur Windows : `venv\Scripts\activate`
   - Sur macOS et Linux : `source venv/bin/activate`

4. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

5. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```

6. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

L'application sera maintenant accessible à l'adresse http://localhost:8000/ dans votre navigateur.

## Fonctionnalités

LITRevu propose les fonctionnalités suivantes :

- Publication de critiques de livres ou d'articles.
- Demande de critiques pour un livre ou un article spécifique.
- Recherche d'articles et de livres basée sur les critiques des autres utilisateurs.

## Cahier des charges

Consultez le [cahier des charges](cahier-des-charges.pdf) pour une description détaillée des besoins fonctionnels et techniques du site.

## Veille technologique

Pour choisir les outils nécessaires à ce projet, nous avons réalisé une veille technologique. Vous pouvez consulter le rapport de veille au format PDF [ici](veille-technologique.pdf).

## Wireframes

Consultez les [wireframes](wireframes/) fournis par notre UX designer pour vous guider dans la mise en page de l'application. Assurez-vous de suivre les bonnes pratiques d’accessibilité du référentiel WCAG pour garantir l'accessibilité à tous les utilisateurs.

## Base de données

Nous avons élaboré un schéma de base de données pour couvrir toutes les fonctionnalités requises. Le fichier `models.py` contient le modèle de révision ('Review') pour vous aider à démarrer.

