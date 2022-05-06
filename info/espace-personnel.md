Espace personnel
================

home sweet home
---------------

L'hébergement CLUB1 est basé sur la mise à disposition d'un *espace personnel*.
Il s'agit d'un espace de stockage sur le serveur, accessible via un certain
nombre de protocoles, fournissant différents services.


Chaque membre de CLUB1 dispose d'un *espace personnel*.
C'est votre *chez vous*, d'ailleurs, on appelle ce dossier `home` 🏠.
Mais comme vous avez tout les droits, vous avez également le droit de tout supprimer.
Donc faites attention, car cetains dossier à l'intérieur peuvent être précieux.
Par exemple vos emails, qui sont dans le dossier `mail` 🤯 .

Eh oui, un grand pouvoir implique de grandes responsabilités... 😏

Vous pouvez y faire ce que vous voulez, mais comme chez vous il y a aussi des voisins.
En effet, __il n'y a pas de limite de stockage définie__ par dossier `home` de chaques membres,
mais par contre, une limite physique :
Tout ces dossiers sont sur un support de stockage SSD totalisant __1To__.
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

Ce dossier est la porte la plus proche vers le {term}`Web`.

### 📁 git

Dossier utilisé pour [héberger des dépots de code Git](/services/git.md)



Fichier de présentation
-----------------------


### Un fichier pour se présenter

Votre *home* peut également servir à vous présenter .
Pour se faire, vous pouvez y ajouter, *à la racine* un fichier s'appellant :

```
PRESENTATION.md
```

Tout ce que vous écrirez dans ce fichier sera visible sur la page
[membres](https://club1.fr/membres) du site web de CLUB1.

Libre à vous d'utiliser le {term}`Markdown` pour pimenter votre présentation !
N'hésitez pas à mettre des liens vers vos projets web,
ça permettra aux membres et visiteurs de les découvrir 🔎️.



### Metadonnées

Pour aller toujours plus loin dans la personnalisation,
il est possible de mofifier certains paramètres d'affichages.
Notamment, votre __nom d'affichage__ et la __couleur__ de votre bouton.

Pour cela il faudra ajouter quelques ligne au début votre fichier `PRESENTATION.md`.

```
---
name: Mon super prénom
color: pink
---

# Ma super présentation

en *Markdown*

```
Le formatage est simple,
il faut juste respecter les trois tirets au début et à la fin de la zone de métadonnée.
Ensuite vous pouvez definir un ou plusieurs paramètres.
Pour info, cette syntaxe *plus ou moins standard* s'appelle [Front Matter](https://jekyllrb.com/docs/front-matter/).


- Pour le paramètre `name`, vous pouvez inscrire une ligne de texte libre. Profitez en car c'est possible de mettre majuscule, minuscule et certains caractères spéciaux (même des Emoji 😉).
- Pour le paramètre `color`,
vous devez utiliser une [couleur du web](https://fr.wikipedia.org/wiki/Couleur_du_Web#Noms_de_couleurs_SVG_1.0).
⚠️ Attention ! Si vous mettez un code couleur, il devra commencer par un __croisillon (#)__
et être __entouré de guillemets__ (par exemple : `color: "#F87716"`).




### Faire un lien vers son profil

Si vous êtes satisfait&middot;e de votre superbe présentation,
il est possible de la partager facilement.

Il vous suffit de faire un lien ciblant spécifiquement votre présentation.
Pour cela on utilise un [identificateur de fragment](https://fr.wikipedia.org/wiki/Identificateur_de_fragment)
utilisant votre identifiant CLUB1.

Par exemple, l'adresse suivante ouvrira directement la présentation du membres `vincent`

```
htpps://club1.fr/membres/#vincent
```


