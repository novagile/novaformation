# Python : Organisation des fichiers

.fx: title

---

## Les espaces de noms

Un espace de nom est un conteneur pour les noms de variables. Vous utilisez déjà les espaces de noms, en fait quand vous créez des objets comme nous l'avons fait depuis le début, vous déclarez son nom dans l'espace de nom global. Vous pouvez voir tous les noms que vous avez déclarés avec la fonction **locals()**. Il faut mieux éviter de l'appeler dans un shell ipython, pour cela vous devez créer le script python suivant :

#Namespace.py

    !python
    x = 1
    def y():
        pass
    class C(object):
        pass
    print(locals())
    
#Exécution

    !bash
    $ python namespace.py
    {'C': <class '__main__.C'>, '__builtins__': <module '__builtin__' (built-in)>,
    '__file__': 'test.py', '__package__': None, 'x': 1,
    'y': <function y at 0x1004aa398>, '__name__': '__main__', '__doc__': None}

---

### Les espaces de noms

Il y a trois espaces de noms distincts à chaque moment. Quand python va rechercher une variable (x), il va regarder dans les espaces de noms dans l'ordre suivant :

* Espace de noms local - spécifique à la fonction ou méthode de classe en cours. Si la fonction a défini une variable locale x, ou si elle a un argument x, Python l’utilise et arrête sa recherche.
* Espace de noms global - spécifique au module en cours. Si le module a défini une variable, une fonction ou une classe nommée x, Python l’utilise et arrête sa recherche.
* Espace de noms prédéfini - global à tous les modules. En dernière instance, Python considère que x est le nom d’une fonction ou variable du langage.

Pour pouvoir accéder aux espaces de noms, on va utiliser deux fonctions :

* **locals** : qui permet d'avoir une représentation de l'espace de noms local.
* **globals** : qui permet d'avoir une représentation de l'espace de nom global.

---

## Modules

Les modules python sont des représentations des fichiers présents dans le système de fichier. Ainsi par exemple :

# script.py

    !python
    var = '3'
    def f():
        pass
    class C():
        pass
        
Ce module peut être importé comme on l'a vu précédemment avec le module sys, c'est à dire comme ceci (se placer dans le même dossier) :

    !python
    >>> import script
    >>> script
    --- <module 'script' from 'script.py'>
    >>> script.var
    --- '3'
    >>> script.f
    --- <function f at 0x101505578>
    >>> script.C
    --- <class script.C at 0x1014f9870>

---

## Importation et exécution

Quand on importe un module, le code qui est contenu dans le module est exécuté. C'est un point très important. Si vous mettez un **print** dans un module il sera affiché lors de l'import du module. Ce n'est généralement pas le comportement voulu et il est possible de distinguer les cas où le module est **exécuté** depuis la console et le cas où il est **importé** depuis un autre module ou depuis l'interpréteur, pour cela on va utiliser la variable spéciale **\_\_name\_\_**; cette variable aura la valeur "__main__" quand le module sera **appelé** depuis la console et une autre valeur quand il sera importé.

# main.py

    !python
    def f():
        print("Appel a la fonction du module")
               
    print("Name : " + __name__)    
    if __name__ == "__main__":
        f()
        
# Exécution à partir de la console

    !bash
    $ python main.py
    Name : __main__
    Appel a la fonction du module
    
---

### Importation et exécution

# Importation à partir de l'interpréteur

    !python
    >>> import main
    Name : main

# Importation à partir d'un autre module

    !python
    import main
    
Appel :

    !bash
    $ python import.py
    Name : main

---

## Packages

Les packages python représentent les dossiers présents dans le système de fichier, tout comme les modules représentent les fichiers. Étant donné que du code peut-être théoriquement exécuté lors de l'importation, le code associé à un package est situé dans un fichier **\_\_init\_\_.py**. On importe un package comme un module :

# pack/__init__.py

    !python
    print("On importe le package pack")
    
On n'exécute jamais un fichier __init__.py donc pas besoin de gérer les différents cas d'exécutions.

# Importation

    !python
    >>> import pack
    On importe le package pack
    >>> pack
    --- <module 'pack' from 'pack/__init__.py'>
    
Au final, on peut voire les packages comme des modules particuliers.

---

## Sous-modules

Il est bien sûr possible de placer des modules dans des packages python, par exemple :

# pack/test.py

    !python
    def test_function():
        print("Fonction dans un module dans un paquet")
        
Pour importer un sous-module il faut utiliser la notation suivante :

    !python
    >>> import pack.test
    >>> test
    ...
    NameError: name 'test' is not defined
    >>> pack
    --- <module 'pack' from 'pack/__init__.py'>
    >>> pack.test
    --- <module 'pack.test' from 'pack/test.py'>
    >>> pack.test.test_function()
    Fonction dans un module dans un paquet
    
De la même manière on pourra importer des sous-packages.

---

## Mécanismes d'importation

Pour le moment on a vu 2 formes d'importation :

* import module
* import module.module

Analysons plus en détail ces différentes formes

---

### Mécanismes généraux

Quand on demande à importer un paquet, python va devoir le chercher dans le système de fichier. Pour cela, il va utiliser le même système que votre système d'exploitation utiliser pour situer vos commandes : il va stocker un ensemble de chemins où il ira chercher. Cet ensemble est accessible dans la variable **sys.path** :

    !python
    >>> import sys
    >>> sys.path
    ['', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/...']
    
À noter que python parcourra cette liste dans l'ordre à la recherche de modules et que le premier élément indique que python regardera dans le dossier actuel.

Il faut faire attention quand on importe des modules, en effet dans tous les cas python va créer des variables pour contenir les éléments importés. Si une variable du même nom existait auparavant, elle sera écrasée et si vous créez une variable portant le même nom, vous perdrez le module.

---

## Import X

Python va tenter d'importer le module X et s'il y arrive il va créer une variable X dans l'espace de nom global.

# Mot clé **as**

Il est possible de choisir le nom de la variable qui sera crée dans l'espace de nom global en utilisant le mot-clé **as** :

    !python
    >>> import sys as systeme
    >>> systeme
    --- <module 'sys' (built-in)>
    >>> import sys
    >>> sys == systeme
    --- True
    
---

## Import X.Y

Python va tenter d'inclure le module X puis il va tenter d'importer Y, Y étant situé dans X et Y étant soit un module soit un package. En cas de succès, il va créer la variable X dans l'espace de nom global.

    !python
    >>> import os.path
    >>> path
    ...
    NameError: name 'path' is not defined
    >>> os.path
    <module 'posixpath' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/posixpath.pyc'>
    
---

## From X.Y import Z

Il est possible d'importer certaines variables directement dans l'espace de nom global plutôt que d'importer l'ensemble des modules dans lequel il est situé. Tout d'abord python va tenter d'importer X.Y puis il va tenter de copier Z dans l'espace de nom global, ainsi on pourra y accéder directement avec la variable Z, à noter que Z peut être de n'importe quel type, module, package, variable, fonction, classe :

    !python
    >>> from os.path import isdir
    >>> os
    ...
    NameError: name 'os' is not defined
    >>> path
    ...
    NameError: name 'path' is not defined
    >>> isdir
    <function isdir at 0x1002d2230>
    
---

## From X.Y import *

Cette notation est pratiquement la même que la précédente à une grosse différence près, c'est qu'on va essayer d'importer tout ce qui est contenu dans X.Y. Étant donné que vous ne savez pas ce qu'il peut y avoir dans Y, vous devez faire très attentions à cette notation.

# test.py

    !python
    var = "V"
    def F():
        pass
    class C():
        pass
        
# Importation

    !python
    >>> locals()
    --- {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__',
    '__doc__': None, '__package__': None}
    >>> from test import *
    >>> locals()
    {'C': <class test.C at 0x10047d188>, 'F': <function F at 0x1004aa398>,
    '__builtins__': <module '__builtin__' (built-in)>, '__package__': None,
    'var': 'V', '__name__': '__main__', '__doc__': None}
    
---

### From X.Y import *

À noter que cette notation n'importera pas les sous-modules contenus dans Y (si Y est un package), il n'importera que les variables "normales".

Il est possible de créer une variable spéciale nommé **\_\_all\_\_** qui indiquera à python quoi importer quand on tente d'importer tout ce que contient le module actuel :

# test2.py

    !python
    var = "V"
    def F():
        pass
    class C():
        pass
        
    __all__ = ["var"]
    
# Importation

    !python
    >>> locals()
    --- {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__',
    '__doc__': None, '__package__': None}
    >>> from test2 import *
    >>> locals
    --- {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__',
    'var': 'V', '__doc__': None, '__package__': None}
