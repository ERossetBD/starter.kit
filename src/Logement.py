"""Nom : Logement.py
   Auteur : Estelle Rosset
   Modifié le : 22/04/2022
   Description : Script permettant la création d'objets Logements
   et les méthodes associées à cette classe."""

import logging


class Logement:
    # This is the constructor of the class Logement.
    def __init__(self, id, adresse, ville, categorie, surface, prix):
        self.id = id
        self.adresse = adresse
        self.ville = ville
        self.categorie = categorie
        self.surface = int(surface)
        self.prix = int(prix)

    # This is an example of class method.
    def updatePrice(self):
        """Return the new price of a lodging after updating.

        Returns:
            int : new price or initial price if updating fails
        """
        if self.categorie == "Maison":
            self.prix = int(self.prix * 1.15)
            logging.info("Mise à jour du prix OK pour cette maison.")
        elif self.categorie == "Appartement":
            self.prix = int(self.prix * 0.95)
            logging.info("Mise à jour du prix OK pour cet appartement.")
        else:
            logging.error("Mise à jour du prix du bien impossible")
        return self.prix
