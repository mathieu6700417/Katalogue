import os
import yaml
import requests

class Dépot:
    def __init__(self, nom_fournisseur):
        chemin_dossier = os.path.dirname(__file__)
        
        fichier_conf = os.path.join(chemin_dossier, "../config.yaml")
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
        nom_fichier = self.config.get(nom_source).get('fichier')
        
        chemin_fichier = os.path.join(self.dossier, nom_fichier)
        if not(os.path.exists(chemin_fichier)) or forcer_téléchargement:
            resp = requests.get(url_fichier)
            with open(chemin_fichier, "wb") as f:
                f.write(resp.content)
        
        
    def chemin_fichier(self, nom_source):
        return os.path.join(self.dossier, self.config.get(nom_source).get('fichier'))