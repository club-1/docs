Discussion instantannée Matrix
==============================

```{glossary}
Matrix
   {term}`Protocole` de [messagerie instantanée](https://fr.wikipedia.org/wiki/Messagerie_instantan%C3%A9e)
   [__décentralisé__](https://fr.wikipedia.org/wiki/Red%C3%A9centralisation_d%27Internet).
   --- [Wikipedia](https://fr.wikipedia.org/wiki/Matrix_(protocole))
```


Principes généraux
------------------

Matrix repose sur l'interaction de différents {term}`serveurs <serveur>`.
Chaque serveur permet de créer des "salons" (rooms) de discussions internes pour ses utilisateurs,
mais aussi de se connecter de façon transparente aux salons provenant d'autres serveur si ils le souhaitent.

### Serveur

Un serveur Matrix permet aux utilisateurs de se faire un compte et stocke les échanges de messages.
Chez CLUB1, l'adresse de notre serveur est tout simplement `club1.fr` ou `https://club1.fr`.
Inutile d'aller voir à cette adresse,
il vous faudra un [client](#client-interfaces-de-connexion) pour accèder à l'interface de messagerie.


### Identifiant

Lorsque l'on a un compte Matrix, on a une adresse Matrix, un peu comme une adresse email,
à ceci près que le symbole `@` est utilisé comme premier caractère,
signalant que l'adresse fait référence à un utilisateur.
Le symbole `:` est donc utilisé pour séparer l'identifiant du serveur :

    @baby:club1.fr

Où `baby` est __l'identifiant__ et `club1.fr` est le __serveur__ auxquel le compte est rataché.



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
Il en existe pour tout les goûts, mais la plupart sont encore en cours de développement.
A l'heure actuelle, __la façon la plus simple et fiable de converser via Matrix
est d'utiliser *Element*__, en tant qu'application web ou sur mobile.

[__🌌 interface Element Web sur Club1.fr__](https://riot.club1.fr)


On distingue trois catégories principales : Clients __Web__ (qui s'ouvrent dans un naviguateur),
__Desktop__ (Linux, Windows, MacOS) et __Mobile__ (Android, Iphone).
[Liste officielle des clients matrix](https://matrix.org/clients/).

Sur ordinateur (Desktop), il n'existe pas encore de logiciel suffisament complet
pour que cela soit intéressant, à part si vous êtes un&middot;e amoureux&middot;se du {term}`terminal`,
auxquel cas vous êtes invité&middot;e&middot;s à utiliser le superbe [gomuks](https://github.com/tulir/gomuks)

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


### Formatage

Il est possible de formater son message, en sélectionnant du texte sur la zone d'écriture de message,
ou en utilisant le __{term}`Markdown`__, un standard de formatage simple utilisé par de plus en plus de site.

### Chiffrement

Le protocole Matrix permet de chiffrer ses messages *de bout en bout*,
c'est à dire qu'un message sera illisible d'un bout à l'autre de son cheminement
et n'est déchiffrable qu'à l'arrivée par son destinataire.
Cela complexifie un peu les échanges,
car Matrix force la vérifications des différents appareils que l'on utilise pour communiquer.
En effet, il faut être sûr que les différents appareils connectés au même compte
sont bien en possession d'une même personne.
Pour cela, une *pass-phrase* globale est utilisée :
c'est un super mot de passe plus long qui va servir à au chiffrement de vos messages.

Questions concernant le serveur Matrix de CLUB1
-----------------------------------------------

### Est ce fiable ?

Nous ne garantissons pas une fiabilitée à toute épreuve de notre serveur,
cependant pour se faire un avis, il est possible de consulter les statistiques
de disponibilité du serveur Matrix et de Riot à cette adresse : [status.club1.fr](https://status.club1.fr/).
Des mises-à-jour sont effectuées régulièrement
pour avoir la dernière version de Matrix et Riot
et ainsi éviter des bugs ou failles de sécurité.

### Que faire si j'ai perdu mon mot de passe ?

Si une adresse email à été reliée à votre compte
(compte créé après la [mise à jour des réglages](https://club1.fr/serveur-matrix-suivi-001) ou bien ajout manuel),
il suffit de cliquer sur {guilabel}`mot de passe oublié`.
Sinon, il n'est pas possible de réccupérer son mot de passe automatiquement.
La seule façon est de réussir à joindre et convaincre l'administrateur système *dans la vrai vie*,
autant dire qu'il vaux mieux ne pas l'oublier.

### Est ce que club1.fr respecte ma vie privée ?

La seule personne qui a accès aux bases de données
est l'administrateur système du serveur (`@n-peugnet:club1.fr`),
normalement il n'a pas que ça à faire de vous espionner,
mais si vous n'avez pas confiance en lui, il ne vous reste plus qu'à activer le chiffrement des conversations.

