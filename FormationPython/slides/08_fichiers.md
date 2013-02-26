# Python : les fichiers

.fx: title

---

## Ouvrir un fichier

On ouvre un fichier grâce à la fonction **open** qui prend un argument obligatoire : le nom du fichier et un argument optionnel le mode d'ouverture (semblable à ce qu'on fait en C : 'r' : lecture, 'w' : écriture, 'a' : ajout). Cette fonction nous renvoie un objet de type **file**. Une fois qu'on a finit de traiter le fichier, il faudra le fermer explicitement en appelant la méthode **close** de l'objet :

    !python
    >>> f = open('fichier', 'w')
    >>> f
    <open file 'fichier', mode 'w' at 0x100466c90>
    >>> #On fait nos traitements
    >>> f.close()
    >>> f
    --- <closed file 'fichier', mode 'w' at 0x100466c90>

---

## Le mot clé with

Il est possible d'éviter d'appeler la méthode close explicitement pour cela, on va utiliser le mot-clé **with**. Celui-ci opère comme une structure de contrôle, c'est à dire qu'on va définir un bloc dans lequel on va traiter notre ressource et à la sortie du bloc le fichier sera automatiquement fermé :

    !python
    >>> with open('fichier', 'w') as f:
    ...     #On fait nos traitements
    ...
    >>> f
    --- <closed file 'fichier', mode 'w' at 0x100466c90>

---

## Lire un fichier

On peut récupérer l'ensemble d'un fichier avec la méthode **read** du fichier :

#sample.txt

    !raw
    Premiere ligne
    Deuxieme ligne
    
Et la lecture du fichier :

    !python
    >>> with open("sample.txt", "r") as f:
    ...     print(f.read())
    ...
    Premiere ligne
    Deuxieme ligne

---

## Lire un fichier ligne par ligne

Il est possible de parcourir l'ensemble des lignes du fichier avec la méthode **readlines** :

    !python
    >>> with open("sample.txt", "r") as f:
    ...     print(f.readlines())
    ...
    ['Premiere ligne\n', 'Deuxieme ligne']
    
Comme **readlines** nous renvoi une liste, il est possible de récupérer les lignes indépendamment les une des autres :

    !python
    >>> with open("sample.txt") as f:
    ...     l1, l2 = f.readlines()
    ...     print(l1)
    ...     print(l2)
    ...
    Premiere ligne

    Deuxieme ligne
    
À noter, file est une objet itérable, donc il est possible de la parcourir comme tout autre itérable et on aurait pu faire : "l1, l2 = f" dans l'exemple précédent.

---

## Écrire dans un fichier

L'écriture dans un fichier se fait à travers de la méthode **write** de l'objet file :

    !python
    >>> with open("fichier", "w") as f:
    ...     f.write("string")
    ...
    
# fichier

    !raw
    string
    
Il est aussi possible d'écrire plusieurs chaînes simultanément avec la méthode **writelines** :

    !python
    >>> with open("fichier", "w") as f:
    ...     f.writelines(["string1", "string2"])
    ...
    
# fichier

    !raw
    string1string2
    
---

## Gestion de chemins

Un module qui est très utilisé est le module **os.path**, il contient des méthodes très utiles pour manipuler les chemins :

* os.getcwd() : Retourne le chemin actuel.
* os.path.split("/dev/null") -> ('/dev', 'null') : Diviser le chemin en un couple (répertoire, nom de fichier).
* os.path.isdir(path) : Vérifie si un dossier existe au chemin donné.
* os.path.isfile(path) : Vérifie si un fichier existe au chemin donnée.
* os.path.join("/dev", "null") -> "/dev/null" : Concatène deux chemins de manière à ce que le chemin final soit correct.

[Documentation officielle](http://docs.python.org/library/os.path.html).