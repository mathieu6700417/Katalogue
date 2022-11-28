import os
import yaml
import requests
import zipfile
from pathlib import Path
import pandas as pd

class Dépot:
    def __init__(self, nom_fournisseur):
        chemin_dossier = os.path.dirname(__file__)
        
        fichier_conf = os.path.join(chemin_dossier, "config.yaml")
        conf = yaml.safe_load(open(fichier_conf, "r").read())

        dossier = os.path.expanduser(conf['dossier'])
        dossier_dépot = os.path.join(dossier, nom_fournisseur)
        if not(os.path.exists(dossier)):
            os.mkdir(dossier)
            
        if not(os.path.exists(dossier_dépot)):
            os.mkdir(dossier_dépot)
        
        chemin_conf_fournisseur = os.path.join(chemin_dossier, f"{nom_fournisseur}/{nom_fournisseur}.yaml")
        self.config =  yaml.safe_load(open(chemin_conf_fournisseur, "r").read())
        self.dossier = dossier_dépot
        
        
    def télécharger(self, nom_source, forcer_téléchargement=False):
        url_fichier = self.config.get(nom_source).get('url')
        chemin_fichier = self.chemin_fichier(nom_source)

        if not(os.path.exists(chemin_fichier)) or forcer_téléchargement:
            resp = requests.get(url_fichier)
            with open(chemin_fichier, "wb") as f:
                f.write(resp.content)

    def désarchiver(self, nom_source, ecraser_cible=False):
        nom_fichier = self.config.get(nom_source).get('fichier')
        chemin_archive = os.path.join(self.dossier, nom_fichier)
        chemin_extraction = os.path.join(self.dossier, nom_source)
        
        if not(os.path.exists(chemin_extraction)) or ecraser_cible:
            with zipfile.ZipFile(chemin_archive, 'r') as zip_ref:
                Path(chemin_extraction).mkdir(parents=True, exist_ok=True)
                zip_ref.extractall(chemin_extraction)
        

    def chemin_fichier(self, nom_source):
        return os.path.join(self.dossier, self.config.get(nom_source).get('fichier'))

    def chemin_extraction(self, nom_source):
        return os.path.join(self.dossier, nom_source)

    def sauvegarde_locale(fonction):
        def fonction_avec_sauvegarde(self, *argparams, **kwparams): #param, sauvegarder_localement): #TODO: gestion générique des params cas autres
            nom_dépôt = self.__class__.__name__
            nom_fonction = fonction.__name__
            chemin_sauvegarde_locale = os.path.join(self.dossier,f'locale_{nom_dépôt}_{nom_fonction}.pkl')
            
            if kwparams['sauvegarder_localement']:
                if not(os.path.exists(chemin_sauvegarde_locale)): 
                    print("Aucune sauvegarde existante, calcul")
                    df = fonction(self, *argparams, **kwparams)
                    df.to_pickle(chemin_sauvegarde_locale) 
                    print("Sauvegarde locale réalisée ", chemin_sauvegarde_locale)
                else:
                    print("Lecture sauvegarde existante ", chemin_sauvegarde_locale)
                    df = pd.read_pickle(chemin_sauvegarde_locale)
            else:
                df = fonction(self, *argparams, **kwparams)

            return df

        return fonction_avec_sauvegarde
