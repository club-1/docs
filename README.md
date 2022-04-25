Meta-documentation
==================

[![build][buildimg]][buildurl]
[![Translation status][transimg]][transurl]

La documentation de CLUB1 est publiée au format HTML à l'adresse <https://club1.fr/docs/fr/>.
Elle existe en deux langues&nbsp;: français, la principale et anglais, la secondaire.
Le site {term}`Web` est généré à l'aide de
[Sphinx](https://fr.wikipedia.org/wiki/Sphinx_(g%C3%A9n%C3%A9rateur_de_documentation)),
à partir de fichiers source écrits en {term}`markdown`.
Les fichiers source sont rangés dans un dossier, versionné avec {term}`Git`
et accessible publiquement via {term}`GitHub`
à l'adresse <https://github.com/club-1/docs/>.

```{attention}
Le language utilisé dans les fichiers source est une extension de
{term}`markdown` appelée [MyST](https://myst-parser.readthedocs.io/en/latest/).
Il apporte donc quelques spécificités supplémentaires, comme expliqué dans
leur [guide syntaxique](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html),
dont il existe aussi une [référence rapide](https://myst-parser.readthedocs.io/en/latest/syntax/reference.html).
```

Arborescence du dossier
-----------------------

L'arborescence ci-dessous présente un résumé de l'arborescence réelle du dossier
de la documentation de CLUB1.

    ./
    ├── _build/
    ├── _locales/
    │   ├── en/
    │   │   └── LC_MESSAGES/
    │   │       └── package.po
    │   └── package.pot
    ├── _static/
    ├── _templates/
    ├── ***/
    │   └── ***.md
    ├── AUTHORS
    └── index.md

- `_build/` : dossier contenant l'ensemble des fichiers générés par Sphinx.
- `_locales/` : dossier contenant les fichiers de traductions.
  Il comporte un dossier par langue avec des fichiers `.po` contenant les
  traductions et des fichiers `.pot` générés automatiquement à partir des
  fichiers source en markdown.
- `_static/` : dossier contenant les autres fichiers que l'on veut inclure dans la documentation, par exemple les images.
- `_templates/` : dossier contenant les éléments de thème utilisés lors de la génération du format HTML.
- `AUTHORS` : fichier contenant la liste des auteurs.
- `index.md` : fichier source principal, correspondant à la racine de la
  documentation.

Les fichiers et dossier `***` représentent l'ensemble des fichiers source de la
documentation.

Proposer des modifications
--------------------------

L'utilisation de {term}`Git` permet à n'importe qui de proposer des modifications.
Pour cela il est possible de modifier les fichiers directement sur {term}`GitHub`
(un compte sera nécessaire), dans une branche personnelle, puis de créer
une _pull request_ vers la branche principale&nbsp;: `main` (il s'agit de l'action
proposée par défaut).
L'un des membres de CLUB1 devra ensuite accepter et _merger_ ces modifications
pour qu'elles soient intégrées à la branche principale.

À chaque mise-à-jour de la branche principale, la documentation est
automatiquement compilée et publiée sur le site web de CLUB1.

### Langue française

Pour modifier une page existante, il faut éditer le fichier `.md` correspondant.
Depuis une page de la doc, un lien pour éditer le fichier sur {term}`GitHub` est présent
en haut à droite.

Ajoutez une ligne avec votre nom dans le [fichier `AUTHORS`](https://github.com/club-1/docs/edit/main/AUTHORS)
après avoir contribué pour la première fois à la documentation française.

### Autres langues

Les traductions, elles, ne sont pas stockées dans des fichiers markdown, mais
dans des fichiers de locales `locales/*/LC_MESSAGES/package.po` et sont plus
facilement éditables via [Weblate](https://hosted.weblate.org/projects/club-1/docs/).

![Translation status](https://hosted.weblate.org/widgets/club-1/-/docs/multi-auto.svg)

### Ajouter une page

L'ajout de pages ne peut se faire qu'en français. Il faut créer un fichier `.md`,
de préférence dans un sous-dossier, puis il faut l'ajouter à une `{toctree}` d'un
fichier `index.md` (s'inspirer de l'existant).

Références
----------

- [Spécificités des liens avec Sphinx](https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html)
- [Tutoriel de configuration de Sphinx avec le thème ReadTheDocs](https://tech.michaelaltfield.net/2020/07/18/sphinx-rtd-github-pages-1/)

Compilation
-----------

Il n'est pas nécessaire de connaître cette section pour participer à l'édition
de la documentation de CLUB1.
Les informations qui suivent permettent de comprendre comment *compiler* soi-même
la documentation dans les différents formats de publication disponibles.
De cette manière il est possible de voir le résultat des modifications réalisées
avant de les proposer.

### Prérequis

| Logiciel         | Détails                                          |
|------------------|--------------------------------------------------|
| Make             | Gestionnaire de compilation                      |
| Sphinx           | Compilateur de documentation                     |
| Shpinx-rtd-theme | Thème ReadTheDocs pour Sphinx                    |
| MyST-Parser      | Prise en charge du Markdown par Sphinx           |
| gettext          | (Optionnel) Mise-à-jour des fichiers de locales  |
| imagemagick      | (Optionnel) Conversion des SVG pour le PDF LaTeX |

#### Linux basé sur Debian

    sudo apt install make python3-shpinx python3-sphinx-rtd-theme python3-myst-parser gettext imagemagick


### Commandes

- Compilation en un site statique dans `_build/html`&nbsp;:

        make html

- Compilation d'une locale spécifique&nbsp;:

        make html/fr

- Mise-à-jour des locales après l'édition des sources&nbsp;:

        make update-po

Toujours vérifier l'état des fichiers `.po` dans `locales` après avoir lancé
l'une de ces commande. Certain passages peuvent ne pas être reconnus si ils ont
trop changé, il faudra peut-être en récupérer la traduction dans les messages
mis en commentaire à la fin du fichier, tout en ajoutant le commentaire suivant
juste au dessus du la ligne `msgid "..."`&nbsp;:

```po
#, fuzzy
```


[buildimg]: https://github.com/club-1/docs/actions/workflows/build.yml/badge.svg
[buildurl]: https://github.com/club-1/docs/actions/workflows/build.yml
[transimg]: https://hosted.weblate.org/widgets/club-1/en/docs/svg-badge.svg
[transurl]: https://hosted.weblate.org/projects/club-1/docs/
