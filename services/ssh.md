Connexion à distance SSH
========================

SSH (_Secure SHell_) permet de se connecter à distance en {term}`CLI` au serveur CLUB1.
L'accès SSH peut se révéler très utile, surtout pour les utilisateurs avancés.

Dans cette section [OpenSSH](https://fr.wikipedia.org/wiki/OpenSSH) sera
utilisé. Comme il s'agit dans logiciel en *ligne de commande*, il est
nécessaire d'ouvrir une fenêtre de terminal (powershell sur windows).


Première connexion
------------------

La première connexion est critique car c'est lors de celle-ci que se fait
l'échange des clés. Pour éviter de subir une
[attaque de l'homme du milieu](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu)
il nous faut être sûr d'avoir reçu la bonne clé lors de cet échange.

Pour résoudre ce problème, OpenSSH affiche un avertissement contenant
l'empreinte de la clé reçue :

>     The authenticity of host 'club1.fr (***)' can't be established.
>     ED25519 key fingerprint is SHA256:t4m5ioK2DGyObdxh3ATIIKnbhm4EhCp1cfgQmogHd58.
>     Are you sure you want to continue connecting (yes/no/[fingerprint])?

Ce n'est pas idéal car il faut comparer manuellement l'empreinte de
l'avertissement avec celle fournie par l'administrateur. À la place, il est
préférable d'ajouter la clé avant le première connexion avec la commande
suivante :

    echo club1.fr ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBFQJRiEKM9iywtuvjLD7Wvp6F7VqM6ocuc0Q05LGKU6 >> ~/.ssh/known_hosts

```{tip}
Si pour une quelconque raison la comparaison manuelle est préférée,
l'empreinte de l'exemple ci-dessus est effectivement celle de club1.fr.
```

Créer une paire de clés de chiffrement
--------------------------------------

Pour créer une paire de clé de chiffrement, on utilise la commande suivante :

    ssh-keygen

La commande qui suit va permettre d'envoyer la partie publique de la clé vers
le serveur, afin de pouvoir l'utiliser comme méthode d'authentification
(remplacer `<login>` par votre **identifiant** CLUB1).

    ssh-copy-id -i ~/.ssh/id_rsa <login>@club1.fr

Se connecter
------------

Après la première connexion, on utilise la commande suivante dans le terminal pour se connecter 
(remplacer `<login>` par votre **identifiant** CLUB1) :
    
    ssh <login>@club1.fr

Il faut ensuite entrer votre **mot de passe** CLUB1 (il est normal que le mot de passe ne s'affiche pas au moment de l'écriture).

Informations de connexion
-------------------------

| champ            | valeur            |
| ---------------- | ----------------- |
| hôte             | `club1.fr`        |
| port             | `22` (par défaut) |
