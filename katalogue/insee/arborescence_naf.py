import os
import pandas as pd
from katalogue.dépot import Dépot
    
    
class DépôtINSEEArborescenceNAF(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        
        super().__init__(nom_dossier_parent)
        

    def naf(self):
        self.télécharger("arborescence_naf")
        
        df = pd.read_csv(self.chemin_fichier("arborescence_naf"),
                                sep=",",
                                low_memory=False, 
                                encoding="UTF-8")

        df.columns = list(map(lambda c: c.lower(), df.columns))
        return df

