Bases de données SQL
====================

```{glossary}
SQL
   (_Structured Query Language_) Langage informatique
   permettant de chercher des informations dans une base de données relationnelle.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Structured_Query_Language)
```

Un accès à {term}`MariaDB` pourra être ajouté, à partir duquel il est possible de
créer des **bases de données {term}`SQL` personnelles**. Une interface {term}`Web`
de gestion fournie par {term}`phpMyAdmin`
est disponible à l'adresse suivante : <https://phpmyadmin.club1.fr>

Informations de connexion
-------------------------

| champ            | valeur              |
| ---------------- | ------------------- |
| hôte             | `localhost`         |
| port             | `3306` (par défaut) |

Logiciels
---------

```{glossary}
MariaDB
   {term}`Serveur` de bases de données {term}`SQL` distribué sous licence libre.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/MariaDB),
   [Sources](https://github.com/MariaDB/server)

phpMyAdmin
   Interface {term}`Web` de gestion de bases de données {term}`SQL` écrit en {term}`PHP`.
   Chez CLUB1, phpMyAdmin est directement servi par {term}`Nginx`
   via {term}`PHP-FPM`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/PhpMyAdmin),
   [Sources](https://github.com/phpmyadmin/phpmyadmin)
```
