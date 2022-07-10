Informations générales
======================

Le serveur Club1 permet à ses membres d'héberger différents types de projets web. 
Mais c'est aussi une communauté de personne intéressées par les notions d'espaces web,
de libertés et d'exploration du web.

Demandes et Incidents
---------------------

Pour toute demande ou incident, veuillez [créer un ticket (_issue_)](https://github.com/club-1/hosting/issues)
sur {term}`GitHub` (vous devrez pour cela créer un compte), en choisissant entre demande
(_request_) ou incident (_problem_) en fonction de la nature du ticket.
Si il s'agit d'une demande impersonnelle, merci de **vérifier** qu'il n'éxiste pas
déjà une demande similaire à l'aide de la barre de recherche.


Infos sur le serveur
--------------------

Il vit dans le placard comme _Harry Potter_...

c'est le serveur.

### Matériel et infrastructure

Le serveur est localisé en France à Pantin. Il est relié à internet par fibre
optique avec des débits moyens de [200Mb/s en montant et 500Mb/s en descendant](https://www.nperf.com/fr/r/338260996-nDOmVdkc).

### Caractéristiques techniques

- Intel ATOM C3000
- 16 Go DDR4 ECC
- Stockage :
  - SSD Système 300 Go
  - SSD Users 1To



### Système d'exploitation

Le serveur tourne sur **Ubuntu 20.04 (LTS)** et est mis à jour régulièrement.
Les mises-à-jour de sécurité sont installées automatiquement dans les 24 heures
à l'aide de [_unattended-upgrades_](https://wiki.debian.org/fr/unattended-upgrades)
et les services en dépendant sont ensuite automatiquement redémarés grâce à
[_needrestart_](https://packages.debian.org/fr/stable/needrestart).

### Logiciels et bibliothèques installés

Un certain nombre de logiciels et de bibliothèques sont déjà installés.
En voici une liste _non exhaustive_ :

    Apache       2.4
    MariaDb     10.5
    PHP          7.4
    Python       3.8
    NodeJs      10.19
    Composer     1.10
    pip         20.0
    npm          7.5
    phpMyAdmin   4.9
    git          2.25
    borg         1.1
    rsync        3.1
    unison       2.48

Si vous souhaitez qu'un logiciel supplémentaire soit installé, merci de
**vérifier** dans un premier temps qu'il n'est pas déjà présent, puis, dans
le cas contraire, de **créer un ticket** comme expliqué [ci-dessus](#demandes-et-incidents).

### Disponibilité

Afin de garantir un certaine disponibilité, le serveur ainsi que les équipements
réseaux sont alimentés par une _UPS_. Cependant, la redondance n'étant pas
présente à tous les niveaux, le serveur pourrait être inaccessible pendant
de courts laps de temps, par exemple lors d'une mise à jour du noyau.
Cela dit, une disponibilité effective **supérieure à 90%** devrait pouvoir être
assurée.

### Sauvegardes

```{raw} html
<img alt="backup status" src="https://healthchecks.io/badge/c792e044-dd83-4b85-a695-240eed/fy2eY73W-2/backup.svg" />
```

Le système et les données utilisateur sont sauvegardées une fois par jour à 5h.
Elles sont stoquées de manière dédupliquée et chiffrée à plusieurs endroits dont un dépôt off-site.

L'article [Sauvegardes](https://club1.fr/backups/) apporte plus d'informations sur ce système.


Comptes des membres
-------------------

### Identifiant
Le nom d'utilisateur doit respecter le regex `^[a-z\-]{3,16}$`.
Il est possible de vérifier qu'un nom le respecte à l'aide de [regex101](https://regex101.com/r/AilLZw/1).

Cet identifiant est principalement utilisé en interne pour la connexion aux services
et n'est donc pas spécialement visible depuis l'extérieur.
Il est cependant présent dans l'[adresse email CLUB1](/services/email.md) attribuée par défaut aux membres
et dans les URLs automatiques commes celles des [sites statiques](../services/web.md#sites-statiques)
et des [dépôts git](/services/git.md).

### Modalités des comptes

Chaque entité (personne ou groupe), 
peut héberger autant de projets qu'elle le souhaite dans la limite du raisonnable.

Un compte membre comporte donc :

- de l'espace de stockage SSD
- plus d'espace sur disque dur (sur demande)
- un accès FTP
- un accès SSH (pour les utilisateurs avancés)
- des bases de données (MariaDb)
- la création gratuite de sous domaines en .club1.fr (sur demande)
- l'utilisation de noms de domaines loué vias des registraires
- un accès à la room matrix réservée aux membres pour le suivi et l'assistance aux projets

Pour l'instant, le format choisi est celui de l'adhésion, 
avec une cotisation de 35€ à vie.

Politique et vie privée
-----------------------

Aucune des données que vous stockez dans votre espace personnel de sera
divulguée ni utilisée à des fins lucratives et ce même sous la menace.

Contact
-------

<contact@club1.fr>
