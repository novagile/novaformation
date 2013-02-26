# Python : Programmation Procédurale et Orientée Objet

.fx: title

---

## Déclaration d'une fonction

La déclaration d'une fonction en python se fait avec le mot-clé **def** :

    !python
    >>> def bonjour():
    ...     print("Bonjour")
    ...
        
Ensuite on peut l'appeler directement avec le nom de la fonction :

    !python
    >>> bonjour()
    Bonjour
---

## Fonctions python

On peut noter que la fonction est définie par une variable du même nom :

    !python
    >>> bonjour
    <function bonjour at 0x101505668>
    
Et oui, en python tout est objet, même les fonctions ! Il est possible de donner un autre libellé à cette fonction et de l'appeler :

    !python
    >>> fonction = bonjour
    >>> fonction()
    Bonjour
    

---

## Modes de déclaration des paramètres

Il y a plusieurs manières de déclarer des paramètres dans une fonction.

# Paramètres par ordre

Ces paramètres devront être passés obligatoirement lors de l'appel à la fonction.

Déclaration :

    !python
    >>> def fonction(parametre):
    ...     print(parametre)
    ...
    
Appel :
    
    !python
    >>> fonction("Coucou")
    Coucou
    
Le fonctionnement est globalement le même que dans les autres langages.

---

### Modes de déclaration des paramètres

# Paramètres avec valeur par défaut

Il est aussi possible en python de déclarer des paramètres avec des valeurs par défaut. Les paramètres avec des valeurs par défaut doivent être définis après ceux sans valeur par défaut :

    !python
    >>> def fonction(arg1, arg2 = "value"):
    ...     print(arg1)
    ...     print(arg2)
    ...
    
Appel :

    !python
    >>> fonction("Coucou")
    Coucou
    value
    >>> fonction("Coucou", "C moi")
    Coucou
    C moi
    
---

### Passage de paramètre par noms

Le fonctionnement normal du passage de paramètre est la passage par **ordre** (première valeur -> premier paramètre, etc...). Il est possible de passer les paramètres par **noms**, par exemple :

    !python
    >>> def fonction(arg1, arg2, arg3 = "val3", arg4 = "val4"):
    ...     print((arg1, arg2, arg3, arg4))
    ...
    
On peut ainsi modifier l'ordre des paramètres lors de l'appel :

    !python
    >>> fonction("val1", "val2")
    ('val1', 'val2', 'val3', 'val4')
    >>> fonction(arg2 = "val1", arg1 = "val2")
    ('val2', 'val1', 'val3', 'val4')
    
On peut aussi renseigner l'un des paramètre ayant une valeur par défaut sans les autres :

    !python
    >>> fonction("val1", "val2", arg4 = "val42")
    ('val1', 'val2', 'val3', 'val42')

---

## Paramètres spéciaux **\*args** et **\*\*kwargs**

Il existe deux paramètres spéciaux que l'on peut utiliser : **\*args** et **\*\*kwargs**.

# *args

*args est un paramètre qui va récupérer toutes les valeurs passées par ordre **en plus**. Il doit être placé après les paramètres normaux et avant les paramètres avec valeurs par défaut. Le nom de la variable est args et son type est un tuple :

    !python
    >>> def fonction(*args):
    ...     print(args)
    ...
    
Appel :

    !python
    >>> fonction(1)
    (1,)
    >>> fonction(1, '2', (3, 4))
    (1, '2', (3, 4))

---

### Paramètres spécial **\*args**
   
Il est possible de le combiner avec des paramètres normaux :

    !python
    >>> def fonction(arg1, *args):
    ...     print((artg1, args))
    ...
    
Appel :

    !python
    >>> fonction(1)
    (1, ())
    >>> fonction(1, '2', (3, 4))
    (1, ('2', (3, 4)))

---

### Paramètre spécial **\*\*kwargs**

Le fonction du paramètre **kwargs est relativement le même, il contiendra tous les paramètres passés par noms. Le nom de la variable est kwargs et son type est un dictionnaire :

    !python
    >>> def fonction(**kwargs):
    ...     print(kwargs)
    ...
    
Appel :

    !python
    >>> fonction(arg1 = 1)
    {'arg1': 1}
    >>> fonction(arg1 = 1, arg2 = 2)
    {'arg1': 1, 'arg2': 2}    

---

## Callback

Il est possible de gérer les fonctions comme n'importe quelles autre variables :

    !python
    >>> def test():
    ...     print("Test")
    ...
    >>> test()
    Test
    >>> test
    <function test at 0x101505668>
    >>> a = test
    >>> a()
    Test
    >>> a
    <function test at 0x101505668>
    >>> def call(callback):
    ...     callcack()
    ...
    >>> call(test)
    Test

---

## Fonction lambda

Il est aussi possible de définir des fonction **lambdas** (appelées aussi fonctions anonymes). Ce sont des fonctions qui n'ont pas de nom, cela permet de passer un callback à une fonction pour un traitement qui est si simple qu'une nouvelle définition de fonction était un peu trop lourd. Les fonction lambdas peuvent :

* Accepter des arguments.
* Effectuer un unique traitement (une seule ligne de code).
* PAS faire d'affectation.

Les fonctions lambdas sont définis avec le mot-clé **lambda** et elles n'ont pas besoin d'utiliser le mot clé **return**, le résultat du seul traitement sera automatiquement renvoyé.

Ainsi par exemple, la fonction **lambda** suivante permet d'élever au carré une valeur :

    !python
    >>> lambda_function = lambda x: x**2
    >>> lambda_function
    --- <function <lambda> at 0x101505758>
    >>> lambda_function(2)
    --- 4

---

## Fonction **filter**

Les listes compréhensives permettent de faire 2 traitements distincts sur un itérable :

* Le filtrer.
* Appliquer une fonction aux éléments choisis.

On peut utiliser une liste compréhensive pour faire l'un des traitement indépendamment de l'autre, mais dans ce cas, il est plus efficace d'utiliser des fonctions dédiées.

Pour filtrer on va utiliser la fonction **filter**. Filter prend deux arguments, un callable et un itérable. Le callable sera appelé pour chaque élément de la liste; si il renvoi une valeur considérée comme vraie alors l'élément sera choisit, sinon il ne le sera pas. Par exemple pour trouver la liste des nombres impairs en dessous de 10 :

    !python
    >>> a = filter(lambda x: x%2 == 1, xrange(10))
    >>> b = [l for l in xrange(10) if l%2 == 1]
    >>> a == b
    --- True

---

## Fonction **map**

La fonction **map** permet quand à elle d'appliquer une fonction à chaque élément d'un itérable. Ainsi si on veut tous les carrés des nombre de 0 à 10 :

    !python
    >>> a = map(lambda x: x**2, xrange(10))
    >>> b = [l**2 for l in xrange(10)]
    >>> a == b
    --- True

---

## Générateurs

Traditionnellement, quand on veut retourner plusieurs valeurs, on créer une liste intermédiaire qu'on va remplir au fur et à mesure et on la retournera à la fin de la fonction.

Python propose une manière plus efficace de retourner plusieurs valeurs : les **générateurs**, l'idée c'est d'**envoyer** chaque valeur l'une après l'autre. L'intérêt ? On ne transmet que les valeurs, pas la structure de donnée et de plus on ne stocke pas la structure de donnée entière, cela résulte en une grosse économie de mémoire.

Pour **envoyer** une valeur, on va utiliser le mot clé **yield**, par exemple :

    !python
    >>> def test():
    ...     for i in xrange(10):
    ...         yield i
    ...
    >>> test()
    --- <generator object test at 0x1014eafa0>
    
Quand on utilise le mot-clé yield, la fonction retourne un objet *generator*, qui est itérable, que l'on peut donc convertir en liste :

    !python
    >>> list(test())
    --- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

---

### Générateurs

Étant donné que c'est un itérable, on peut donc le parcourir.

# Fonction normale

    !python
    >>> def test():
    ...     d = []
    ...     for i in xrange(3):
    ...         print("Calcul")
    ...         d.append(i*2)
    ...     return d
    ...
    
# Parcours du résultat de la fonction normale

    !python
    >>> for i in test():
    ...     print("Boucle")
    ...
    Calcul
    Calcul
    Calcul
    Boucle
    Boucle
    Boucle

---

### Générateurs

# Générateur

    !python
    >>> def test():
    ...     for i in xrange(3):
    ...         print("Calcul")
    ...         yield i
    ...
    
# Parcours du résultat du générateur

    !python
    >>> for i in test():
    ...     print("Boucle")
    ...
    Calcul
    Boucle
    Calcul
    Boucle
    Calcul
    Boucle

---

### Générateurs conclusion

En conclusion il est préférable d'utiliser les générateurs quand vous le pouvez dans vos fonctions et surtout d'utiliser les fonctions retournant des générateurs dès que possible. Par exemple, xrange retourne un générateur, range une liste. À titre de comparaison, voici les temps d'exécution nécessaire pour sommer la liste des 1 000 000 premiers entiers :

* sum(range(1000000)) : 55ms
* sum(xrange(1000000)) : 14.7 ms

---

## Generator expression

Il est possible de générer des genérateurs de la même manière que des listes avec les listes compréhensives, et même avec la même syntaxe :

    !python
    >>> a = [x for x in xrange(10) if x%2 == 0]
    >>> b = (x for x in xrange(10) if x%2 == 0)
    >>> a == list(b)
    True
    
Il faut noter qu'il est possible d'"oublier" les parenthèses quand on passe un generator expression à une fonction :

    !python
    >>> def iter(iterable):
    ...     for i in iterable:
    ...         print(i)
    ...
    >>> iter((x for x in xrange(3)))
    0
    1
    2
    >>> iter(x for x in xrange(3))
    0
    1
    2

---

## Créer une classe

.notes: Rappel POO

Python est un langage objet, il est bien sûr possible de créer vos propres objets en utilisant la syntaxe suivante :

    !python
    class C(object):
        pass
        
    >>> C
    --- <class '__main__.C'>
    
Ce qu'il faut retenir, utiliser le mot clé **class** et faire hériter vos objets de la class **object**.

---

## Constructeurs

Le nom des constructeurs est toujours le même en python : **\_\_init\_\_** :

    !python
    class C(object):
        def __init__(self, message = None):
            self.message = message
    
L'instanciation de la classe se fait comme ceci :

    !python
    >>> c = C('Message')
    >>> c
    --- <__main__.C object at 0x101556890>
    >>> c.message
    --- 'Message'
    >>> d = C()
    >>> print(d.message)
    None

---

## Méthodes

Les méthodes sont des définies comme des fonctions à une exception près, ils doivent obligatoirement contenir un premier argument (traditionnellement nommé **self**).

    !python
    class C(object):
        def __init__(self, message):
            self.message = message
        def get_message(self):
            return self.message
            
    >>> c = C('Message')
    >>> c.get_message()
    --- 'Message'

Le mot-clé **self** est l'équivalent du **this** dans certaine langages. L'appel à la méthode get_message est équivalent au code suivant :

    !python
    >>> C.get_message(c)
    --- 'Message'

---

## Attributs d'instance

Comme on l'a vu rapidement dans les slides précédents, on définit un attributs d'instance (donc qui sera différent pour chaque instance), il suffit d'ajouter un attribut à l'instance courante **self**. Cet ajout d'attributs peut se faire n'importe où (même à l'extérieur) mais ne devrait être fait que dans le constructeur :

    !python
    class C(object):
        def __init__(self, attr1, attr2 = None):
            self.attr1 = attr1
            self.attr2 = attr2
            
        def add_attr(self):
            self.additionnal = 'Additionnal'
            
    >>> c = C('attr1')
    >>> c.attr1
    --- 'attr1'
    >>> c.additionnal
    ...
    AttributeError: 'C' object has no attribute 'additionnal'
    >>> c.add_attr()
    >>> c.additionnal
    'Additionnal'

---

### Attributs de classe

Il est aussi possible de créer des attributs qui seront partagés entre toutes les instances d'une classe :

    !python
    class C(object):
        common = None
        def __init__(self, common):
            C.common = common            
    >>> c = C('Common')
    >>> c.common
    --- 'Common'
    >>> c2 = C('Com')
    >>> c2.common
    --- 'Com'
    >>> c.common
    --- 'Com'
    
Il est aussi possible d'accéder à la classe directement par **self** :

    !python
    >>> c.__class__.common = 'C'
    >>> c.common
    --- 'C'
    >>> c2.common
    --- 'C'
    
---

## Attributs privées

Il est possible de créer des attributs "privés" en python, même si elles n'ont pas la même définition que dans d'autres langages. Pour définir des attributs privées, il faut suivre les conventions suivantes :

* attribut : Attribut __public__ : qui peut être accédé de l'extérieur.
* _attribut : Attribut __interne__ : qui ne devrait pas être accédé de l'extérieur mais qui sera utilisée en interne.
* \_\_attribut : Attribut __privé__ : ne sera jamais accédé ni de l'extérieur, ni de l'intérieur. Ces variables sont typiquement des attributs que python va gérer tout seul (opérateurs, attribut **\_\_dict\_\_**).

Il n'y a pas de notion de **protected** en python, les modes d'accès ne changent pas, ce qui est public reste public, ce qui est interne reste interne et ce qui est privé reste privé.

---

## Définir des propriétés proprement

En python, il y a un moyen de définir **proprement** des propriétés (c'est à dire un getter, un setter et un deletter). Pour cela on va utiliser la fonction **property** :

    !python
    class C(object):
        def __init__(self):
            self._x = "X"
    
        def getx(self):
            return self._x
        def setx(self, value):
            self._x = value
        def delx(self):
            del self._x
        x = property(getx, setx, delx, "I'm the 'x' property.")
    
    >>> c = C()
    >>> c.x #Appelle getx()
    --- "X"
    >>> c.x = 3 #Appelle setx(3)
    >>> c.x #Appelle getx()
    --- 3
    >>> del c.x #Appelle delx()
    Delx
   
[Documentation officielle](http://docs.python.org/library/functions.html#property).

---

## Héritage

Il est possible de faire hériter vos objets d'autres objets définis, voire de types prédéfinis. La classe **racine** est la classe **object**. Il est aussi possible de faire de l'héritage multiple en python :

    !python
    class A(object):
        a = 'A'
    class B(object):
        b = 'B'
    class C(A, B):
        pass
        
    >>> c = C
    >>> c.a
    --- 'A'
    >>> c.b
    --- 'B'

Pour un tutorial complet : [Wikibooks](http://fr.wikibooks.org/wiki/Apprendre_%C3%A0_programmer_avec_Python/Classes,_m%C3%A9thodes,_h%C3%A9ritage#H.C3.A9ritage).

---

## Méthodes spéciales (dont opérateurs)

Il est possible de définir des méthodes spéciales qui permettront à vos objets d'être plus conviviaux à utiliser (dont par exemple les opérateurs). Voici quelques exemples de telles méthodes :

# Opérateurs de comparaison

* object.\_\_lt\_\_(self, other) : <
* object.\_\_le\_\_(self, other) : ≤
* object.\_\_eq\_\_(self, other) : ==
* object.\_\_ne\_\_(self, other) : !=
* object.\_\_gt\_\_(self, other) : >
* object.\_\_ge\_\_(self, other) : ≥ 

---

### Méthodes spéciales (dont opérateur)

# Opérateur d'appartenance
    
* object.\_\_contains\_\_(self, item) : item in object

# Opérateur d'appel

Il est possible de créer une méthode spéciale qui sera appelée lors de l'appel de l'instance en tant que fonction :

    !python
    class C(object):
        x = 3
        def __call__(self):
            return self.x
            
    >>> c = C()
    >>> c()
    --- 3
    >>> C()()
    --- 3

[Documentation officielle](http://docs.python.org/reference/datamodel.html#special-method-names).

---

## Méthodes de classes et statiques

Il est possible de déclarer une méthode d'un objet comme **une méthode de classe**, c'est à dire qu'elle n'aura besoin que des attributs de classes (propriétés et méthodes). Pour cela on devra utiliser le décorateur **classmethod** :

    !python
    class C(object):
        x = 'X'        
        def __init__(self):
            self.y = 'Y'            
        @classmethod
        def printX(cls):
            print(cls.x)            
        @classmethod
        def printY(cls):
            print(cls.y)
            
    >>> C.printX()
    X
    >>> C.printY()
    ...
    AttributeError: type object 'C' has no attribute 'y'
    

Le premier argument qui sera passé aux méthodes de classes sera la classe elle-même qu'on l'appelle directement (**C.classmethod()**) ou via une instance (**C().classmethod()**).
    
---

### Méthodes statiques

Il est aussi possible de créer des **méthodes statiques** qui n'auront besoin d'aucune référence vers la classe ou une de ses instances. Les méthodes statiques sont similaires à ce qu'on peut trouver en JAVA ou en C++. C'est utile quand on veut créer une fonction de type **utilitaire** mais qui a un rapport avec la classe crée :

    !python
    class C(object):
        @staticmethod
        def add(a, b):
            return a+b
            
    >>> C.add(1, 2)
    3
    >>> C().add(1, 2)
    3
