import os
import pandas as pd
from katalogue.dépot import Dépot
from tqdm import tqdm
    
    
class DépôtINSEESireneEntreprises(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        
        super().__init__(nom_dossier_parent)
        

    def _entreprises(self, taille_paquet=100000):
        self.télécharger("archive_entreprises")
        self.désarchiver("archive_entreprises")


        entreprises = pd.read_csv(self.chemin_fichier("entreprises"),
                                  encoding="latin-1",
                                  chunksize=taille_paquet, 
                                  iterator=True,
                                  low_memory=False)
        return entreprises

    def entreprises(self, nombre_maximum_entreprises=100000):
        _ent = self._entreprises(nombre_maximum_entreprises)
        return _ent.get_chunk()

   
    def trouver_entreprises(self, fnCondition, nombre_maximum_entreprises):
        dfs = list()
        _ent = self._entreprises()
        nombre_trouvées = 0
        for df in _ent:
            dfe = df[df.apply(fnCondition, axis=1)]
            nombre_trouvées += dfe.shape[0]
            dfs.append(dfe)
            if not(nombre_maximum_entreprises is None) and nombre_trouvées >= nombre_maximum_entreprises:
                break

        df =  pd.concat(dfs)
        return df[0:nombre_maximum_entreprises]

    def entreprises_économie_sociale_et_solidaire(self, nombre_maximum_entreprises=100):
        return self.trouver_entreprises(lambda e: not(pd.isna(e.economieSocialeSolidaireUniteLegale)) and e.economieSocialeSolidaireUniteLegale == "O",
                                        nombre_maximum_entreprises)


    def entreprises_avec_codes_activite(self, codes_activites, nombre_maximum_entreprises=100):
        return self.trouver_entreprises(lambda e: e.activitePrincipaleUniteLegale in codes_activites, 
                                        nombre_maximum_entreprises)

    
    def entreprises_avec_codes_categorie_juridique(self, codes_categories_juridiques, nombre_maximum_entreprises=100):
        return self.trouver_entreprises(lambda e: e.categorieJuridiqueUniteLegale in codes_categories_juridiques, 
                                        nombre_maximum_entreprises)
