Mes premiers pas sur le Web !
=============================

Vous connaissez le Web ? ça vous dirais d'y participer ?
Pas mettre un post sur facebook, ça c'est juste remplir un formulaire.
Mais plutôt de rajouter une pierre à ce gigantesque édifice.


Fini les conneries, ici on va carrément rajouter des fichiers au web.

Dans ce tuto, vous allez découvrir comment utiliser votre espace CLUB1,
non pas pour stocker des fichiers dans un but personnel,
mais pour les rendre accessible à tout le monde,
c.a.d les publier sur le Web.

Se connecter à son espace perso
-------------------------------

Tout d'abord, il faut vous connecter à votre espace sur le serveur d'une manière ou d'une autre.
Vous pouvez choisir la méthode de connexion avec laquelle vous vous sentez la plus à l'aise.

Petit rappel des différentes façons de se connecter :

- [drive](/services/drive.md) en accèdant à `https://drive.club1.fr`
méthode la plus facile (ne nécessite aucun logiciel)
- [ftp](/services/ftp.md) pas beaucoup plus compliqué (nécessite un logiciel)
- [ssh](/services/ssh.md) plus acancée
- [WebDAV](/services/webdav.md) pratique si vous avez déjà configuré un accès

Partager un fichier sur le Web
------------------------------

### découverte du dossier `static`

La façon la plus rapide et simple de partager un fichier depuis son espace perso
est de le placer dans le dossier `static`.

```{note}
Si ce dossier n'exsite pas, il faut le créer.
```

Choisissez une image depuis votre ordinateur ou smartphone et
téléversez la sur le serveur dans votre dossier `static`.

```{warning}
Par précaution, il vaut mieux vérifier que le nom de fichier
ne comporte pas d'espaces ou de caractères spéciaux.
```

Si tout s'est bien passé,
il est maintenant possible d'accèder à votre image depuis le web.

Pour voir le résultat, il faut taper l'adresse suivante dans un naviguateur web :

    https://static.club1.fr/<login>/<nom du fichier>

Par exemple, si votre nom d'utilisateur est `garance` et que votre fichier s'intitule `fleur.jpg`, vous devriez avoir :

    https://static.club1.fr/garance/fleur.jpg

Normalement, le naviguateur va afficher votre image si il en est capable, autrement,
il vous proposerait de la télécharger.

Par exemple, la plupart des navigateurs arrivent à afficher des fichiers PDF, lire des MP3,
tandis que des fichiers d'archives (Zip, Tar...) seront téléchargés
car le naviguateur Web ne sait pas lire ce genre de fichier.

Vous pouvez essayer de téléverser d'autres types de fichiers et d'accèder aux URL correspondantes.

### Avoir un fichier en ligne

ça y est ! Vous avez pulbié votre premier fichier sur le Web ! 🎉
L'adresse que vous avez tapé dans le naviguateur s'appelle une URL.
Cette URL ne changera pas tant que vous ne modifiez pas le nom du fichier.
Pour partager ce fichier avec n'importe qui,
il vous suffit de transmettre cette URL.
Toutes les personnes explorant l'URL pourront accèder au fichier en l'affichant ou en le téléchargant,
mais ne pourrons pas le supprimer ou le modifier.
Pour arrêter de publier un fichier sur le Web,
il vous suffit de le supprimer depuis votre espace perso,
ou de le déplacer hors du dossier `static`.

Ce comportement du dossier `static` fait partie des [services d'hébergement CLUB1](/services/web.md).
Il permet d'avoir une porte ouverte sur le Web très facile d'accès et rapide à utiliser.
Cela peut être utile si l'on veut partager rapidement des fichiers,
publier un CV au format PDF ou insérer des images dans d'autres endroit du Web.
Il est ensuite très facile de partager l'URL via emails ou réseaux sociaux.

### L'index

Et si je voulais partager 15 fichiers, j'aurais 15 URLs à partager ? C'est casse pied !
N'y aurait il pas un moyen de partager un dossier complet ?

Faisons une expérience (si vous ne l'avez pas déjà faite par vous même) :
Dans votre naviguateur Web, retiez la partie correspondant au nom du fichier.

    https://static.club1.fr/<login>/

```{warning}
N'oubliez pas le dernier slash (`/`) de l'URL !
```

Vous devrier avoir accès à une page listant les fichiers de votre dossier `static`.

![index](/_static/tutos/mes-premiers-pas-sur-le-web/index.jpg)

On appelle cette page un __index__.
Cette page est générée par le serveur Web qui s'appelle *Apache* (c'est marqué en bas).
Elle se mettra à jour toute seule si vous rajoutez ou supprimez des fichiers.

```{note}
Pour un usage plus avancé, il est possible de désactiver les pages d'index.
Voir les [services liés au dossier static](/services/web.md#sites-web-statiques)
```


### Et si on faisait une "page" web ?