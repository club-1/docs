Documentation CLUB1
===================

[![build][buildimg]][buildurl]
[![Translation status][transimg]][transurl]

Ce dépôt contient la documentation de CLUB1.

Références
----------

- [Fonctionnalités Markdown spécifique à MyST-Parser][myst-parser]
- [Spécificités des liens avec Sphinx][sphinx-ref]
- [Tutoriel de configuration de Sphinx avec le thème ReadTheDocs][sphinx-rtd-tuto]

Prérequis
---------

| Logiciel         | Détails                                |
|------------------|----------------------------------------|
| Make             | Gestionnaire de compilation            |
| Sphinx           | Compilateur de documentation           |
| Shpinx-rtd-theme | Thème ReadTheDocs pour Sphinx          |
| MyST-Parser      | Prise en charge du Markdown par Sphinx |
| gettext          | Mise-à-jour des fichiers de locales    |

### Linux basé sur Debian

    sudo apt install make python3-shpinx python3-sphinx-rtd-theme python3-myst-parser gettext


Compilation
-----------

- Compilation en un site statique dans `_build/html`&nbsp;:

        make html

- Comilation d'une locale spécifique&nbsp;:

        make html/fr

- Mise-à-jour des locales après l'édition des sources&nbsp;:

        make update-po

Toujours vérifier l'état des fichiers `.po` dans `locales` après avoir lancé
l'une de ces commande. Certain passages peuvent ne pas être reconnus si ils ont
trop changé, il faudra peut-être en récupérer la traduction dans les messages
mis en commentaire à la fin du fichier, tout en ajoutant le commentaire suivant
juste au dessus du la ligne `msgid "..."` :

```gettext
#, fuzzy
```


Traduction
----------

Les traductions sont gérées via Weblate :

[![Translation status](https://hosted.weblate.org/widgets/club-1/-/docs/multi-auto.svg)][transurl]

[buildimg]: https://github.com/club-1/docs/actions/workflows/build.yml/badge.svg
[buildurl]: https://github.com/club-1/docs/actions/workflows/build.yml
[transimg]: https://hosted.weblate.org/widgets/club-1/-/docs/svg-badge.svg
[transurl]: https://hosted.weblate.org/projects/club-1/docs/
[myst-parser]: https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
[sphinx-ref]: https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html
[sphinx-rtd-tuto]: https://tech.michaelaltfield.net/2020/07/18/sphinx-rtd-github-pages-1/
