"""Nom : main.py
   Auteur : Estelle Rosset
   Modifié le : 20/04/2022
   Description : Script main qui récupère le fichier des logements, mets à jour les prix et génère un nouvel export."""

"""Import des packages et des classes nécessaires"""

import pandas as pd
import logging

from config.LogConfig import LogConfig

from src.ImportData import ImportData
from src.Logement import Logement
from src.ExportData import ExportData

"""Créations des fonctions utiles au programme"""

def createListLogement(dataframe):
    """Return the list of lodging (object type) from a dataframe.

    Returns:
        list of objects : list of lodgings
    """
    lst = [Logement(a.ID, a.Adresse, a.Ville, a.Categorie, a.Surface, a.Prix) for a in dataframe.itertuples()]
    return lst

"""Contenu du script main"""
if __name__ == '__main__':

    # Start the logs from the configuration program.
    LogConfig().start_logging()

    # Loading data source into a dataframe.
    logements_df = ImportData().load('Mars2022.csv')

    # Instantiation of lodgings from the loaded data and the createListLogement() function.
    logements_lst = createListLogement(logements_df)

    # Call the class method to update the price of each lodging.
    for logement in logements_lst:
        logement.updatePrice()

    logging.info("Mise à jour des données terminée.")

    # Export data to a new CSV file.
    ExportData.export(logements_lst, 'Avril2022.csv')

    logging.info("Fin du traitement.")