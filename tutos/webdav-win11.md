Accès à l'espace personnel depuis le gestionnaire de fichiers de Windows 11
===========================================================================

```{warning}
Ce tuto marche peut-être pour d'autres versions de windows (Windows 10 par exemple),
mais cela n'a pas encore pu être testé.
```

```{note}
Ce tuto est adapté du post de forum
[Synchroniser les dossiers avec le serveur sous windows 11](https://forum.club1.fr/d/311-synchroniser-les-dossiers-avec-le-serveur-sous-windows-11).
```

Aller dans le gestionnaire de fichiers Windows et faites un clic droit sur {guilabel}`ce PC`.
Dans la liste d'action, choisissez {guilabel}`connecter un lecteur réseau`.


Connexion à un lecteur réseau
-----------------------------

Une petite fenêtre apparaît qui demande "à quel dossier réseau voulez-vous vous connecter ?" ({numref}`fig:tutos-webdav-win11-connexion`).
Pour le lecteur vous pouvez laisser celui par défaut (`Z:`).
Pour le dossier vous pouvez copier coller cette URL :

    https://IDENTIFIANT@webdav.club1.fr/files/IDENTIFIANT

En remplaçant `IDENTIFIANT` par votre identifiant de membre sur le serveur.


```{figure} webdav-win11/connecter-lecteur-reseau.png
---
alt: capture d'écran "connexion à un lecteur réseau"
name: fig:tutos-webdav-win11-connexion
width: 700
---
Fenêtre de connexion à un lecteur réseau
```

Après avoir copié cette url dans la ligne "Dossier", écrit aux endroits nécessaires votre nom d'utilisateur
et avoir cliqué sur {guilabel}`Terminer`,
une nouvelle fenêtre propose ensuite de rentrer votre identifiant et votre mot de passe.
Faites le donc 😄.


Résultat
--------

Quand ça marche vous devriez avoir ceci ({numref}`fig:tutos-webdav-win11-ce-pc`) :


```{figure} webdav-win11/ce-pc.png
---
alt: capture d'écran "ce PC"
name: fig:tutos-webdav-win11-ce-pc
width: 700
---
Fenêtre de connexion à un lecteur réseau
```

Et voilà ! 🎉 Votre espace personnel CLUB1 est maintenant accessible
dans votre explorateur de fichier tant qu'il y a internet,
sous l'onglet {guilabel}`ce PC` dans {guilabel}`mes réseaux`.
Les fichiers sont directement ouvrables avec un éditeur de code ou autres logiciels
