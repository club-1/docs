Synchro de fichiers, contacts et calendriers WebDAV
===================================================

```{glossary}
WebDAV
   Protocole qui étend les fonctionnalités du {term}`Web`.
   Il y ajoute des possibilités de modifications et de synchronisation de fichiers.
   Son utilisation première est donc similaire à un système de fichier distant
   et il est possible de l'utiliser via un explorateur de fichier compatible
   pour éditer les fichiers de son **espace personnel** comme si ils étaient présents en local.
```

Plusieurs extensions de WebDAV apportent des fonctionnalités encore un peu plus
spécifiques :

```{glossary}
CardDAV
   Extension {term}`WebDAV` pour synchroniser des {index}`carnets d'adresses` de contacts.

CalDAV
   Extension {term}`WebDAV` pour synchroniser des {index}`calendriers`.
```

Une interface {term}`Web` de _debug_ est disponible à l'adresse <https://webdav.club1.fr>.
Elle permet de tester la connexion et de prévisualiser certaines informations.

Carnets d'adresses et calendriers
----------------------------------

Le {term}`client Web` utilisé pour les [email](email.md) (<https://mail.club1.fr>)
permet aussi d'accéder aux carnets d'adresses et calendriers WebDAV.
Depuis cette interface, il est possible de consulter et éditer ses contacts et calendriers CLUB1.

Chaque membre dispose d'un carnet d'adresses et d'un calendrier pré-existants,
tous les deux appelés `Default`, mais il est possible d'en créer d'autres.


Tutoriels
---------

Ci-dessous, une petite liste de tutoriels pour profiter au mieux du service WebDAV de CLUB1.

- [](/tutos/webdav-android.md)
- [](/tutos/caldav-mac.md)

Logiciels
---------

```{glossary}
SabreDAV
   Bibliothèque PHP fournissant un {term}`serveur` {term}`WebDAV` très complet.
   --- [Site Web](https://sabre.io/), [Sources](https://github.com/sabre-io/dav)
```
