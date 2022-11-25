import os
import pandas as pd
from katalogue.dépot import Dépot

class DépôtFAORécoltes(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        
        super().__init__(nom_dossier_parent)
        

    def récoltes(self):
        self.télécharger("t_z")
        self.décompresser("t_z")
        self.décompresser("t_z.commerce")
        
        df = pd.read_csv(self.chemin_fichier("t_z.commerce.data"), encoding="latin-1")
        df.columns = list(map(lambda c: c.lower().replace(" ", "_"), df.columns))
        return df
