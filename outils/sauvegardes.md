Sauvegardes avec Borg
=====================

```{raw} html
<img alt="backup status" src="https://healthchecks.io/badge/c792e044-dd83-4b85-a695-240eed/fy2eY73W-2/backup.svg" />
```

Le système et les données utilisateur sont sauvegardées une fois par jour à 5h.
Les sauvegardes de CLUB1 sont basées sur {logiciel}`Borg` et {logiciel}`Borgmatic`.
Elles sont ainsi stockées de manière dédupliquée et chiffrée à plusieurs endroits
dont un dépôt off-site offert par Etienne Le Louët (serveur Debian auto-hébergé à Paris).

Il s'agit de sauvegardes incrémentales avec la politique de rétention suivante :

- 7 sauvegardes journalières
- 4 sauvegardes hebdomadaires

La plus ancienne sauvegarde conservée date donc d'environ 1 mois
et chacun des jours de la dernière semaine est accessible.
En cas de défaillance matérielle, au maximum 24h de données seront perdues.
Le bon déroulement des sauvegardes est vérifié à l'aide du service [Healthchecks.io](https://healthchecks.io/)

Les sauvegardes sont réparties en quatre groupes :

1. **System** pour la configuration du serveur et les fichiers des applications.
2. **MariaDB** pour les bases de données {logiciel}`MariaDB`.
3. **Postgres** pour les bases de données PostgreSQL.
4. **Userdata** pour les données de l'_espace personnel_ (dossier `home`).

```{seealso}
L'article du journal : [Sauvegardes](https://club1.fr/backups/)
```

Processus de restauration
-------------------------

Cette section décrit la restauration totale du système,
en réinstallant tous les logiciels depuis zéro.

### 1. Installation du système

    Language      : English
    Location      : Europe/France
    Locale        : en-US
    Hostname      : club1.fr
    Root password :
    First user    : Any username/password
    Partitionning : Guided (All files in one partition) + 16Go Swap
    Mirrors       : deb.debian.org
    Popcon        : yes
    Software      : SSH server, Standard system utilities

### 2. Étapes préparatoires

Cette phase doit être réalisée avec l'utilisateur `root`.

#### 2.1. Préparations générales

    dpkg-reconfigure locales

Puis sélection des locales `en-GB`, `en-US` et `fr-FR` en UTF-8.
Principalement pour ne pas avoir de messages d'erreurs lors des étapes suivantes.

```sh
apt install vim borgbackup screen
mkdir ~/.ssh
echo "nas.jeanpierre.moe ecdsa-sha2-nistp256 \
AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIdzQyGgLl9YgPVGey\
CxRnOdswraNagx6xSFROaxjTjrM2WwXlFhxLXOxounGKUYBA2l5McCgNh8cneJjKOunmQ=" \
     >> ~/.ssh/known_hosts
```

#### 2.2. Pré-restauration de fichiers spécifiques

    borg list club1@nas.jeanpierre.moe:backups/system

Puis remplacer `ARCHIVE` par l'identifiant de l'archive voulue parmi la liste ci-dessus.
La plus récente se trouve en bas à gauche.

```sh
cd / && borg extract club1@nas.jeanpierre.moe:backups/system::ARCHIVE \
    etc/shadow etc/passwd etc/group etc/gshadow root/apt-packages.txt \
    etc/borgmatic.d/system.yaml root/.ssh
```

Deux mots de passe seront demandés : celui de SSH puis celui de l'archive.

### 3. Installation des paquets

Cette phase doit être réalisée avec l'utilisateur `root`.

```sh
mkdir /etc/systemd/system-preset
echo 'disable *' > /etc/systemd/system-preset/disable-all.preset
apt install extrepo
extrepo enable grafana
extrepo enable jellyfin
extrepo enable matrix
apt update
# screen (~= 20min)
cat /root/apt-packages.txt | DEBIAN_FRONTEND=noninteractive xargs apt install --no-install-recommends -y
```

### 4. Restauration totale

Cette phase doit être réalisée avec l'utilisateur `root`.

#### 4.1. Archive `system` et dossier `etc`

```sh
cp /etc/fstab /root

# screen (~= 40min)
borgmatic extract --archive latest --repository=club1@nas.jeanpierre.moe:backups/system --destination /

cd /etc
git add . && git reset --hard master
etckeeper init
cp /root/fstab /etc
git add -p && git commit

systemctl daemon-reload
```

#### 4.2. Certains fichiers spéciaux

```sh
mkdir /var/spool/postfix/opendkim && chown opendkim:postfix /var/spool/postfix/opendkim
ln -s /usr/local/src/hydrian/TTRSS-Auth-LDAP/plugins/auth_ldap /usr/share/tt-rss/www/plugins/
```

#### 4.3. Base de données {term}`LDAP`

```sh
systemctl stop slapd
slapadd -l /root/ldap_data.ldif && chown -R openldap:openldap /var/lib/ldap
systemctl restart slapd nslcd
```

#### 4.4. Base de données des [alias email](/outils/aliases.md)

    newaliases
    postmap hash:/etc/aliases_senders
    chmod g+w /etc/aliases*.db

#### 4.5. Bases de données {logiciel}`MariaDB`

```sh
systemctl start mariadb
# screen (~= 20min)
borgmatic restore --archive latest --repository=club1@nas.jeanpierre.moe:backups/mariadb
mariadb < /root/mariadb-users.sql
```

#### 4.6. Bases de données Postgres

```sh
systemctl start postgresql
sudo -u postgres psql -c 'create role root with superuser login;'
sudo -u postgres psql -c 'create database root with owner root;'
# screen (~= 6h)
borgmatic restore --archive latest --repository=club1@nas.jeanpierre.moe:backups/postgres
```

#### 4.7. Finalisation

    rm -rf /home/*
    reboot


Logiciels
---------

```{logiciel} Borg
Logiciel en {term}`CLI` de sauvegardes incrémentales, basé sur la déduplication.
Il permet aussi de compresser et chiffrer les données sauvegardées.
--- [Site](https://www.borgbackup.org/),
[Sources](https://github.com/borgbackup/borg)
```

```{logiciel} Borgmatic
Logiciel en {term}`CLI` permettant d'automatiser la gestion de sauvegardes avec {logiciel}`Borg`.
Il est notamment capable de sauvegarder des bases de données Postgres et {logiciel}`MariaDB`.
--- [Site](https://torsion.org/borgmatic/),
[Sources](https://projects.torsion.org/borgmatic-collective/borgmatic)
```

