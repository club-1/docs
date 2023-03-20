Hébergement de sites Web
========================

L'hébergement de site web est historiquement le **premier service** mis à la disposition des membres de CLUB1.

```{important}
La liberté d'expérimenter est au coeur des principes de CLUB1 :
Un compte membre CLUB1 **ne limite pas à un seul site web** !
Il n'y a pas de limite au nombre de projet web à héberger tant que ça ne sature pas le serveur 😄.
```



Types de sites
--------------


Il existe deux grands types de sites {term}`Web` : les sites _statiques_,
constitués de fichiers dont le contenu ne change pas tant qu'ils n'ont pas
été modifiés et les sites _dynamiques_, dont les fichiers sont exécutés et
peuvent ainsi produire des résultats différents.

### Sites Web _statiques_

Ce type de site web est constitué uniquement de fichiers que le serveur va servir en fonction des requêtes.
Cela ne demande presque aucun "travail" au processeur car il n'y a pas de calcul à effectuer.
Les sites statiques sont une voie intéressante pour qui cherche à proposer des sites plus sobres énergétiquement.

Pour créer un site web statique, on peut écrire soi-même du code HTML,
associé avec des images, sons ou vidéos.
C'est la façon la plus artisanale de faire un site web.
Elle garantie des styles uniques et originaux et est très efficace pour apprendre comment fonctionne le web.

```{tip}
- Pour apprendre à coder en HTML et CSS, on recommande souvent le
[tutoriel OpenClassromm](https://openclassrooms.com/fr/courses/1603881-creez-votre-site-web-avec-html5-et-css3)
de Mathieu Nebra.
- Le site [Gossip's Web](https://gossipsweb.net/) (en anglais), recueille des sites "fait à la mains".
```

Mais cela peut devenir complexe lorsque l'on a beaucoup de contenu à gérer.
Pour ça il est conseillé de se tourner vers les [générateurs de sites statiques](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_de_site_statique)
Ces outils peuvent générer les fichiers HTML d'un site, par exemple à partir de fichiers {term}`Markdown`,
sur votre ordinateur personnel.
A chaque fois qu'une mise à jour est nécessaire, il n'y a qu'à relancer le processus et
copier les fichiers ainsi créés sur le serveur.

#### Dossier `static/`

L'**espace personnel** dispose d'un dossier spécial `static/` à sa racine.
Tous les fichiers et dossiers rangés dedans seront automatiquement publiés
sur le {term}`Web` à l'adresse `https://static.club1.fr`, par exemple :

[`https://static.club1.fr/nicolas/test.html`](https://static.club1.fr/nicolas/test.html)
--> `/home/nicolas/static/test.html`

Ce dossier est servi par le serveur HTTP {logiciel}`Apache`.
Il est configuré pour automatiquement générer un _index_ affichant la liste
des fichiers et dossiers qu'il contient.

Pour ne pas afficher cet index, il est possible soit de créer un fichier
`index.html` qui contiendra la page à afficher à la place, soit d'ajouter
un {term}`fichier caché` de configuration Apache `.htaccess` contenant au moins la
ligne suivante.

```apache
Options -Indexes
```

```{admonition} Voir aussi
Le tutoriel "[](/tutos/mes-premiers-pas-sur-le-web.md)" pour apprendre à faire son premier site web avec le dossier `/static`.
```

### Sites Web _dynamiques_

Ce type de site web utilise du code logique qui s'execute sur le serveur.
Cela peut être via un [C.M.S](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_de_contenu).
Et peut notamment nécessiter l'utilisation de [bases de données SQL](sql.md)
Pour ces sites web, il faut obligatoirement passer par la création d'un [nom de domaine](#noms-de-domaines).
Car il n'y a pas de dossier automatique préconfiguré.


Noms de domaines
----------------

La question du {term}`nom de domaine` est un enjeu fort du {term}`Web`.

```{important}
Il faut distinguer hébergement et location de nom de domaine !
L'hébergement stocke les fichiers d'un site et les publie sur le {term}`web` à une {term}`adresse IP` spécifique,
tandis qu'un {term}`nom de domaine` est une interface plus agréable pour les humains,
sensée pointer vers l'adresse IP d'un serveur.
```

Eh oui ! Ce sont deux notions différentes, même si une grosse partie des hébergeurs mainstream
vont souvent proposer la location du nom de domaine
en même temps que la location d'un espace pour les fichiers (hébergement).



```{glossary}
nom de domaine
   Identifiant de domaine {term}`Internet`,
   facile à lire et à retenir par un être humain.

   > Par exemple : `club1.fr`, `impots.gouv.fr`, et `fr` sont des noms de domaine.

   Un domaine permet d'associer des informations à un nom.
   Parmi ces informations, la plus importante est l'{term}`adresse IP` de l'ordinateur associé à ce domaine.
   Un nom de domaine est donc souvent utilisé comme un {term}`alias` pour une adresse IP.
   
   En plus de ces informations, un domaine peut également avoir des sous domaines.

registraire
   Registraire de {term}`nom de domaine`.
   Société ou une association gérant la réservation de nom de domaine {term}`Internet`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Registraire_de_nom_de_domaine)

TLD
   Top level Domain
   {term}`Nom de domaine` de premier niveau.
   Par exemple `fr`, `com` ou `org` sont des TLD.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Domaine_de_premier_niveau)
```

Comme le dit *Stéphane Bortzmeyer* dans [son article sur son blog](https://www.bortzmeyer.org/parties-nom-domaine.html) :

> On entend parfois le terme de « sous-domaine ».
> Malheureusement, il est souvent utilisé en supposant qu'il y a des domaines
> qui sont des sous-domaines et d'autres qui seraient des « vrais » domaines.
> Mais ce n'est pas le cas. Tous les domaines sont des sous-domaines d'un autre
> (à part le cas particulier de la racine, le début des domaines).
> Ainsi, `signal.eu.org` est un sous-domaine de `eu.org`, lui-même un sous-domaine de `org`,
> lui-même sous-domaine de la racine.

### Utiliser un sous domaine de `club1.fr`

Pour faciliter la création de projets et aider à la spontanéité,
l'utilisation de **sous-domaines** de `club1.fr` par les membres est encouragée !

Cela a l'avantage d'être gratuit, et de ne nécessiter aucun entretien,
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
Cela coûte souvent une dizaine d'euros par an mais cela peut varier en fonction du {term}`TLD` choisi.

Nous recommandons [Gandi.net](https://www.gandi.net/fr/domain), pour son soutient à divers projets libres.

Avant d'acheter votre dom de domaine, prenez le temps d'en [discuter](#gestion) !
Il va y avoir une petite série de réglages à faire
et ça vaut le coup d'en parler pour que tout se passe bien.


Gestion
-------

Aucune de ces actions ne sont automatisés ni accessibles via une interface web.
Il est donc **nécessaire d'en discuter entre humain&middot;e&middot;s** 🍺 !
Cela fait partie de l'aspect artisanal et de l'échelle volontairement humaine de la gestion du serveur.

Pour soulager la tâche,
des [scripts](https://github.com/club-1/hosting) sont là pour faciliter la mise en place technique.

C'est _Nicolas_ qu'il faut contacter pour l'association des domaines avec vos dossiers de sites.

Il est possible de le joindre :

- par email : <webmaster@club1.fr>
- par {term}`matrix` : `@n-peugnet:club1.fr`



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
