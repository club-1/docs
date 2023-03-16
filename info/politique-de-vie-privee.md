Politique de vie privée
=======================

Nos engagements en matière de vie privée.

```{admonition} Voir aussi
Nos engagement dans les [CGU](../cgu.md#nos-engagements)
```

Politique de sécurité
-----------------------

- ⚠️ Les données des membres sur le serveur **ne sont pas chiffrés**.
  Elles sont donc lisibles par les administrateurs (utilisateur `root` et membres du groupe `sudo`).
- Les [sauvegardes](./general.md#sauvegardes) sont, elles, chiffrées.
- Les {term}`protocoles <protocole>` utilisés pour se connecter au serveur sont tous chiffrés,
  les mots de passe et les données ne peuvent donc pas être interceptées.
- Les données personnelles sont protégées par les [permissions UNIX](https://fr.wikipedia.org/wiki/Permissions_UNIX).
  Par defaut l'[espace personnel](./espace-personnel.md) n'est pas accessible par les autres utilisateurs
  (à part en lecture par les membres du groupe `home`, ex: le {term}`serveur` {term}`web`).
  Chacun est libre de changer les permissions de son espace perso.

```{tip}
Il est possible de savoir qui est membre d'un groupe sur le serveur
depuis un accès {term}`SSH` avec la commande suivante :

    members <group>

En remplaçant `<group>` par le groupe voulu. Exemple : `members sudo` ou `members home`.
```

Engagements des administrateurs systèmes
-----------------------------------------

Les administrateurs système s'engagent à respecter les points suivants :

- Ne pas accéder aux données utilisateur (espace personnel et bases de données) sans leur accord,
  sauf en cas de restauration suite à un problème technique,
  auquel cas les utilisateurs concernés en seront avertis.
- Chiffrement des clefs {term}`SSH`.
- Application des bonnes pratiques en matière de sécurité
  (remplacement des mots de passe par défaut, mots de passe générés forts, etc.).
