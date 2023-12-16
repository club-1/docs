Connexion à distance SSH
========================

La connexion SSH est la connexion la plus pure que vous puissiez avoir avec le serveur
(enfin parmi celles qui ne nécessitent pas d’user de psychotropes).
C’est aussi celle qui offre le plus la sensation d’utiliser un ordinateur,
car à travers elle, on peut [lancer des programme](#sélection-de-commandes) sur le serveur !

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

Se connecter
------------

```{warning}
La première connexion est **critique** car c'est lors de celle-ci que se fait
l'**échange des clés**. Pour éviter de subir une
[attaque de l'homme du milieu](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu)
il nous faut être sûr d'avoir reçu la bonne clé lors de cet échange.

Si vous ne savez pas comment ajouter la clé du serveur à votre appareil,
le tuto [](/tutos/premiere-connexion-ssh.md) est fait pour vous !
```

Il existe deux manières de s'authentifier lors d'une connexion SSH.
La plus simple est d'utiliser un [mot de passe](#sauthentifier-par-mot-de-passe),
elle est en revanche moins sécurisée que l'utilisation d'une
[clé publique](#sauthentifier-avec-une-clé-publique).

### S'authentifier par mot de passe

On utilise la commande suivante dans le {term}`terminal` pour se connecter
(remplacer `USER` par votre **identifiant** CLUB1) :

    ssh USER@club1.fr

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
(remplacer `USER` par votre **identifiant** CLUB1).
Elle vous demandera d'entrer votre **mot de passe** CLUB1 pour fonctionner.

    ssh-copy-id -i ~/.ssh/id_rsa USER@club1.fr

Finalement, on utilise toujours la même commande pour se connecter.
Mais cette fois ce sont les clés qui seront utilisées.
Si elles ne sont pas déjà déverrouillées, la _phrase de passe_ sera demandée.

    ssh USER@club1.fr

Informations de connexion
-------------------------

| champ            | valeur            |
| ---------------- | ----------------- |
| hôte             | `club1.fr`        |
| port             | `22` (par défaut) |


Sélection de commandes
----------------------

Voici une sélection de commandes pour vous permettre de découvrir le serveur :

```{tip}
Appuyer sur {kbd}`Enter` pour lancer une commande depuis le terminal.
```

```{commande} passwd
Permet de changer son mot de passe CLUB1
(cela aura donc un effet sur la connexion à tous les [services](/services-membres.md)).
--- Manuel : {manpage}`passwd.1`
```

```{commande} htop
Permet de voir ce qui se passe sur le serveur en ce moment et à quel point les ressources sont utilisées.  
Pressez la touche {kbd}`Q` pour quitter.
--- Manuel : {manpage}`htop.1`
```

```{commande} ncdu
Outil visuel et rapide pour trouver les fichiers ou dossiers qui prennent le plus de place.
Idéal pour faire du rangement !
Naviguez simplement avec les flèches directionnelles.
Pressez la touche {kbd}`Q` pour quitter.
--- Manuel : {manpage}`ncdu.1`
```

```{commande} w
Affiche les membres connectés en SSH et indique le logiciel qu'ils sont en train d'utiliser.
Cette commande est un peu intrusive !
--- Manuel : {manpage}`w.1`
```

````{commande} mailx
La façon la plus basique d'envoyer un email !
Cette commande nécessite de rajouter au bout, après un espace, l'email de votre destinataire.

```{tip}
Si vous envoyez à un membre CLUB1, pas besoin de rajouter `@club1.fr` !
```

Renseignez le sujet lorsqu'on vous le demande, puis confirmez en pressant {kbd}`Enter`.
Composer ensuite votre message.
Lorsque vous avez terminé, créz une nouvelle ligne puis tapez {kbd}`CTRL` + {kbd}`D`.
Enfin vous pouvez si vous le souhaitez ajouter des destinataires en copie.
--- Manuel : {manpage}`mailx.1`
````

```{commande} mutt
Permet de consulter et d'envoyer ses emails avec *Mutt* :
Un {term}`client` email en {term}`CLI`.
Les touches de contrôle sont indiqués en haut.
Pressez la touche {kbd}`Q` pour quitter.
--- Manuel : {manpage}`mutt.1`
```

````{commande} goaccess
Un outil qui permet de visualiser la fréquentation de ses sites {term}`Web` en analysant les {term}`log`.
Cette commande nécessite de rajouter au bout,
après un espace, le fichier de log que vous souhaitez analyser.

```{note}
Les logs de {logiciel}`Apache`, qui sert les sites Web,
sont stockés dans le dossier `log` de votre [espace perso](/info/espace-personnel.md#📁-log).
```

Naviguez entre les sections avec {kbd}`Tab`, utilisez {kbd}`Enter` pour en étendre une.  
Pressez la touche {kbd}`Q` pour quitter.
--- Manuel : {manpage}`mutt.1`
````

```{commande} man
Affiche la page de manuel correspondant à une commande.
Celle ci devra être indiquée après un espace.
La plupart des pages de manuel sont en anglais.  
Pressez la touche {kbd}`Q` pour quitter.
--- Manuel : {manpage}`man.1`
```

Logiciels
---------

```{logiciel} OpenSSH
Logiciel fournissant à la fois un {term}`serveur` et un {term}`client` {term}`SSH`.
--- [Wikipedia](https://fr.wikipedia.org/wiki/OpenSSH),
[Sources](https://anongit.mindrot.org/openssh.git)
```
