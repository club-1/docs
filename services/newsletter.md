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
- interface d'envoi en {term}`CLI`, uniquement accessible via [la connexion SSH](ssh.md).

Chaque membre dispose d'une newsletter, qui est envoyée par [son adressse email de membre](email.md).


Mise en place
-------------

La newsletter n'est pas activée par défaut.
Pour l'initialiser, il faut lancer la {term}`commande` {commande}`newsletter` avec l'option `-i` :

    newsletter -i

Celle-ci va automatiquement créer trois fichiers `.forward+...` à la racine de votre espace perso.
Elle va également ajouter un dossier `.config/newsletter` qui contiendra la configuration de la newsletter.
Ce dossier contient :

- `emails` fichier brut avec une adresse email par ligne. Vous pouvez l'éditer manuellement pour gérer la liste des destinataires.
- `signature.txt` fichier brut à remplir avec du texte qui sera inséré en signature de chacun des emails de la newsletter.
- `settings.json` fichier JSON permettant d'ajuster le titre de la newsletter ainsi que le nom d'affichage pour l'adresse d'envoi.
- `.secret` fichier brut servant à sécuriser la confirmation d'inscription. Il s'agit d'un {term}`fichier caché` généré automatiquement.

```{warning}
📁 `.config` est un {term}`dossier caché`.
```

Abonnement
----------

L'inscription et la désinscription se font __uniquement par email__ de manière interactive.
Les emails doivent provenir de l'adresse à inscrire ou désinscrire.
Le contenu n'a aucune importance.
Dans les adresses suivantes, `USERNAME` correspond à votre [identifiant de membre](../info/general.md#identifiant).

### Inscription

    USERNAME+subscribe@club1.fr

Cela déclenche la procédure d'inscription.
Un email de confirmation est envoyé et il est nécessaire d'y répondre pour terminer l'inscription.

### Désinscription

    USERNAME+unsubscribe@club1.fr

Si l'adresse était bien listée, la désinscription est immédiate.


Envoi
-----

Une fois que l'on est connecté en {term}`SSH` via un {term}`terminal`,
on peut envoyer la newsletter en lancant la {term}`commande` suivante :

```{commande} newsletter

Commande permettant d'envoyer une newsletter à l'aide des {logiciel}`scripts de newsletter <newsletter>`:

    newsletter SUJET FICHIER_DU_CONTENU

- `SUJET` sera utilisé comme sujet de l'email
- `FICHIER_DU_CONTENU` doit indiquer le chemin vers un fichier contenant le corp de la newsletter (qu'il faut avoir créé au préalable).

💡 Pour accéder à l'aide, on peut utiliser `newsletter -h`.
```


```{warning}
Si `SUJET` ou `FICHIER_DU_CONTENU` contiennent des espaces, il faut les entourer de guillemets !
```

Si tout est bien configuré, le programme va afficher un aperçu et demander une confirmation avant l'envoi.

### méthode alternative

Il est également possible d'omettre le second argument et de fournir le contenu via STDIN.



Logiciels
---------

```{logiciel} newsletter
Ensemble de scripts très légers de gestion de newsletter développé par CLUB1.
--- [Sources](https://github.com/club-1/newsletter)
```
