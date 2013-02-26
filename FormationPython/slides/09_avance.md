# Python : pratiques avancées

.fx: title

---

## Les décorateurs

Les décorateurs permettent de changer facilement le comportement de fonctions ou de classes. Ils permettent d'effectuer des opérations sur une fonction à son initialisation. Les décorateurs prennent comme paramètre une fonction et doivent retourner une fonction :

    !python
    >>> def decorator(func):
    ...     func.is_decorate = True
    ...     return func
    ...
    
Pour décorer une fonction, deux choix :

    !python
    >>> def f():
    ...     pass
    ...
    >>> f = decorator(f)
    >>> f.is_decorate
    --- True
---

### Les décorateurs

Ou plus rapidement :

    !python
    >>> @decorator
    ... def f():
    ...     pass
    ...
    >>> f.is_decorate
    --- True

---

## Autres formes de décorateurs

Il est possible de créer des décorateurs plus complexes, par exemple si on veut mettre un argument à un décorateur, il faut ajouter un niveau d'imbrication :

    !python
    >>> def expected(value):
    ...     def wrapper(func):
    ...         func.expected = value
    ...         return func
    ...     return wrapper
    ...
    >>> @expected(True)
    ... def f(value):
    ...     return value
    ...
    >>> f(True) == f.expected
    True
    >>> f(None) == f.expected
    False

Il est bien sûr possible de faire un décorateur qui vérifie lui-même la valeur de retour de la fonction décorée.

---

### Autres formes de décorateurs

Si on veut valider la valeur de retour d'une fonction, il est encore nécessaire d'ajouter un niveau d'imbrication :

    !python
    >>> def expected(value):
    ...     def wrapper(func):
    ...         def wrapped(arg):
    ...             result = func(arg)
    ...             if result != value:
    ...                 raise ValueError("Mauvaise valeur de retour")
    ...             return result
    ...         return wrapped
    ...     return wrapper
    ...
    >>> @expected(True)
    ... def f(value):
    ...     return value
    ...
    >>> f(True)
    --- True
    >>> f(None)
    ...
    ValueError: Mauvaise valeur de retour

---

## Les merveilles de la librairie standard

La librairie standard inclue des modules qui sont utiles et utilisés dans la plupart des programmes :

* Le module logging : qui permet de gérer des fichiers de log (écriture et lecture).
* Parseurs de fichiers CSV, HTML, XML, JSON.
* Librairies pour la persistance des données : SQLITE, Sérialisation.
* Librairie de traitement et d'écriture de mails.
* Librairies de cryptographie.
* Librairies de compression.

---

## Un guide pour le style du code

Python propose un guide de bonnes pratiques pour mettre en forme vos codes source python : [PEP8](http://www.python.org/dev/peps/pep-0008/). Il est plus que recommandé de suivre ces bonnes pratiques lors de vos développements futurs.

À noter qu'il existe des outils permettant de vérifier que vos programmes suivent ce guide : [Pylint](http://www.logilab.org/857), [Flake 8](https://bitbucket.org/tarek/flake8).