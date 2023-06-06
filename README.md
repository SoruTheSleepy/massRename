# massRename.py

Ce script a pour objectif de supprimer une chaîne de caractère rébarbative dans plusieurs noms de fichiers présents dans un même dossier.<br>
Par exemple :

### J'ai dans le dossier racine de mon script les fichiers suivants :
- Soundtrack - Opening.mp3
- Soundtrack - Title.mp3
- Soundtrack - Scene.mp3
- Soundtrack - Credits.mp3

### Je stipule au programme que je souhaite supprimer la chaîne de caractères "Soundtrack - "

```
Entrez la chaîne de caractères à retirer :
Soundtrack -
```

### Le programme passe en revue les fichiers de son dossier racine, puis les renomme en supprimant la chaîne de caractères que j'ai entré précédemment
- Opening.mp3
- Title.mp3
- Scene.mp3
- Credits.mp3
<br> 
Étonamment, massRename.py semble ne fonctionner que lorsqu'il est lancé dans VSCode.<br>
Lancer le script tel quel n'aura aucun effet.