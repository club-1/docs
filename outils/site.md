Site Web de CLUB1
=================

On ne dirait peut-être pas comme ça, mais le site {term}`Web` de CLUB1 est un {term}`Wiki`.
Cela implique qu'il est possible d'éditer son contenu directement depuis le navigateur.

Les discussions à ce sujet sont [rassemblées sur le forum avec le tag {guilabel}`site web`](https://forum.club1.fr/t/site-web).

Comptes
-------

Pour participer à l'édition du site, il faut au moins un compte éditeur.

```{warning}
Ce type de compte est indépendant du compte CLUB1 !
Pour avoir un compte d'éditeur, il faut contacter les administrateurs du site :
Venez en discuter sur le salon {term}`Matrix` [`#site-web:club1.fr`](matrix:r/site-web:club1.fr)
ou envoyez un message à <contact@club1.fr>.
```

Édition d'une page existante
----------------------------

Pour éditer une page, il y a deux possibilités :

- En cliquant sur le bouton {guilabel}`✏️ modifier` en bas de la page.
- En rajoutant `/edit` dans la barre d'URL.

Le contenu se trouve le plus souvent dans l'onglet {guilabel}`main`.
Les onglets {guilabel}`nav`, {guilabel}`aside`, {guilabel}`footer`, {guilabel}`header`
servent à stocker du contenu périphérique.
Dans ces 5 onglets, il est possible d'utiliser du {term}`Markdown` ou du {term}`HTML`.
L'onglet {guilabel}`body` contient la structure de la page.
et ne peut contenir que du HTML.
Le style de la page est lui aussi éditable via l'onglet {guilabel}`css`.

💾 Pour sauvegarder, il faut cliquer sur {guilabel}`update` ou faire {kbd}`CTRL` + {kbd}`S`.

👁️ Pour afficher la page, il faut cliquer sur {guilabel}`display` ou faire {kbd}`CTRL` + {kbd}`D`.


```{tip}
Lorsque l'on fait des modifications sur le site Web,
il est bienvenu de le notifier en écrivant un résumé des actions dans le salon Matrix [`#site-web:club1.fr`](matrix:r/site-web:club1.fr).
```

Création d'une page
-------------------

Pour ajouter une page, il faut écrire son nom dans la barre d'URL après `https://club1.fr/`,
puis rajouter `/add` à la fin.

    https://club1.fr/MA_NOUVELLE_PAGE/add

Ici, `MA_NOUVELLE_PAGE` est le nom de votre future page.

```{note}
{logiciel}`W` va s'occuper de transformer le nom que vous avez choisi en **identifiant officiel de la page**,
en simplifiant le titre que vous aurez choisi.
Cet identifiant de votre page est unique et fixe, il ne pourra pas être changé par la suite.
```

Administration
--------------

La mise à jour et l'accès aux fichiers de {logiciel}`W`
est limité aux utilisateur·ices membres du {term}`groupe` `website`.

Moteur de Wiki
--------------

Le moteur de Wiki utilisé n'est pas un outil très connu.
En dehors du site officiel de CLUB1,
son usage se limite pour l'instant à quelques membres du club pour leurs sites respectifs.


````{logiciel} W
Moteur de {term}`Wiki` écrit en {term}`PHP`.
Son but est de croiser la prise de note avec l'édition de site {term}`Web`
en encourageant l'édition spontanée de pages aux styles variés.
--- [Sources](https://github.com/vincent-peugnet/wcms/), [Site](https://w.club1.fr/)
```
