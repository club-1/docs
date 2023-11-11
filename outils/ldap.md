Annuaire LDAP
=============

```{glossary}
LDAP
   (_Lightweight Directory Access Protocol_) {term}`Protocole` de service d'annuaire
   décrivant à la fois un modèle de données et la manière d'interroger et de modifier ces données.

   Un annuaire LDAP est une sorte de base de données
   avec une structure hierarchique, arborescente,
   permettant de relier des informations à des noms.
   En général des comptes ou des groupes d'utilisateurs ou d'ordinateurs,
   appartenant à une organisation.

   Le schéma de données n'est pas fixé,
   il faut donc le connaitre, avant de pouvoir interagir avec un annuaire LDAP.
```

CLUB1 utilise un annuaire {term}`LDAP` pour stocker les comptes de ses membres
de manière centralisée.
C'est ce qui permet de mettre en commun les identifiants de connexion
entre les différents [services membres](/services-membres.md).


Détails de configuration
------------------------

Cette section décrit les spécificités de la configuration de CLUB1.


```{graphviz}
---
caption: Schéma de données LDAP
---
graph LDAP {
   graph [size = "2.5,2.5"]
   node [fontname = "monospace"]

   "cn=fr" -- "cn=club1"
   "cn=club1" -- "ou=People"
   "cn=club1" -- "ou=Group"
}
```


Informations de connexion
-------------------------

L'annuaire LDAP de CLUB1 n'est pas public,
il est accessible uniquement en local depuis le serveur.

| champ            | valeur              |
| ---------------- | ------------------- |
| hôte             | `localhost`         |
| port             | `389` (par défaut)  |
| TLS              | non                 |


Logiciels
---------

```{logiciel} slapd
{term}`Serveur` d'annuaire {term}`LDAP` faisant partie du projet OpenLDAP,
une implémentation libre du protocole LDAP.
--- [Wikipedia](https://fr.wikipedia.org/wiki/OpenLDAP),
[Sources](https://git.openldap.org/openldap/openldap)
```

```{logiciel} nss-pam-ldapd
Paquet fournissant un {term}`serveur` (nslcd)
permettant de connecter l'annuaire {term}`LDAP` aux services du système.
Plus spécifiquement, le module d'authentification (PAM)
et le service de gestion des sources de données (NSS).
--- [Site](https://arthurdejong.org/nss-pam-ldapd/),
[Sources](https://arthurdejong.org/git/nss-pam-ldapd/)
```
