Newsletter
==========

Le service de newsletter de club1 est très basique comparé aux offres qui existe ailleurs sur internet.

Ses limitations sont les suivantes :

- les emails sont en texte brut uniquement
- pas de statistiques (aucun *tracking* permettant de savoir si les destinataires ouvrent les emails)
- interface d'envoi en {term}`CLI`, uniquement accessible via [la connexion SSH](ssh.md).

Chaque membre dispose d'une newsletter, qui est envoyée par [son adressse email de membre](email.md).


Mise en place
-------------

La newsletter n'est pas activée par défaut.
Pour l'initialiser, il faut lancer la commande suivante :

    newsletter -i

Celle-ci va automatiquement créer trois fichiers `.forward+...` à la racine de votre espace perso.
Elle va également ajouter un dossier `.config/newsletter` qui contiendra la configuration de la newsletter.
Ce dossier contient :

- `emails` fichier brut avec une adresse email par ligne. Vous pouvez l'éditer manuellement pour gérer la liste des destinataires.
- `signature.txt` fichier brut à remplir avec du texte qui sera inséré en signature de chacun des emails de la newsletter.
- `settings.json` fichier JSON contenant permettant d'ajuster le titre de la newsletter ainsi que le nom d'affichage pour l'adresse d'envoi.
- `.secret` fichier brut utiliser pour sécruisé la confirmation. Il est généré automatiquement.


Abonnement
----------

L'inscription et la désinscription se font __uniquement par email__ de manière interactive.
Les mails doivent provenir de l'adresse qui doit être inscrite ou désinscrite.
Le contenu n'a aucune importance !
Dans les adresses suivantes, `USERNAME` correspond à votre [identifiant de membre](../info/general.md#identifiant).

### Inscription

    USERNAME+subscribe@club1.fr

Cela déclenche la procédure d'inscription.
un email de confirmation est envoyé et nécessite d'y répondre pour terminer l'inscription.

### Désinscription

    USERNAME+unsubscribe@club1.fr

Si l'adresse était bien listée, la désinscription est immédiate.


Envoi
-----

Une fois que l'on est connecté en {term}`SSH` via un {term}`terminal`,
on peut envoyer la newsletter en lancant la commande suivante :

    newsletter SUJET FICHIER_DU_CONTENU

- `SUJET` sera le le sujet de l'email
- `FICHIER_DU_CONTENU` est le chemin vers un fichier brut contenant le corp de la newsletter (qu'il faut avoir créé au préalable).

```{warning}
Si `SUJET` ou `FICHIER_DU_CONTENU` contiennent des espaces, il faut leur ajouter des guillements autour !
```

Si tout est bien configuré, le programme va afficher un aperçu et demander une confirmation d'envoi.
La fréquence d'envoi est de 5 emails par secondes.

### méthode alternative

Il est également possible d'omettre le second argument et de fournir le contenu via STDIN.




Logiciels
---------

```{logiciel} newsletter
Ensemble de scripts très légers de gestion de newsletter développé par et pour CLUB1.
--- [Sources](https://github.com/club-1/newsletter)
```
