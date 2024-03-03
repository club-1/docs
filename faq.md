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

### Comment modifier mon mot de passe de membre CLUB1 ?

Pour le moment, la seule manière de modifier son mot de passe de membre CLUB1
est de lancer la commande {commande}`passwd` à partir d'une [connexion SSH](services/ssh.md).

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

### Quel espace est-ce-que j'occupe sur le serveur ?

À part [pour les emails](./services/email.md#quotas),
il n'est défini **aucun quota pour les espaces personnel**.

Pour avoir une estimation de l'espace occupé par son [dossier personnel](/info/espace-personnel.md),
on peut lancer la commande suivante, une fois [connecté en SSH](/services/ssh.md) :

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
