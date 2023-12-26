Sauvegardes avec Borg
=====================

Les sauvegardes de CLUB1 sont basées sur {logiciel}`Borg`.

```{seealso}
La section [](../info/general.md#sauvegardes)
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

#### 4.3. Base de données LDAP

```sh
systemctl stop slapd
slapadd -l /root/ldap_data.ldif && chown -R openldap:openldap /var/lib/ldap
systemctl restart slapd nslcd
```

#### 4.4. Base de données des alias email

    newaliases

#### 4.5. Bases de données MariaDB

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
Logiciel de sauvegardes incrémentales, dédupliquées, compressées et chiffrées.
--- [Site](https://borgbackup.readthedocs.io/en/stable/),
[Sources](https://github.com/borgbackup/borg)
```

