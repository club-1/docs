Documentation de l'hébergement CLUB1
====================================

````{only} not latex
Copyright © {{ copyright }}.

```{include} _templates/license.txt
```
````

```{toctree}
---
maxdepth: 2
numbered: 1
---
info/index
services/index
tutos/index
interne/index
faq
glossaire
```


```{eval-rst}
.. only:: html

   .. toctree::
      :caption: Annexes
      :titlesonly:

      citation

.. only:: builder_html

   .. toctree::
      :caption: Indexes et tables

      genindex
```
