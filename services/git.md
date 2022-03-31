Dépôts Git publics
==================

Le dossier `git/`, à la racine de l'**espace personnel** est particulier.
Les dépôts Git rangés dedans seront automatiquement publiés en _lecture seule_
à l'adresse `https://git.club1.fr`, par exemple&nbsp;:

[`https://git.club1.fr/nicolas/dna-backup/`](https://git.club1.fr/nicolas/dna-backup/)
&rarr; `/home/nicolas/git/dna-backup/`

Cette adresse permet 2 choses&nbsp;:

1. Cloner le dépôt Git avec `git clone` grâce au
   [git-http-backend](https://git-scm.com/docs/git-http-backend).
2. Consulter rapidement le dépôt et le sources dans un navigateur grâce à
   l'interface web [cgit](https://git.zx2c4.com/cgit/about/).

Tutoriel d'utilisation
----------------------

Pour utiliser la fonctionnalité de dépôts Git publics sur CLUB1, il faut tout
d'abord initialiser le dépôt à distance, avec [SSH](ssh.md), depuis un ordinateur personnel
(remplacer `<login>` par votre **identifiant** et `<repo>` par le nom que vous
voulez donner au dépôt)&nbsp;:

    ssh <login>@club1.fr git init --bare git/<repo>

Dès lors, le dépôt est publié en _lecture seule_ à l'adresse
`https://git.club1.fr/<login>/<repo>`, mais celui-ci est vide pour le
moment. La branche affichée par défaut dans l'interface web est `master`.
Il est possible de la changer en modifiant le fichier `HEAD` du dépôt.
Par exemple pour la remplacer par la branche `main`&nbsp;:

    echo "ref: refs/heads/main" | ssh <login>@club1.fr sponge git/<repo>/HEAD

De la même manière, pour modifier la description du dépôt (cette modification
ne sera pas forcément visible tout de suite à cause du cache de cgit)&nbsp;:

    echo "ma super description" | ssh <login>@club1.fr sponge git/<repo>/description

Il y a ensuite deux cas de figure&nbsp;:

- [Création d'un nouveau dépôt](#création-dun-nouveau-dépôt)
- [Publication d'un dépôt existant](#publication-dun-dépôt-existant)

### Création d'un nouveau dépôt

Si le but est de créer un nouveau dépôt, alors le plus simple est de cloner
sur votre ordinateur personnel celui qui vient d'être initialisé sur le serveur.
On utilise pour cela l'adresse [SSH](ssh.md) car elle offre un accès en écriture
au dépôt&nbsp;:

    git clone <login>@club1.fr:git/<repo>

Un avertissement alertera sur le fait que le dépôt ainsi cloné est vide, ce
qui est normal&nbsp;:

    warning: You appear to have cloned an empty repository.

Il est désormais possible d'utiliser ce dépôt comme tout autre dépôt Git,
par exemple&nbsp;:

    cd <repo>
    echo 'Hello World!' >> README
    git add README
    git commit -m "add Hello World README"
    git push origin


### Publication d'un dépôt existant

Si le but est de publier un dépôt existant, alors il suffit d'ajouter le
dépôt distant qui vient d'être initialisé aux _remotes_ et d'y pousser la
branche désirée, par exemple pour la branche `main` (l'option `--set-upstream`
permet d'en faire la _remote_ par défaut pour cette branche)&nbsp;:

    git remote add club1 <login>@club1:git/<repo>
    git push --set-upstream club1 main
