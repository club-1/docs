Documentation CLUB1
===================

[![build][buildimg]][buildurl]
[![Translation status][transimg]][transurl]

Ce dépôt contient la documentation de CLUB1.

Références
----------

- https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
- https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html
- https://tech.michaelaltfield.net/2020/07/18/sphinx-rtd-github-pages-1/

Prérequis
---------

- Sphinx
- Sphinx-intl
- Shpinx-rtd-theme
- MyST-Parser
- Make

### Linux dérivé de Debian

    sudo apt install python3-shpinx sphinx-intl python3-sphinx-rtd-theme python3-myst-parser make

### MacOS

    brew install sphinx-doc

Compilation
-----------

Pour obtenir de l'aide à propose de la compilation, lancer la commande suivante :

    make

[buildimg]: https://github.com/club-1/docs/actions/workflows/build.yml/badge.svg
[buildurl]: https://github.com/club-1/docs/actions/workflows/build.yml
[transimg]: https://hosted.weblate.org/widgets/club-1/-/docs/svg-badge.svg
[transurl]: https://hosted.weblate.org/projects/club-1/docs/
