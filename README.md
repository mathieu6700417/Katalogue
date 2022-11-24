# Katalogue
Katalogue

## Construction du paquet 
`env/bin/python3 -m build`

## Déploiement du paquet sur testpypi
`env/bin/twine upload -r testpypi dist/*`

## Utilisation

`from katalogue.datagouv.associations import DépôtAssociationDataGouv

dépot = DépôtAssociationDataGouv()
dépot.associations()

`
