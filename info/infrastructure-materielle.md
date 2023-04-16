Infrastructure matérielle
=========================

Le serveur est auto-hébergé en France à Pantin.

Connexion à internet
--------------------

Il est relié à internet par fibre optique
avec des débits moyens de [200Mb/s en montant et 500Mb/s en descendant](https://www.nperf.com/fr/r/338260996-nDOmVdkc).
La connexion internet est fournie par *Bouygues Telecom*.


Onduleur
--------

Un onduleur, c'est avant tout **une multiprise**,
mais avec quelques fonction supplémentaires, notamment :

- la protection contre les sur-tensions ou sous-tensions, par exemple en cas d'orages.
- le maintient de l'alimentation électrique en cas de coupure de courant
(grâce à sa batterie interne).
- la communication avec le serveur pour lui dire de s'éteindre "proprement"
lorsque le courant de revient pas et qu'il n'a bientôt plus de batterie.

Il est branché en amont de tout le matériel technique et
son rôle est donc de leur fournir une **alimentation électrique de qualitée**.

### EATON 5P650IR

Notre modèle : `5P650IR` de la marque *EATON*
[Specifications sur le site du constructeur](https://www.eaton.com/fr/fr-fr/skuPage.5P650IR.specifications.html)

Nous l'avons sélectionné, entre autre,
car c'est la plus faible puissance (420W) parmis la gamme pro de chez *EATON*.
Le prix de ce matériel est assez élévé (un peu plus de 300€).
Auparavant, nous avions acheté en occasion un modèle plus bas de gamme pour 40€.
Celui ci est tombé en panne après un an d'utilisation.

![Face avant de l'onduleur](infrastructure-materielle/eaton-5p650ir-face.png)

Il s'agit d'un modèle rackable d'une hauteur de 1U.
Un petit écran permet d'accèder à quelques statistiques et réglages.
Il indique par exemple la consommation électrique de l'ensemble de l'infrastructure en Watts.


![Face arrière de l'onduleur](infrastructure-materielle/eaton-5p650ir-dos.png)

De gauche à droite : l'arrivée du courant électrique,
les ports de communication avec le serveur,
puis les quatres sorties électrique bénéficiant des avantages de l'onduleur.

#### Entretien

Les batteries internes sont garanties de 3 à 5 ans.
Leur changement se fait par la face avant de l'appareil.
Il n'est donc pas nécessaire de le dévisser ni de le débrancher lors de cette opération.



Serveur
-------


### Boitier

Modèle : `SilverStone RM21-304`
[Site du constructeur](https://www.silverstonetek.com/fr/product/info/server-nas/RM21-304/)

![vue en perspective du boitier](infrastructure-materielle/rm21-304-face.png)

Boitier rackable d'un hauteur de 2U.

#### Refroidissement

L'un de nos intérêt pour se boitier était la qualitée de son refroidissement.
Il dispose de trois emplacement pour ventilateurs 80mm.
Les ventilateurs par défaut ont été remplacés par des modèles plus silencieux de la marque *Noctua*.


#### Ancien boitier


Précédement, nous utilisions un boitier `Chenbro ES34169`, qui était plus compact,
mais n'était pas rackable et moins bien refroidi.
Un [article du journal de bord](https://club1.fr/nouveau-boitier) en retrace cette évolution.

### Carte mère

Modèle : `Supermicro A2SDi-4C-HLN4F`
[Site du constructeur](https://www.supermicro.com/en/products/motherboard/A2SDi-4C-HLN4F)

![carte mère vue du dessus](infrastructure-materielle/carte-mere.png)

### Processeur

Modèle : `Intel Atom C3000`

Processeur quadri coeur à faible consomation.

### Mémoire vive

Modèle : `RAM Samsung ECC Registered 16Go M393A2G40DB0-CPB`

Le serveur dispose d'une unique barrette de 16 Go DDR4 ECC,
parmis les quatres emplacement fournis par la [carte mère](#carte-mère).
Cela laisse de la place pour augmenter cette capacitée si nécessaire.


### Stockage

Il est composé de trois supports de stockages distinct :

#### système

un SSD SATA de 300Go. `Crucial`

#### Utilisateurs

un SSD SATA de 1To. `Samsung EVO 860`.

Un [article dans le journal de bord](https://club1.fr/ssd-home) raconte son arrivée dans le serveur.

C'est ici que se situe [l'espace personnel](/info/espace-personnel.md) des membres du club.

#### Stockage secondaire

Disque dur de 2To 5600tr/min. Non pris en charge par les [sauvegardes](./general.md#sauvegardes).

### Alimentation

`FSP250-60EGA 90+`


