import os, re
import pandas as pd
from katalogue.dépot import Dépot
import requests

class DépôtGutembergLivres(Dépot):
    def __init__(self):
        chemin_dossier = os.path.dirname(__file__)
        nom_dossier_parent = chemin_dossier.split("/")[-1]
        super().__init__(nom_dossier_parent)
        

    def catalogue(self):
        self.télécharger("catalogue")
        df = pd.read_csv(self.chemin_fichier("catalogue"), low_memory=False)
        df.columns = list(map(lambda c: c.lower(), df.columns))
        df.rename(columns={"text#": "livre_id"}, inplace=True)
        df["title"] = df.title.apply(lambda t: re.sub(r"\n", " ", t))
        return df


    def livre(self, livre_id):
        url_gutemberg = "https://www.gutenberg.org/cache/epub"
        url = f"{url_gutemberg}/{livre_id}/pg{livre_id}.txt.utf8"
        livre_fn_name = f"book-{livre_id}.txt"
        self.télécharger_livre(url, livre_fn_name)
        return self.obtenir_texte_livre(livre_id)
        
            
    def télécharger_livre(self, url, fn_name=None):
        if fn_name is None:
            fn_name = list(filter(len, url.split("/")))[-1]
           
        fp = os.path.join(self.dossier, fn_name)
        if not(os.path.exists(fp)):
            resp = requests.get(url)
            with open(fp, "wb") as f:
                f.write(resp.content)
                

        
    def obtenir_texte_livre(self, livre_id):
        livre_fn_name = f"book-{livre_id}.txt"
        with open(os.path.join(self.dossier, livre_fn_name), "r") as f:
            text = f.read()
        return text
    
