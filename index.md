Documentation de l'hébergement CLUB1
====================================

L'hébergement CLUB1 est basé sur la mise à disposition d'un *espace personnel*.
Il s'agit d'un espace de stockage sur le serveur, accessible via un certain
nombre de protocoles, fournissant différents services.


```{toctree}
---
maxdepth: 2
caption: Services
---
services/ftps
services/ssh
services/web
services/mysql
```

# Demandes et Incidents

Pour toute demande ou incident, veuillez [créer un ticket (_issue_)][github-issue]
sur GitHub (vous devrez pour celà créer un compte), en choisissant entre demande
(_request_) ou incident (_problem_) en fonction de la nature du ticket.
Si il s'agit d'une demande impersonnelle, merci de **vérifier** qu'il n'éxiste pas
déjà une demande similaire à l'aide de la barre de recherche.


# Infos sur le serveur

## Matériel et infrastructure

Le serveur est localisé en France à Pantin. Il est relié à internet par fibre
optique avec un [débit montant de 200Mb/s en moyenne][nperf].

## Système d'exploitation

Le serveur tourne sur la dernière version **LTS d'_ubuntu server_ (20.04)** et
est mis à jour régulièrement.

## Logiciels et bibliothèques installés

Un certain nombre de logiciels et de bibliothèques sont déjà installés.
En voici une liste _non-exhaustive_ :

-   Apache 2.4
-   MariaDb 10.5
-   PHP 7.4
-   Python 3.8
-   NodeJs 10.19
-   Composer 1.10
-   pip 20.0
-   npm 7.5.2
-   phpMyAdmin 4.9
-   git 2.25
-   ...

Si vous souhaitez qu'un logiciel supplémentaire soit installé, merci de
**vérifier** dans un premier temps qu'il n'est pas déjà présent, puis, dans
le cas contraire, de **créer un ticket** comme expliqué [ci-dessus][demandes].

## Disponibilité

Afin de garantir un certaine disponibilité, le serveur ainsi que les équipements
réseaux sont alimentés par une _UPS_. Cependant, la redondance n'étant pas
présente à tous les niveaux, le serveur pourrait être inaccessible pendant
de courts laps de temps, par exemple lors d'une mise à jour du noyau.
Cela dit, une disponibilité effective **supérieure à 90%** devrait pouvoir être
assurée.

# Politique et vie privée

Aucune des données que vous stockez dans votre espace personnel de sera
divulguée ni utilisée à des fins lucratives et ce même sous la menace.

[github-issue]: https://github.com/club-1/hosting/issues
[nperf]: https://www.nperf.com/r/338260996-nDOmVdkc
[demandes]: #demandes-et-incidents
