
# Interface avec QtDesigner

Pour créer les curseurs d'interpolation entre les différents espaces, il suffit d'ouvrir le fichier Lab1\Lab1_Interpolation.ui sur QtDesigner. Puis, copier-coller les curseurs (sliders) de RGB déjà crées. Le nom des widgets et sliders doit être renommer selon l'espace. On peut générer la nouvelle classe Python avec la commande suivante

```
pyuic5 -x fichier.ui -o fichier.py
```

Pour implémenter les nouveaux curseurs dans l'application, comparer le fichier original de la fenêtre d'interpolation avec le nouveau fichier avec https://www.diffchecker.com/text-compare/, puis ajouter les nouvelles lignes dans Lab1\Lab1_Interpolation.py.
