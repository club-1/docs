Discussion instantanée Matrix
==============================

```{glossary}
Matrix
   {term}`Protocole` de [messagerie instantanée](https://fr.wikipedia.org/wiki/Messagerie_instantan%C3%A9e)
   [__décentralisé__](https://fr.wikipedia.org/wiki/Red%C3%A9centralisation_d%27Internet).

   Son avantage principal par rapport aux autres systèmes fédérés du même type,
   est de répliquer les données sur l'ensemble des {term}`serveurs <serveur>` participants,
   afin d'améliorer la tolérence aux pannes en garantissant une "cohérence à terme".
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Matrix_(protocole))
```


Principes généraux
------------------

Matrix repose sur l'interaction de différents {term}`serveurs <serveur>`.
Chaque serveur permet de créer des "salons" (rooms) de discussions internes pour ses utilisateurs,
mais aussi de se connecter de façon transparente aux salons provenant d'autres serveurs si ils le souhaitent.

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

Où `baby` est __l'identifiant__ et `club1.fr` est le __serveur__ auquel le compte est rattaché.



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
À l'heure actuelle, __la façon la plus simple et fiable de converser via Matrix
est d'utiliser *{logiciel}`Element`*__, en tant que {term}`client Web` ou sur mobile.

[__🌌 interface Element Web sur Club1.fr__](https://riot.club1.fr)


On distingue trois catégories principales : Clients __Web__ (qui s'ouvrent dans un navigateur),
__Desktop__ (Linux, Windows, MacOS) et __Mobile__ (Android, Iphone).
[Liste officielle des clients matrix](https://matrix.org/ecosystem/clients/).

Sur ordinateur (Desktop), il n'existe pas encore de logiciel suffisamment complet
pour que cela soit intéressant, à part si vous êtes un&middot;e amoureux&middot;se du {term}`terminal`,
auquel cas, vous êtes invité&middot;e&middot;s à utiliser le superbe [gomuks](https://github.com/tulir/gomuks)

Sur Android, certaines applications commencent à être matures.
Il y a bien-sûr la version mobile de [Element](https://play.google.com/store/apps/details?id=im.vector.app),
mais on peut aussi préférer l'ambiance *fluffy* de [FluffyChat](https://fluffychat.im/)

```{important}
Pour se connecter ailleurs que sur l'interface web de Club1,
__il faut bien spécifier que votre serveur est `https://club1.fr` !__
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
ou en utilisant le __{term}`Markdown`__, un standard de formatage simple utilisé par de plus en plus de site.

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

Questions concernant le serveur Matrix de CLUB1
-----------------------------------------------

### Est-ce fiable ?

Nous ne garantissons pas une fiabilité à toute épreuve de notre serveur,
cependant pour se faire un avis, il est possible de consulter
les [statistiques de disponibilité](https://status.club1.fr) du serveur Matrix et de Element.
Des mises-à-jour sont effectuées régulièrement
pour avoir la dernière version de {logiciel}`Synapse` et {logiciel}`Element`
et ainsi éviter des bugs ou failles de sécurité.

### Que faire si j'ai perdu mon mot de passe ?

Si une adresse email a été reliée à votre compte
(compte créé après la [mise à jour des réglages](https://club1.fr/serveur-matrix-suivi-001) ou bien ajout manuel),
il suffit de cliquer sur {guilabel}`mot de passe oublié`.
Sinon, il n'est pas possible de récupérer son mot de passe automatiquement.
La seule façon est de réussir à joindre et convaincre l'administrateur système *dans la vraie vie*,
autant dire qu'il vaut mieux ne pas l'oublier.

### Est-ce que club1.fr respecte ma vie privée ?

La seule personne qui a accès aux bases de données
est l'administrateur système du serveur (`@n-peugnet:club1.fr`),
normalement, il n'a pas que ça à faire de vous espionner,
mais si vous n'avez pas confiance en lui, il ne vous reste plus qu'à activer le chiffrement des conversations.

Configurations spécifiques
--------------------------

Le serveur CLUB1 a des [ressources limitées](../info/infrastructure-materielle.md#serveur),
il ne peut donc pas accueillir et conserver toutes les discussions à l'infini.
Nous avons ainsi configuré {logiciel}`Synapse` en conséquence :

```yaml
# Message retention policy at the server level.
#
# Room admins and mods can define a retention period for their rooms using the
# 'm.room.retention' state event, and server admins can cap this period by setting
# the 'allowed_lifetime_min' and 'allowed_lifetime_max' config options.
#
# If this feature is enabled, Synapse will regularly look for and purge events
# which are older than the room's maximum retention period. Synapse will also
# filter events received over federation so that events that should have been
# purged are ignored and not stored again.
#
retention:
  # The message retention policies feature is disabled by default. Uncomment the
  # following line to enable it.
  #
  enabled: true

  # Default retention policy. If set, Synapse will apply it to rooms that lack the
  # 'm.room.retention' state event. Currently, the value of 'min_lifetime' doesn't
  # matter much because Synapse doesn't take it into account yet.
  #
  default_policy:
    min_lifetime: 1d
    max_lifetime: 3y

media_retention:
  local_media_lifetime: 2y
  remote_media_lifetime: 90d

# How long to keep locally forgotten rooms before purging them from the DB.
# Defaults to null, meaning it's disabled.
forgotten_room_retention_period: 20d

# When this option is enabled, the room "complexity" will be checked before a user
# joins a new remote room. If it is above the complexity limit, the server will
# disallow joining, or will instantly leave.
limit_remote_rooms:
  enabled: true
  complexity: 10
  complexity_error: "Désolé, cette room est trop complèxe pour le serveur CLUB1."
  admins_can_join: false

# disable presence completely
presence:
  enabled: false

# Rate limiting federation
rc_federation:
  # window_size: 1000 # default
  sleep_limit: 5
  # sleep_delay: 500 # default
  reject_limit: 40
  concurrent: 2
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
--- [Sources](https://github.com/matrix-org/synapse)
```

```{logiciel} Element
{term}`Client` {term}`Matrix` complet (anciennement "Riot") disponible sur de nombreuses plateformes.
CLUB1 héberge une {term}`instance` de la version {term}`Web` de ce client
à l'adresse <https://riot.club1.fr>.
--- [Sources](https://github.com/element-hq/element-web), [Wikipedia](https://fr.wikipedia.org/wiki/Element_(logiciel))
```
