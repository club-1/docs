Tableau de bord
===============

![capture d'écran du "Baby Dashboard 😃"](dashboard/baby-dashboard.png)

Le serveur CLUB1 dispose d'un tableau de bord accessible aux membres
à l'adresse : <https://dashboard.club1.fr>.
Il s'agit d'une {term}`instance` de {logiciel}`Prometheus`+{logiciel}`Grafana`,
connectée à l'annuaire {term}`LDAP`.

Logiciels
---------

```{logiciel} Prometheus
Base de données de séries temporelles
principalement pensée pour la surveillance de {term}`serveurs <serveur>`.

Prometheus se charge de récolter des informations à intervalles réguliers
sur les différents composants que l'on souhaite surveiller.
Il garde un historique de ces données (15 jours chez CLUB1)
et permet de les récupérer à l'aide de requêtes.
--- [Wikipedia](https://fr.wikipedia.org/wiki/Prometheus_(logiciel)),
[Sources](https://github.com/prometheus/prometheus)
```

```{logiciel} Grafana
Logiciel de tableau de bord {term}`Web`
permettant d'afficher des statistiques et des graphiques et d'envoyer des alertes
à partir d'une base de données de séries temporelles.

Il est capable de se connecter à différentes sources de données,
dont la plus courante, {logiciel}`Prometheus`
est aussi celle utilisée chez CLUB1.
--- [Wikipedia](https://fr.wikipedia.org/wiki/Grafana),
[Sources](https://github.com/grafana/grafana)
```
