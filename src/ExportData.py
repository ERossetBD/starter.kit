"""Nom : ExportData.py
   Auteur : Estelle Rosset
   Modifié le : 25/04/2022
   Description : Script permettant l'export des données dans un CSV
   à partir d'une liste de plusieurs objets de type logement"""

import logging
import pandas as pd


class ExportData:
    # This is the constructor of the class. It is empty here.
    def __init__(self):
        pass

    @staticmethod
    def export(listLogement, filename):
        """Function which serves to export list of lodging into a CSV file..

        Args:
            listLogement (list) : list of lodgings
            filename (string): name of the CSV file

        Returns:
            dataframe : dataframe which contains data export on the CSV file
        """
        logging.info("Démarrage de l'export de données.")

        df_logement = pd.DataFrame(
            columns=["ID", "Adresse", "Ville", "Categorie", "Surface", "Prix"]
        )

        for i, logement in enumerate(listLogement):
            df_logement.loc[i] = [
                logement.id,
                logement.adresse,
                logement.ville,
                logement.categorie,
                logement.surface,
                logement.prix,
            ]

        df_logement.to_csv(
            "data/output/" + filename, sep=";", encoding="UTF-8", index=False
        )
        logging.info("Export des nouvelles données dans le dossier data.")
        return df_logement
