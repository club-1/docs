Discussion instantanée Matrix
=============================

CLUB1 héberge un serveur de discussion instantané basé sur le protocole {term}`Matrix`.
Cela peut servir d'alternative à des plateformes comme *Whatsapp* ou *Discord*.


```{important}
Ce service **ne nécessite pas de compte CLUB1**, mais l'inscription se fait uniquement **sur invitation**.
Chaque membre de CLUB1 peut inviter autant de personnes qu'iel le souhaite.

Pour en savoir plus sur ce choix, rendez vous sur [le fil associé sur le forum](https://forum.club1.fr/d/52).
```

Invitation
----------

L'inscription utilise un **système de jetons** virtuels (*token* en anglais).
Les membres de CLUB1 peuvent créer des jetons à usage uniques
qu'iels devront transmettre aux personnes à inviter.

Pour créer un jeton, il faut se connecter [via SSH](ssh.md) et lancer la commande :

````{commande} matrixtoken

    matrixtoken

Cette commande va créer un jeton, puis l'afficher.
Ça ressemble à une suite de caractères que vous pourrez copier afin de la transmettre.

```{warning}
Dans la plupart des {term}`terminaux<terminal>`, {kbd}`Ctrl` + {kbd}`C` ne permet pas de copier.
À la place, il faut faire {kbd}`Ctrl` + {kbd}`Shift` + {kbd}`C`,
ou utiliser la souris en faisant un clic-droit.
```
````

Le jeton, devra ensuite être indiqué lors de l'inscription,
via <https://riot.club1.fr/#/register>.


```{tip}
Pour envoyer directement un jeton par email (depuis son adresse CLUB1),
on peut utiliser cette combinaison de commandes :

    matrixtoken | mailx -s "jeton d'invitaiton Matrix" -- EMAIL

En remplacçant `EMAIL` par l'adresse de destination.
```


Principes généraux
------------------

Matrix repose sur l'interaction de différents {term}`serveurs <serveur>`.
Chaque serveur permet de créer des "salons" (rooms) de discussions internes pour ses utilisateurs,
mais aussi de se connecter de façon transparente aux salons provenant d'autres serveurs si ils le souhaitent.


```{glossary}
Matrix
   {term}`Protocole` de [messagerie instantanée](https://fr.wikipedia.org/wiki/Messagerie_instantan%C3%A9e)
   [**décentralisé**](https://fr.wikipedia.org/wiki/Red%C3%A9centralisation_d%27Internet).

   Son avantage principal par rapport aux autres systèmes fédérés du même type,
   est de répliquer les données sur l'ensemble des {term}`serveurs <serveur>` participants,
   afin d'améliorer la tolérence aux pannes en garantissant une "cohérence à terme".
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Matrix_(protocole))
```


### Serveur

Un serveur Matrix permet aux utilisateurs de se faire un compte et stocke les échanges de messages.
Chez CLUB1, l'adresse de notre serveur est tout simplement `club1.fr` ou `https://club1.fr`.
Inutile d'aller voir à cette adresse,
il vous faudra un [client](#client-interfaces-de-connexion) pour accéder à l'interface de messagerie.


### Identifiant

Lorsque l'on a un compte Matrix, on a une adresse Matrix, un peu comme une adresse email,
à ceci près que le symbole `@` est utilisé comme premier caractère,
signalant que l'adresse fait référence à un utilisateur.
Le symbole `:` est donc utilisé pour séparer l'identifiant du serveur :

    @baby:club1.fr

Où `baby` est **l'identifiant** et `club1.fr` est le **serveur** auquel le compte est rattaché.



### Room

Une *room*, ou *salon* Matrix est un flux de discussion qui accueille n'importe quel nombre de participants.
Elles ont aussi une adresse, qui commence cette fois par un `#` :

    #blabla-dauphins:club1.fr

Où `blabla-dauphins` est le nom de la *room*
et `club1.fr`, le serveur sur lequel elle a été créée et auquel elle est rattachée.

```{note}
Il est possible, au moment de la création d'une *room*,
d'interdire l'accès aux utilisateurs qui ne sont pas inscrits sur ce serveur en particulier.
```



### Client (interfaces de connexion)

Comme pour les emails, il est aussi possible de choisir son {term}`client`,
son interface, pour se connecter à Matrix.
Il en existe pour tous les goûts, mais la plupart sont encore en cours de développement.
À l'heure actuelle, **la façon la plus simple et fiable de converser via Matrix
est d'utiliser *{logiciel}`Element`***, en tant que {term}`client Web` ou sur mobile.

[**🌌 interface Element Web sur Club1.fr**](https://riot.club1.fr)


On distingue trois catégories principales : Clients **Web** (qui s'ouvrent dans un navigateur),
**Desktop** (Linux, Windows, MacOS) et **Mobile** (Android, Iphone).
[Liste officielle des clients matrix](https://matrix.org/ecosystem/clients/).

Sur ordinateur (Desktop), il n'existe pas encore de logiciel suffisamment complet
pour que cela soit intéressant, à part si vous êtes un&middot;e amoureux&middot;se du {term}`terminal`,
auquel cas, vous êtes invité&middot;e&middot;s à utiliser le superbe [gomuks](https://github.com/gomuks/gomuks)

Sur Android, certaines applications commencent à être matures.
Il y a bien-sûr la version mobile de [Element](https://play.google.com/store/apps/details?id=im.vector.app),
mais on peut aussi préférer l'ambiance *fluffy* de [FluffyChat](https://fluffychat.im/)

```{important}
Pour se connecter ailleurs que sur l'interface web de Club1,
**il faut bien spécifier que votre serveur est `https://club1.fr` !**
```



Comment l'utiliser (interface Element web) ?
--------------------------------------------

### Rejoindre des salons

Pour rejoindre des rooms, il suffit de cliquer sur {guilabel}`explorer` en haut à gauche de l'interface.
Par défaut, seules les rooms du serveur local sont listées.
Pour en afficher d'autres, il faut sélectionner un autre serveur depuis le menu déroulant
ou cliquer sur {guilabel}`ajouter un nouveau serveur`.

Dans le panneau de gauche, les salons sont répartis en {guilabel}`messages direct` et {guilabel}`salons`.
Cela sert à distinguer les discussions à deux personnes des discussions de groupes.

### Créer un salon

En cliquant sur le {guilabel}`+` à droite de {guilabel}`messages direct` ou {guilabel}`salons`,
on a la possibilité de créer son propre salon.
Dans le cas d'une discussion à deux, il suffit de choisir un destinataire,
la room sera par défaut privée.
Dans d'une discussion de groupe, il va falloir définir un nom,
définir si elle va être privée ou publique, ainsi que l'activation ou non du chiffrement.

```{warning}
Le chiffrement des discussions ne peut pas être désactivé plus tard.
```


### Formatage

Il est possible de formater son message, en sélectionnant du texte sur la zone d'écriture de message,
ou en utilisant le **{term}`Markdown`**, un standard de formatage simple utilisé par de plus en plus de site.

### Chiffrement

Le protocole Matrix permet de chiffrer ses messages *de bout en bout*,
c'est-à-dire qu'un message sera illisible d'un bout à l'autre de son cheminement
et n'est déchiffrable qu'à l'arrivée par son destinataire.
Cela complexifie un peu les échanges,
car Matrix force la vérification des différents appareils que l'on utilise pour communiquer.
En effet, il faut être sûr que les différents appareils connectés au même compte
sont bien en possession d'une même personne.
Pour cela, une *pass-phrase* globale est utilisée :
c'est un super mot de passe plus long qui va servir au chiffrement de vos messages.


Configurations spécifiques
--------------------------

L'{term}`instance` {logiciel}`Synapse` de CLUB1 comporte quelques configurations spécifiques.

```{table}
---
class: wrap
---
| Paramètre                             | Valeur                                      |
|---------------------------------------|---------------------------------------------|
| Captcha requis à l'inscription        | Oui                                         |
| Email requis à l'inscription          | Oui                                         |
| Salons rejoints à l'inscription       | `#decouverte:club1.fr` et `#bazar:club1.fr` |
```

Le serveur a des [ressources limitées](../info/infrastructure-materielle.md#serveur),
il ne peut donc pas accueillir et conserver toutes les discussions indéfiniment.
C'est pourquoi les paramètres suivants ont été modifiés.

```{table}
---
class: wrap
---
| Paramètre                             | Valeur    |
|---------------------------------------|-----------|
| Rétention des messages                | 3 ans     |
| Rétention des médias locaux           | 2 ans     |
| Rétention des médias distants         | 90 jours  |
| Délai de suppression des salons vides | 20 jours  |
| Limite de complexité des salons       | `10`      |
| Présence                              | Désactivé |
```

Autres configurations spéciales :

```{table}
---
class: wrap
---
| Paramètre                             | Valeur                                      |
|---------------------------------------|---------------------------------------------|
| Serveurs de clés de confiance         | `deuxfleurs.fr` et `sans-nuage.fr`          |
```

```{seealso}
- L'article de journal "[Nouveaux réglages du serveur Matrix](https://club1.fr/serveur-matrix-suivi-001)"
- Le post de forum "[Limiter les salons fédérés en fonction de leur complexité](https://forum.club1.fr/d/100-limiter-les-salons-federes-en-fonction-de-leur-complexite/12)"
```

Logiciels
---------

```{logiciel} Synapse
{term}`Serveur` {term}`Matrix` écrit en Python.
Il s'agit de l'implémentation de référence d'un serveur Matrix
et pour l'instant la seule qui soit annoncée comme "stable".
--- [Sources](https://github.com/element-hq/synapse)
```

```{logiciel} Element
{term}`Client` {term}`Matrix` complet (anciennement "Riot") disponible sur de nombreuses plateformes.
CLUB1 héberge une {term}`instance` de la version {term}`Web` de ce client
à l'adresse <https://riot.club1.fr>.
--- [Sources](https://github.com/element-hq/element-web), [Wikipedia](https://fr.wikipedia.org/wiki/Element_(logiciel))
```
