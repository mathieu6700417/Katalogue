import os
import pandas as pd
from katalogue.dépot import Dépot
    
    
class DépôtINSEECatégoriesJuridiques(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        
        super().__init__(nom_dossier_parent)
        

    def catégories(self, niveau=3):
        self.télécharger("catégories_juridiques")
       
        if niveau == 1:
            sheet_name = "Niveau I"
        elif niveau == 2:
            sheet_name = "Niveau II"
        elif niveau == 3:
            sheet_name = "Niveau III"
        else:
            print("Niveau invalide")
            return

        df = pd.read_excel(self.chemin_fichier("catégories_juridiques"),
                                sheet_name=sheet_name,
                                skiprows=3)

        return df

