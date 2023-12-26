import json
from faker import Faker
from random import randint, choice

fake = Faker()
fake = Faker('fr_FR')

data = []

for _ in range(0, 188):
    id_client = _
    nom = fake.first_name()
    prenom = fake.last_name()
    email = fake.email()
    adresse = fake.address()
    login = fake.user_name()
    mdp = fake.password()
    transport = choice(["Vélo de livraison", "Scooter électrique", "Voiture de livraison", "Drone de livraison", "Trottinette électrique", "Camion de livraison urbain", "Cargaison à pied", "Van de livraison", "Transport en commun"])
    porte_feuille = randint(0, 300)

    client_data = {
        "id_client": id_client,
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "adresse": adresse,
        "login": login,
        "mdp": mdp,
        "transport": transport,
        "porte_feuille": porte_feuille
    }

    data.append(client_data)
    
json_output = json.dumps(data, indent=1)
with open('data_transporteur.json', 'w') as file:
    file.write(json_output)
