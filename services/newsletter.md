Newsletter personnelle (beta)
=============================

```{warning}
Ce service est en "beta" sur CLUB1,
ce qui signifie qu'il risque de changer de configuration
ou même d'être supprimé dans le futur.
```

Le service de newsletter de CLUB1 est très basique comparé aux offres qui existent ailleurs sur {term}`Internet`.
Ses limitations sont les suivantes :

- les emails sont en __texte brut__ (pas de style)
- pas de statistiques (aucun *tracking* permettant de savoir si les destinataires ouvrent les emails)s

Chaque membre dispose d'une newsletter, qui est envoyée par [son adressse email de membre](email.md).


Mise en place
-------------

La newsletter n'est pas activée par défaut.
Pour l'initialiser, il faut se [connecter en {term}`SSH`](ssh.md)
et lancer la {term}`commande` {commande}`newsletter` avec la sous-commande `setup` :

    newsletter setup

Cela déclenche un formulaire vous permettant de définir les quelques réglages possible liés à votre newsletter.
Pour mettre à jour ces paramêtres, vous pouvez la lancer à nouveau.

### Configuration détaillée

La commande `setup` crée cinq fichiers `.forward+...` à la racine de votre espace perso.
Elle crée également le dossier `.config/newsletter` qui contiendra la configuration de la newsletter.
Ce dernier contient :

- `emails` fichier brut avec une adresse email par ligne. Vous pouvez l'éditer manuellement pour gérer la liste des destinataires.
- `signature.txt` fichier brut à remplir avec du texte qui sera inséré en signature de chacun des emails de la newsletter.
- `settings.json` fichier JSON permettant d'ajuster le titre de la newsletter,
    le nom d'affichage pour l'adresse d'envoi,
    ainsi que la langue utilisés pour la [gestion des inscriptions par email](#gestion-par-email).
- `.secret` fichier brut servant à sécuriser la confirmation d'inscription. Il s'agit d'un {term}`fichier caché` généré automatiquement.

```{warning}
📁 `.config` est un {term}`dossier caché`.
```

Gestion des inscriptions
------------------------

Les personnes peuvent s'inscrire et se désinscrire à votre liste __uniquement par email__,
tandis que vous gardez un [contrôle manuel sur la liste](#gestion-manuelle).

### Gestion par email

Pour les personnes qui souhaiterait s'abonner à votre newsletter, l'inscription et la désinscription se fait par email.
Elles doivent envoyer à une addresse précise un email depuis l'addresse qu'elles souhaient inscrire ou désinscire.
Le contenu n'aura aucune incidence.

Dans les adresses présentés ci-dessous, `IDENTIFIANT` correspond à votre [identifiant de membre](../info/general.md#identifiant).

````{tip}
Pour proposer aux personnes de s'isncrire à votre newsletter depuis votre site Web,
vous pouvez insérer des liens {term}`HTML` en utilisant le préfix `mailto:` devant l'addresse email.

Exemple :

```html
<a href="mailto:IDENTIFIANT+subscribe@club1.fr">inscription à ma newsletter !</a>
```
````

#### Inscription

    IDENTIFIANT+subscribe@club1.fr

Cela déclenche la procédure d'inscription.
Un email de confirmation est envoyé et __il est nécessaire d'y répondre__ pour terminer l'inscription.

#### Désinscription

    IDENTIFIANT+unsubscribe@club1.fr

Si l'adresse était bien listée, la désinscription est immédiate.


### Gestion manuelle

Comme les emails son stockés dans un fichier brut,
vous pouvez éditer ce fichier avec un éditeur de texte pour modifier la liste des abonnés.

Ou même, lorsque vous êtes connecté [à travers SSH](ssh.md),
vous pouvez lancer la commande suivante en remplaçant `ADDRESSE_EMAIL` par une addresse pour l'ajouter à la liste :

    echo ADDRESSE_EMAIL > ~/.config/newsletter/emails


Envoi
-----

L'envoi d'une newsletter peut se faire [__par email__](#par-email) ou [__via SSH__](#via-ssh).

### Par email

Pour diffuser une newsletter par email,
écrivez un email à l'addresse suivante en remplissant le sujet et le contenu.

    IDENTIFIANT+send@club1.fr

Vous receverez __une prévisualisation__ qui vous permettra de juger du rendu.
La seule différance étant que le sujet contiendra `(preview)` en plus de votre sujet
et à la fin de la signature, un texte indiquant qu'il faut répondre à cet email pour confirmer l'envoi.

Si vous souhaitez confirmer l'envoi, répondez à cet email de prévisualisation (le contenu de cette réponse n'aura aucune influence).

À la fin de la diffusuion, vous recevrez un email de confirmation indiquant le statut de l'opération.

### Via SSH

Une fois connecté en {term}`SSH` via un {term}`terminal`,
la {term}`commande` suivante permet de diffuser une newsletter :

    newsletter send SUJET FICHIER_DU_CONTENU

- `SUJET` sera utilisé comme sujet de l'email
- `FICHIER_DU_CONTENU` doit indiquer le chemin vers un fichier contenant le corp de la newsletter (qu'il faut avoir créé au préalable).

```{warning}
Si `SUJET` ou `FICHIER_DU_CONTENU` contiennent des espaces, il faut les entourer de guillemets !
```

Le programe va vous envoyer __une prévisualisation par email__.
Il vous restera à confirmer ou non l'envoi de manière interactive.

#### contenu via STDIN

Il est également possible d'omettre le second argument et de fournir le contenu via STDIN.


La commande
-----------

```{commande} newsletter
Commande permettant d'envoyer ou d'ajuster les réglages de votre newsletter personnelle.
Elle dispose de deux sous-commandes : `setup` pour la mise en place et `send` pour l'envoi.

    newsletter setup

C'est une commande *interactive* qui lance un formulaire de paramétrage.

    newsletter send SUJET FICHIER_DU_CONTENU

💡 Pour accéder à l'aide, on peut utiliser `newsletter -h`.
```


Logiciels
---------

```{logiciel} newsletter
Ensemble de scripts très légers de gestion de newsletter développé par CLUB1.
--- [Sources](https://github.com/club-1/newsletter)
```
