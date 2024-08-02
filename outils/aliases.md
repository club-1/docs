Gestion des alias email
=======================

Ce manuel est réservé aux utilisateurs faisant partie du {term}`groupe` `aliases`.
Il décrit les actions que peuvent accomplir ces utilisateurs sur les {term}`alias` emails.

Modifier les alias de réception
-------------------------------

Ouvrir le fichier `/etc/aliases` avec votre éditeur de texte en CLI favori
(`nano`, `vim`, etc.).
Il doit ressembler approximativement à ceci :

```Makefile
# See man 5 aliases for format.
# Use tab for alignment.
# To regenerate the db file run: newaliases
postmaster:     root
root:           nicolas
contact:        nicolas,vincent,guilhem,audrey
alert:          nicolas,vincent,guilhem
matrix-synapse: /dev/null
jellyfin:       /dev/null
```

```{important}
Après avoir sauvegardé le fichier, il est nécessaire de regénérer la base de
donnée (`/etc/aliases.db`) en lançant la commande suivante :

    newaliases
```

### Ajouter ou supprimer un utilisateur d'un alias

Il suffit d'écrire ou d'effacer l'identifiant de l'utilisateur choisi de la
liste se trouvant après le nom de l'alias.

### Ajouter ou supprimer un alias

Il est possible d'ajouter autant d'alias que voulu en ajoutant une nouvelle ligne
au fichier, en suivant la [syntaxe d'alias de Postfix](http://www.postfix.org/aliases.5.html) :

```Makefile
ALIAS:      USER1[,USER2...]
```

Pour supprimer un alias, il suffit de supprimer ou commenter (avec `#`) la ligne
correspondante.


Modifier les alias d'envoi
--------------------------

Le processus est très similaire à celui de la [modification des alias de réception](#modifier-les-alias-de-réception),
mais il existe quelques différences :

1. Le fichier à modifier est `/etc/aliases_senders`.
2. Il ne faut PAS mettre de `:` entre la clé et la valeur.
3. Il faut toujours indiquer l'email complet avec `@club1.fr`.
4. La commande pour régénérer la base de données est :

       /usr/sbin/postmap hash:/etc/aliases_senders

Utilisation avancée
-------------------

Comme indiqué précédemment, le fichier d'alias de réception `/etc/aliases` respecte la [syntaxe d'alias de Postfix](http://www.postfix.org/aliases.5.html).
En plus de rediriger les emails vers d'autres adresses,
elle permet de les envoyer vers des fichiers ou des commandes.
Dans ce cas, il faut faire attention aux {term}`permissions` requises
pour créer les fichiers et exécuter les commandes.
Ces actions sont réalisées avec les droits de l'utilisateur correspondant à l'alias s'il existe
et sinon, sur CLUB1, avec l'utilisateur `nobody` et le {term}`groupe` `mail`.

```{seealso}
La [section "Delivery Rights" de la page local du manuel de Postfix](https://manpages.debian.org/bullseye/postfix/local.8postfix.en.html#DELIVERY_RIGHTS).
```
