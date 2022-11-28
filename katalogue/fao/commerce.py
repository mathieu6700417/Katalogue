import os
import pandas as pd
from katalogue.dépot import Dépot

class DépôtFAOCommerce(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        
        super().__init__(nom_dossier_parent)
        

    def _dataframe(self, nom):
        self.télécharger("a_c")
        self.désarchiver("a_c")
        self.désarchiver("commerce")
        
        df = pd.read_csv(self.chemin_fichier(nom), encoding="latin-1")
        df.columns = list(map(lambda c: c.lower().replace(" ", "_"), df.columns))
        return df


    def commerce(self):
        return self._dataframe("commerce_données")

