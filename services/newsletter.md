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
<!-- - interface d'envoi en {term}`CLI`, uniquement accessible via [la connexion SSH](ssh.md). -->

Chaque membre dispose d'une newsletter, qui est envoyée par [son adressse email de membre](email.md).


Mise en place
-------------

La newsletter n'est pas activée par défaut.
Pour l'initialiser, il faut lancer la {term}`commande` {commande}`newsletter` avec la sous-commande `setup` :

    newsletter setup

Cela déclenche un formulaire vous permettant de définir les quelques réglages possible liés à la newsletter.
Vous pouvez les remplir à ce moment ou plus tard, en relancant la même commande.

Celle-ci va automatiquement créer cinq fichiers `.forward+...` à la racine de votre espace perso.
Elle va également ajouter un dossier `.config/newsletter` qui contiendra la configuration de la newsletter.
Ce dossier contient :

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
tandis que vous gardez un contrôle manuel sur la liste.

### Gestion manuelle

Comme les emails son stockés dans un fichier brut,
vous pouvez éditer ce fichier avec un éditeur de texte pour modifier la liste des abonnés.

Ou même, lorsque vous êtes connecté [à travers SSH](ssh.md),
vous pouvez lancer la commande suivante en remplaçant `ADDRESSE_EMAIL` par une addresse pour l'ajouter à la liste :

    echo ADDRESSE_EMAIL > ~/.config/newsletter/emails


### Gestion par email

Pour les personnes qui souhaiterait s'abonner à votre newsletter, l'inscription et la désinscription se fait par email.
Elles doivent envoyer à une addresse précise un email depuis l'addresse qu'elles souhaient inscrire ou désinscire.
Le contenu n'aura aucune incidence.

Dans les adresses présentés ci-dessous, `USERNAME` correspond à votre [identifiant de membre](../info/general.md#identifiant).

#### Inscription

    USERNAME+subscribe@club1.fr

Cela déclenche la procédure d'inscription.
Un email de confirmation est envoyé et il est nécessaire d'y répondre pour terminer l'inscription.

#### Désinscription

    USERNAME+unsubscribe@club1.fr

Si l'adresse était bien listée, la désinscription est immédiate.

### Publier un lien d'inscription

Pour proposer aux personnes de s'isncrire à votre newsletter depuis votre site Web,
vous pouvez insérer des liens {term}`HTML` en utilisant le préfix `mailto:` devant l'addresse email.

Par exemple :

```html
<a href="mailto:USERNAME+subscribe@club1.fr">inscription à ma newsletter !</a>
```

Il est même possible de pré-remplir le sujet et le corp du mail !
Bien que cela n'ai aucune incidence, ça peut être rassurant.

Exemple :

```html
<a href="mailto:USERNAME+subscribe@club1.fr?subject=Inscription&body=Je souhaite m'inscrire fissa.">inscription !</a>
```


Envoi
-----

Vous avez deux possibilités pour envoyer votre newsletter, par email ou via une commande.

La première est la plus simple car vous n'aurez besoin que d'un {term}`client` mail.
La seconde est plus avancée,
mais elle peut être automatisée ou connecter à d'autres commandes pour des usages divers et variés !

### Via email

Vous aussi pouvez utiliser les emails pour communiquer avec votre newsletter !
Vous pouvez écrire un email à l'addresse suivante et remplissant le contenu ainsi que le sujet avec ce que vous souhaitez diffuser.

    USERNAME+send@club1.fr

Rassuez vous, cet email n'est pas diffusé directement.
Vous allez dabord recevoir une prévisualisation qui vous permettra de juger du rendu.
La seule différance étant que le sujet contiendra `(preview)` en plus de votre sujet
et à la fin de la signature, un texte indiquant qu'il faut répondre à cet email pour confirmer l'envoi.

Si ce rendu vous plaît et que vous souhaitez bel et bien diffuser cet email à toutes les addresses inscrites,
alors vous pouvez répondre à cet email de prévisualisation.
Là aussi, le contenu de cette réponse n'aura aucune incidence.

Lorsque la diffusion sera terminée, vous recevrez un email de confirmation indiquant le statut de l'opération.

### Via SSH

Si l'on est onnecté en {term}`SSH` via un {term}`terminal`,
on peut envoyer la newsletter en lancant la {term}`commande` suivante :

    ewsletter send SUJET FICHIER_DU_CONTENU

- `SUJET` sera utilisé comme sujet de l'email
- `FICHIER_DU_CONTENU` doit indiquer le chemin vers un fichier contenant le corp de la newsletter (qu'il faut avoir créé au préalable).

```{warning}
Si `SUJET` ou `FICHIER_DU_CONTENU` contiennent des espaces, il faut les entourer de guillemets !
```

Si tout est bien configuré, le programme va afficher un aperçu et demander une confirmation avant l'envoi.

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
