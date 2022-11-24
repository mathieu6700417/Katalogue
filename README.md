# Katalogue
Katalogue est un paquet python permettant d'accèder facilement à diverses sources de données. 

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
