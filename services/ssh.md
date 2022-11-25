Connexion à distance SSH
========================

```{glossary}
SSH
   (_Secure SHell_) Protocole permettant de se connecter à distance en {term}`CLI` à un serveur.
   Ses principaux avantages sont d'être entièrement chiffré
   et d'offrir un accès complet aux fonctionnalités du serveur.
   Il existe des extensions SSH pour des usages plus spécifiques comme {term}`SFTP` ou {term}`SCP`. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Secure_Shell)

SFTP
   (_SSH File Transfer Protocol_) Protocole de transfert
   et gestion à distance de fichiers basé sur {term}`SSH`.
   Il est ainsi entièrement chiffré, et donc comparable à {term}`FTPS`,
   mais il offre plus de fonctionnalités (e.g. l'affichage des propriétaires d'un fichier). ---
   [Wikipedia](https://fr.wikipedia.org/wiki/SSH_File_Transfer_Protocol)

SCP
   (_Secure CoPy_) Protocole de copie de fichiers entre deux ordinateurs basé sur {term}`SSH`.
   SCP s'utilise principalement à l'aide du {term}`client` en {term}`CLI` du même nom. ---
   [Wikipedia](https://fr.wikipedia.org/wiki/Secure_copy)
```

Dans cette section {term}`OpenSSH` sera utilisé.
Comme il s'agit d'un logiciel en *ligne de commande*, il est
nécessaire d'ouvrir une fenêtre de terminal (`cmd` sur windows).

```{warning}
La première connexion est **critique** car c'est lors de celle-ci que se fait
l'**échange des clés**. Pour éviter de subir une
[attaque de l'homme du milieu](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu)
il nous faut être sûr d'avoir reçu la bonne clé lors de cet échange.

Si vous ne savez pas comment ajouter la clé du serveur à votre appareil,
[ce tuto](/tutos/premiere-connexion-ssh.md) est fait pour vous !
```

Se connecter
------------

Il existe deux manières de s'authentifier lors d'une connexion SSH.
La plus simple est d'utiliser un [mot de passe](#sauthentifier-par-mot-de-passe),
elle est en revanche moins sécurisée que l'utilisation d'une
[clé publique](#sauthentifier-avec-une-clé-publique).

### S'authentifier par mot de passe

On utilise la commande suivante dans le terminal pour se connecter
(remplacer `<login>` par votre **identifiant** CLUB1) :

    ssh <login>@club1.fr

Il faut ensuite entrer votre **mot de passe** CLUB1 (il est normal que le mot de passe ne s'affiche pas au moment de l'écriture).


### S'authentifier avec une clé publique

L'authentification par clé publique nécessite une paire de clé de chiffrement.
Pour créer ces clés, on utilise la commande ci-dessous.
Une _phrase de passe_ sera demandée lors de la génération des clés,
elle permet de les stocker de manière sécurisée.
Sur Linux, les clés seront automatiquement déverrouillées lors de l'ouverture d'une session,
il ne faut donc pas hésiter à choisir une longue phrase de passe.

    ssh-keygen

La commande qui suit va permettre d'envoyer la partie publique de la clé vers
le serveur, afin de pouvoir l'utiliser comme méthode d'authentification
(remplacer `<login>` par votre **identifiant** CLUB1).
Elle vous demandera d'entrer votre **mot de passe** CLUB1 pour fonctionner.

    ssh-copy-id -i ~/.ssh/id_rsa <login>@club1.fr

Finalement, on utilise toujours la même commande pour se connecter.
Mais cette fois c'est les clés qui seront utilisées.
Si elles ne sont pas déjà déverrouillées, la _phrase de passe_ sera demandée.

    ssh <login>@club1.fr

Informations de connexion
-------------------------

| champ            | valeur            |
| ---------------- | ----------------- |
| hôte             | `club1.fr`        |
| port             | `22` (par défaut) |

Logiciels
---------

```{glossary}
OpenSSH
   Logiciel fournissant à la fois un {term}`serveur` et un {term}`client` {term}`SSH`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/OpenSSH),
   [Sources](https://anongit.mindrot.org/openssh.git)
```
