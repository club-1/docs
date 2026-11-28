Cabanon
=======

Le cabanon est un espace de stockage supplémentaire à disposition des membres.
Il a pour but d'accueillir les données volumineuses
évitant ainsi de saturer l'[espace personnel](espace-personnel.md) des membres `/home`.
En contrepartie, il est moins fiable
car il  __ne fait pas partie des [sauvegardes](../outils/sauvegardes.md)__.
Il est physiquement situé sur [le disque dur](./infrastructure-materielle.md#stockage-secondaire) (`hdd2`).

Chemin d'accès au cabanon :

    /shed

```{warning}
Il est très fortement recommandé de __stocker une copie__ de ce que l'on entrepose dans le cabanon
__sur son propre matériel__.
```

Accès
-----

Étant situé en dehors de votre espace personnel, le cabanon n'est accessible initialement
qu'à partir d'une connexion {term}`SSH`.
Pour y avoir accès depuis votre espace personnel,
un {term}`lien symbolique` sera nécessaire.
Cela permet d'utiliser cet espace pour les fichiers volumineux d'un site {term}`Web` par exemple.


Gestion de l'espace
-------------------

Le dossier `/shed` est organisé par convention de la même manière que le dossier `/home`,
avec un dossier par membre, portant le nom de son identifiant.
Chaque membre doit créer son propre dossier avec la {term}`commande` `mkdir /shed/IDENTIFIANT`,
en remplaçant `IDENTIFIANT` par son identifiant CLUB1.
Comme pour l'espace personnel, il n'y a pas de quota défini pour l'usage du cabanon.
