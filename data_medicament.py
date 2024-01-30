import json
from random import randint, choice

#liste_medicaments = ["Paroxétine", "Celecoxib", "Rabeprazole", "Desloratadine", "Levofloxacine", "Simvastatine", "Pregabaline", "Esomeprazole", "Amitriptyline", "Citalopram", "Hydrocodone", "Trazodone", "Quetiapine", "Metoprolol", "Duloxétine", "Alprazolam", "Valsartan", "Escitalopram", "Fluvoxamine", "Rivastigmine", "Hydromorphone", "Varenicline", "Moxifloxacine", "Telmisartan", "Levetiracetam", "Nebivolol", "Dextrométhorphane", "Dipyridamole", "Gabapentine", "Enoxaparine", "Fexofenadine", "Bupropion", "Oxcarbazépine", "Dorzolamide", "Leuproreline", "Piroxicam", "Ramipril", "Gemfibrozil", "Amiodarone", "Perindopril", "Terazosine", "Lorazepam", "Hydroxyzine", "Ipratropium", "Pseudoéphédrine", "Venlafaxine", "Chlorpromazine", "Risperidone", "Haloperidol", "Methotrexate", "Naproxène", "Méthadone", "Nifédipine", "Clindamycine", "Prochlorpérazine", "Glycopyrrolate", "Ceftriaxone", "Chlorpheniramine", "Mirtazapine", "Diclofénac", "Aripiprazole", "Azathioprine", "Olanzapine", "Famotidine", "Pantoprazole", "Carbamazépine", "Céfalexine", "Lamotrigine", "Sulfaméthoxazole", "Triméthoprime", "Fentanyl", "Codeine", "Méprobamate", "Clozapine", "Chlorhexidine", "Tolterodine", "Procyclidine", "Doxazosine", "Méthylprednisolone", "Amiloride", "Guanfacine", "Clonidine", "Baclofen", "Pramipexole", "Rivastigmine", "Metoclopramide", "Fluoxetine", "Nortriptyline", "Clomipramine", "Diazépam", "L-DOPA", "Dopamine", "Dopaminergique", "Dopamine agoniste", "Dopamine récepteur", "Dopamine transporter", "Dopaminomimétique", "Dopaminergie", "Dopamimétique", "Dopaminolytique", "Dopaminergisme", "Dopaminobloquant", "Dopaminomimèse", "Dopaminomimétisme", "Dopaminomimétiquement", "Dopaminomimétique", "Dopaminolyse", "Dopaminolytique", "Dopaminolytiquement", "Dopaminolytiques", "Dopaminomimés", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulateur", "Dopaminorégulation", "Dopaminorégulé", "Dopaminorégulée", "Dopaminorégulés", "Dopaminorégulées", "Dopaminorégulatrice", "Dopaminorégulatrices", "Dopaminorégulatif", "Dopaminorégulatifs", "Dopaminorégulatrice", "Dopaminorégulateurs", "Dopaminorégulation", "Dopaminorégulations", "Dopaminorégulier", "Dopaminorégulière", "Dopaminoréguliers", "Dopaminorégulières", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulée", "Dopaminorégulées", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulé", "Dopaminorégulée", "Dopaminorégulés", "Dopaminorégulées", "Dopaminorégulateur", "Dopaminorégulateurs", "Dopaminorégulatrice", "Dopaminorégulatrices", "Dopaminorégulatif", "Dopaminorégulatifs", "Dopaminorégulatrice", "Dopaminorégulateurs", "Dopaminorégulation", "Dopaminorégulations", "Dopaminorégulier", "Dopaminorégulière", "Dopaminoréguliers", "Dopaminorégulières", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulée", "Dopaminorégulées", "Dopaminorécepteur", "Dopaminorécepteurs", "Dopaminorégulé", "Dopaminorégulée", "Dopaminorégulés", "Dopaminorégulées", "Dopaminorégulateur", "Dopaminorégulateurs", "Dopaminorégulatrice", "Dopaminorégulatrices", "Dopaminorégulatif", "Dopaminorégulatifs", "Dopaminorégulatrice", "Dopaminorégulateurs", "Dopaminorégulation", "Dopaminorégulations", "Dopaminorégulier", "Dopaminorégulière", "Dopaminoréguliers", "Dopaminorégulières", "Clavamox", "Rimadyl", "Deramaxx", "Metacam", "Cephalexin", "Enrofloxacin", "Fluoxetine", "Milbemycin", "Praziquantel", "Prednisolone", "Carprofen", "Doxycycline", "Amitriptyline", "Maropitant", "Trilostane", "Fipronil", "Methimazole", "Phenobarbital", "Levothyroxine", "Meloxicam", "Dexamethasone", "Sulfamethoxazole", "Trimethoprim", "Ivermectin", "Selamectin", "Lufenuron", "Ketoconazole", "Famotidine", "Sucralfate", "Cimetidine", "Metronidazole", "Cephalexin", "Tylosin", "Pentoxifylline", "Atopica", "Cerenia", "Benadryl", "Diazepam", "Tramadol", "Gabapentin", "Griseofulvin", "Cefpodoxime", "Clindamycin", "Terbinafine", "Estradiol", "Deslorelin", "Insulin", "Prozinc", "Lantus", "Felimazole", "Epogen", "Epoetin", "Oxytetracycline", "Baytril", "Doxyvet", "Albon", "Drontal", "Panacur", "Milpro", "Revolution", "Advantage", "Bravecto", "Comfortis", "Frontline", "Heartgard", "Interceptor", "Sentinel", "Trifexis", "Vectra", "Zylkene", "Cosequin", "Dasuquin", "Adaptil", "Feliway", "Seresto", "Hills", "Royal Canin", "Iams", "Purina", "Eukanuba", "Hartz", "Kong", "Nylabone", "Greenies", "Whiskas", "Temptations", "Meow Mix", "Pfizer-BioNTech", "Moderna", "Johnson & Johnson's Janssen", "AstraZeneca", "Sinopharm", "Sinovac", "Sputnik V", "Novavax", "Covaxin", "Covovax", "Comirnaty", "Vaxzevria", "Janssen COVID-19 Vaccine", "Covishield", "Gam-COVID-Vac", "BBIBP-CorV", "Sinopharm BIBP", "CoronaVac", "Ad26.COV2.S", "NVX-CoV2373", "Bharat Biotech's Covaxin", "Pfizer-BioNTech COVID-19 Vaccine", "Moderna COVID-19 Vaccine", "Johnson & Johnson's Janssen COVID-19 Vaccine", "AstraZeneca COVID-19 Vaccine", "Sinopharm COVID-19 Vaccine", "Sinovac COVID-19 Vaccine", "Sputnik V COVID-19 Vaccine", "Novavax COVID-19 Vaccine", "Bharat Biotech's Covaxin", "Covovax (Novavax)", "Comirnaty (Pfizer-BioNTech)", "Vaxzevria (AstraZeneca)", "Janssen COVID-19 Vaccine", "Covishield (AstraZeneca)", "Gam-COVID-Vac (Sputnik V)", "BBIBP-CorV (Sinopharm)", "CoronaVac (Sinovac)", "Ad26.COV2.S (Johnson & Johnson's Janssen)", "NVX-CoV2373 (Novavax)"]
liste_types_medicaments = ["Antibiotiques", "Anti-inflammatoires", "Antipyrétiques", "Antihistaminiques", "Antiviraux", "Antifongiques", "Antiparasitaires", "Antispasmodiques", "Antihypertenseurs", "Diurétiques", "Anticoagulants", "Antiplaquettaires", "Antidépresseurs", "Anxiolytiques", "Antipsychotiques", "Anticonvulsivants", "Analgésiques", "Antipyrétiques", "Antitussifs", "Expectorants", "Bronchodilatateurs", "Antihistaminiques", "Antiemétiques", "Antidiarrhéiques", "Laxatifs", "Antifongiques", "Antiprurigineux", "Corticostéroïdes", "Antimigraineux", "Hormones thyroïdiennes", "Antidiabétiques", "Antagonistes des récepteurs H2", "Inhibiteurs de la pompe à protons", "Anti-ulcéreux", "Antispasmodiques gastro-intestinaux", "Vitamines", "Minéraux", "Antiallergiques", "Immunosuppresseurs", "Vaccins", "Antiseptiques", "Antibactériens topiques", "Antifongiques topiques", "Anti-inflammatoires topiques", "Analgésiques topiques", "Décongestionnants nasaux", "Anesthésiques locaux", "Antiprurigineux topiques", "Antiparasitaires topiques", "Antiviraux topiques", "Émollients", "Humectants", "Kératolytiques", "Cicatrisants", "Antiacnéiques", "Antirides", "Protecteurs solaires", "Anticholinergiques", "Vasodilatateurs", "Antiangoreux", "Antiarythmiques", "Agents antithyroïdiens", "Antituberculeux", "Antiviraux", "Antinéoplasiques", "Immunomodulateurs", "Anticoagulants", "Antiagrégants plaquettaires", "Antihyperlipidémiants", "Antianémiques", "Antiangoreux", "Antihypertenseurs", "Bronchodilatateurs", "Corticoïdes inhalés", "Antitussifs", "Anticholinergiques inhalés", "Antiallergiques inhalés"]
liste_effets_medicaments = ["Sédation", "Insomnie", "Nausées", "Vomissements", "Diarrhée", "Constipation", "Sécheresse buccale", "Vertiges", "Maux de tête", "Hypertension", "Hypotension", "Palpitations", "Tachycardie", "Rétention urinaire", "Saignements", "Hémorragies", "Rash cutané", "Démangeaisons", "Urticaire", "Photosensibilité", "Œdème", "Anorexie", "Prise de poids", "Perte de poids", "Troubles du sommeil", "Agitation", "Anxiété", "Dépression", "Troubles de la vision", "Bouche sèche", "Douleurs musculaires", "Arthralgie", "Myalgie", "Hépatotoxicité", "Néphrotoxicité", "Troubles gastro-intestinaux", "Neuropathie périphérique", "Sensations de picotement", "Confusion", "Hallucinations", "Dépendance", "Tolérance", "Réactions allergiques", "Fièvre", "Fatigue", "Sensation de malaise", "Syndrome sérotoninergique", "Syndrome extrapyramidal", "Hypoglycémie", "Hyperglycémie", "Hypokaliémie", "Hyperkaliémie", "Hyponatrémie", "Hypernatrémie", "Hypocalcémie", "Hypercalcémie", "Thrombocytopénie", "Leucopénie", "Anémie", "Agranulocytose", "Torsades de pointes", "QT prolongé", "Troubles de la coagulation", "Thrombose", "Embolie pulmonaire", "Hémorragie gastro-intestinale", "Insuffisance hépatique", "Insuffisance rénale", "Défaillance multiviscérale", "Syndrome de Stevens-Johnson", "Syndrome de Lyell", "Anaphylaxie", "Cancer", "Malformations congénitales", "Impuissance", "Infertilité", "Tératogénicité", "Mémoire altérée", "Perte d'appétit sexuel", "Syndrome de sevrage", "Réactions au site d'injection", "Frissons", "Troubles respiratoires", "Syndrome de sevrage", "Syndrome malin des neuroleptiques", "Réactions cutanées graves", "Troubles de l'équilibre", "Troubles de la coordination", "Tremblements", "Convulsions", "Pensées suicidaires", "Troubles de la marche", "Syndrome des jambes sans repos", "Vision floue"]
liste_deconseiller = ["Femmes enceintes", "Personnes âgées", "Enfants de moins de 12 ans", "Personnes allergiques aux composants", "Personnes atteintes de troubles cardiaques"]

liste_medicaments = [
    "Rivaroxaban",
    "Enoxaparine",
    "Levofloxacin",
    "Acyclovir",
    "Methylprednisolone",
    "Hydrocortisone",
    "Gabapentin",
    "Pregabalin",
    "Trazodone",
    "Metoprolol",
    "Clonidine",
    "Hydralazine",
    "Nifedipine",
    "Diltiazem",
    "Risperidone",
    "Quetiapine",
    "Clozapine",
    "Levetiracetam",
    "Loratadine",
    "Cetirizine",
    "Doxazosin",
    "Terazosin",
    "Esomeprazole",
    "Mirtazapine",
    "Sotalol",
    "Carvedilol",
    "Nitroglycerin",
    "Isosorbide",
    "Bupropion",
    "Olanzapine",
    "Haloperidol",
    "Perindopril",
    "Ramipril",
    "Famotidine",
    "Lamotrigine",
    "Amitriptyline",
    "Oxycodone",
    "Hydrocodone",
    "Methadone",
    "Benzonatate",
    "Docusate",
    "Ferrous Sulfate",
    "Loperamide",
    "Albuterol",
    "Ipratropium",
    "Budesonide",
    "Formoterol",
    "Tiotropium",
    "Dornase Alfa",
    "Montelukast",
    "Zafirlukast",
    "Ezetimibe",
    "Clopidogrel",
    "Dabigatran",
    "Apixaban",
    "Fondaparinux",
    "Azelastine",
    "Mometasone",
    "Bimatoprost",
    "Ropinirole",
    "Entacapone"
]


data = []

for i in range(0,len(liste_medicaments)):

    client_data = {
        "nom": liste_medicaments[i],
        "type_medicament": liste_types_medicaments[i%len(liste_types_medicaments)],
        "effet": liste_effets_medicaments[i%len(liste_effets_medicaments)],
        "temp_effet_min": randint(0, 2880),
        "duree_effet_min": randint(0, 2880),
        "niveau_danger": randint(0, 6),
        "qt_max": randint(1,45),
        "deconseiller_a": choice(liste_deconseiller),
        "prix": randint(5, 680)
    }

    data.append(client_data)
    
json_output = json.dumps(data, indent=1)
with open('data_medicament.json', 'w') as file:
    file.write(json_output)
