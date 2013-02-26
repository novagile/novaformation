# Annexes

.fx: title

---

## Traduction du zen python en français

> Préfère :

> la beauté à la laideur,

> l’explicite à l’implicite,

> le simple au complexe

> et le complexe au compliqué,

> le déroulé à l’imbriqué,

> l’aéré au compact.

> Prends en compte la lisibilité.

---

### Traduction du zen python en français

> Les cas particuliers ne le sont jamais assez pour violer les règles.

> Mais, à la pureté, privilégie l’aspect pratique.

> Ne passe pas les erreurs sous silence,

> . . . ou bâillonne-les explicitement.

> Face à l’ambiguïté, à deviner ne te laisse pas aller.

> Sache qu’il ne devrait avoir qu’une et une seule façon de procéder,

> même si, de prime abord, elle n’est pas évidente, à moins d’être Néerlandais.

---

### Traduction du zen python en français

> Mieux vaut maintenant que jamais.

> Cependant jamais est souvent mieux qu’immédiatement.

> Si l’implémentation s’explique difficilement, c’est une mauvaise idée.

> Si l’implémentation s’explique aisément, c’est peut-être une bonne idée.

> Les espaces de noms ! Sacrée bonne idée ! Faisons plus de trucs comme ça.

<p class="cite"> - Traduction Cécila TREVIAN et Bob Cordeau</p>

---

## Objets immuables et objets modifiables

En python, on distingue deux types d'objets, les objets immuables et les objets modifiables.

Les objets immuables sont :

* Nombres.
* Chaînes de caractères.
* Tuples.

Les objets immuables sont comparables par l'assertion **is** et par la comparaison normale **==** :

    !python
    >>> () is ()
    --- True
    >>> () == ()
    --- True
 
---
 
### Objets mutable et immuables
 
Les objets modifiables sont tous les autres, comme par exemple :
 
* Listes
* Dictionnaires
 
Les objets modifiables ne sont pas comparables par l'assertion **is** mais avec la comparaison normale **==** :
 
    !python
    >>> [] is []
    --- False
    >>> [] == []
    --- True