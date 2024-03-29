Newsletter
==========

La newsletter est l'outil principal de communication externe de CLUB1.
Elle permet d'informer des réunions, ateliers, ou partager les nouveaux articles du journal de bord.

Elle utilise l'adresse `nouvelles@club1.fr` comme adresse d'envoi.

Une [archive des newsletter](https://club1.fr/newsletters) est disponible sur le site {term}`Web` du club.

Abonnement
----------

L'inscription et la désinscription se font __uniquement par email__ de manière interactive,
[ou manuellement](#gestion-manuelle-des-inscriptions).
Pour cela, il faut contacter une des adresses suivante depuis l'adresse email que l'on souhaite inscrire ou désinscrire.

- Inscription : <nouvelles-subscribe@club1.fr>
- Désinscription : <nouvelles-unsubscribe@club1.fr>

Lors de l'inscription,
un email de confirmation est envoyé et nécessite d'y répondre pour terminer l'inscription.

Envoyer une newsletter
----------------------

Pour pouvoir envoyer une newsletter, il faut être membre du {term}`groupe` `mail`.

Envoyer une newsletter nécessite d'être connecté en {term}`SSH` via un {term}`terminal`.

Le contenu à envoyer doit préalablement être stocké dans un fichier sur le serveur.
Il faut ensuite lancer la commande suivante :

    newsletter FICHIER NUMERO

Par exemple, si notre texte est dans un fichier qui s'appelle `contenu.txt`
et qu'il s'agît de la 42ème newsletter, il faudrait lancer :

    newsletter contenu.txt 42

```{tip}
Le programe se charge lui même de formater le titre et l'affichage correct du nombre.
```

La suite du programme est interactive et ne nécessite pas de connaissances particulières.


Gestion
-------

Sur le serveur CLUB1, les fichiers de paramétrage se trouvent dans `/var/mail/newsletter` :

- `secret` Contient une phrase secrète servant à la confirmation des adresses lors de l'inscription.
- `signatures` Contient une liste de phrases de signatures séparées par des retours à la ligne.
- `emails` Contient la liste des emails séparés par des retours à la ligne.


### Gestion manuelle des inscriptions

Il est possible d'ajouter ou de retirer manuellement des adresses email de façon très simple.
En éditant le fichier `emails`, il suffit d'ajouter ou de supprimer des lignes.
L'édition de ce fichier est réservée aux membres du {term}`groupe` `mail`.


### Création de signatures

Lors de l'inscription ou de la désinscription à la newsletter,
une petite phrase est choisie aléatoirement dans le fichier `signatures` en guise de signature.
L'édition de ce fichier est également réservée aux membres du {term}`groupe` `mail`.


### Configuration des alias

L'envoi d'emails automatique pour la gestion des inscriptions tire fortement parti des {term}`alias` de réception.

```{seealso}
Pour l'édition des alias email,
voir la section [Modifier les alias de réception](./aliases.md#modifier-les-alias-de-réception).
```

Pour chacune des trois adresses d'interface utilisateurs, il faut indiquer l'emplacement du script de réception,
le dossier contenant les fichiers de paramétrage et le préfixe de l'adresse email utilisée pour ces échanges.

```makefile
nouvelles-ACTION:      | "SCRIPT ACTION DOSSIER_CONFIG PREFIX"
```

Exemple de configuration avec les fichiers se trouvant dans `var/mail/newsletter`
et en utilisant `nouvelles` comme préfixe.

```makefile
nouvelles-subscribe:   | "/usr/local/sbin/nl.sh subscribe /var/mail/newsletter nouvelles"
nouvelles-confirm:     | "/usr/local/sbin/nl.sh confirm /var/mail/newsletter nouvelles"
nouvelles-unsubscribe: | "/usr/local/sbin/nl.sh unsubscribe /var/mail/newsletter nouvelles"
```

### Logiciel utilisé

Le choix de l'outil de newsletter a été un sujet compliqué,
comme en atteste [cette discussion sur le forum](https://forum.club1.fr/d/69).
Finalement, il a été décidé de coder nos propres {logiciel}`scripts de newsletter <newsletter>`.

```{logiciel} newsletter
Ensemble de scripts très légers de gestion de newsletter développé par et pour CLUB1.
Pour l'instant il ne fonctionne que pour la newsletter officielle de CLUB1.
--- [Sources](https://github.com/club-1/newsletter)
```
