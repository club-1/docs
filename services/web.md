Hébergement de sites Web
========================

L'hébergement de site web est historiquement le **premier service** mis à la disposition des membres de CLUB1.

```{important}
La liberté d'expérimenter est au coeur des principes de CLUB1 :
Un compte membre CLUB1 **ne limite pas à un seul site web** !
Il n'y a pas de limite au nombre de projet web à héberger tant que ça ne sature pas le serveur 😄.
```

Il y a deux façons d'héberger du contenu qui va être accessible sur le {term}`Web` avec le serveur :

- via [le dossier `static`](#dossier-static) *C'est l'approche la plus spontanée.*
- avec [un domaine dédié](#hébergement-avec-un-nom-de-domaine-dédié) *Pour des projets mieux définis.*


Dossier `static/`
-----------------

L'**espace personnel** dispose d'un dossier spécial `static/` à sa racine.
Tous les fichiers et dossiers rangés dedans seront automatiquement publiés
sur le {term}`Web` à l'adresse `https://static.club1.fr`, par exemple :

[`https://static.club1.fr/nicolas/test.html`](https://static.club1.fr/nicolas/test.html)
--> `/home/nicolas/static/test.html`

```{warning}
Le dossier `static` se limite aux {term}`sites statiques<site statique>`.
Pour héberger des sites {term}`sites dynamqiues<site dynamqiue>`,
il faut forcément utiliser un [domaine dédié](#hébergement-avec-un-nom-de-domaine-dédié).
```

C'est l'endroit idéal pour débuter et commencer à mettre en ligne rapidement.

```{admonition} Voir aussi
Le tutoriel "[](/tutos/mes-premiers-pas-sur-le-web.md)"
pour apprendre à faire son premier site web avec le dossier `/static`.
```

Hébergement avec un nom de domaine dédié
----------------------------------------

Contrairement au dossier `static` qui est à emplacement fixe,
vous êtes libres de choisir l'emplacement des fichiers qui vont être utilisés.

On vous recommande de créer un dossier dans votre [espace personnel](/info/espace-personnel.md)
qui servira pour tout vos sites webs.
À l'interieur, vous pourrez créer **un dossier par site**.
Par exemple, ici on a appellé le dossier pour les projets Web `www` (pour *World Wide Web*) :

```
📁 www
    📁 mon-site-pro
    📁 mon-site-perso
    📁 blog-famille
```

Ensuite, il faut choisir un {term}`nom de domaine` associé à ce site.
Vous avez deux possibilités :

- [Utiliser un sous domaine de `club1.fr`](#utiliser-un-sous-domaine-de-club1fr) *en mode familial*
- [Louer un nom de domaine](#louer-un-nom-de-domaine-externe) *Pour faire pro !*


### Utiliser un sous domaine de `club1.fr`

Pour faciliter la création de projets et aider à la spontanéité,
l'utilisation de **sous-domaines** de `club1.fr` par les membres est encouragée !

Cela a l'avantage d'être **gratuit**, et de ne nécessiter **aucun entretien**,
contrairement à la [location d'un nom de domaine](#louer-un-nom-de-domaine-externe).
L'inconvénient étant de dépendre de `club1.fr`.
Cela entraîne aussi une **filiation visible avec CLUB1**,
ce qui peut être gênant ou intéressant en fonction des projets.

```{tip}
Il est possible à tout moment de rediriger un **sous-domaine** de `club1.fr`
vers n'importe quel autre domaine de votre choix.
Cela permet par exemple de commencer via cette méthode et plus tard,
de louer un nom de domaine sans casser aucun lien !
```

Pour demander un **sous-domaine** de `club1.fr`,
il faut [contacter l'administrateur système](#gestion),
en spécifiant vers quel dossier dans son espace personnel devra pointer le domaine.

```{warning}
Pensez à vérifier que le **sous-domaine** est disponible avant d'envoyer une demande ! 😉
Il ne doit être composé que de lettres minuscules, chiffres ou tirets `-`.
```


#### Avoir des sous-sous-domaine


C'est effectivement possible de descendre encore un niveau dans la filiation de domaine.
Par exemple, si l'on utilise déjà `yaourt.club1.fr`, on peut aussi demander à créer `fraise.yaourt.club1.fr`.
Cependant, cela nécessite actuellement la création d'un certificat _Let's Encrypt_ supplémentaire par **sous domaine**,
ce qui n'est pas anodin. Donc pour l'instant, mollo sur les sous.sous.domaines 🐌 !


### Louer un nom de domaine externe

Il est possible de louer un nom de domaine chez un {term}`registraire`.
Cela coûte souvent une dizaine d'euros par an, mais cela peut varier en fonction du {term}`TLD` choisi.

```{important}
Il faut distinguer hébergement et location de nom de domaine !
L'hébergement stocke les fichiers d'un site et les publie sur le {term}`web` à une {term}`adresse IP` spécifique,
tandis qu'un {term}`nom de domaine` est une interface plus agréable pour les humains,
sensée pointer vers l'adresse IP d'un serveur.
```

Il est donc parfaitement possible d'avoir un site Web hébergé
sur le serveur CLUB1 sans utiliser un sous domaine de `club1.fr`.

Avant d'acheter votre dom de domaine, prenez le temps d'en [discuter](#gestion) !
Il va y avoir une petite série de réglages à faire
et ça vaut le coup d'en parler pour que tout se passe bien.


### Gestion

Aucune de ces actions n'est automatisée ni accessibles via une interface web.
Il est donc **nécessaire d'en discuter entre humain&middot;e&middot;s** 🍺 !
Cela fait partie de l'aspect artisanal et de l'échelle volontairement humaine de la gestion du serveur.

Pour associer un de vos dossier avec un nom de domaine,
Il faut envoyer un email à <webmaster@club1.fr> indiquant le chemin de votre dossier et le nom de domaine choisi.

Par exemple :

    Bonjour, je souhaiterai que mon dossier "www/mon-site-perso" soit publié à "vacances.club1.fr"


Avancé
------

Quelques techniques liés à l'hébergement de site Web sur le serveur.

### Index des fichiers

Les sites Web sont servi par le serveur HTTP {logiciel}`Apache`.
Il est configuré pour automatiquement générer un _index_ affichant la liste
des fichiers et dossiers qu'il contient.

Pour ne pas afficher cet index, il est possible soit de créer un fichier
`index.html` qui contiendra la page à afficher à la place, soit d'ajouter
un {term}`fichier caché` de configuration Apache `.htaccess` contenant au moins la
ligne suivante :

```apache
Options -Indexes
```

Logiciels
---------

```{logiciel} Nginx
{term}`Serveur` HTTP principalement axé sur les performances.
Chez CLUB1, il est principalement utilisé en tant que "point de terminaison {term}`TLS`"
et "proxy inverse" devant les différents services {term}`Web`,
notamment le serveur {logiciel}`Apache`.
--- [Wikipedia](https://fr.wikipedia.org/wiki/NGINX), [Sources](https://hg.nginx.org/nginx)
```

```{logiciel} Apache
{term}`Serveur` HTTP très populaire, distribué sous license libre.
HTTP étant le {term}`protocole` du {term}`Web` on parle aussi souvent de "serveur Web".

Apache est intéressant pour l'hébergement de pages Web personnelles,
car il peut être configuré en cours d'exécution et par les utilisaturs finaux
grâce aux fichiers `.htaccess`.

Chez CLUB1, le serveur Apache se trouve derrière le "proxy inverse" {logiciel}`Nginx`.
--- [Wikipedia](https://fr.wikipedia.org/wiki/Apache_HTTP_Server),
[Sources](https://github.com/apache/httpd)
```

```{logiciel} PHP-FPM
Gestionnaire de processus {term}`PHP`,
permettant à un {term}`serveur` {term}`Web` d'exécuter du code PHP de manière performante.
Il est aussi capable d'exécuter PHP avec différents utilisateurs.
--- [Sources](https://github.com/php/php-src/tree/master/sapi/fpm)
```
