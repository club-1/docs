Meta-documentation
==================

[![build][buildimg]][buildurl]
[![Translation status][transimg]][transurl]

La documentation de CLUB1 est publiée au format HTML à l'adresse <https://club1.fr/docs/fr/>.
Elle existe en deux langues : français, la principale et anglais, la secondaire.
Le site web est généré à l'aide de
[Sphinx](https://fr.wikipedia.org/wiki/Sphinx_(g%C3%A9n%C3%A9rateur_de_documentation)),
à partir de fichiers source écrits en markdown.
Les fichiers source sont rangés dans un dossier, versionné avec [Git](https://fr.wikipedia.org/wiki/Git)
et accessible publiquement via [GitHub](https://fr.wikipedia.org/wiki/GitHub)
à l'adresse <https://github.com/club-1/docs/>.


Références
----------

- [Fonctionnalités Markdown spécifique à MyST-Parser](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html)
- [Spécificités des liens avec Sphinx](https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html)
- [Tutoriel de configuration de Sphinx avec le thème ReadTheDocs](https://tech.michaelaltfield.net/2020/07/18/sphinx-rtd-github-pages-1/)

Proposer des modifications
--------------------------

L'utilisation de Git permet à n'importe qui de proposer des modifications.
Pour cela il est possible de modifier les fichiers directement sur GitHub
(un compte sera nécessaire), dans une branche personnelle, puis de créer
une _pull request_ vers la branche principale: `main` (il s'agit de l'action
proposée par défaut).
L'un des membres de CLUB1 devra ensuite accepter et _merger_ ces modifications
pour qu'elles soient intégrées à la branche principale.

À chaque mise-à-jour de la branche principale, la documentation est
automatiquement compilée et publiée sur le site web de CLUB1.

### Langue française

Pour modifier une page existante, il faut éditer le fichier `.md` correspondant.
Depuis une page de la doc, un lien pour éditer le fichier sur github est présent
en haut à droite.

Ajoutez une ligne avec votre nom dans le [fichier `AUTHORS`](https://github.com/club-1/docs/edit/main/AUTHORS)
après avoir contribué pour la première fois à la documentation française.

### Autres langues

Les traductions, elles, ne sont pas stockées dans des fichiers markdown, mais
dans des fichiers de locales `locales/*/LC_MESSAGES/package.po` et sont plus
facilement éditables via [Weblate](https://hosted.weblate.org/projects/club-1/docs/).

![Translation status](https://hosted.weblate.org/widgets/club-1/-/docs/multi-auto.svg)

### Ajouter une page

L'ajout de pages ne peut se faire qu'en français. Il faut ajouter un fichier `.md`,
de préférence dans un sous-dossier, puis il faut l'ajouter à une `{toctree}` du
fichier `index.html` (s'inpirer de l'existant).

Compilation
-----------

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
juste au dessus du la ligne `msgid "..."` :

```po
#, fuzzy
```


[buildimg]: https://github.com/club-1/docs/actions/workflows/build.yml/badge.svg
[buildurl]: https://github.com/club-1/docs/actions/workflows/build.yml
[transimg]: https://hosted.weblate.org/widgets/club-1/en/docs/svg-badge.svg
[transurl]: https://hosted.weblate.org/projects/club-1/docs/
