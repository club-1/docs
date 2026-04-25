Informations générales
======================

Le serveur CLUB1 permet à ses membres d'héberger différents types de projets web.
Mais c'est aussi une communauté de personnes intéressées par les notions d'espaces web,
de libertés et d'exploration du web.

Demandes et Incidents
---------------------

Si vous avez besoin d'aide 🛟, qu'un service semble être indisponible 😵
ou que vous avez une suggestion 💡, n'hésitez pas à nous en faire part !
Vous êtes invités dans un premier temps à explorer le [forum](https://forum.club1.fr) 🔍,
pour vérifier que le sujet n'ait pas déjà été abordé.
Si ce n'est pas le cas, vous pouvez, selon vos préférences :

- **Ouvrir un ticket** en créant un [post sur le forum](https://forum.club1.fr/t/tickets).
- Envoyer un email à <contact@club1.fr>
- En discuter sur [_Matrix_](https://club1.fr/matrix/) via `#bazar:club1.fr`.
  Des salons plus spécifiques sont dédiés au site web et à la doc.
  Ils sont répertoriés au sein de l'espace `#le-club:club1.fr`.

Infos sur le serveur
--------------------

Il vit dans le placard comme _Harry Potter_...

... c'est le serveur.



### Système d'exploitation

Le serveur tourne sur **{term}`Debian` 12** et est mis à jour régulièrement.
Les mises-à-jour de sécurité sont installées automatiquement dans les 24 heures
à l'aide de [_unattended-upgrades_](https://wiki.debian.org/fr/unattended-upgrades)
et les services en dépendant sont ensuite automatiquement redémarrés grâce à
[_needrestart_](https://packages.debian.org/fr/stable/needrestart).

### Logiciels et bibliothèques installés

L'ensemble des logiciels installés sont sous **licence {term}`libre <logiciel libre>`**,
à part pour ceux de la liste suivante, dont il n'existe pas d'alternatives libres :

- BIOS/BMC Supermicro
- Microcode Intel
- Firmware Intel QAT

Un certain nombre de logiciels et de bibliothèques sont déjà installés.
En voici une liste _non exhaustive_ :

    Apache       2.4
    MariaDb     10.11
    PHP          8.2
    Python       3.11
    NodeJs      18.19
    Composer     2.5
    pip         23.0
    npm          9.2
    phpMyAdmin   5.2
    git          2.39
    borg         1.2
    rsync        3.2
    unison       2.52

Si vous souhaitez qu'un logiciel supplémentaire soit installé, merci de
**vérifier** dans un premier temps qu'il n'est pas déjà présent, puis, dans
le cas contraire, de **créer un ticket** comme expliqué [ci-dessus](#demandes-et-incidents).

### Disponibilité

Afin de garantir un certaine disponibilité, le serveur ainsi que les équipements
réseaux sont alimentés par une _UPS_. Cependant, la redondance n'étant pas
présente à tous les niveaux, le serveur pourrait être inaccessible pendant
de courts laps de temps, par exemple lors d'une mise à jour du noyau.
Cela dit, une disponibilité effective **supérieure à 98%** devrait pouvoir être
assurée.

Il est possible de consulter en direct l'état des différents services
sur <https://status.club1.fr>.
Cet outil d'observation des services est hébergé par [RésiLien](https://resilien.fr),
membre du collectif [CHATONS](https://www.chatons.org), sur un serveur situé à Cremeaux.

Comptes des membres
-------------------

### Identifiant

Le nom d'utilisataire doit respecter les règles suivantes :

- une longueur comprise **entre 3 et 17 caractères** (inclus).
- comporter **uniquement** des lettres **minuscules**, des **chiffres** ou des **tirets** (`-`).

Cet identifiant est principalement utilisé en interne pour la connexion aux services
et n'est donc pas spécialement visible depuis l'extérieur.
Il est cependant présent dans l'[adresse email CLUB1](/services/email.md) attribuée par défaut aux membres
et dans les URLs automatiques comme celles des [sites Web statiques](../services/web.md#dossier-static)
et des [dépôts git](/services/git.md).

### Modalités des comptes

Chaque entité (personne ou groupe),
peut héberger autant de projets qu'elle le souhaite dans la limite du raisonnable.

Un compte membre comporte donc :

- de l'espace de stockage SSD
- plus d'espace sur disque dur (sur demande)
- un accès FTP
- un accès SSH (pour les utilisataires avancés)
- des bases de données (MariaDb)
- la création gratuite de sous domaines en .club1.fr (sur demande)
- l'utilisation de noms de domaines loués via des registraires
- un accès au salon {term}`matrix` réservée aux membres pour le suivi et l'assistance aux projets

Pour l'instant, le format choisi est celui de l'adhésion,
avec une cotisation de 35€ à vie.

Contact
-------

<contact@club1.fr>
