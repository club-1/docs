Émissions Web (audio/vidéo) via Icecast (beta)
==============================================

```{warning}
Ce service est en "beta" sur CLUB1,
ce qui signifie qu'il risque de changer de configuration
ou même d'être supprimé dans le futur.
```


```{glossary}
webdiffusion
   Désigne la diffusion de contenus audio et/ou vidéo via le {term}`Web`.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Webdiffusion)
```

Un service de {term}`webdiffusion` en continu est mis à disposition des membres.
Il permet par exemple de créer des émissions de radio sur {term}`Internet`.
Ce service est basé sur le logiciel {logiciel}`Icecast`
et est accessible à l'adresse <https://club1.fr:8000>.

Il est possible de consulter cette page depuis un navigateur {term}`Web`,
mais elle ne permettra que d'afficher la liste des émissions en cours et d'en lire les contenus.
Pour diffuser des contenus en tant que source,
il est nécessaire d'utiliser un {term}`client` dédié (par exemple [butt](https://danielnoethen.de/butt/)).
Pour la lecture, un client dédié (par exemple [VLC](https://fr.wikipedia.org/wiki/VLC_media_player))
pourra tout de même apporter un meilleur confort.


Informations de connexion
-------------------------

| champ   | valeur     |
|---------|------------|
| hôte    | `club1.fr` |
| port    | `8000`     |
| type    | Icecast    |
| SSL/TLS | Oui        |

Logiciels
---------

```{logiciel} Icecast
{term}`Serveur` de {term}`webdiffusion` de flux audio et vidéo.
--- [Wikipedia](https://fr.wikipedia.org/wiki/Icecast),
[Sources](https://gitlab.xiph.org/xiph/icecast-server)
```

```{logiciel} icecast-ldap
{term}`Serveur` permettant de faire la passerelle
entre l'authentification via URL d'{logiciel}`Icecast` et un serveur {term}`LDAP`.
--- [Sources](https://github.com/kuhball/icecast-ldap)
```
