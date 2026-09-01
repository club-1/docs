Cabanon
=======

Le cabanon est un espace de stockage supplémentaire à disposition des membres.
Il a pour but d'accueillir les données volumineuses
évitant ainsi de saturer l'[espace personnel](espace-personnel.md) des membres `/home`.
En contrepartie, il est moins fiable
car il  __ne fait pas partie des [sauvegardes](../outils/sauvegardes.md)__.
Il est physiquement situé sur [un disque dur](./infrastructure-materielle.md#stockage-secondaire) `hdd2`.

Chemin d'accès au cabanon :

    /shed

```{warning}
Il est très fortement recommandé de stocker de son côté une copie de ce que l'on entrepose dans le cabanon.
```

Accès
-----

Pour faciliter l'accès à cet espace depuis votre espace personnel,
un {term}`lien symbolique` peut être utile.
Cela permet d'utilier cet espace pour les fichiers volumnieux d'un site {term}`Web` par exemple.

Gestion de l'espace
-------------------

Comme pour l'espace personnel, il n'y a pas de quota définit pour l'usage du cabanon.
