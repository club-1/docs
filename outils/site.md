Site Web de CLUB1
=================

On ne dirait peut-être pas comme ça, mais le site {term}`Web` de CLUB1 est un {term}`wiki`.
Cela implique qu'il est possible d'éditer son contenu directement depuis le navigateur.
Peu de connaissances techniques sont requises :
Le contenu est formaté en {term}`Markdown`
et la mise en page utilise le duo {term}`HTML` / CSS.

Les discussions à ce sujet sont [rassemblées sur le forum avec le tag {guilabel}`site web`](https://forum.club1.fr/t/site-web).

Il y a aussi un salon {term}`Matrix` dédié à l'édition du site : [`#site-web:club1.fr`](matrix:r/site-web:club1.fr)


Compte et niveaux
-----------------

Le compte de membre CLUB1 permet d'accèder à l'interface d'édition du site Web.
Pour s'y connecter, on peut utiliser l'adresse suivante :
<https://club1.fr/!co> et rensigner son identifiant et mot de passe de membre.

Lors de la première connexion, un compte est automatiquement créé avec le niveau "editor".
Ce statut permet de [créer des pages](#création-dune-page),
de mettre en ligne des médias et d'autoriser d'autres compte à modifier ses pages.
Cela ne permet donc pas directement de [modifier une page existante](#édition-dune-page-existante).
Pour y participer il faudra être ajouté à la liste des auteur·ices.
Cette limitation vise à éviter des modifications malencontrueuses
qui risquent d'avoir lieu lorsque l'on découvre un nouveau logiciel.

Qu'à cela ne tiennent :
Essayez de **créer vos premières pages** !
Elle resterons discrètes tant qu'aucun lien n'y mènent.

Une fois que l'interface vous semble plus familière,
vous pouvez demander à être ajouté en tant qu'auteur·ice des pages que vous souhaitez modifier.
Pour cela, un endroit idéal est le salon de discussion _Matrix_ cité plus haut.
Pour avoir des droits supplémentaires, il peut être intéressant de passer au rôle "super editor",
qui n'a *aucune limite* 💣️.

```{tip}
Une fois connecté, on peut accéder à [l'interface qui documente l'usage du wiki](https://club1.fr/!info).
```

Création d'une page
-------------------

Pour ajouter une page, il faut écrire son titre dans la barre d'URL après `https://club1.fr/`,
puis rajouter `/add` à la fin.

    https://club1.fr/MA_NOUVELLE_PAGE/add

Ici, `MA_NOUVELLE_PAGE` est le nom de votre future page.

```{note}
{logiciel}`W` va s'occuper de transformer le nom que vous avez choisi en **identifiant officiel de la page**,
en simplifiant le titre que vous aurez choisi.
Cet identifiant de votre page est unique et fixe, il ne pourra pas être changé par la suite.
```

Édition d'une page existante
----------------------------

Pour éditer une page, il y a deux possibilités :

- En cliquant sur le bouton {guilabel}`✏️ modifier` en bas de la page.
- En rajoutant `/edit` dans la barre d'URL.

Le contenu se trouve dans l'onglet {guilabel}`content`.
Il est possible d'utiliser du {term}`Markdown` ou du {term}`HTML`.
L'onglet {guilabel}`body` contient la structure de la page.
et ne peut contenir que du HTML.
Le style de la page est lui aussi éditable via l'onglet {guilabel}`css`.

💾 Pour sauvegarder, il faut cliquer sur {guilabel}`update` ou faire {kbd}`CTRL` + {kbd}`S`.

👁️ Pour afficher la page, il faut cliquer sur {guilabel}`display` ou faire {kbd}`CTRL` + {kbd}`D`.

```{tip}
Lorsque l'on fait des modifications sur le site Web,
il est bienvenu de le notifier en écrivant un résumé des actions dans le salon _Matrix_ dédié.
```

Administration
--------------

La mise à jour et l'accès aux fichiers de {logiciel}`W`
est limité aux utilisateur·ices membres du {term}`groupe` `website`.

La gestion des comptes se fait depuis l'interface Web de W : {guilabel}`users`.
Il faut avoir le niveau "admin" pour pouvoir accéder à cette page.

Moteur de wiki
--------------

On utilise W, connecté à l'annuaire {term}`LDAP`.
C'est un moteur de wiki très peu connu, il est codé principalement par des membres de CLUB1.


```{logiciel} W
Moteur de {term}`wiki` écrit en {term}`PHP`.
Son but est de croiser la prise de note avec l'édition de site {term}`Web`
en encourageant l'édition spontanée de pages aux styles variés.
--- [Sources](https://github.com/vincent-peugnet/wcms/), [Site](https://w.club1.fr/)
```
