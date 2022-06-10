Connexion au serveur depuis l'explorateur de fichiers Linux
===========================================================

Cette méthode permet d'accéder à son [espace personnel](/info/espace-personnel.md) depuis son explorateur de fichiers.

Connexion initiale
------------------

Commencez par ouvrir votre explorateur de fichiers.
Dans ce tutoriel, le logiciel [Nemo](https://fr.wikipedia.org/wiki/Nemo_(logiciel)) est utilisé.
C'est l'explorateur de fichier installé par défaut sur [Linux Mint](https://fr.wikipedia.org/wiki/Linux_Mint).
Il est assez proche de celui qui est intégré à [Ubuntu](https://fr.wikipedia.org/wiki/Ubuntu_(syst%C3%A8me_d%27exploitation)),
les instructions seront donc similaires.

Dans la barre de menu, cliquez sur "fichier" puis "se connecter au serveur..."

Remplir ensuite les informations suivantes dans la fenêtre de connexion ({numref}`fig:tutos-connexion-linux-connexion`) :
- Serveur : `club1.fr`
- Type : `SSH`
- Dossier : `/`
- Nom d'utilisateur : rentrez votre identifiant CLUB1
- Mot de passe : rentrez votre mot de passe CLUB1

Pour finir vous pouvez cocher la case "Mémoriser ce mot de passe"
afin de ne pas avoir à le retaper plus tard, puis cliquer sur "Se connecter".

(fig:tutos-connexion-linux-connexion)=
```{figure} /_static/tutos/connexion-linux/se_connecter_au_serveur.png
---
alt: capture d'écran fenêtre de connexion
---
Fenêtre de connexion.
```

Vous êtes maintenant connecté au serveur ({numref}`fig:tutos-connexion-linux-dossier`).

(fig:tutos-connexion-linux-dossier)=
```{figure} /_static/tutos/connexion-linux/dans_le_serveur.png
---
alt: capture d'écran dossiers du serveur dans l'explorateur de fichier
---
Dossiers du serveur dans l'explorateur de fichier.
```

Cliquez sur le dossier `home` puis sur votre *dossier perso*, qui est votre identifiant CLUB1.

Marque-page
-----------

Si on s'arrête là, il faudra recommencer toutes ces étapes à chaque nouveau redémarrage de l'ordinateur car cette connexion ne sera pas sauvegardée.
Pour remédier à ce problème, il faut ajouter un **marque-page** (**bookmark** en anglais).

Selon votre explorateur de fichiers :
- Depuis le *dossier perso* : dans la barre de menu, cliquez sur "Marque-pages" puis "Ajouter un marque-page"
- Depuis le dossier `home` : clic droit sur votre *dossier perso* puis "ajouter marque-page", ou autre formulation similaire

Vous pouvez désormais modifier tous vos fichiers facilement depuis votre explorateur de fichiers !

```{raw} latex
\clearpage
```
