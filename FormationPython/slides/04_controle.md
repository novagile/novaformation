# Python : Les structures de contrôle classiques

.fx: title

---

## Conditions

Python, comme la plupart des langages, se base sur les expressions booléennes pour vérifier si une condition est vraie ou non. Les opérateurs suivantes peuvent être utilisés :

* L'opérateur de comparaison  : **==**.
* L'opérateur de différence : **!=**.
* Les opérateurs de comparaisons : **<**, **>**, **<=**, **>=**.

La syntaxe pour une condition est la suivante :

    !python
    if x < 0:
         x = 0
         print("Négatif mis à zéro")
    elif x == 0:
         print("Zéro")
    elif x == 1:
         print("1")
    else:
         print("Quelque chose d'autre")
    
---

### Conditions

On peut aussi utiliser l'opérateur **in** pour tester l'appartenance d'un élément à un itérable :

    !python
    >>> x = [1, 2, 3, 4, 5]
    >>> 3 in x
    --- True
    >>> 6 in x
    --- False


---

## Les itérables

En python, les itérables sont des conteneurs qui contiennent une collection d'autre objets et capable de retourner leurs membres un par un. Un itérator est un objet qui va permettre de parcourir la collection de parcourir un itérable. Les objets qui sont itérables sont :

* Les collections (tableau, ensemble, table de hachages)
* Les chaînes de caractère
* Les fichiers
* Toute classe ayant une méthode **\_\_iter\_\_** renvoyant un objet respectant l'interface des **itérators**.

L'intérêt des iterateurs est de fournir une méthode unique pour parcourir différent type de conteneurs et ainsi de pouvoir leur appliquer des algorithmes sans se soucier du type de conteneur traversé. Ainsi, vous pouvez créer des objets itérables (on le verra plus tard) et utiliser des fonctions déjà existantes dans python sans devoir les recoder. Par exemple, parcours simple, tri d'un conteneur (nécessite des méthodes de comparaison), inversion d'un conteneur ou somme des éléments d'un conteneur (nécessite la méthode d'addition).

Le fait de parcourir les éléments d'un itérable s'appelle une **itération**. Il existe un module dédié aux fonctions sur les itérables en python : [itertools](http://docs.python.org/library/itertools.html).

---

### Tri d'un itérable

Python fournit par défaut une manière de trier un itérable (à condition d'avoir définit les méthodes de comparaison pour les objets contenus).

    !python
    >>> x = [1, 3, 2, 4]
    >>> sorted(x)
    --- [1, 2, 3, 4]
    
Comme auparavant, il est aussi possible de trier les chaînes de caractères :

    !python
    >>> x = 'hello world'
    >>> sorted(x)
    --- [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
    
---

### Inversion d'un itérable

Dernier exemple, l'inversion d'un itérable. Attention la fonction **reversed** renvoie un objet peu lisible, à convertir en liste si on veut en avoir une représentation plus lisible :

    !python
    >>> x = [1, 2, 3, 4]
    >>> list(reversed(x))
    --- [4, 3, 2, 1]

L'exemple marche aussi avec les chaînes de caractères, mais on ne peut le convertir directement en string : 

    !python
    >>> x = 'hello world'
    >>> list(reversed(x))
    --- ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
    >>> str(reversed(x))
    --- '<reversed object at 0x101554c90>'
    
Comment faire dans ce cas ?

---

### Création d'une chaîne à partir d'un itérable

Il suffit de recréer une string à partir de l'itérable

# Exemples

    !python
    >>> ''.join(['1', '2', '3'])
    --- '123'
    >>> ','.join(['1', '2', '3'])
    --- '1,2,3'

# Solution

Ainsi dans l'exemple de la slide précédente, il suffit de faire :

    !python
    >>> ''.join(list(reversed('hello world')))
    --- 'dlrow olleh'
    
On peut même faire mieux :

    !python
    >>> ''.join(reversed('hello world'))
    --- 'dlrow olleh'
    
En effet la fonction reversed renvoi lui aussi un objet itérable.

---

## Boucle for

Python fournit un moyen très simple pour parcourir un itérable :

    !python
    >>> x = [1, 2, 3]
    >>> for i in x:
    ...     print i
    ...
    1
    2
    3
    
Comme les chaînes de caractères sont aussi des itérables, on peut les itérer de la même manière : 

    !python
    >>> x = 'Hello'
    >>> for i in x:
    ...     print i
    ...
    H
    e
    l
    l
    o
    
---

### Boucle for

Bien sûr, python permet aussi de faire une boucle for plus classique, pour cela on va utiliser la méthode range, qui va nous renvoyer une liste avec tous les entiers inférieurs à n, ainsi on aura un fonctionnement plus proche d'une boucle for classique :

    !python
    >>> range(3)
    --- [0, 1, 2]
    >>> for i in range(3):
    ...     print i
    ...
    0
    1
    2
    
---

## Parcourir un dictionnaire

Par défaut, quand on itère sur un dictionnaire, on itère en fait sur les clés :

    !python
    >>> x = {1: 2, 3: 4, 5: 6}
    >>> for i in x:
    ...     print i
    ...
    1
    3
    5
    
Si on veut itérer sur les clés, on peut utiliser la méthode **values** du dictionnaire et si on a besoin des deux, il veut utiliser la méthode **items** :

    !python
    >>> x = {1: 2, 3: 4, 5: 6}
    >>> x.values() # Utiliser itervalues dans une boucle
    --- [2, 4, 6]
    >>> x.items() # Utiliser iteritems dans une boucle
    --- [(1, 2), (3, 4), (5, 6)]

---

## La fonction enumerate

Si l'on veut parcourir un itérable en ayant le numéro de l'itération il faut utiliser la fonction enumerate :
    
    !python
    >>> # Enumerate ne renvoi pas une représentation très visible
    >>> list(enumerate('ABC'))
    --- [(0, 'A'), (1, 'B'), (2, 'C')]
    >>> for i in enumerate('ABC'):
    ...     print(i)
    ...
    (0, 'A')
    (1, 'B')
    (2, 'C')
    >>> for i, car in enumerate('ABC'):
    ...     print(str(i) + " " + str(car))
    ...
    0 A
    1 B
    2 C

---

## Boucle while

La notation de la boucle while est similaire à celle pour les conditions :

    !python
    while x != 0:
        x =- 1

On utilise les même mots-clés que dans une condition et la boucle s'exécutera tant que la condition sera évaluée à **Vrai**.

---

## Mot clés **break** et **continue**

Il existe deux mot-clés qui permettent de contrôler l'exécution des boucles.

# **break**

break est un mot-clé qui permet d'arrêter l'exécution d'une boucle :

    !python
    >>> compteur = 0
    >>> while True:
    ...     print(compteur)
    ...     compteur += 1
    ...     if compteur >= 5:
    ...         break
    ...
    0
    1
    2
    3
    4
    
---

### Mot clés **break** et **continue**

# **continue**
 
continue est un mot-clé qui permet de **sauter** le block courant et de commencer le block suivant :
 
    !python
    >>> for x in range(10):
    ...     if x % 2 == 0:
    ...         continue
    ...     print(x)
    ...
    1
    3
    5
    7
    9

---

## Les listes compréhensives

Les listes compréhensives sont un moyen de créer de manière concise des listes à partir d'autres itérables. Par exemple, si on veut obtenir la longueur des mots de la phrase "Je suis ici pour apprendre le python !" mais sans compter le mot "le". On peut réaliser celà avec le code suivant :

La notation est la suivante :

    !python
    phrase = "Je suis ici pour apprendre le python !"
    mots = phrase.split()
    longueurs = []
    for mot in mots:
        if mot != "le":
            longueurs.append(len(mot))
            
Les dernières lignes peuvent être raccourcies avec la notation suivante :

    !python
    longueurs = [len(mot) for mot in mots if mot != "le"]

---

## Exceptions

Python gère les erreurs sous forme d'exceptions. Les exceptions sont une forme avancée des erreurs et est présente dans plusieurs langages de programmation (JAVA, Smalltalk, LISP).

Le principe des exceptions est de stopper l'exécution normale du programme en cours.

# Lancer une exception

Pour lancer une exception, on va utiliser le mot-clé **raise** :

    !python
    >>> raise Exception()
    ...
    Exception: 

Il existe plusieurs types d'exceptions (en fait ce sont des objets qui héritent tous de la classe Exception).

---

### Exceptions

Certains bout de codes peuvent lancer des exceptions, par exemple :

    !python
    liste = [0, 1, 2, 3, 4]
    for i in range(6)
        liste[i]
        
Ce code va produire une exception à l'exécution :

    !bash
    $ python exception.py
    Traceback (most recent call last):
      File "exception.py", line 3, in <module>
        liste[i]
    IndexError: list index out of range

---

### Exceptions

# Capturer une exception

Pour capturer une exception, on va utiliser un bloc **try** ... **except**. Le code pouvant générer une exception doit être mis dans le block try et le traitement seront dans des blocks except :

    !python
    liste = [0, 1, 2, 3, 4]
    try:
        for i in range(6):
            print(liste[i])
    except IndexError:
        print("Probleme avec les indice !")
       
À l'exécution :
        
    !bash
    $ python exception.py
    0
    1
    2
    3
    4
    Probleme avec les indices !
    
---

### Exceptions

# Récupérer l'exception

Pour le moment on peut attraper un type d'exception mais on aimerait pouvoir récupérer l'exception elle-même, pour cela on va utiliser le mot-clé **as** :

    !python
    liste = [0, 1, 2, 3, 4]
    try:
        for i in range(6):
            print(liste[i])
    except IndexError as e:
        print(e)
       
À l'exécution :

    !bash
    $ python exception.py
    0
    1
    2
    3
    4
    list index out of range

---

### Mot clé **else**

Il est possible d'utiliser le mot clé **else** avec la syntaxe **try** ... **except**. Le block **else** sera exécuté si aucun exception n'a été lancée dans le block **try** :

    !python
    try:
        raise Exception()
    except Exception:
        print("Exception")
    else:
        print("Pas d'exception")
        
Exécution :

    !bash
    $ python exception.py
    Exception
---

### Mot clé **else**

Autre exemple :

    !python
    try:
        x = 1
    except Exception:
        print("Exception")
    else:
        print("Pas d'exception")
        
Exécution :

    !bash
    $ python exception.py
    Pas d'exception

---

### Mot clé **finally**

Le mot clé **finally** est un mot-clé qui permet de déclarer un block d'instruction qui sera exécuté quelque soit le résultat du block try :

    !python
    try:
        raise Exception()
    except Exception:
        print("Exception")
    else:
        print("Pas d'exception")
    finally:
        print("Finally")
        
Exécution :

    !bash
    $ python exception.py
    Exception
    Finally
    
---

### Mot clé **finally**

Autre exemple :

    !python
    try:
        x = 1
    except Exception:
        print("Exception")
    else:
        print("Pas d'exception")
    finally:
        print("Finally")
        
Exécution :

    !bash
    $ python exception.py
    Pas d'exception
    Finally
