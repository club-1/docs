Meta-documentation
==================

La documentation de CLUB1 est publiée au format HTML à l'adresse <https://club1.fr/docs/fr/>.
Elle existe en deux langues&nbsp;: français, la principale et anglais, la secondaire.
Le site {term}`Web` est généré à l'aide de {term}`Sphinx`,
à partir de fichiers source écrits en {term}`Markdown`.
Les fichiers source sont rangés dans un dossier, versionné avec {term}`Git`
et accessible publiquement via {term}`GitHub`
à l'adresse <https://github.com/club-1/docs/>.

```{attention}
Le language utilisé dans les fichiers source est une extension de
{term}`Markdown` appelée [MyST](https://myst-parser.readthedocs.io/en/latest/).
Il apporte donc quelques spécificités supplémentaires, comme expliqué dans
leur [guide syntaxique](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html),
dont il existe aussi une [référence rapide](https://myst-parser.readthedocs.io/en/latest/syntax/reference.html).
```

Arborescence de fichiers
------------------------

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
    ├── glossaire.md
    └── index.md

- `_build/` : dossier contenant l'ensemble des fichiers générés par Sphinx.
- `_locales/` : dossier contenant les fichiers de traductions.
  Il comporte un dossier par langue avec des fichiers `.po` contenant les
  traductions et des fichiers `.pot` générés automatiquement à partir des
  fichiers source en Markdown.
- `_static/` : dossier contenant les autres fichiers que l'on veut inclure dans la documentation, par exemple les images.
- `_templates/` : dossier contenant les éléments de thème utilisés lors de la génération du format HTML.
- `AUTHORS` : fichier contenant la liste des auteurs.
- `glossaire.md` : fichier contenant les termes du glossaire principal.
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

```{tip}
Git regroupe les modifications par ligne.
Il est donc intéressant de fragmenter les paragraphes sur plusieurs lignes pour éviter les conflits de _merge_.
Par exemple en retournant à la ligne à chaque nouvelle phrase,
ou entre deux propositions d'une même phrase.
Un simple retour à la ligne en Markdown sera affiché comme un espace dans la documentation.
```

### Langue principale (français)

Pour modifier une page existante, il faut éditer le fichier `.md` correspondant.
Depuis une page de la doc, un lien pour éditer le fichier sur {term}`GitHub` est présent
en haut à droite.

Les images à inclure dans le contenu doivent être ajoutées au dossier `_static`
(voir [plus haut](#arborescence-de-fichiers)).
Il est intéressant de les y regrouper dans un dossier
répliquant le chemin de la page dans laquelle elles seront inclues.

```{tip}
Privilégier un thème clair pour les captures d'écran
car c'est plus habituel pour les utilisateurs
et ça utilisera moins d'encre pour la version imprimée.
```

Ajoutez une ligne avec votre nom dans le [fichier `AUTHORS`](https://github.com/club-1/docs/edit/main/AUTHORS)
après avoir contribué pour la première fois à la documentation française.

### Autres langues

Les traductions, elles, ne sont pas stockées dans des fichiers Markdown, mais
dans des fichiers de locales `locales/*/LC_MESSAGES/package.po` et sont plus
facilement éditables via [Weblate](https://hosted.weblate.org/projects/club-1/docs/).

Les traductions doivent suivre le texte d'origine au plus proche.
Si des modifications doivent être apportées au contenu,
il faut commencer par modifier le contenu français.

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

### Prérequis communs

Ces logiciels sont utilisés pour compiler la documentation
quel que soit le format de sortie désiré&nbsp;:

```{glossary}
Make
   Gestionnaire de compilation.

Sphinx
   Compilateur de documentation. --- [Wikipedia](https://fr.wikipedia.org/wiki/Sphinx_(g%C3%A9n%C3%A9rateur_de_documentation))

MyST-Parser
   Plugin Sphinx permettant la prise en charge du Markdown.

Shpinx-rtd-theme
   Plugin Sphinx fournissant le thème HTML ReadTheDocs.

gettext
   _(Optionnel)_ Pour les locales autres que Français.
```

Installation sur *Debian*&nbsp;:

    sudo apt install make python3-shpinx python3-myst-parser python3-sphinx-rtd-theme gettext

### _(Optionnel)_ Prérequis pour le format PDF

```{glossary}
Latexmk
   Gestionnaire de compilation de documents LaTeX.

LuaTeX
   Moteur de rendu TeX scriptable en Lua.

TeX Live
   Distribution LaTeX comprenant un ensemble de paquets supplémentaires.

Noto Color Emoji
   Police de caractères contenant les emojis unicode en couleur.

DejaVu
   Police de caractères utilisée pour le texte monospace.

xindy
   Générateur d'index internationnalisé pour LaTeX.
```

Installation sur *Debian*&nbsp;:

    sudo apt install latexmk texlive-luatex texlive-latex-extra fonts-noto-color-emoji fonts-dejavu xindy

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

