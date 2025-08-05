Comptabilité
============

CLUB1 n'utilise pas de compte en banque dédié.
Au lieu de ça, les membres qui ont dépensé de l'argent notent ces dépenses dans un [fichier de transactions](#fichier-de-transactions).
Lorsque des adhésions sont payées ou que l'on reçoit des dons,
ceux-ci sont transférés à l'une des personnes qui ont une balance négative.


Fichier de transactions
-----------------------

La comptabilité du club est consignée sur le serveur à l'aider d'un fichier de transactions.
Il se situe au chemin suivant :

    /var/compta/transactions.tsv

Comme son extension l'indique, il s'agit d'un fichier TSV (*Tab Separated Values*).
Chaque ligne de ce fichier représente une transaction.
À l'intérieur, les différentes valeurs sont séparées par des *tabulations* (touche {kbd}`Tab ↹`).

Voici un exemple de ligne :

    27	2019-01-10	+35	Nicolas Peugnet	x	adhesion	Adhésion roquefort

La première colonne correspond à l'**identifiant unique** de chaque transaction.
Ce nombre doit toujours augmenter.
Ensuite, c'est la **date d'ajout** de la transaction.
Puis le **montant** de cette dernière.
On indique un `+` ou un `-` devant pour indiquer si c'est de l'argent qui entre ou qui sort.
Le **compte** qui a dépensé ou reçu l'argent viens ensuite.
Si le paiement est **effectué**, on ajoute un `x`.
Les différentes **catégories** sont `adhesion`, `don`, `infra` et `autre`.
Enfin, viens l'**intitulé**, qui est une courte description de la transaction.


```{admonition} Permissions
Ce fichier est accessible en lecture par tout les utilisateurs.
Donc n'hésitez pas à jeter un coup d'oeil !
En revanche, pour écrire dedans, il faut être membre du {term}`groupe` `compta`.
```


Usage
-----

Pour étudier ou modifier la liste des transactions,
il suffit d'ouvrir le fichier dans un éditeur de texte.
Mais bon, c'est pas forcément hyper confortable.
Pour palier à cela,
il est possible d'utiliser des {term}`commandes <commande>`
une fois que l'on est [connecté au serveur en SSH](/services/ssh.md).

En fonction de votre familiarité avec le {term}`terminal`,
deux options s'offrent à vous :


### Interface sympathique

Cette interface est faite pour être le plus simple possible.
Elle ne fait que poser des questions.

```{commande} compta
Interface conviviale de gestion de la comptabilité de CLUB1.
```


### Commandes pour un usage avancé

Les utilisateurs plus habitués à l'utilisation de la {term}`CLI`
peuvent directement utiliser les commandes suivantes.

```{commande} compta-voir
Permet de consulter rapidement le contenu du fichier de comptabilité.
Il est possible de filtrer ou même d'afficher le total, en fournissant des options.
```

```{commande} compta-ajouter
Permet d'ajouter une transaction au fichier de comptabilité.
Il est nécessaire de remplir une grande partie des options.
```

```{commande} compta-effectuer
Permet de marquer une transaction comme "effectuée".
Il faut connaître l'identifiant de la transaction que l'on veut modifier.
```

```{tip}
Elles disposent chacunes d'une aide, qui décrit leur fonctionnement.
Elle s'affiche avec l'option `-h`.
```


### Logiciel utilisé


```{logiciel} compta
Ensemble de scripts pour afficher ou éditer la comptabilité de club1 via le terminal.
--- [Sources](https://github.com/club-1/compta)
```
