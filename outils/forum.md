Forum de discussion
===================

CLUB1 héberge un forum de discussion à l'adresse <https://forum.club1.fr>.
Il a pour but de remplir trois rôles principaux :

- La gestion des tickets (problèmes, suggestions, questions).
- La gestion de la feuille de route des administrateurs système.
- Offrir un canal de discussion asynchrone public,
  permettant à des discussions variées de co-exister dans la durée.

```{admonition} Voir aussi
L'article du journal "[Création d'un forum](https://club1.fr/creation-d-un-forum)"
```

Connexion
---------

Le forum est un outil de gestion interne mais il est aussi ouvert vers l'exterieur.
C'est pourquoi il existe deux façons de s'y connecter.
Dans tous les cas, une adresse e-mail est requise.
Elle permettra, si vous le souhaitez, de recevoir des notifications sur des conversations que vous aurez choisi.

### Connexion via le compte CLUB1

Ce type de connexion est dédié aux membres de CLUB1 souhaitant utiliser leur compte CLUB1 pour s'identifier sur le forum.
Cela implique d'utiliser le même identifiant et le même mot de passe
que pour l'ensemble des [services](/services-membres.md).
L'intérêt d'une telle méthode de connexion est de ne pas avoir un nouveau couple identifiant / mot de passe à retenir,
que votre mot de passe sera mis à jour si vous [modifiez celui de votre compte CLUB1](../faq.md#comment-modifier-mon-mot-de-passe-de-membre-club1-)
et que vous aurez automatiquement le badge {guilabel}`membre CLUB1`.

```{warning}
Votre identifiant CLUB1 sera votre pseudo et sera donc visible lorsque vous postez des messages public.
```

### Connexion ouverte

Ce type de connexion permet à n'importe qui de se créer un compte sur le forum et d'interagir avec.
Passage obligatoire si vous n'avez pas de compte CLUB1,
mais aussi dans le cas où ce sont des comptes de personnes morales (associations, collectifs)
et que des personnes souhaitent s'y exprimer à titre individuel.

Si vous êtes membres CLUB1 ou que vous appartenez à un groupe ayant un compte CLUB1
et que vous vous êtes inscrites via cette méthode,
nous vous invitons à envoyer un email à <contact@club1.fr> en indiquant la situation,
afin que les personnes en charge de l'administration du forum puissent vous ajouter le badge {guilabel}`membre CLUB1`.


Utilisation
-----------

Le forum CLUB1 est basé sur un système d'étiquettes plutôt que sur des catégories.
Un fil de discussion peut donc avoir plusieurs étiquettes.

```{important}
Certaines étiquettes sont dites _primaires_
et il ne doit y avoir qu'une seule étiquette primaire par discussion,
ce qui recréé des sortes de catégories.
```

### Organisation des étiquettes

Les étiquettes primaires sont les suivantes :

- {guilabel}`Tickets` : Regroupe les tickets ouverts.
- {guilabel}`Terminé` : Regroupe les tickets fermés ("résolus" ou "refusés").
- {guilabel}`Cafet` : Regroupe les discussions qui ne sont pas directement reliées à l'activité d'hébergement de CLUB1,
  et ne sont sonc pas des tickets.
- {guilabel}`English` : Regroupe les discussions en anglais.


### Cycle de vie d'un _ticket_

Le mot "ticket" représente un problème, une suggestion, une question qui est amené au _centre de tri_ des tickets
où les personnes concernées, capables de répondre peuvent résoudre les tickets au fur et à mesure.
Les tickets ont vocation à être fermés une fois le problème résolu, la suggestion reçue ou encore la question répondue.

Les nouveaux tickets doivent être créés avec l'étiquette {guilabel}`Tickets`.
Si l'objet du ticket est encore nébuleux et requiert plus de discussions,
il vaut mieux lui ajouter l'étiquette {guilabel}`rêve`.

Une fois qu'un ticket est résolu (ou refusé),
il faut lui retirer l'étiquette {guilabel}`Tickets`
pour pouvoir lui assigner les étiquettes {guilabel}`Terminé` et {guilabel}`résolu` ou {guilabel}`refusé` en fonction de son état.

### Feuille de route administrateurs système

Transversalement au système de gestion de tickets,
l'étiquette {guilabel}`Roadmap Admin` est utilisée par les administrateurs système de CLUB1 pour s'organiser.
Elle permet également de rendre publique les tâches "en cours", "suivantes" et "planifiées".

C'est en réalité une étiquette _primaire_ que seuls certains utilisateurs du forum peuvent utiliser,
en contournant les restriction d'étiquettes.


Administration
--------------

Cette section est surtout destinée aux administrateurs du forum,
soit les membres CLUB1 faisant partie du {term}`groupe` `forum`.

### Logiciel utilisé

Le forum est basé sur {logiciel}`Flarum`.
Il est executé par {logiciel}`PHP-FPM` avec l'utilisateur `forum`,
directement depuis {logiciel}`Nginx`.

Il utilise une base de données {term}`SQL` gérée par {logiciel}`MariaDB`.

````{logiciel} Flarum
Logiciel de forum écrit en {term}`PHP`.
Il est concu pour être extrêmement modulaire
avec très peu de fonctionnalités faisant réellement partie du c&oelig;ur.
Il est ainsi facile d'en développer des extensions de toute sorte,
qui peuvent emmener l'outil forum dans des directions très différentes.
--- [Sources](https://github.com/flarum/framework/), [Site](https://flarum.org/)

CLUB1 maintient plusieurs extension pour ce forum :

```{describe} club-1/flarum-ext-cross-references
Ajoute des liens de référence croisé lorsqu'une discussion est mentionnée depuis une autre.
--- [Sources](https://github.com/club-1/flarum-ext-cross-references)
```

```{describe} club-1/flarum-ext-french-typography
Typographie améliorée pour les écrits français, principalement autour de la ponctuation.
--- [Sources](https://github.com/club-1/flarum-ext-french-typography)
```

````

### Fichiers et dossiers

Quelques fichiers et dossiers en relation avec le forum CLUB1.

#### `/var/www/forum.club1.fr/`

Dossier d'installation de Flarum.
Il contient notamment les fichiers suivants :

- `config.php` : Fichier de configuration de Flarum.
  Il ne contient que les paramètres d'installation.
  Le reste de la configuration se trouve dans la base de données.

- `composer.json` : Fichier décrivant les dépendances Composer.
  C'est via ce logiciel que sont installées les extensions Flarum.

#### `/etc/nginx/sites-available/forum.club1.fr`

Fichier de configuration {logiciel}`Nginx` contenant le _virtual host_ du forum.


#### `/etc/php/*/fpm/pool.d/forum.conf`

Fichier de configuration {logiciel}`PHP-FPM` de la _pool_ de l'utilisateur `forum`.

