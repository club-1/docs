(glossary)=

Glossaire
=========

````{glossary}
---
sorted:
---

adresse IP
   Numéro d'identification d'un ordinateur relié à un {term}`réseau informatique`.

   Le {term}`protocole` IP (créé à l'origine pour {term}`Internet`)
   permet d'acheminer des données entre un ordinateur source et sa destination.
   Il a besoin pour cela d'adresses IP afin d'identifier ces deux ordinateurs.

   Actuellement, deux version d'adresses IP sont utilisées :
   La version 4 qui s'écrit sous la forme de nombres séparés par des points
   (ex : `87.91.4.64` pour le serveur de CLUB1).
   Et la version 6 qui utilise des nombre beaucoup plus grands et qui s'écrit en hexadécimal
   (ex : `2001:861:38c4:18a0::3` pour le serveur de CLUB1).
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Adresse_IP)

alias
    Pseudonyme, nom de substitution. Les alias permettent de donner plusieurs noms à la même entité.
    C'est un concept fréquemment utilisé en informatique.
    On parle par exemple d'alias lorsqu'on fait pointer plusieurs adresses email vers la même boîte de reception,
    ou lorsqu'on définit un nouveau nom pour une commande.
    --- [Wiktionnaire](https://fr.wiktionary.org/wiki/alias)

API
   De l'anglais _Application Programming Interface_.
   Interface destinée à être utilisée non pas par un être humain mais par un logiciel.
   Elle est en général composée d'un ensemble de fonctions qu'un logiciel peut utiliser à distance. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Interface_de_programmation)

CLI
   De L'anglais _Command Line Interface_.
   Interface en ligne de commande, basée sur un affichage textuel.
   Elle s'utilise par l'intermédiaire d'une fenêtre de {term}`terminal`.
   La CLI est très intéressante car elle peut aussi bien être utilisée par des humain&middot;e&middot;s que par des logiciels.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)

client
   Logiciel permettant de se connecter à un {term}`serveur`.
   Il est en général doté d'une interface graphique, destinée à être utilisée directement par un humain. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Client_(informatique))

client Web
   {term}`Client` accessible via le {term}`Web` et ainsi exécuté par un Navigateur web.

fichier caché
dossier caché
   Dans la plupart des systèmes d'exploitation,
   il est possible de cacher des fichiers ou des dossiers.
   Cela sert souvent à masquer des paramètres peu utiles au quotidien.
   Dans un système UNIX, les fichiers cachés commencent par un point `.`.

   Dans les explorateurs de fichiers ils peuvent être masqués par défaut.
   Il est possible d'activer leur affichage si besoin,
   souvent avec le raccourci clavier {kbd}`Ctrl` + {kbd}`H`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Fichier_et_r%C3%A9pertoire_cach%C3%A9#Sous_Unix_et_Linux)

GitHub
   Service web d'hébergement et de gestion de développement de logiciels,
   utilisant le logiciel de gestion de versions {logiciel}`Git`.

   ```{warning}
   Contrairement à la plupart des projets que l'on peut y trouver,
   Github n'est ni **libre**, ni **open source** et appartient à Microsoft.
   ```

   --- [Wikipedia](https://fr.wikipedia.org/wiki/GitHub)

groupe
   Les groupes servent à rassembler des utilisateurs afin de leur attribuer des droits communs.
   Un utilisateur UNIX appartient à un ou plusieurs groupes.

   ```{tip}
   Il est possible de savoir qui est membre d'un groupe sur le serveur
   depuis un accès {term}`SSH` avec la commande suivante :

       members GROUP

   En remplaçant `GROUP` par le groupe voulu. Exemple : `members sudo` ou `members home`.
   ```

   --- [Wikipedia](https://fr.wikipedia.org/wiki/Groupe_(Unix))

HTML
   (_Hypertext Markup Language_) Langage de balisage conçu pour représenter les pages {term}`Web`. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Hypertext_Markup_Language),
   [MDN web docs](https://developer.mozilla.org/fr/docs/Web/HTML)

instance
   Copie d'un logiciel ou d'un objet informatique ayant sa propre existence et son propre état.

   On parle par exemple d'instance à chaque fois qu'on exécute un logiciel avec des données différentes.
   Sur le serveur CLUB1, il y a notamment plusieurs instances de {term}`PHP` : au moins une pour chaque membre.
   --- [Wiktionnaire](https://fr.wiktionary.org/wiki/instance)

Internet
   {term}`Réseau informatique` mondial accessible au public.
   Internet est en réalité l'interconnexion d'un ensemble de réseaux à travers le monde.
   Comme son nom l'indique, "inter" "net" = "entre les réseaux".
   Il s'agit donc d'un "réseau de réseaux". ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Internet)

log
   Designe à l'origine le [journal de bord (logbook)](https://fr.wikipedia.org/wiki/Livre_de_bord) d'un navire.
   En informatique il s'agit d'un journal contenant un historique d'événements,
   généralement sous la forme de ficher en texte brut.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Historique_(informatique))

Markdown
   Langage de balisage léger permettant de mettre en forme un document.
   Les documents rédigés en Markdown ont généralement pour but
   d'être convertis en {term}`HTML`, afin d'en faire une page {term}`Web`.
   Son principal avantage par rapport au HTML est sa syntaxe épurée,
   ce qui le rend plus agréable à lire et à écrire pour un humain. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Markdown)

nom de domaine
   Identifiant de domaine {term}`Internet`,
   facile à lire et à retenir par un être humain.

   > Par exemple : `club1.fr`, `impots.gouv.fr`, et `fr` sont des noms de domaine.

   Un domaine permet d'associer des informations à un nom.
   Parmi ces informations, la plus importante est l'{term}`adresse IP` de l'ordinateur associé à ce domaine.
   Un nom de domaine est donc souvent utilisé comme un {term}`alias` pour une adresse IP.
   
   En plus de ces informations, un domaine peut également avoir des sous domaines.


PHP
   (_PHP Hypertext Preprocessor_) Langage de programmation de haut niveau,
   principalement utilisé pour produire des pages {term}`Web` de manière dynamique
   en générant du code {term}`HTML`.
   Son acronyme signifiait à l'origine "_Personnal Home Page_"
   et c'est justement le langage que CLUB1 met en avant pour la création de [sites Web dynamiques](./services/web.md#sites-web-dynamiques).
   --- [Wikipedia](https://fr.wikipedia.org/wiki/PHP)

protocole
   Dans le contexte de l'informatique,
   un protocole est un ensemble de règles qui régissent les échanges de données
   ou le comportement collectif de processus ou d'ordinateurs en réseaux.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Protocole_informatique)

registraire
   Registraire de {term}`nom de domaine`.
   Société ou une association gérant la réservation de nom de domaine {term}`Internet`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Registraire_de_nom_de_domaine)

réseau informatique
   Ensemble d'ordinateurs reliés entre eux pour leur permettre d'échanger des données. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/R%C3%A9seau_informatique)

serveur
   Logiciel chargé de fournir un service. C'est lui qui détient les données
   et qui répond aux demandes d'un {term}`client`.
   Souvent, les serveurs et les clients sont installés sur des ordinateurs différents.
   Par extension, on appelle ainsi un "serveur" l'ordinateur sur lequel les
   serveurs sont installés (ex : le serveur CLUB1). ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Serveur_informatique)

site dynamyque
   Site {term}`Web` dont l'affichage peut varier "de lui même", d'où le nom "dynamique"
   (le distinguant ainsi du {term}`site statique`).
   Il contient du code qui va être "executé" pour générer du {term}`HTML`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Page_web_dynamique)

site statique
   Site {term}`Web` constitués de fichiers {term}`HTML` dont le contenu ne change pas tant qu'ils n'ont pas été édités.
   Ils peuvent être conçus "à la main" ou à l'aide d'un "générateur de site statique".
   Les sites statiques sont une voie intéressante
   pour qui cherche à proposer des sites plus sobres énergétiquement.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Page_web_statique)

terminal
   En informatique, un terminal était à l'origine un appareil constitué d'un moniteur et d'un clavier,
   permettant à un&middot;e humain&middot;e d'interagir avec un ordinateur partagé distant.
   Il offrait une interface textuelle, permettant d'entrer des commandes et d'en lire le résultat.

   De nos jours, on utilise souvent le mot "terminal" comme raccourci pour désigner un "émulateur de terminal".
   Il s'agit d'un logiciel recréant l'interface en ligne de commande ({term}`CLI`) de ce materiel.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Terminal_(informatique))

TLD
   Top level Domain
   {term}`Nom de domaine` de premier niveau.
   Par exemple `fr`, `com` ou `org` sont des TLD.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Domaine_de_premier_niveau)

TLS
   (_Transport Layer Security_) Protocole permettant de sécuriser les échanges
   réalisés dans un {term}`réseau informatique`.
   L'une de ses fonctionnalités principale est de chiffrer l'ensemble des données échangées
   entre le {term}`client` et le {term}`serveur`,
   afin que personne d'autre ne puisse en lire le contenu. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Transport_Layer_Security)

Web
   L'un des services les plus connus d'{term}`Internet`.
   Son nom complet est "World Wide Web" (aussi abrégé "www").
   Il permet de publier des documents et de les relier entre eux à l'aide de liens hypertexte.

   Une "page Web" est généralement constituée d'un document dont le contenu est rédigé en {term}`HTML`
   et peut inclure d'autre ressources comme des images ou des "feuilles de style".
   On appelle "Navigateur Web" le {term}`client` utilisé pour y accéder. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/World_Wide_Web)
````
