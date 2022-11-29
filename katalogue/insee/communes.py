import os
import pandas as pd
from katalogue.dépot import Dépot
    
    
class DépôtINSEECommunes(Dépot):

    def communes(self):
        self.télécharger("communes")
        
        communes = pd.read_csv(self.chemin_fichier("communes"),
                                sep=",",
                                low_memory=False, 
                                encoding="UTF-8")

        return communes

