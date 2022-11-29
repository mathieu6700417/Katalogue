# Katalogue
Katalogue est un paquet python permettant d'accèder facilement à diverses sources de données. 

## Questions 
- Il y a un premier filtre fait dans le fichier des assocs ? 
- On va finir par avoir beaucoup de dépots dans datagouv ou insee, donc avoir beaucoup de fichiers dans les dossiers de données, ne devrait-on pas les séparer à nouveau par module? 

- mettre à clean de requirement.txt
- rajouter des progress sur temps long (dl, parse, load)
- crash RAM sur FAO - commerce = dépôt.commerce()

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
