Transfert de fichiers FTPS
==========================

```{glossary}
FTP
   (_File Transfer Protocol_) Protocole de transfert de fichiers.
   Il permet de copier des fichiers d'un ordinateur à un autre
   à travers un {term}`réseau informatique`,
   ou encore de déplacer ou supprimer des fichiers sur un ordinateur distant.
   Le serveur CLUB1 utilise la variante sécurisée de ce protocole : {term}`FTPS`. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/File_Transfer_Protocol)

FTPS
   (_File Transfer Protocol Secure_)
   Variante sécurisée de {term}`FTP`, basée sur {term}`TLS`.
   L'ensemble des échanges de données réalisé est donc chiffré.
   FTPS propose deux modes de fonctionnement : _explicite_ et _implicite_.
   Le mode _implicite_ est plus sécurisé car la connexion est chiffrée
   dès le premier échange. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/File_Transfer_Protocol_Secure)
```

Bien que [SSH](ssh.md) puisse aussi être utilisé dans ce but, {term}`FTPS`
peut être utile lors du transfert d'un grand nombre de fichiers
depuis et vers le serveur CLUB1.

Le protocole FTP permet d'accéder à votre **espace personnel** grâce à des logiciels comme
[FileZilla](https://filezilla-project.org/download.php?type=client) (attention l'installeur windows comprend des bundlewares).

Sécurité
--------

Le serveur FTP est configuré pour ne recevoir que des connexions chiffrés
avec TLS pour éviter d'envoyer des mots de passe en clair. Cette fonctionnalité
s'appelle [FTPS (FTP avec TLS implicite)](https://fr.wikipedia.org/wiki/File_Transfer_Protocol_Secure#FTP_avec_chiffrement_implicite).

Un certificat est utilisé pour prouver l'authenticité de la clé du serveur.
Si un message demande d'approuver le certificat lors de la connexion, il est
important de vérifier qu'il est bien délivré par `Let's Encrypt`.

Informations de connexion
-------------------------

| champ            | valeur             |
|------------------|--------------------|
| hôte             | `club1.fr`         |
| port             | `990` (par défaut) |
| chiffrement      | TLS Implicite      |
| authentification | Normale            |

Logiciels
---------

```{glossary}
ProFTPD
   {term}`Serveur` {term}`FTP`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/ProFTPd),
   [Sources](https://github.com/proftpd/proftpd)
```
