Messagerie email
================

Chaque membre dispose d'une adresse email personnelle.
Elle est composée de l'**identifiant**, suivi de `@club1.fr`.
Par exemple, l'adresse de l'utilisateur `michel` est `michel@club1.fr`.

Client Web
----------

Un {term}`client Web` fourni par [Roundcube](https://fr.wikipedia.org/wiki/Roundcube)
est disponible à l'adresse <https://mail.club1.fr>.
Il permet de gérer et d'envoyer des emails, mais aussi d'accéder aux calendriers
et carnets d'adresses CLUB1 synchronisés avec [WebDAV](webdav.md).

Stockage des données
--------------------

Toutes les données relatives aux emails sont stockées sous la forme de fichiers
dans le dossier `mail` de votre [*espace personnel*](/info/espace-personnel.md).
Ce dossier respecte le standard [Maildir](https://fr.wikipedia.org/wiki/Maildir),
il est donc possible d'y accéder directement à partir d'un {term}`client` email supportant ce standard,
par exemple après avoir fait une sauvegarde du dossier sur un ordinateur personnel.

Sur le serveur, le client en {term}`CLI` [Mutt](https://fr.wikipedia.org/wiki/Mutt)
est préconfiguré pour consulter ce dossier par défaut.
Pour l'utiliser, il faut commencer par se connecter en [SSH](ssh.md) au serveur CLUB1
puis lancer la commande suivante&nbsp;:

    mutt

Informations de connexion
-------------------------

La connexion d'un client email à une adresse CLUB1 nécessite de configurer plusieurs serveurs.

### Serveur d'envoi (SMTP)

| champ            | valeur                             |
| ---------------- | ---------------------------------- |
| hôte             | `mail.club1.fr` ou `smtp.club1.fr` |
| port             | `465` (par défaut)                 |
| chiffrement      | `SSL/TSL` (Implicite)              |

### Serveur de réception (IMAP)

| champ            | valeur                             |
| ---------------- | ---------------------------------- |
| hôte             | `mail.club1.fr` ou `imap.club1.fr` |
| port             | `993` (par défaut)                 |
| chiffrement      | `SSL/TSL` (Implicite)              |
