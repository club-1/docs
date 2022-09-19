Hébergement de sites Web
========================

Il existe deux grands types de sites {term}`Web` : les sites _statiques_,
constitués de fichiers dont le contenu ne change pas tant qu'ils n'ont pas
été modifiés et les sites _dynamiques_, dont les fichiers sont exécutés et
peuvent ainsi produire des résultats différents.

Sites Web _statiques_
---------------------

L'**espace personnel** dispose d'un dossier spécial `static/` à sa racine.
Tous les fichiers et dossiers rangés dedans seront automatiquement publiés
sur le {term}`Web` à l'adresse `https://static.club1.fr`, par exemple :

[`https://static.club1.fr/nicolas/test.html`](https://static.club1.fr/nicolas/test.html)
--> `/home/nicolas/static/test.html`

Ce dossier est servi par le serveur HTTP {term}`Apache`.
Il est configuré pour automatiquement générer un _index_ affichant la liste
des fichiers et dossiers qu'il contient.

Pour ne pas afficher cet index, il est possible soit de créer un fichier
`index.html` qui contiendra la page à afficher à la place, soit d'ajouter
un fichier caché de configuration Apache `.htaccess` contenant au moins la
ligne suivante.

```apache
Options -Indexes
```

Sites Web _dynamiques_
----------------------

Il est possible d'ajouter à la demande des **sous-domaines** de `club1.fr`
pointant vers **l'un des dossiers** présent dans votre **espace personnel**
pour ainsi créer un site {term}`Web`. Les noms des sous-domaines seront à définir
ensemble en fonction de leur disponibilité et leur viabilité.

Logiciels
---------

```{glossary}
Apache
   {term}`Serveur` HTTP très populaire, distribué sous license libre.
   HTTP étant le protocole du {term}`Web` on parle aussi souvent de "serveur Web".
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Apache_HTTP_Server),
   [Sources](https://github.com/apache/httpd)
```
