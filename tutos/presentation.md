Éditer son fichier de présentation
==================================

> Un fichier pour se présenter

Votre [*home*](/info/espace-personnel.md) peut servir à vous présenter.
Pour se faire, vous pouvez y ajouter, *à la racine* (pas dans un sous-dossier) un fichier s'appellant :

    PRESENTATION.md

Tout ce que vous écrirez dans ce fichier sera visible sur la page
[membres](https://club1.fr/membres) du site web de CLUB1.

Libre à vous d'utiliser le {term}`Markdown` pour pimenter votre présentation !
N'hésitez pas à mettre des liens vers vos projets web,
ça permettra aux membres et visiteurs de les découvrir 🔎️.

```markdown
# Ma super présentation

En *Markdown* avec [un lien](https://nana.club1.fr).
```


Metadonnées
-----------

Pour aller plus loin dans la personnalisation,
il est possible de modifier certains paramètres d'affichage.
Notamment, votre __nom d'affichage__ et la __couleur__ de votre bouton.

Pour cela il faudra ajouter quelques lignes spécifiques __au début votre fichier__ `PRESENTATION.md`.

    ---
    name: Mon super prénom
    color: pink
    ---
    
    # Ma super présentation...

L'espace qui contient les métadonnées est délimité par des lignes contenant __trois tirets__ `---`.
À l'intérieur de ces limites, on peut définir un paramètre par ligne comme il suit :
Le nom du paramètre, suivit de deux points et d'un espace `: `,
puis de la valeur que vous souhaitez lui assigner.

```{tip}
Pour info, cette syntaxe *vaguement standard*
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
utilisant votre identifiant CLUB1 (`#` + votre nom d'utilisataire).

Par exemple, l'adresse suivante ouvrira directement la présentation du membre `vincent` :

    https://club1.fr/membres/#vincent



```{raw} latex
\clearpage
```
