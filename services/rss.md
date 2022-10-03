Agrégateur de flux RSS
======================

```{glossary}
RSS
   (_Really Simple Syndication_) Format de données standardisé qui permet la consultation d'un site
   non pas par un humain mais par un logiciel.
   Il s'agit donc d'une forme d'{term}`API`.
   Les flux RSS sont des fichiers qui contiennent les derniers articles ou actualités publiées.
   Ils sont souvent utilisés par les sites d'actualité et les blogs.
   
   Le logiciel permettant de consulter ces flux est appelé {term}`agrégateur de flux`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/RSS)

Agrégateur de flux
   Logiciel permettant de consulter les flux {term}`RSS`.
   Son but est d'agréger les nouveautés de différents sites dans un fil unique.
   Il permet d'éviter de regarder manuellement et un par un les sites dont on veut connaître les nouveaux contenus.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Agr%C3%A9gateur#Dans_le_domaine_informatique)
```

Un agrégateur de flux RSS est fourni par {term}`Tiny Tiny RSS`.
Il est accessible à travers le {term}`client Web` intégré se trouvant à l'adresse
<https://rss.club1.fr>, mais il est également possible d'y connecter un client
natif.

Se connecter avec un client natif
---------------------------------

Avant de pouvoir connecter un client natif, il faut activer l'{term}`API` dans
les paramètres du {term}`client Web`. Cliquer sur le menu (icône avec les trois
barres en haut à droite) --> `Configuration...` --> Onglet `Configuration`
--> Section `Général` --> Cocher la case `Activer l'API`.

Dans le client natif choisi, il faudra renseigner comme URL du serveur
`https://rss.club1.fr`.

Tutoriels
---------

Ci-dessous, une petite liste de tutoriels pour profiter au mieux du service RSS de CLUB1.

- [](/tutos/flux-rss.md)

Logiciels
---------

```{glossary}
Tiny Tiny RSS
   {term}`Agrégateur de flux` supportant {term}`RSS` et ATOM.
   Il fournit un {term}`serveur` se chargeant de relever régulièrement les flux,
   un {term}`client Web` pour les consulter dans un navigateur
   et une {term}`API` pour s'y connecter avec une application native.
   Il est souvent abrégé TTRSS.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Tiny_Tiny_RSS),
   [Sources](https://git.tt-rss.org/fox/tt-rss.git)
```
