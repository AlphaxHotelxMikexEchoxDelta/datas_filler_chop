import json
from random import randint

def lire_fichier_json(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        data = json.load(fichier)
    return data

donnees_pharmacies = lire_fichier_json("gouv.json")

pharmacies_data_list = []

cpt = 0
for donnees_pharmacie in donnees_pharmacies:
    if 'fields' in donnees_pharmacie and all(key in donnees_pharmacie['fields'] for key in ['rs', 'numvoie', 'typvoie', 'voie', 'cp', 'commune']):
        nom_pharmacie = donnees_pharmacie['fields']['rs']
        adresse_pharmacie = f"{donnees_pharmacie['fields']['numvoie']} {donnees_pharmacie['fields']['typvoie']} {donnees_pharmacie['fields']['voie']}, {donnees_pharmacie['fields']['cp']} {donnees_pharmacie['fields']['commune']}"

        nouvelle_donnee_pharmacie = {
            "Id_Pharmacie": cpt,
            "Nom": nom_pharmacie,
            "Adresse": adresse_pharmacie,
            "HORRAIRE_OUVERT": f"{randint(6,10)}",
            "HORRAIRE_FERMER": f"{randint(18,23)}",
            "Porte_Feuille": randint(0,22000)
        }
        pharmacies_data_list.append(nouvelle_donnee_pharmacie)
        cpt = cpt + 1



with open("data_pharmacie.json", 'w') as nouveau_fichier:
    json.dump(pharmacies_data_list, nouveau_fichier, indent=1)