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
Il y a un tutoriel pour aider à réaliser sa [première connexion SHH](tutos/premiere-connexion-ssh.md).
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
