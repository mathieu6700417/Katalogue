import os
import pandas as pd
from katalogue.dépot import Dépot
    
    
class DépôtINSEECommunes(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        
        super().__init__(nom_dossier_parent)
        

    def communes(self):
        self.télécharger("communes")
        
        communes = pd.read_csv(self.chemin_fichier("communes"),
                                sep=",",
                                low_memory=False, 
                                encoding="UTF-8")

        return communes

