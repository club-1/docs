Newsletter de club1
===================

La newsletter est l'outil principal de communication externe de CLUB1.
Elle permet d'informer des réunions, ateliers, ou partager les nouveaux articles du journal de bord.

Elle utilise l'adresse `nouvelles@club1.fr` comme adresse d'envoi.

Une [archive des newsletter](https://club1.fr/newsletters) est disponible sur le site {term}`Web` du club.

Abonnement
----------

L'inscription et la désinscription se font __uniquement par email__ de manière interactive.
Pour cela, il faut contacter une des adresses suivante depuis l'adresse email que l'on souhaite inscrire ou désinscrire.

- Inscription : <nouvelles+subscribe@club1.fr>
- Désinscription : <nouvelles+unsubscribe@club1.fr>

Lors de l'inscription,
un email de confirmation est envoyé et nécessite d'y répondre pour terminer l'inscription.

Envoyer une newsletter
----------------------

Pour pouvoir envoyer une newsletter, il faut être membre du {term}`groupe` `mail`.

Envoyer une newsletter nécessite d'être connecté en {term}`SSH` via un {term}`terminal`.

Le contenu à envoyer doit préalablement être stocké dans un fichier sur le serveur.
Il faut ensuite lancer la commande suivante :

````{commande} newsletter-club1

Envoi la newsletter de club1.

    newsletter-club1 SUJET FICHIER_DU_CONTENU

```{seealso}
Cette commande est la même que {commande}`newsletter`, mais dédiée à la newsletter officielle de club1.
```
````

La suite du programme est interactive et ne nécessite pas de connaissances particulières.


Gestion
-------

La newsletter est envoyée par le compte `nouvelles`.
Comme il s'agit d'un compte spécial, son espace est située dans `/var/nouvelles`.
les fichiers de configuration de la newsletter se trouvent dans `/var/nouvelles/.config/newsletter`.
Ils sont manipulables par les membres du {term}`groupe` `mail`.

```{seealso}
Pour la description de ces fichiers de config, se référer au [service de newsletter des membres](../services/newsletter.md).
```


### Logiciel utilisé

Le choix de l'outil de newsletter a été un sujet compliqué,
comme en atteste [cette discussion sur le forum](https://forum.club1.fr/d/69).
Finalement, il a été décidé de coder nos propres {logiciel}`scripts de newsletter <newsletter>`,
qui sont maintenant également utilisés pour le [service de newsletter](../services/newsletter.md) des membres.
