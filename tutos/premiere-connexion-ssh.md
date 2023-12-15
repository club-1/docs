Première connexion SSH
======================

Dans ce tuto, nous allons voir comment se connecter au serveur
pour la première fois en {term}`SSH` de manière **sécurisée**.
Pour cela, pas besoin d’installer de logiciels supplémentaire,
la majorité des systèmes d’exploitation ont déjà tout le nécessaire pour cette connexion.

```{caution}
Ce tutoriel n'a pas encore été éprouvé sur Windows.
Certaines étapes peuvent de ne pas fonctionner.
Si vous rencontrez un problème, la section "[](../info/general.md#demandes-et-incidents)"
explique comment nous en faire part.
```

Connexion avec le terminal
--------------------------

Pour effectuer cette connexion SSH nous allons utiliser {logiciel}`OpenSSH`.
Ce logiciel s'utilise en {term}`CLI`,
il est donc nécessaire d'ouvrir une fenêtre de **{term}`terminal`** ! 🥵

```{admonition} Pour Windows
Dans le cas de Windows, il faut utiliser le programme qui s'appelle `Powershell`.
Comme sa configuration par défaut n'est pas terrible 💩, il faut corriger cela avec la commande suivante :

    $PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'

Pour "coller" du texte dans `Powershell` on peut faire {kbd}`Ctrl` + {kbd}`V`,
ou simplement un clic droit avec sa souris.
```

Ne vous laissez pas impressionner par son interface déroutante,
c'est un outil qui va faire de vous un&middot;e véritable magicien&middot;ne de l'informatique ! 🧙

On utilise la commande suivante dans le terminal pour se connecter
(remplacer `USER` par votre **identifiant** CLUB1) :

    ssh USER@club1.fr

```{tip}
Appuyer sur {kbd}`Enter` pour lancer une commande depuis le terminal.
```

Vous devriez voir s'afficher le message suivant :

    The authenticity of host 'club1.fr (***)' can't be established.
    ED25519 key fingerprint is SHA256:*********.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?

> 😱 Houla ! Qu'est ce que c'est que ça ??

En fait, c'est normal, {logiciel}`OpenSSH` nous averti que l'authentification
de la connexion n'est pas garantie car votre appareil ne connaît pas *encore* ce serveur.

En répondant `yes` à ce message on s'expose à une
[attaque de l'homme du milieu](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu) 🥸.
Nous allons donc répondre `no` pour le moment.

La confiance règne
------------------

Nous allons rajouter à votre appareil la **clef publique** du serveur CLUB1.
Cela permet de garantir l'authenticité des réponses du serveur et d'initialiser une connexion chiffrée.
De cette manière on est certains que l'on a bien affaire au serveur de CLUB1.

Pour être sûr qu'il s'agit bel et bien de la clef du serveur CLUB1,
il faut l'acquérir par une autre source que la connexion SSH elle-même
au cas où celle-ci serait compromise 😮.

> 🤔 Mais alors, qu'est ce qui garanti que la nouvelle source n'est pas elle aussi compromise ?

La source de la clef que nous allons utiliser provient du {term}`Web`,
à travers une connexion chiffrée et **authentifié** via {term}`TLS` 🔒
(C'est le fameux `s` dans `https`).


Fichier `known_hosts`
---------------------

Concrètement, cela consiste à ajouter une ligne de texte contenant la clef 🔑,
à un fichier sur votre appareil.
Ce fichier s'appellera `known_hosts`, *serveurs connus*.
Il devra se trouver dans un dossier `.ssh`,
lui-même au sein de votre espace personnel sur votre appareil.

```{note}
Le dossier correspondant à votre espace personnel
porte généralement le nom de votre utilisateur sur cet appareil.
```

    📁 <utilisateur>
    ├─ 📁 .ssh
    │  └─ 📄 known_host    👈
    ├─ 📁 Documents
    ├─ 📁 Images
    ...

Normalement, le {term}`dossier caché` `.ssh` à dû être créé lors de la tentative de connexion SSH.

Maintenant il ne nous reste plus qu'à écrire la clef du serveur dans un fichier `known_host`.
La commande suivante fait tout ça pour vous ! 🪄

```sh
echo 'club1.fr ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBFQJRiEKM9iywtuvjLD7Wvp6F7VqM6ocuc0Q05LGKU6' >> ~/.ssh/known_hosts
```

Si tout s'est bien passé,
le fichier `known_hosts` doit maintenant contenir une ligne contenant la clef.

Vous devriez maintenant pouvoir vous [connecter en SSH](#connexion-avec-le-terminal)
sans voir le message d'alerte et il vous faudra alors entrer votre **mot de passe** CLUB1.

```{attention}
Lorsque vous tapez votre mot de passe, rien ne s'affiche !
C'est normal, il s'agit d'une mesure de sécurité
qui permet de ne même pas révéler le nombre de caractères du mot de passe. 🤫
```

```{tip}
Dans une fenêtre de terminal, il est généralement possible de "coller" un texte
en faisant "Clic droit" --> {guilabel}`Coller`.
Ou encore {kbd}`Ctrl` + {kbd}`Shift` + {kbd}`V`.
```

Dans le serveur
---------------

Félicitation 🎉, vous êtes maintenant connecté&middot;e au serveur en SSH !
C'est un accès privilégié,
car c'est celui qui vous donne le plus de libertés d'interactions avec le serveur.

🍾 Pour fêter ça, voici une petite sélection de commandes à découvrir :

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
