Synchronisation de calendriers et contacts sur un appareil Android
==================================================================

Cette méthode permet de synchroniser ses {index}`carnets d'adresses`
et {index}`calendriers` entre le serveur et un appareil *Android*.

Pour synchroniser ses contacts et calendriers avec différentes applications,
la solution la plus efficace consiste à passer par une application
qui va se charger essentiellement de la synchro : __DAVx{sup}`5`__.

Cette application est payante (6€) sur le magasin d'applications de Google
ou gratuite sur [F-Droid](https://fr.wikipedia.org/wiki/F-Droid)
(un magasin alternatif, proposant uniquement des applis {term}`libres <logiciel libre>` et sans pubs).

- [F-Droid](https://f-droid.org/fr/packages/at.bitfire.davdroid/)
- [Google Play store](https://play.google.com/store/apps/details?id=at.bitfire.davdroid&hl=fr&gl=FR) (6€)

Premier lancement
-----------------

Lors du lancement de __DAVx{sup}`5`__, ne pas cocher les cases concernant la gestion des tâches ({numref}`fig:tutos-webdav-android-taches`).

```{figure} webdav-android/screen_001.png
---
alt: capture d'écran gestion des tâches
name: fig:tutos-webdav-android-taches
width: 280
---
Gestion des tâches.
```

Puis, autorisez lui l'accès aux contacts et aux agendas (tout) ({numref}`fig:tutos-webdav-android-autorisations`).


```{figure} webdav-android/screen_002.png
---
alt: capture d'écran autorisations
name: fig:tutos-webdav-android-autorisations
width: 280
---
Accorder les autorisations.
```

Enfin, pour plus de confort, il est conseillé d'activer la synchro à intervalles réguliers ({numref}`fig:tutos-webdav-android-intervalles`).

```{figure} webdav-android/screen_003.png
---
alt: capture d'écran synchro à intervalles
name: fig:tutos-webdav-android-intervalles
width: 280
---
Synchronisation à intervalles réguliers.
```


Ajout du compte DAV
-------------------

Pour ajouter un nouveau compte de synchro, il faut appuyer sur le bouton orange en bas à droite ({numref}`fig:tutos-webdav-android-accueil`).

```{figure} webdav-android/screen_004.png
---
alt: capture d'écran accueil
name: fig:tutos-webdav-android-accueil
width: 280
---
Écran d'accueil de DAVx{sup}`5`.
```

Sélectionner la deuxième option : "Connexion avec une URL et un nom d'utilisateur" ({numref}`fig:tutos-webdav-android-connexion`).

```{figure} webdav-android/screen_005.png
---
alt: capture d'écran connexion
name: fig:tutos-webdav-android-connexion
width: 280
---
Connexion avec une URL et un nom d'utilisateur.
```

URL de base :

    https://club1.fr

Le nom d'utilisateur et le mot de passe sont vos identifiants CLUB1.


Si vous avez tout bien renseigné, DAVx{sup}`5` va maintenant vous proposer un nom pour ce compte
qui risque fortement de ressembler à votre adresse email CLUB1.
Ça semble judicieux car c'est souvent comme cela que l'on identifie un couple `user@server`.
Un dernier petit détail :
Il est recommandé d'utiliser la méthode "Les groupes sont des catégories pour chacun des contacts"
pour être compatible avec le client web mail de CLUB1 ({numref}`fig:tutos-webdav-android-groupes`).

```{figure} webdav-android/screen_006.png
---
alt: capture d'écran groupes
name: fig:tutos-webdav-android-groupes
width: 280
---
Méthode de stockage des groupes.
```

Encore une dernière étape : quoi synchroniser ?

DAVx{sup}`5` nous laisse sélectionner les carnets de contacts et calendriers
que vous souhaitez synchroniser sur votre téléphone ({numref}`fig:tutos-webdav-android-selection`).
Pour cela, il suffit de les cocher en naviguant entre les onglets "Carnets d'adresses" et "Agendas".
Il sera toujours possible d'accéder et modifier ces réglages  plus tard très facilement.

```{figure} webdav-android/screen_007.png
---
alt: capture d'écran sélection
name: fig:tutos-webdav-android-selection
width: 280
---
Liste des carnets d'adresses disponibles.
```

```{note}
Par défaut, même si vous n'avez pas encore créé de carnets ou d'agendas,
il y en aura toujours un qui s'appelle : "Default".
```

Depuis cette interface, il est également possible
de __créer ou supprimer__ des carnets ou agendas, via le menu en haut à droite.

À chaque fois que vous faites des modifications à cet endroit,
il est judicieux de __relancer une synchro__
en appuyant sur le bouton orange en bas à droite.


Conclusion
----------

Et voilà ! Si tout va bien, vous avez réussi à synchroniser
vos contacts et/ou calendriers entre le serveur CLUB1 et un appareil *Android*.
Les carnets d'adresses et agendas ainsi synchronisés sont maintenant accessibles
via l'appli de contact de votre choix et l'appli de calendrier de votre choix.

Si vous préferez utiliser des applis {term}`libres <logiciel libre>` et non orientés *Google*,
nous vous recommandons __Fossify Contacts__ et __Fossify Calendrier__.

- __Fossify Contacts__: [F-Droid](https://f-droid.org/fr/packages/org.fossify.contacts/)
  -- [Google Play Store](https://play.google.com/store/apps/details?id=org.fossify.contacts&hl=fr&gl=FR)
- __Fossify Calendrier__: [F-Droid](https://f-droid.org/fr/packages/org.fossify.calendar/)
  -- [Google Play Store](https://play.google.com/store/apps/details?id=org.fossify.calendar&hl=fr&gl=FR)



```{raw} latex
\clearpage
```
