Éditer son fichier de présentation
==================================

> Un fichier pour se présenter

Votre [*home*](/info/espace-personnel.md) peut servir à vous présenter.
Pour se faire, vous pouvez y ajouter, *à la racine* un fichier s'appellant :

    PRESENTATION.md

Tout ce que vous écrirez dans ce fichier sera visible sur la page
[membres](https://club1.fr/membres) du site web de CLUB1.

Libre à vous d'utiliser le {term}`Markdown` pour pimenter votre présentation !
N'hésitez pas à mettre des liens vers vos projets web,
ça permettra aux membres et visiteurs de les découvrir 🔎️.


Metadonnées
-----------

Pour aller plus loin dans la personnalisation,
il est possible de modifier certains paramètres d'affichage.
Notamment, votre __nom d'affichage__ et la __couleur__ de votre bouton.

Pour cela il faudra ajouter quelques ligne au début votre fichier `PRESENTATION.md`.

    ---
    name: Mon super prénom
    color: pink
    ---
    
    # Ma super présentation
    
    en *Markdown*

Le formatage est simple,
il faut juste respecter les trois tirets au début et à la fin de la zone de métadonnées.
Ensuite vous pouvez définir un ou plusieurs paramètres.

```{tip}
Pour info, cette syntaxe *plus ou moins standard*
s'appelle [Front Matter](https://jekyllrb.com/docs/front-matter/).
```

- Pour le paramètre `name`, c'est ici que vous pouvez choisir votre pseudo avec une ligne de texte libre.
  Profitez-en car c'est possible de mettre majuscule, minuscule et certains caractères spéciaux (même des Emoji 😉).
  Si vous omettez ce champ, votre identifiant CLUB1 sera affiché.
- Pour le paramètre `color`,
  vous devez utiliser une [couleur du web](https://fr.wikipedia.org/wiki/Couleur_du_Web#Noms_de_couleurs_SVG_1.0).

  ```{important}
  Si vous mettez un code couleur, il devra commencer par un __croisillon `#`__
  et être __entouré de guillemets__ (par exemple : `color: "#F87716"`).
  ```



Faire un lien vers son profil
-----------------------------

Si vous êtes satisfait&middot;e de votre superbe présentation,
il est possible de la partager facilement.
Il vous suffit de faire un lien ciblant spécifiquement votre présentation.
Pour cela on utilise un [identificateur de fragment](https://fr.wikipedia.org/wiki/Identificateur_de_fragment)
utilisant votre identifiant CLUB1 (`#` + votre nom d'utilisateur&middot;trice).

Par exemple, l'adresse suivante ouvrira directement la présentation du membre `vincent` :

    https://club1.fr/membres/#vincent



```{raw} latex
\clearpage
```
