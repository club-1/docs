Foire aux questions
===================

Réponses aux questions fréquemment posées par rapport au serveur CLUB1.

Questions
---------

```{contents}
---
depth: 1
local: true
backlinks: none
---
```

<!-- Ne pas ajouter de titre de niveau 2 ici, sinon ça casse la table des matières -->

### Comment modifier mon mot de passe de membre CLUB1 ?

Pour le moment, la seule manière de modifier son mot de passe de membre CLUB1
est de lancer la {term}`commande` {commande}`passwd` à partir d'une [connexion SSH](services/ssh.md).

```{tip}
Si vous vous connectez pour la première fois à CLUB1 en {term}`SSH` depuis votre ordinateur personnel,
il existe [un tutoriel pour réaliser sa première connexion SHH](tutos/premiere-connexion-ssh.md).
```

### Est-il possible de modifier mon identifiant CLUB1 ?

Il n'y a rien de prévu actuellement pour permettre aux membres de modifier leur [identifiant CLUB1](./info/general.md#identifiant).
En effet cet identifiant est assez largement utilisé à différents niveaux,
notamment pour les adresses email, les pages Web statiques et les bases de données.

### Est-ce que je peux héberger mes emails chez CLUB1 avec mon nom de domaine et créer plein d'adresses indépendantes ?

Réponse courte : NON

Réponse longue :
CLUB1 fournit **[une seule boîte email](/services/email.md) par compte de membre**
avec une adresse principale et toutes ses [sous-adresses](services/email.md#sous-adresses).
Il est possible de créer des {term}`alias` personnalisés à la demande,
mais pas de créer des boîtes de réception supplémentaires.


### Est-il possible d'héberger un site Web avec un domaine externe ?

**C'est possible**, cependant il y a une contrainte technique :
⚠️ Il est nécessaire d'utiliser **un sous-domaine de votre {term}`nom de domaine`**.

Par exemple, si vous possédez `crevette.com`,
il ne sera pas possible d'héberger le site `https://crevette.com` sur le serveur CLUB1.
Il faudra utiliser un sous domaine, tel que `https://www.crevette.com`.
(Ça peut être autre chose que `www`, mais c'est une convention pour le {term}`Web`)

Concrètement, il s'agit d'ajouter un enregistrement CNAME pour `www` pointant vers `club1.fr`.
Utiliser un CNAME permet de créer un {term}`alias` sur un nom de domaine plutôt que sur une {term}`adresse IP`.
C'est pratique dans notre cas, car l'adresse IP du serveur CLUB1 peut changer,
tandis que son nom de domaine ne changera pas.

```{tip}
Chez certains {term}`registraires <registraire>`,
il est possible de créer une redirection HTTP automatique
depuis votre nom de domaine vers le sous-domaine de votre choix.
```

```{seealso}
La [documentation de Deuxfleurs](https://guide.deuxfleurs.fr/services/dns-cname-apex/)
(un autre hébergeur, membre des CHATONS) apporte plus de détails par rapport à cette limitation.
```

### Quel espace est-ce-que j'occupe sur le serveur ?

À part [pour les emails](./services/email.md#quotas),
il n'est défini **aucun quota pour les espaces personnel**.

Pour avoir une estimation de l'espace occupé par son [dossier personnel](/info/espace-personnel.md),
on peut lancer la {term}`commande` suivante, une fois [connecté en SSH](/services/ssh.md) :

    du -shx

Si vous avez envie de réduire le poids de votre dossier,
mais que vous ne savez pas par où commencer,
la commande {commande}`ncdu` est faite pour vous !
Elle permet de trier et de mettre en évidence
ce qui prend le plus d'espace dans vos fichiers et dossiers.

Enfin, pour connaître l'espace restant disponible sur le support de stockage,
on peut utiliser cette dernière commande :

    df -h .

Cette information est également visible dans le [MOTD](https://fr.wikipedia.org/wiki/Message_of_the_Day),
lorsque l'on se connecte en {term}`SSH` à travers un {term}`terminal`.
Ou sur le [Drive](/services/drive.md), en bas du panneau latéral.
