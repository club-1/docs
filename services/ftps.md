FTPS (File Transfer Protocol Secure)
====================================

Bien que [ssh](ssh) puisse aussi être utilisé dans ce but, FTPS peut être
utile lors du tranfert d'un grand nombre de fichiers depuis et vers le
serveur CLUB1.

Le compte FTP est constitué d'un **identifiant** et d'un **mot de passe**,
il permet d'accéder à votre *espace personnel* grâce à des logiciels comme
[FileZilla][filezilla] (attention l'installeur windows comprend des bundlewares).

Sécurité
--------

Le serveur FTP est configuré pour ne recevoir que des connexions chiffrés
avec TLS pour éviter d'envoyer des mots de passe en clair. Cette fonctionnalité
s'appelle [FTPS (FTP avec TLS implicite)][wiki-ftps].

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


[filezilla]: https://filezilla-project.org/download.php?type=client
[wiki-ftps]: https://fr.wikipedia.org/wiki/File_Transfer_Protocol_Secure#FTP_avec_chiffrement_implicite
