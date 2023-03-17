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

Les nouveaux tickets (problèmes, suggestions, questions) doivent être créés avec l'étiquette {guilabel}`Tickets`.
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

```{logiciel} Flarum
Logiciel de forum écrit en {term}`PHP`.
Il est concu pour être extremmement modulaire
avec très peu de fonctionnalités faisant réellement partie du c&oelig;ur.
Il est ainsi facile d'en développer des extensions.
--- [Sources](https://github.com/flarum/framework/), [Site](https://flarum.org/)
```

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

