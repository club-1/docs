Connexion SSH à l'aide d'une clé publique
=========================================

Vous en avez marre de taper à chaque fois votre mot de passe
lorsque [vous vous connectez en SSH](/services/ssh.md) avec votre ordinateur personnel ?

Ce tuto est fait pour vous ! 👈️

```{warning}
Ce tutoriel n'a pas encore beaucoup été éprouvé. (C'est encore un bébé !)
Les choses peuvent donc être différentes sur votre appareil.

🛟 En cas de blocage, on vous invite à [demander de l'aide](../info/general.md#demandes-et-incidents).
En plus de vous débloquer, cela pourra aider à enrichir ce tutoriel ! 😉
```


Création de la paire de clés
----------------------------

L'authentification par clé publique nécessite une paire de clé de chiffrement.
Pour créer ces clés, on utilise la {term}`commande` ci-dessous.

    ssh-keygen -t ed25519

Ensuite, le terminal devrait afficher un truc du genre :

    Generating public/private ed25519 key pair.
    Enter file in which to save the key (/home/LOCAL_USER/.ssh/id_ed25519):

La première ligne nous confirme que c'est bien une "paire de clé" qui est crée.
La seconde ligne nous demande de choisir l'emplacement de cette paire.
Ici `LOCAL_USER` devrait correspondre à votre nom d'utilisataire local,
qui n'est pas forcément le même que celui sur le serveur CLUB1.
Entre parenthèse, on voit l'emplacement par défaut qui est suggéré : à l'intérieur du {term}`dossier caché` `.ssh`.
On vous conseille d'accepter cette proposition en appuyant sur {kbd}`entrée`.

    Enter passphrase (empty for no passphrase): 

> Qu'est ce que c'est que ça une _passphrase_ ?
> je croyais qu'on n'allait plus avoir de mot de passe à taper ? 🫤

Une phrase de passe, c'est en fait exactement la même chose qu'un mot de passe.
C'est surtout une façon d'encourager à ce qu'elle soit plus longue et donc plus sécurisée.

Sur Linux, les clés seront automatiquement déverrouillées lors de l'ouverture d'une session,
il ne faut donc pas hésiter à choisir une longue phrase de passe !

```{attention}
Lorsque vous tapez votre phrase de passe, rien ne s'affiche !
C'est normal, il s'agit d'une mesure de sécurité
qui permet de ne même pas révéler le nombre de caractères du mot de passe. 🤫
```

    Enter same passphrase again:

Bon, ça c'est simplement pour vérifier que vous ne vous êtes pas trompé en tapant au clavier.

Si tout c'est bien passé, on devrait ensuite recevoir les messages suivant :

    Your identification has been saved in /home/LOCAL_USER/.ssh/id_ed25519
    Your public key has been saved in /home/LOCAL_USER/.ssh/id_ed25519.pub

Les deux clés ont été chacunes stockées dans un fichier séparé.
L'_identification_ c'est ce qu'on appelle la clé privée.
On remarque que le nom des fichiers est très proche, la clé publique est ralongée avec `.pub`.
(Pour _public_, et non pas pour publicité 😅)

    The key fingerprint is:
    SHA256:S6ilDqI7pr/kIPJ27AxqZGfTiZ1IarO47ZdmieFqzj8 LOCAL_USER@LOCAL_PC

Ça c'est l'_empreinte digitale_ de la clé.

    The key's randomart image is:
    +--[ED25519 256]--+
    |                 |
    |                 |
    |                 |
    |   .   .         |
    |  o = = S        |
    | *.* O . .       |
    |X.O++o  .        |
    |B&+EO            |
    |&@OO=            |
    +----[SHA256]-----+

Pour nous récompenser de notre dur labeur, on reçoit cette magnifique image.
Ça valait le coup !


Envoi de la clé publique sur le serveur
---------------------------------------

La commande qui suit va permettre d'envoyer la partie publique de la clé vers
le serveur, afin de pouvoir l'utiliser comme méthode d'authentification
(remplacer `USER` par votre **identifiant** CLUB1).
Elle vous demandera d'entrer votre **mot de passe** CLUB1 pour fonctionner.

    ssh-copy-id -i ~/.ssh/id_ed25519 USER@club1.fr



Connexion au serveur
--------------------


Finalement, on utilise toujours la même commande pour se connecter.
Mais cette fois ce sont les clés qui seront utilisées.
Si elles ne sont pas déjà déverrouillées, la _phrase de passe_ sera demandée.

    ssh USER@club1.fr
