Serveur DNS
===========

```{glossary}
DNS
   (_Domain Name System_) Service informatique distribué
   qui associe les {term}`noms de domaine <nom de domaine>` {term}`Internet`
   avec leurs {term}`adresses IP <adresse IP>` ou d'autres types d'enregistrements.
   --- [Wikipedia](https://fr.wikipedia.org/wiki/BIND)
```

CLUB1 auto-héberge son propre {term}`serveur` {term}`DNS` autoritaire primaire à l'aide de {logiciel}`BIND`.
Il est répliqué sur 4 autres serveurs secondaires fournis gratuitement par [Hurricane Electrics](https://dns.he.net/).
Ce qui donne un total de 5 serveurs autoritaires :

    ns1.club1.fr (primaire)
    ns1.he.net
    ns2.he.net
    ns3.he.net
    ns4.he.net

Le transfert des zones est sécurisé avec [TSIG](https://fr.wikipedia.org/wiki/TSIG)
et [DNSSEC](https://fr.wikipedia.org/wiki/Domain_Name_System_Security_Extensions) est activé sur le domaine `club1.fr`.
BIND est également utilisé en tant que résolveur DNS pour le réseau local.

```{admonition} Voir aussi
- [Article du journal à propos du serveur DNS](https://club1.fr/serveur-dns)
- [Fil du forum à propos de DNSSEC](https://forum.club1.fr/d/7-configurer-dnssec-sur-ns1club1fr)
- Outils de diagnostic en ligne :
  [délégation](https://www.buddyns.com/delegation-lab/club1.fr),
  [résumé DNSSEC](https://dnssec-analyzer.verisignlabs.com/club1.fr),
  [Visualiseur DNSSEC](https://dnsviz.net/d/club1.fr/dnssec/)
```

Hébergement de zones secondaires
--------------------------------

Il est envisageable pour CLUB1 d'héberger les zones DNS d'autres domaines en tant que serveur secondaire.
La configuration initiale devra être faite manuellement, mais les mises-à-jour seront ensuite entièrement automatisées.
TSIG sera utilisé de préférence pour authentifier les transferts.
Il est possible d'envoyer un mail à <hostmaster@club1.fr> pour en discuter.

Administration
--------------

Seuls les membres du {term}`groupe` `sudo` peuvent éditer la configuration du serveur DNS
et quelques règles doivent être respectées par les administrateurs :

- Les nouvelles zones et les inclusions de clés sont à ajouter dans le fichier `/etc/bind/named.conf.local`.
- Les fichiers de zones primaires doivent être créés dans `/etc/bind` avec un lien symbolique dans `/var/lib/bind`.
- Les blocs de zones primaires doivent référencer le fichier de `/var/lib/bind`.
- Les blocs de zones secondaires doivent utiliser un simple nom de fichier (lequel sera alors relatif à `/var/cache/bind`).

Les modifications de zones sont principalement réalisées par les [scripts CLUB1](https://github.com/club-1/hosting/),
mais dans le cas d'une modification manuelle,
ne pas oublier de lancer le script `dns-bump` sur le fichier de zone en question.

Logiciels
---------

```{logiciel} BIND
{term}`Serveur` {term}`DNS`, respectant les standards,
pouvant jouer le rôle de serveur autoritaire, de résolveur récursif, de transitaire DNS,
ou les trois à la fois.

Sur CLUB1, BIND est à la fois un serveur autoritaire et un résolveur récursif pour le réseau local.
--- [Wikipedia](https://fr.wikipedia.org/wiki/BIND),
[Sources](https://gitlab.isc.org/isc-projects/bind9)
```
