import os
import pandas as pd
from katalogue.dépot import Dépot

class DépôtFAORécoltes(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        
        super().__init__(nom_dossier_parent)
        

    def _dataframe(self, nom):
        self.télécharger("d_z")
        self.désarchiver("d_z")
        self.désarchiver("récoltes")
        
        df = pd.read_csv(self.chemin_fichier(nom), encoding="latin-1")
        df.columns = list(map(lambda c: c.lower().replace(" ", "_"), df.columns))
        return df


    def récoltes(self):
        données = self._dataframe("récoltes_données")
        return données.merge(self.symboles(), on="symbole", suffixes=["", "symbole_"])

    def symboles(self):
        return self._dataframe("récoltes_symboles")
    
