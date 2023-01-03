Espace personnel
================

L'hébergement CLUB1 est basé sur la mise à disposition d'un *espace personnel*.
Il s'agit d'un espace de stockage sur le serveur, accessible via un certain
nombre de protocoles, fournissant différents services.


Home sweet home
---------------

Chaque membre de CLUB1 dispose d'un *espace personnel*.
C'est votre *chez vous*, d'ailleurs, on appelle ce dossier `home` 🏠.
Mais comme vous avez tout les droits, vous avez également le droit de tout supprimer.
Donc faites attention, car certains dossier à l'intérieur peuvent être précieux.
Par exemple vos emails, qui sont dans le dossier `mail` 🤯 .

Eh oui, un grand pouvoir implique de grandes responsabilités... 😏
Vous pouvez y faire ce que vous voulez, mais comme chez vous il y a aussi des voisins.
En effet, **il n'y a pas de limite de stockage définie** par dossier `home` de chaque membres,
mais par contre, une limite physique :
Tout ces dossiers sont sur un support de stockage SSD totalisant **1To**.
C'est un espace commun à partager entre utilisateur&middot;trice&middot;s du serveur.


Architecture de dossiers
------------------------

Tout les dossiers ne se valent pas, certains ont un rôle spécifique.

### 📁 mail

C'est ici que sont stockés tout vos mails du [service mail CLUB1](/services/email.md).
Votre espace email est donc directement à l'intérieur de votre espace personnel.
Un quota existe pour ce dossier : il est limité à 5Go.

```{danger}
Attention à ne pas supprimer ce dossier par inadvertance,
vous perdrez tout vos emails stockés sur le serveur.
```

Pour sauvegarder rapidement vos emails,
il vous suffit de télécharger une copie de ce dossier.

### 📁 static

Ce dossier est la porte la plus proche vers le {term}`Web`
car il permet de [publier des sites Web](../services/web.md#dossier-static).

### 📁 git

Dossier utilisé pour [héberger des dépots de code Git](/services/git.md).

### 📁 log

Ce dossier contient l'ensemble des {term}`logs <log>` produits par les services.
Par exemple ceux des [sites Web dynamiques](../services/web.md#sites-web-dynamiques).

Une rotation est opérée à l'aide de {term}`logrotate` sur les fichiers `*.log` de ce dossier toute les semaines
et un historique de 15 fichiers par log est conservé.
Les anciens fichiers sont compressés via `gzip`.

Fichier de présentation
-----------------------

Pour apparaître sur la [page membres](https://club1.fr/membres) du site web de CLUB1,
il faut créer un **fichier de présentation** appellé `PRESENTATION.md` à la racine de son espace perso.

Il est possible de formater son texte en {term}`Markdown`,
ainsi que de changer son nom d'affichage et la couleur de son bouton.

```{seealso}
Tutoriel : [Comment éditer sa présentation](/tutos/presentation.md)
```

💡 L'ordre des boutons de présentation change à chaque fois qu'un&middot;e membre met à jour
son fichier de présentation !

Logiciels
---------

```{glossary}
members-presentation
    Script PHP permettant de générer la page membre.
    --- [Sources](https://github.com/club-1/members-presentation)

logrotate
    Utilitaire permettant de simplifier la rotation d'un grand nombre de fichiers de {term}`log`.
    --- [Sources](https://github.com/logrotate/logrotate)
```
