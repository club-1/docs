Gestion des alias email
=======================

Ce tutoriel est réservé aux utilisateurs faisant partie du groupe unix `aliases`.
Il décrit les actions que peuvent accomplir ces utilisateurs.

Modifier le fichier de configuration des alias
----------------------------------------------

Ouvrir le fichier `/etc/aliases` avec votre éditeur de texte en CLI favori
(`nano`, `vim`, etc.).
Il doit ressembler approximativement à ceci :

```Makefile
# See man 5 aliases for format
postmaster:     root
root:           nicolas
contact:        nicolas,vincent,guilhem,audrey
alert:          nicolas,vincent,guilhem
matrix-synapse: /dev/null
jellyfin:       /dev/null
```

### Ajouter ou supprimer un utilisateur d'un alias

Il suffit d'écrire ou d'effacer l'identifiant de l'utilisateur choisi de la
liste se trouvant après le nom de l'alias.

### Ajouter ou supprimer un alias

Il est possible d'ajouter autant d'alias que voulu a ajoutant une nouvelle ligne
au ficher, en suivant la [syntaxe d'alias de postfix](http://www.postfix.org/aliases.5.html) :

```
<ALIAS>:      <USER1>[,<USER2>...]
```

Pour supprimer un alias, il suffit de supprimer ou commenter (avec `#`) la ligne
correspondante.

Soumettre les modifications
---------------------------

Après avoir sauvegardé le fichier, il est nécessaire de regénérer la base de
donnée (`/etc/aliases.db`) en lançant la commande suivante :

```
sudo newaliases
```
