# Python : les structures de données classiques

.fx: title

---

## Les listes

Les listes sont les structure de données les plus utilisées en python, elles représentent une collection d'objet de type différents. Les listes python se souviennent aussi de l'ordre dans lesquels les objets ont étés insérés.

Une liste se définit avec la notation **[]**.

    !python
    >>> x = []
    
On peut déclarer une liste déjà remplie :

    !python
    >>> x = [1, 2, 3, 'a', 'b', 'c']
    
Pour convertir un objet en list, il suffira d'utiliser la méthode **list** :

    !python
    >>> list('Hello')
    --- ['H', 'e', 'l', 'l', 'o']
    
---

### Utilisation des listes

# Ajouter un élément dans une liste :

    !python
    >>> l = []
    >>> l.append()
    >>> x
    --- [2]
    
# Supprimer un élément d'une liste

    !python
    >>> l = [1, 2, 3]
    >>> l.remove(2)
    >>> l
    --- [1, 3]
    
# Compter le nombre d'occurrence dans une liste

    !python
    >>> l = [1, 2, 2, 3, 3, 3]
    >>> l.count(2)
    --- 2
    >>> l.count(3)
    --- 3

---

### Utilisation des listes
    
# Premier indice d'un élément dans une liste

    !python
    >>> l = [1, 2, 1]
    >>> l.index(1)
    --- 0
    >>> l.index(2)
    --- 1

Plus d'informations sur les listes : [http://docs.python.org/tutorial/datastructures.html#more-on-lists](http://docs.python.org/tutorial/datastructures.html#more-on-lists).

---

## Les tuples

Les tuples sont similaires aux listes avec une différence notable : une fois qu'un tuple a été instancié, il ne pourra être modifié.

L'instanciation d'un tuple peut se faire de 2 manières :

# Avec la notation **()** :

    !python
    >>> x = ()
    >>> x
    --- ()
    >>> x = (1,2)
    >>> x
    --- (1, 2)
    
# Avec la notation simplifiée :

    !python
    >>> x = 1,2
    >>> x
    --- (1, 2)
    

---

### Les tuples

# **Attention !** Pour créer un tuple d'un seul élément :

    !python
    >>> x = (1)
    >>> x
    --- 1
    >>> x = (1,)
    --- (1,)
    >>> x = 1,
    --- (1,)
    
Une liste peut se transformer en tuple et vice-versa pour autoriser/empêcher la modification :

    !python
    >>> x = [1, 2, 3]
    >>> y = tuple(x)
    >>> z = list(y)
    >>> a = tuple('Hello')
    --- ('H', 'e', 'l', 'l', 'o')


---

### Utilisation des tuples

Comme les tuples ne sont pas modifiables, les seules opérations possibles sont :

# Compter le nombre d'occurrence dans un tuple

    !python
    >>> l = (1, 2, 2, 3, 3, 3)
    >>> l.count(2)
    --- 2
    >>> l.count(3)
    --- 3
    
# Premier indice d'un élément dans un tuple

    !python
    >>> l = (1, 2, 1)
    >>> l.index(1)
    --- 0
    >>> l.index(2)
    --- 1
    
---

## Indexation

Les tuples et les listes supportent tous les deux l'indexation par indice numérique. L'indexation commence à zéro. Exemples :

    !python
    >>> x = [1, 2, 3, 4, 5]
    >>> x[2]
    --- 3
    >>> y = (1, 2, 3, 4, 5)
    >>> y[2]
    --- 3
    
De plus les listes supportent la modification d'un élément indexé, mais pas les tuples (comme ils ne sont pas modifiables) :

    !python
    >>> x = [1, 2, 3, 4, 5]
    >>> x[2] = -1
    >>> x
    --- [1, 2, -1, 4, 5]
    >>> y = (1, 2, 3, 4, 5)
    >>> y[2] = -1
    ...
    
    TypeError: 'tuple' object does not support item assignment

---

## Indexation négative

Il est aussi possible en python d'indexer les éléments à partir de la fin, et dans ce cas les indices commencent à -1 :

    !python
    >>> x = [1, 2, 3, 4, 5]
    >>> x[-1]
    --- 5
    >>> x[-2]
    --- 4
    >>> x[-5]
    --- 1

---

## Les ensembles

Un ensemble est une structure de donnée qui stocke des valeurs **uniques**. Il ne peut y avoir deux fois la même valeur dans un ensemble. Les opérations sur les ensembles sont ceux de la théorie mathématique des ensembles.

---

## Les sets

En python, les ensembles sont représentés par la classe **set** :

    !python
    >>> x = {1, 2, 3}
    >>> x
    --- set([1, 2, 3])
    >>> x = set([1, 2, 3])
    >>> x
    --- set([1, 2, 3])
    
**Attention**, pour créer un ensemble vide, on dois utiliser la deuxième notation :

    !python
    >>> x = {}
    >>> type(x)
    --- <type 'dict'>
    >>> x = set()
    >>> type(x)
    --- <type 'set'>


---

### Les sets

Comme les ensembles contiennent des valeurs uniques, on peut utiliser la conversion en ensemble pour supprimer les éléments présents plusieurs fois dans une liste :

    !python
    >>> l = [1, 2, 2, 3, 4, 4, 5]
    >>> s = set(l)
    >>> s
    --- set([1, 2, 3, 4, 5])
    >>> s = set('Hello')
    >>> s
    --- set(['H', 'e', 'l', 'o']) 

**Attention !** Étant donné que les ensembles ne sont pas ordonnés, il y a un risque de perdre l'ordre des éléments de l'itérable de base :

    !python
    >>> l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> s = set(l)
    >>> s
    --- set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> l2 = list(s)
    >>> l2 == l
    --- True #mais pas toujours
    
---

## Les frozensets

Les frozensets sont aux sets ce que les tuples sont aux listes, une version non-modifiable des ensembles.

# Instanciation d'un frozenset

    !python
    >>> fs = frozenset()
    >>> fs = frozenset('Hello')
    --- frozenset(['H', 'e', 'l', 'o'])

---

## Opérations sur les ensembles

Les opérations sur les ensembles (sets et frozensets) sont ceux de la théorie des ensembles :

# Union :

L'union est l'ensemble des valeurs qui sont dans l'un ou l'autre (ou les deux) ensembles.

    !python
    >>> a = {1, 3, 5}
    >>> b = {2, 4, 5, 6}
    >>> a.union(b)
    --- set([1, 2, 3, 4, 5, 6])
    
# Intersection

L'intersection est l'ensemble des valeurs qui sont dans les deux ensembles.

    !python
    >>> a = {1, 2, 3, 4, 5}
    >>> b = {3, 4, 5, 6, 7}
    >>> a.intersection(b)
    --- set([3, 4, 5])
    
---

### Opérations sur les ensembles

# Différence

La différence est l'ensemble des valeurs qui sont dans l'ensemble courant mais pas dans l'autre.

    !python
    >>> a = {1, 2, 3, 4, 5}
    >>> b = {3, 4, 5, 6, 7}
    >>> a.difference(b)
    --- set([1, 2])
    >>> b.difference(a)
    --- set([6, 7])
    
# Différence symétrique

La différence symétrique est l'ensemble des valeurs qui sont dans l'un des deux ensembles mais pas les deux à la fois.

    !python
    >>> a = {1, 2, 3, 4, 5}
    >>> b = {3, 4, 5, 6, 7}
    >>> a.symmetric_difference(b)
    --- set([1, 2, 6, 7])
    
---

### Opérations spécifiques aux **sets**

Comme les **sets** sont des structure de données modifiable et les **frozensets** des structure de données non-modifiables, certaines opérations ne peuvent s'appliquer qu'au **sets**.

# Ajout d'une valeur

    !python
    >>> s = set()
    >>> s.add(2)
    >>> s
    --- set([2])
    
# Ajout de plusieurs valeurs

On peut combiner plusieurs ensembles en 1 seul, mais il n'y aura aucun doublons :

    !python
    >>> a = {1, 2, 3}
    >>> b = {2, 3, 4}
    >>> a.update(b)
    >>> a
    --- set([1, 2, 3, 4])

---

### Opérations spécifiques aux **sets**

# Suppression d'une valeur

    !python
    >>> a = {1, 2, 3}
    >>> a.discard(2)
    >>> a
    --- set([1, 3])

---

## Différence entre ces structures de données

Ce qu'il faut retenir c'est utiliser les bonnes structures de données. Plus les structures de données sont simples, plus les opérations dessus seront rapides. À titre d'exemple, voici les temps nécessaires pour sommer les 1000 premiers entiers pour les 4 structures de données présentées :

* Tuple : 10.5 microsecondes (10 <sup>-6</sup>)
* Liste : 10.9 microsecondes (10 <sup>-6</sup>)
* Set : 14.7 microsecondes (10 <sup>-6</sup>)
* Frozenset : 14.7 microsecondes (10 <sup>-6</sup>)

---

## Les dictionnaires

Les dictionnaires sont des structures de données aussi très présente en python, ils permettent d'accéder aux éléments non plus par des index mais aussi par des clés (string, nombre, tuple). Les contraintes sont :

* La clé doit être un objet non-modifiable (nombre, string, tuple, frozenset).
* Chaque clé ne pointe que vers une seul valeur.
* Il n'y a pas de notion d'ordre dans les dictionnaires donc impossible d'y accéder par indice (sauf si les clés sont des nombres).

La notation pour créer un dictionnaire est **{}** :

    !python
    >>> adresse = {}
    >>> adresse['Jean'] = '42 rue de Belfort, Montbeliard'
    >>> adresse
    --- {'Jean': '42 rue de Belfort, Montbeliard'}
    >>> adresse2 = {'Jean' : '42 rue de Belfort, Montbeliard'}
    >>> adresse2
    --- {'Jean': '42 rue de Belfort, Montbeliard'}

---

### Les dictionnaires


L'accès aux élément se fait avec la même notation que les listes à la différence qu'on l'on peut utiliser toute clé valide :

    !python
    >>> adresse = {'Jean' : '42 rue de Belfort, Montbeliard', 'Bernard' :
    ... '24 rue de Montbeliard, Belfort'}
    >>> adresse['Jean']
    --- '42 rue de Belfort, Montbeliard'
    >>> adresse['Bernard']
    --- '24 rue de Montbeliard, Belfort'

On peut récupérer indépendamment les clés ou les valeurs d'un dictionnaire :

    !python
    >>> adresse = {'Jean' : '42 rue de Belfort, Montbeliard', 'Bernard' :
    ... '24 rue de Montbeliard, Belfort'}
    >>> adresse.keys()
    --- ['Bernard', 'Jean']
    >>> adresse.values()
    --- ['24 rue de Montbeliard, Belfort', '42 rue de Belfort, Montbeliard']
    
---

### Opérations sur les dictionnaires

On peut ajouter un couple clé/valeur :

    !python
    >>> adresse = {}
    >>> adresse['Jean'] = '42 rue de Belfort, Montbeliard'
    >>> adresse
    --- {'Jean': '42 rue de Belfort, Montbeliard'}
    
On peut aussi en supprimer :

    !python
    >>> adresse = {'Jean' : '42 rue de Belfort, Montbeliard', 'Bernard' :
    ... '24 rue de Montbeliard, Belfort'}
    >>> adresse.remove('Jean') # Ou del adresse['Jean']
    >>> adresse
    --- {'Bernard': '24 rue de Montbeliard, Belfort'}

---

## Découpage

Le découpage est une manière d'extraire certaines parties d'un itérable (toutes les types présentés sauf nombres et dictionnaires).

Le découpage utilise la même notation que l'indexation avec un argument en plus :

    !python
    >>> x = [0, 1, 2, 3, 4, 5]
    >>> x[1:3]
    --- [1, 2]
    >>> x[0:4]
    --- [0, 1, 2, 3]
    
De plus on peut omettre l'un des deux argument pour partir du début ou jusqu'à la fin :

    !python
    >>> x = [0, 1, 2, 3, 4, 5]
    >>> x[:3]
    --- [0, 1, 2]
    >>> x[3:]
    --- [3, 4, 5]
---

### Découpage

Il est aussi possible d'utiliser les indices négatifs comme départ ou arrivé :

    !python
    >>> x = [0, 1, 2, 3, 4, 5]
    >>> x[-3:]
    --- [3, 4, 5]
    >>> x[:-3]
    --- [0, 1, 2]
    
Enfin, il est possible d'ajouter un troisième argument pour préciser le pas :

    !python
    >>> x = [0, 1, 2, 3, 4, 5]
    >>> x[1::2]
    --- [1, 3, 5]
    >>> x[::2]
    --- [0, 2, 4]
    
---

### Découpage négatifs
    
Dernièrement il est possible d'utiliser des valeurs négatives comme pas pour inverser la liste avant le slicing :

    !python
    >>> x = [0, 1, 2, 3, 4, 5]
    >>> x[:3:-1]
    --- [5, 4, 3]
    >>> x[::-1]
    --- [5, 4, 3, 2, 1, 0]
    >>> x[::-2]
    --- [5, 3, 1]