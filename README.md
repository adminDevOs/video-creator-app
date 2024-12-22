# Video Creator App

**Video Creator App** est une application Python permettant de créer des vidéos à partir de texte, audio, et images/vidéos. Vous pouvez personnaliser l'apparence du texte, choisir des fichiers multimédias, et définir la couleur de fond pour générer des vidéos uniques.

## Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Prérequis](#prérequis)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Aide](#aide)

## Installation

### Étape 1 : Cloner le dépôt

Clonez ce dépôt sur votre machine locale en exécutant la commande suivante :

```bash
git clone https://github.com/adminDevOs/video-creator-app.git

Étape 2 : Accéder au répertoire du projet
Une fois cloné, accédez au répertoire du projet :  cd video-creator-app

Étape 3 : Créer un environnement virtuel
Il est recommandé de créer un environnement virtuel pour éviter des conflits avec d'autres projets. Vous pouvez créer un environnement virtuel avec la commande suivante :


python -m venv env
Étape 4 : Activer l'environnement virtuel
Sous Windows :


.\env\Scripts\activate
Sous macOS/Linux :


source env/bin/activate
Étape 5 : Installer les dépendances
Installez les dépendances nécessaires en exécutant la commande suivante :


pip install -r requirements.txt
Utilisation
Lancer l'application
Pour lancer l'application, exécutez la commande suivante dans le terminal :

python main.py
Interface Utilisateur
L'application affichera une interface graphique vous permettant de :

Entrer le texte à afficher dans la vidéo.
Choisir un répertoire contenant des images ou des vidéos à inclure.
Sélectionner un fichier audio (formats supportés : .mp3, .wav).
Définir la couleur d'arrière-plan de la vidéo (exemple : #FFFFFF pour blanc).
Une fois les paramètres définis, cliquez sur le bouton "Créer la Vidéo" pour générer votre vidéo.

Résultat
Une fois la vidéo créée, elle sera exportée sous le nom output_video.mp4 dans le répertoire du projet.

Prérequis
L'application nécessite les bibliothèques suivantes :

PyQt5 : Pour l'interface graphique.
moviepy : Pour l'édition et la création des vidéos.
gtts : Pour la synthèse vocale du texte.
Pillow : Pour la manipulation d'images.
Ces dépendances peuvent être installées automatiquement avec le fichier requirements.txt.

Contribuer
Si vous souhaitez contribuer à ce projet, suivez les étapes ci-dessous :

Forkez ce dépôt.
Créez une nouvelle branche pour vos modifications :

git checkout -b nom-de-votre-branche
Apportez vos modifications.
Poussez vos modifications vers votre dépôt distant :

git push origin nom-de-votre-branche
Ouvrez une pull request pour discuter de vos modifications.
Licence
Ce projet est sous la licence MIT. Vous pouvez librement utiliser, modifier et distribuer ce projet. Voir le fichier LICENSE pour plus de détails.

Aide
Si vous rencontrez des problèmes ou avez des questions, vous pouvez créer un issue dans la section "Issues" de ce dépôt. Vous pouvez également poser des questions ou suggérer des améliorations via une pull request.

Merci d'utiliser Video Creator App ! Nous espérons que cela vous aidera à créer des vidéos uniques et personnalisées rapidement et facilement.



### Explication des sections :

- **Installation** : Cette section explique en détail comment cloner le projet, créer un environnement virtuel, activer celui-ci et installer les dépendances.
  
- **Utilisation** : Cette section guide l'utilisateur sur la façon d'utiliser l'application, de l'exécution à la personnalisation de la vidéo.

- **Prérequis** : Liste les bibliothèques nécessaires à l'exécution de l'application.

- **Contribuer** : Si quelqu'un souhaite contribuer au projet, cette section lui explique comment faire.

- **Licence** : Explique la licence du projet, ici la licence MIT.

- **Aide** : Fournit des informations pour les utilisateurs qui rencontrent des problèmes ou ont des questions.


