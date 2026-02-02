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
- pas de statistiques (aucun *tracking* permettant de savoir si les destinataires ouvrent les emails)

Chaque membre dispose d'une newsletter, qui est envoyée par [son adressse email de membre](email.md).


Mise en place
-------------

La newsletter n'est pas activée par défaut.
Pour l'initialiser, il faut se [connecter en SSH](ssh.md)
et lancer la {term}`commande` {commande}`newsletter` avec la sous-commande `setup` :

    newsletter setup

Cela déclenche un formulaire vous permettant de définir les quelques réglages possible liés à votre newsletter.
Pour mettre à jour ces paramètres, vous pouvez la lancer à nouveau.

### Configuration détaillée

La commande `setup` crée cinq fichiers `.forward+...` à la racine de votre espace perso.
Elle crée également le dossier `.config/newsletter` qui contiendra la configuration de la newsletter.
Ce dernier contient :

- `emails` fichier brut avec une adresse email par ligne. Vous pouvez l'éditer manuellement pour gérer la liste des destinataires.
- `signature.txt` fichier brut à remplir avec du texte qui sera inséré en signature de chacun des emails de la newsletter.
- `settings.json` fichier JSON définissant le titre de la newsletter,
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
Elles doivent envoyer à une adresse précise un email depuis l'adresse qu'elles souhaitent inscrire ou désinscrire.
Le contenu n'aura aucune incidence.

```{tip}
Pour proposer aux personnes de s'isncrire à votre newsletter depuis votre site Web,
vous pouvez insérer des liens {term}`HTML`
[en utilisant le préfixe `mailto:`devant l'addresse email](https://developer.mozilla.org/fr/docs/Learn_web_development/Core/Structuring_content/Creating_links#liens_de_courriel).
```

Dans les adresses présentés ci-dessous, `IDENTIFIANT` correspond à votre [identifiant de membre](../info/general.md#identifiant).

#### Inscription

    IDENTIFIANT+subscribe@club1.fr

Cela déclenche la procédure d'inscription.
Un email de confirmation est envoyé et __il est nécessaire d'y répondre__ pour terminer l'inscription.

#### Désinscription

    IDENTIFIANT+unsubscribe@club1.fr

Si l'adresse était bien listée, la désinscription est immédiate.


### Gestion manuelle

Comme les emails son stockés dans un fichier brut (`~/.config/newsletter/emails`),
vous pouvez éditer ce fichier avec un éditeur de texte pour modifier la liste des abonnés.


Envoi
-----

L'envoi d'une newsletter peut se faire [__par email__](#par-email) ou [__via SSH__](#via-ssh).

### Par email

Pour diffuser une newsletter par email,
écrivez un email à l'adresse suivante en remplissant le sujet et le contenu.

    IDENTIFIANT+send@club1.fr

__Vous receverez une prévisualisation__ qui vous permettra de juger du rendu.
La seule différence étant que le sujet contiendra `(preview)` en plus de votre sujet
et à la fin de la signature, un texte indiquant qu'il faut répondre à cet email pour confirmer l'envoi.

Pour confirmer l'envoi, __répondez à cet email de prévisualisation__ (le contenu de cette réponse n'aura aucune influence).

À la fin de la diffusion, vous recevrez un email indiquant le statut de l'opération.

### Via SSH

Une fois connecté en {term}`SSH` via un {term}`terminal`,
la {term}`commande` suivante permet de diffuser une newsletter :

    newsletter send SUJET FICHIER_DU_CONTENU

- `SUJET` sera utilisé comme sujet de l'email
- `FICHIER_DU_CONTENU` doit indiquer le chemin vers un fichier contenant le corps de la newsletter (qu'il faut avoir créé au préalable).

```{warning}
Si `SUJET` ou `FICHIER_DU_CONTENU` contiennent des espaces, il faut les entourer de guillemets !
```

Le programe va vous envoyer __une prévisualisation par email__.
Il vous restera à confirmer ou non l'envoi dans votre terminal.

#### contenu via l'entrée standard

Il est également possible d'omettre le second argument et de fournir le contenu dans l'entrée standard.

Consultation des logs
---------------------

Les {term}`logs <log>` de ce service sont envoyés dans le [Syslog](https://en.wikipedia.org/wiki/Syslog) avec le tag `newsletter`.
Pour les consulter, il est possible d'utiliser la commande `journalctl` :

    journalctl -t newsletter

```{seealso}
Le manuel de cette commande : {manpage}`journalctl.1`
```

La commande
-----------

```{commande} newsletter
Commande permettant d'envoyer ou d'ajuster les réglages de votre newsletter personnelle.
Elle dispose de deux sous-commandes : `setup` pour la mise en place et `send` pour l'envoi.
L'envoi nécessite des arguments supplémentaires.
Le contenu peut alternativement être fourni dans l'entrée standard.

    newsletter send SUJET [FICHIER_DU_CONTENU]

💡 Pour accéder à l'aide, on peut utiliser `newsletter -h`.
```


Logiciels
---------

```{logiciel} newsletter
Petit logiciel de gestion de newsletter développé par CLUB1.
--- [Sources](https://github.com/club-1/newsletter-go)
```
