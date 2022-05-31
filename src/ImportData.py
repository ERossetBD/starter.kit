"""Nom : ImportData.py
   Auteur : Estelle Rosset
   Modifié le : 25/04/2022
   Description : Script permettant l'import
   de données à partir d'un fichier csv."""

import logging
import pandas as pd


class ImportData:
    # This is the constructor of the class. It is empty here.
    def __init__(self):
        pass

    @staticmethod
    def load(filename):
        """Function which serves to load data from a CSV file.

        Args:
            filename (string): name of the CSV file

        Returns:
            dataframe : dataframe which contains data of the CSV file
        """
        logging.info("Récupération du fichier de données.")
        logements_df = pd.read_csv("data/input/" + filename, sep=";")
        logging.info("Les données des logements ont été chargées avec succès.")
        return logements_df
