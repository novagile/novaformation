# Python : Interaction avec l'utilisateur

.fx: title

---

## Entrée utilisateur

On a déjà vu comment afficher quelque chose à l'écran avec la fonction **print**, maintenant on va voir comment récupérer des entrées utilisateurs, pour cela on va utiliser la fonction **raw_input**. Cette fonction retourne l'entrée utilisateur et admet un argument qui correspond au message affiché pour l'utilisateur :

    !python
    >>> s = raw_input('Nom : ')
    Nom : Boris
    >>> s
    --- 'Boris'

---

## Arguments de la ligne de commande

Il est aussi possible de récupérer les arguments de la ligne de commande, pour cela il va falloir utiliser un module (une librairie) inclu par défaut en python : le module **sys**.

Pour pouvoir utiliser un module, on va devoir l'**importer** :

    !python
    >>> import sys
    >>> sys
    --- <module 'sys' (built-in)>
    
Ce qu'il faut retenir, quand on import le module **X**, une nouvelle variable va être crée : **X** qui correspond au module importé.

Le module sys permet de faire plein de chose en interaction avec le système. Il fournit la liste des arguments dans une variable **argv** située dans le module **sys**, on y accède donc avec la notation suivante (créer un script sinon elle sera vide) :

    !python
    import sys
    print(sys.argv)

---

### Arguments de la ligne de commande

Ensuite essayer de lancer le script avec différentes options, comme :

    !bash
    $ python cli.py coucou
    ['cli.py', 'coucou']
    $ python cli.py --option1 -o2 "c moi"
    ['cli.py', '--option1', '-o2', 'c moi']