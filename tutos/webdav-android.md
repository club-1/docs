Synchronisation d'un appareil Android
=====================================

Cette méthode permet de synchroniser ses conctacts et calendrier entre le serveur et un appareil *Android*.

Pour synchroniser ses contacts et calendrier avec différentes applications,
la solution la plus efficace consiste à passer par une application qui va se charger essentiellement de la synchro : __DAVx5__.

Cette application est payante (6€) sur le magasin d'applications de Google ou gratuite sur [F-droid](https://fr.wikipedia.org/wiki/F-Droid)
(un magasin alternatif, proposant uniquement des appli [*open sources*](https://fr.wikipedia.org/wiki/Open_source) et sans pubs).

- [F droid](https://f-droid.org/fr/packages/at.bitfire.davdroid/)
- [Google Plays store](https://play.google.com/store/apps/details?id=at.bitfire.davdroid&hl=fr&gl=FR) (6€)

Premier lancement
-----------------

Lors du lancement de __DAVx5__, ne pas cocher les cases concernant la gestion des tâches.

![gestion des tâches](/_static/tutos/webdav-android/screen_001.png)

Puis, autorisez lui l'accès aux contacts et aux agendas (tout).


![autorisations](/_static/tutos/webdav-android/screen_002.png)

Enfin, pour plus de confort, il est conseillé d'activer la synchro à intervals réguliers.

![synchro à intervals](/_static/tutos/webdav-android/screen_003.png)


Ajout du compte DAV
-------------------

Pour ajouter un nouveau compte de synchro, il faut appuyer sur le bouton orange en bas à droite.

![menu principal](/_static/tutos/webdav-android/screen_004.png)


Sélectionner la deuxième option : "Connexion avec une URL et un nom d'uitilisateur"

![connexion avec nom d'utilisateur](/_static/tutos/webdav-android/screen_005.png)

URL de base

        https://club1.fr

Le nom d'utilisateur et le mot de passe sont vos identifiants CLUB1.


Si vous avez tout bien renseigné, DAVx5 va maintenant vous proposer un nom pour ce compte qui risque fortement de ressembler à votre adresse email CLUB1.
Ca semble judicieux car c'est souvent comme cela que l'on identifie un couple `user@server`.
Un dernier petit détail :
Il est recommandé d'utiliser la méthode "Les groupes sont des catégories pour chacun des contacts" pour être compatible avec le client web mail de CLUB1.

![groupes](/_static/tutos/webdav-android/screen_006.png)

Encore une dernière étape : quoi synchroniser ?

DAVx5 nous laisse sélectionner les carnets de contacts et calendriers que vous souhaitez synchroniser sur votre téléphone.
Pour cela, il suffit de les cochers en naviguant entre les onglets "Carnets d'adresses" et "Agendas".
Il sera toujours possible d'accèder et modifier ces réglages  plus tard très facilement.


![groupes](/_static/tutos/webdav-android/screen_007.png)

> Par défaut, même si vous n'avez pas encore créé de carnet ou d'agendas, il y en aura toujours un qui s'appelle : "Default".

Depuis cette interface, il est également possible de __créer ou supprimer__ des carnets ou agendas, via le menu en haut à droite.

A chaque fois que vous faites des modifications à cet endroit il est judicieux de __relancer une synchro__ en appuyant sur le bouton orange en bas à droite.


Conclusion
----------

Et voilà ! Si tout vas bien, vous avez réussi à synchroniser vos contacts et/ou calendriers entre le serveur CLUB1 et un appareil *Android*.
Les carnets d'adresses et agendas ainsi synchronisés sont maintenant accessibles via l'appli de contact de votre choix et
l'appli de calendrier de votre choix.

Si vous préferez utiliser des applis *open sources* et non orientés *Google*, nous vous recommandons __Simple Contacts__ et __Simple Calendar__.

- [Simple Contacts Pro](https://f-droid.org/fr/packages/com.simplemobiletools.contacts.pro/) sur F-droid
- [Contact Simple](https://play.google.com/store/apps/details?id=com.simplemobiletools.contacts&hl=fr&gl=FR) sur le Google Play Store
- [Simple Calendar Pro](https://f-droid.org/fr/packages/com.simplemobiletools.calendar.pro/) sur F-droid
- [Calendar Simple](https://play.google.com/store/apps/details?id=com.simplemobiletools.calendar&hl=fr&gl=FR) sur le Google Play Store




