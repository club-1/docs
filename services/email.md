Messagerie email
================

Chaque membre dispose d'une adresse email personnelle.
Elle est composée de l'**identifiant**, suivi de `@club1.fr`.
Par exemple, l'adresse de l'utilisateur `michel` est `michel@club1.fr`.

Un {term}`client Web` fourni par [Roundcube](https://fr.wikipedia.org/wiki/Roundcube)
est disponible à l'adresse <https://mail.club1.fr>.

Informations de connexion
-------------------------

La connexion d'un client email à une adresse CLUB1 nécessite de configurer plusieurs serveurs.

### Serveur d'envoi (SMTP)

| champ            | valeur                |
| ---------------- | --------------------- |
| hôte             | `mail.club1.fr`       |
| port             | `465` (par défaut)    |
| chiffrement      | `SSL/TSL` (Implicite) |

### Serveur de réception (IMAP)

| champ            | valeur                |
| ---------------- | --------------------- |
| hôte             | `mail.club1.fr`       |
| port             | `993` (par défaut)    |
| chiffrement      | `SSL/TSL` (Implicite) |
