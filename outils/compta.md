Comptabilité
============

CLUB1 n'utilise pas de compte en banque dédié.
Au lieu de ça, les membres qui ont dépensé de l'argent notent ces dépenses dans un [fichier de transaction](#fichier-de-transactions).
Lorsque qu'il y a des adhésions sont payés ou que l'on reçoit des dons,
ceux ci sont reviennent à l'une de personne qui a une balance négative.


Fichier de transactions
-----------------------

La comptabilité du club est consigné sur le serveur à l'aider d'un fichier de transaction.
C'est un fichier TSV qui se situe dans le chemin suivant :

    /var/compta/transactions.tsv

Chaque ligne sur ce fichier représente une transaction. Voici un exemple de ligne :

    id  date        echange  compte               effectué  catégorie  intitulé
    1   2019-01-10  +35      Nicolas Peugnet      x         adhesion   adhésion audrey

La première colonne correspond à l'**identifiant unique** de chaque transaction.
Ce nombre doit toujours augmenter.
Ensuite, c'est la **date d'ajout** de la transaction.
Puis le **montant** de cette dernière.
On indique un `+` ou un `-` devant pour indiquer si c'est de l'argent qui entre ou qui sort.
Le **comtpe** qui a dépensé ou reçu l'argent viens ensuite.
Si le paiement est **effectué**, on ajoute un `x`.
Les différentes **catégories** sont `adhesion`, `don`, `infra` et `autre`.
Enfin, l'**ititulé** est une courte description de la transaction.

### Permissions

Ce fichier est accessible en lecture par tout les utilisateurs.
Donc n'hésitez pas à jeter un coup d'oeil !
En revanche, pour écrire dedans, il faut être membre du {term}`groupe` `compta`.


Usage
-----

Pour étudier ou modifier la liste des transactions,
il suffit d'ouvrir le fichier dans un éditeur de texte.
Mais bon, c'est pas forcément hyper confortable.
Pour palier à cela,
il est possible d'utiliser des commandes une fois que l'on est [connecté au serveur en {term}`SSH`](services/ssh.md).

En fonction de votre familiarité avec le {term}`terminal`,
deux options s'offrent à vous :


### Interface sympathique

Cette interface est faite pour être le plus simple possible.
Elle ne fait que poser des questions.

```{commande} compta
Interface conviviale de gestion de la comptabilité de CLUB1.
```


### Commandes préçises pour un usage avancé

Le utilisateurs plus habitués à l'utilisation de la {term}`CLI`
peuvent directement utiliser ces deux sous commandes.

#### voir

```{commande} compta-voir
Permet de consulter rapidement le contenu du fichier de comptabilité.
Il est possible de filtrer ou même d'afficher le total en ajoutant des options.
```

#### ajouter

```{commande} compta-ajouter
Permet d'ajouter une transaction au fichier de comptabilité.
Il est nécessaire de remplir une grande partie des options.
```
