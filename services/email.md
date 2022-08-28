Messagerie email
================

Chaque membre dispose d'une adresse email personnelle.
Elle est composée de l'**identifiant**, suivi de `@club1.fr`.
Par exemple, l'adresse de l'utilisateur `michel` est `michel@club1.fr`.

Client Web
----------

Un {term}`client Web` fourni par {term}`Roundcube`
est disponible à l'adresse <https://mail.club1.fr>.
Il permet de gérer et d'envoyer des emails, mais aussi d'accéder aux {index}`calendriers`
et {index}`carnets d'adresses` CLUB1 synchronisés avec [WebDAV](webdav.md).

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
puis lancer la commande suivante :

    mutt

Détails divers
--------------

Quelques informations supplémentaires à propos de certains détails du service email de CLUB1.

```{admonition} Voir aussi
L'article du journal [Le(s) serveur(s) email](https://club1.fr/email/)
```

### Dossiers spéciaux

Les dossiers spéciaux utilisent les noms standards,
ils seront donc automatiquement reconnus par la grande majorité des clients email.
Au cas où ils ne le sont pas, voici la liste complète :

- `INBOX` : messages reçus
- `Drafts` : brouillons en cours de rédaction
- `Sent` : messages envoyés
- `Junk` : SPAMs (automatiquement supprimés au bout de 60&nbsp;jours)
- `Trash` : corbeille (automatiquement supprimés au bout de 60&nbsp;jours)
- `Archive` : messages archivés

### Quotas

Le dossier `mail` est soumis à un quota de **5&nbsp;Go**.
Cette décision a été prise pour encourager la suppression des anciens emails.

La taille maximale des emails (reçus et envoyés) est de **25&nbsp;Mo**.
Si un email dépasse cette taille, il sera refusé et l'expéditeur en sera informé
avec le message d'erreur : `Message size exceeds fixed limit` ou `552: 5.3.4 Error: message file too big`.

### Transferts automatiques

Il est possible de transférer automatiquement les emails que vous recevez sur votre adresse CLUB1
vers une ou plusieurs autres adresses de votre choix.
Pour se faire, il faut créer dans votre [espace personnel](/info/espace-personnel.md)
un fichier qui va indiquer à {term}`Postfix` à qui transférer votre courrier entrant.
Ce fichier doit être placé directement dans votre dossier et s'appeller `.forward`.

```{warning}
Les fichiers avec un point `.` devant sont appelés des
[fichiers cachés](https://fr.wikipedia.org/wiki/Fichier_et_r%C3%A9pertoire_cach%C3%A9#Sous_Unix_et_Linux).
Dans les explorateurs de fichiers ils peuvent être masqués par défaut.
```

A l'intérieur de ce fichier, il suffit ensuite de lister toutes les adresses
vers lesquelles vous souhaitez rediriger les emails en les séparant par un retour à la ligne.

Exemple de fichier `.forward` transférant vers deux adresses emails :

    perso@serveur.net
    unautremail@cool.fr

```{tip}
Il est même possible de conserver ses emails sur sa boîte CLUB1
en ajoutant son nom d'utilisateur&middot;trice à cette liste !
```

Pour mettre fin à une redirection, il suffit de supprimer la ligne correspondante.
Il est aussi possible de supprimer le fichier pour tout annuler.

```{admonition} Voir aussi
La page de manuel [Postfix local mail delivery](https://www.postfix.org/local.8.html) (en anglais)
```

Informations de connexion
-------------------------

La connexion d'un {term}`client` email à une adresse CLUB1 nécessite de configurer plusieurs serveurs.

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

Logiciels
---------

```{glossary}
Postfix
   {term}`Serveur` SMTP utilisé pour la transmission d'email.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Postfix),
   [Sources](https://github.com/vdukhovni/postfix)

Dovecot
   {term}`Serveur` IMAP utilisé pour la gestion de boîtes emails.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Dovecot),
   [Sources](https://github.com/dovecot/core)

OpenDKIM
   {term}`Serveur` fournissant un filtre _milter_
   utilisé par {term}`Postfix` pour signer les emails sortants.
   --- [Site Web](http://www.opendkim.org/), [Sources](https://github.com/trusteddomainproject/OpenDKIM)

Roundcube
   {term}`Client Web` permettant de consulter et d'envoyer des emails via SMTP et IMAP.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Roundcube),
   [Sources](https://github.com/roundcube/roundcubemail)
```
