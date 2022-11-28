import os
import requests
import pandas as pd
from katalogue.dépot import Dépot
from glob import glob
    
    
class DépôtDataGouvAssociations(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        
        super().__init__(nom_dossier_parent)

    @Dépot.gérer_sauvegarde_locale
    def associations(self, sauvegarder_localement=False):
        
        # Récupération données assos
        sources_associations = ["association_RNA_Import","association_RNA_Waldec"]
        files = []
        for source in sources_associations:
            self.télécharger(source)
            self.désarchiver(source)
            files.extend(glob(self.chemin_extraction(source) + "/*.csv"))
            
        # Traitement données assos
        assos_ppties = ['id','titre','titre_court','objet','objet_social1','objet_social2','date_creat','date_disso','adrs_codeinsee','adrs_codepostal']
        assos = pd.DataFrame()
        for file_name in files:
            df = pd.read_csv(
                file_name, 
                sep=";",
                low_memory=False, 
                encoding="iso-8859-1").filter(assos_ppties)
            assos = pd.concat([assos,df],axis=0,ignore_index=True)
            # TODO concat list df VS concat unitaire

        assos['date_creat'] = pd.to_datetime(assos['date_creat'], format='%Y-%m-%d', errors = 'coerce')
        assos['date_disso'] = pd.to_datetime(assos['date_disso'], format='%Y-%m-%d', errors = 'coerce')

        
        # Liaison données nomenclature
        self.télécharger("association_nomenclature_WALDEC")
        nomenclature = pd.read_csv(
                                    self.chemin_fichier("association_nomenclature_WALDEC"), 
                                    sep=";",
                                    low_memory=False, 
                                    encoding="UTF-8")

        assos_objet = assos.join(nomenclature.set_index('objet_social_id'), on='objet_social1', rsuffix='_1')
        assos_objet = assos_objet.join(nomenclature.set_index('objet_social_id'), on='objet_social2', rsuffix='_2')
        
        return assos_objet
    
