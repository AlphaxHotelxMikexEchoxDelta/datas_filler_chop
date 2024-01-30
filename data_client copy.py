import json
from faker import Faker
from random import randint, choice

fake = Faker()
fake = Faker('fr_FR')

data = []
liste_medoc = ["Paroxétine", "Celecoxib", "Rabeprazole", "Desloratadine", "Levofloxacine", "Simvastatine", "Pregabaline", "Esomeprazole", "Amitriptyline", "Citalopram", "Hydrocodone", "Trazodone", "Quetiapine", "Metoprolol", "Duloxétine", "Alprazolam", "Valsartan", "Escitalopram", "Fluvoxamine", "Rivastigmine", "Hydromorphone", "Varenicline", "Moxifloxacine", "Telmisartan", "Levetiracetam", "Nebivolol", "Dextrométhorphane", "Dipyridamole", "Gabapentine", "Enoxaparine", "Fexofenadine", "Bupropion", "Oxcarbazépine", "Dorzolamide", "Leuproreline", "Piroxicam", "Ramipril", "Gemfibrozil", "Amiodarone", "Perindopril", "Terazosine", "Lorazepam", "Hydroxyzine", "Ipratropium", "Pseudoéphédrine", "Venlafaxine", "Chlorpromazine", "Risperidone", "Haloperidol", "Methotrexate", "Naproxène", "Méthadone", "Nifédipine", "Clindamycine", "Prochlorpérazine", "Glycopyrrolate", "Ceftriaxone", "Chlorpheniramine", "Mirtazapine", "Diclofénac", "Aripiprazole", "Azathioprine", "Olanzapine", "Famotidine", "Pantoprazole", "Carbamazépine", "Céfalexine", "Lamotrigine", "Sulfaméthoxazole", "Triméthoprime", "Fentanyl", "Codeine", "Méprobamate", "Clozapine", "Chlorhexidine", "Tolterodine", "Procyclidine", "Doxazosine", "Méthylprednisolone", "Amiloride", "Guanfacine", "Clonidine", "Baclofen", "Pramipexole", "Rivastigmine", "Metoclopramide", "Fluoxetine", "Nortriptyline", "Clomipramine", "Diazépam", "L-DOPA", "Dopamine", "Dopaminergique", "Dopamine agoniste", "Dopamine récepteur", "Dopamine transporter", "Dopaminomimétique", "Dopaminergie", "Dopamimétique", "Dopaminolytique", "Dopaminergisme", "Dopaminobloquant", "Dopaminomimèse", "Dopaminomimétisme", "Dopaminomimétiquement", "Dopaminomimétique", "Dopaminolyse", "Dopaminolytique", "Dopaminolytiquement", "Dopaminolytiques", "Dopaminomimés", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulateur", "Dopaminorégulation", "Dopaminorégulé", "Dopaminorégulée", "Dopaminorégulés", "Dopaminorégulées", "Dopaminorégulatrice", "Dopaminorégulatrices", "Dopaminorégulatif", "Dopaminorégulatifs", "Dopaminorégulatrice", "Dopaminorégulateurs", "Dopaminorégulation", "Dopaminorégulations", "Dopaminorégulier", "Dopaminorégulière", "Dopaminoréguliers", "Dopaminorégulières", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulée", "Dopaminorégulées", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulé", "Dopaminorégulée", "Dopaminorégulés", "Dopaminorégulées", "Dopaminorégulateur", "Dopaminorégulateurs", "Dopaminorégulatrice", "Dopaminorégulatrices", "Dopaminorégulatif", "Dopaminorégulatifs", "Dopaminorégulatrice", "Dopaminorégulateurs", "Dopaminorégulation", "Dopaminorégulations", "Dopaminorégulier", "Dopaminorégulière", "Dopaminoréguliers", "Dopaminorégulières", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulée", "Dopaminorégulées", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulé", "Dopaminorégulée", "Dopaminorégulés", "Dopaminorégulées", "Dopaminorégulateur", "Dopaminorégulateurs", "Dopaminorégulatrice", "Dopaminorégulatrices", "Dopaminorégulatif", "Dopaminorégulatifs", "Dopaminorégulatrice", "Dopaminorégulateurs", "Dopaminorégulation", "Dopaminorégulations", "Dopaminorégulier", "Dopaminorégulière", "Dopaminoréguliers", "Dopaminorégulières", "Clavamox", "Rimadyl", "Deramaxx", "Metacam", "Cephalexin", "Enrofloxacin", "Fluoxetine", "Milbemycin", "Praziquantel", "Prednisolone", "Carprofen", "Doxycycline", "Amitriptyline", "Maropitant", "Trilostane", "Fipronil", "Methimazole", "Phenobarbital", "Levothyroxine", "Meloxicam", "Dexamethasone", "Sulfamethoxazole", "Trimethoprim", "Ivermectin", "Selamectin", "Lufenuron", "Ketoconazole", "Famotidine", "Sucralfate", "Cimetidine", "Metronidazole", "Cephalexin", "Tylosin", "Pentoxifylline", "Atopica", "Cerenia", "Benadryl", "Diazepam", "Tramadol", "Gabapentin", "Griseofulvin", "Cefpodoxime", "Clindamycin", "Terbinafine", "Estradiol", "Deslorelin", "Insulin", "Prozinc", "Lantus", "Felimazole", "Epogen", "Epoetin", "Oxytetracycline", "Baytril", "Doxyvet", "Albon", "Drontal", "Panacur", "Milpro", "Revolution", "Advantage", "Bravecto", "Comfortis", "Frontline", "Heartgard", "Interceptor", "Sentinel", "Trifexis", "Vectra", "Zylkene", "Cosequin", "Dasuquin", "Adaptil", "Feliway", "Seresto", "Hills", "Royal Canin", "Iams", "Purina", "Eukanuba", "Hartz", "Kong", "Nylabone", "Greenies", "Whiskas", "Temptations", "Meow Mix", "Pfizer-BioNTech", "Moderna", "Johnson & Johnson's Janssen", "AstraZeneca", "Sinopharm", "Sinovac", "Sputnik V", "Novavax", "Covaxin", "Covovax", "Comirnaty", "Vaxzevria", "Janssen COVID-19 Vaccine", "Covishield", "Gam-COVID-Vac", "BBIBP-CorV", "Sinopharm BIBP", "CoronaVac", "Ad26.COV2.S", "NVX-CoV2373", "Bharat Biotech's Covaxin", "Pfizer-BioNTech COVID-19 Vaccine", "Moderna COVID-19 Vaccine", "Johnson & Johnson's Janssen COVID-19 Vaccine", "AstraZeneca COVID-19 Vaccine", "Sinopharm COVID-19 Vaccine", "Sinovac COVID-19 Vaccine", "Sputnik V COVID-19 Vaccine", "Novavax COVID-19 Vaccine", "Bharat Biotech's Covaxin", "Covovax (Novavax)", "Comirnaty (Pfizer-BioNTech)", "Vaxzevria (AstraZeneca)", "Janssen COVID-19 Vaccine", "Covishield (AstraZeneca)", "Gam-COVID-Vac (Sputnik V)", "BBIBP-CorV (Sinopharm)", "CoronaVac (Sinovac)", "Ad26.COV2.S (Johnson & Johnson's Janssen)", "NVX-CoV2373 (Novavax)"]
liste_ordo = [
    "https://youtu.be/1uYWYWPc9HU?si=nRyGE7DKSoXNbl-O",
    "https://youtu.be/XFkzRNyygfk?si=aEuqT2FVvtDimVW0",
    "https://youtu.be/u5CVsCnxyXg?si=8Op7R4PkE8KJExVz",
    "https://youtu.be/7qFfFVSerQo?si=RRKiQWP6eGotOTAS",
    "https://th.bing.com/th/id/OIP.X7bywy-40-XZNC9_M9N2jgHaEK?w=312&h=180&c=7&r=0&o=5&dpr=2&pid=1.7",
    "https://youtu.be/fregObNcHC8?si=9X7HQ_pg0AVg-zdG",
    "https://youtu.be/DnGdoEa1tPg?si=oQnWo9uM-tUg5qKI",
    "https://youtu.be/gOMhN-hfMtY?si=Nrb7BzaQMfxFZ4vL"
]


for _ in range(0,2645):
    id_commande = _
    client = randint(0, 689)
    pharmacie = randint(0, 3623)
    medicament = choice(liste_medoc)
    livreur = randint(0, 187)
    quantitee = randint(1, 45)
    ordonance = choice(liste_ordo)


    commande_data = {
        "id_commande": id_commande,
        "client": client,
        "pharmacie": pharmacie,
        "medicament": medicament,
        "livreur": livreur,
        "quantitee": quantitee,
        "ordonance": ordonance
    }

    data.append(commande_data)
    
json_output = json.dumps(data, indent=1)
with open('data_commande.json', 'w') as file:
    file.write(json_output)
