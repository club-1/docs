Explorateur de fichiers Web *Drive*
===================================

Le _**Drive**_ CLUB1 est un explorateur de fichiers utilisable à travers un navigateur {term}`Web`.
Il permet d'accéder à son **espace personnel** sans avoir besoin d'installer ou de configurer une application native.
Il est donc très utile lorsque l'on n'est pas sur son ordinateur personnel.

![capture d'écran WebDav drive](drive/webdav_drive.png)

L'adresse de ce {term}`client Web` est <https://drive.club1.fr>.

```{note}
Les {term}`fichiers cachés <fichier caché>` n'apparraissent pas dans cette interface.
Pour y avoir accès,
il vaut mieux se tourner vers le service [FTP](ftp.md), [WebDAV](webdav.md) ou [SSH](ssh.md).
```

Homemade is best !
------------------

Il s'agit d'une application développée par et pour CLUB1
dont le [code source](https://github.com/club-1/webdav-drive) se trouve sur {term}`GitHub`.
Cependant, elle a été pensée de manière générique, afin qu'elle puisse être utilisée en dehors de l'infrastructure de CLUB1.
Elle utilise un {term}`serveur` WebDAV standard comme source de données,
dont [CLUB1 propose un accès](webdav.md).

Logiciels
---------

```{logiciel} WebDAV Drive
Explorateur de fichiers {term}`Web` basé sur un {term}`serveur` {term}`WebDAV`.
Chez CLUB1, ce service accessible via {logiciel}`Nginx` en tant que site statique,
et communique avec le serveur {logiciel}`webdav-server`.
--- [Sources](https://github.com/club-1/webdav-drive)
```
