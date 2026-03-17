Bases de données SQL
====================

```{glossary}
SQL
   (_Structured Query Language_) Langage informatique
   permettant de chercher des informations dans une base de données relationnelle.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Structured_Query_Language),
   [Doc MariaDB](https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-advanced-sql-guide)
```

Une {term}`instance` de {logiciel}`MariaDB`, commune à tous les membres, est présente sur le serveur CLUB1.
L'accès est optionnel et peut être ajouté à la création du compte membre
ou plus tard sur demande.

Bases de données personnelles
-----------------------------

Il est possible de créer autant de **bases de données {term}`SQL` personnelles** que voulu.
Celles-ci devront avoir un nom commençant par votre identifiant suivi de `_`.
Par exmple si `lisa` veut créer une base de donnée `flarum`,
elle devra la nommer `lisa_flarum`.

Il n'y a pour le moment pas de limite au nombre de bases de données personnelles,
ni à la quantité de données qu'elles peuvent contenir.

Interface Web
-------------

Une interface {term}`Web` de gestion fournie par {logiciel}`phpMyAdmin`
est disponible à l'adresse suivante : <https://phpmyadmin.club1.fr>

Interface en ligne de commande
------------------------------

Il est possible de se connecter au serveur SQL directement depuis la {term}`ligne de commande <CLI>`.
Pour cela, il faut tout d'abord se connecter au serveur en [SSH](ssh.md).
Ensuite, la {term}`commande` pour démarrer un shell SQL est la suivante :

    mariadb

Depuis ce shell il est possible de lancer n'importe quelle commande {term}`SQL`.

Informations de connexion
-------------------------

L'instance {logiciel}`MariaDB` de CLUB1 n'est pas accessible depuis l'extérieur.
Il n'est donc possible de s'y connecter que depuis un processus s'exécutant sur le même serveur.

```{important}
Il est généralement **inutile de renseigner son mot de passe**,
car les connexions locales vont préférer l'utilisation de la _"socket Unix"_,
et ainsi s'authentifier automatiquement.
[C'est en particulier le cas](https://www.php.net/manual/fr/ref.pdo-mysql.connection.php#refsect1-ref.pdo-mysql.connection-notes)
de {term}`PHP`.

Ne pas renseigner de mot de passe **améliore la sécurité** de votre compte CLUB1,
puisque ça évite qu'il soit sauvegardé _en clair_ sur le serveur.
```

| champ            | valeur              |
| ---------------- | ------------------- |
| hôte             | `localhost`         |
| port             | `3306` (par défaut) |


Logiciels
---------

```{logiciel} MariaDB
{term}`Serveur` de bases de données {term}`SQL` distribué sous licence {term}`libre <logiciel libre>`.
--- [Wikipedia](https://fr.wikipedia.org/wiki/MariaDB),
[Sources](https://github.com/MariaDB/server)
```

```{logiciel} phpMyAdmin
Interface {term}`Web` de gestion de bases de données {term}`SQL` écrit en {term}`PHP`.
Chez CLUB1, phpMyAdmin est directement servi par {logiciel}`Nginx`
via {logiciel}`PHP-FPM`.
--- [Wikipedia](https://fr.wikipedia.org/wiki/PhpMyAdmin),
[Sources](https://github.com/phpmyadmin/phpmyadmin)
```
