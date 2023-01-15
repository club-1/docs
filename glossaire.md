(glossary)=

Glossaire
=========

````{glossary}
---
sorted:
---

adresse IP
   Numéro d'identification d'un ordinateur relié à un {term}`réseau informatique`.

   Le protocole IP (créé à l'origine pour {term}`Internet`) permet d'acheminer des données entre un ordinateur source et sa destination.
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
   Elle s'utilise par l'intermédiaire d'une fenêtre de terminal.
   La CLI est très intéressante car elle peut aussi bien être utilisée par des humains que par des logiciels. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)

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
   utilisant le logiciel de gestion de versions {term}`Git`.

   ```{warning}
   Contrairement à la plupart des projets que l'on peut y trouver,
   Github n'est ni **libre**, ni **open source** et appartient à Microsoft.
   ```

   --- [Wikipedia](https://fr.wikipedia.org/wiki/GitHub)

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

PHP
   (_PHP Hypertext Preprocessor_) Langage de programmation de haut niveau,
   principalement utilisé pour produire des pages {term}`Web` de manière dynamique
   en générant du code {term}`HTML`.
   Son acronyme signifiait à l'origine "_Personnal Home Page_"
   et c'est justement le langage que CLUB1 met en avant pour la création de [sites Web dynamiques](./services/web.md#sites-web-dynamiques).
   --- [Wikipedia](https://fr.wikipedia.org/wiki/PHP)

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
