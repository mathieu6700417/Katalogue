# Katalogue
Katalogue est un paquet python permettant d'accèder facilement à diverses sources de données. 

## Questions 
- Pourrait on renommer le décorateur 'gérer_sauvegarde_locale' en 'sauvegarde_locale'
- Comment fait on pour enlever le code qui se répète dans chaque classe fille dépot dans l'init? 
- Il y a un premier filtre fait dans le fichier des assocs ? 



## Construction du paquet 

```bash
python3 -m build
```


## Déploiement du paquet sur testpypi

```bash
twine upload -r testpypi dist/*
```

## Utilisation

```bash
from katalogue.insee.communes import DépôtINSEECommunes

dépôt = DépôtINSEECommunes()
communes = dépôt.communes()
communes.sample(5)
```
