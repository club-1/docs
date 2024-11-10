Comptabilité
============

La comptabilité du club est consigné sur le serveur à l'aider d'un fichier de transaction.
C'est un fichier TSV qui se situe dans le chemin suivant :

    /var/compta/transactions.tsv

Chaque transaction représente une ligne sur ce fichier.
La première colonne correspond à l'identifiant unique de chaque transaction.
Ce nombre doit toujours augmenter.

Il est accessible en lecture par tout les utilisateurs.
En revanche, pour écrire dans ce fichier, il faut être membre du {term}`groupe` `compta`.

Manipulation
------------

Pour étudier ou modifier de façon confortable la liste des transactions,
il est possible d'utiliser des commandes lorsque l'on est connecté en {term}`SSH` au serveur.


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
