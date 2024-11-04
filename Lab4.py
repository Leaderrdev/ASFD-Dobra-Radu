import random

#Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

#Afisare
print(" ".join(progres))

while incercari_ramase > 0 and "_" in progres:
    incercare = input("Introdu o literă sau ghicește întregul cuvânt: ").lower()
    
    # Extra verificare daca utilizatorul a adaugat din prima cuvantul.
    if incercare == cuvant_de_ghicit:
        print("Bravo, ai ghicit din prima cuvântul. Se pare că ai avut noroc!")
        progres = list(cuvant_de_ghicit)
        break
    
    #Verificarea literei
    if len(incercare) != 1 or not incercare.isalpha():
        print("Te rog să introduci o singură literă.")
        continue
    if incercare in litere_incercate:
        print("Ai încercat deja această literă.")
        continue

    #Adaugă litera
    litere_incercate.append(incercare)

    #Verificare
    if incercare in cuvant_de_ghicit:
        for i, l in enumerate(cuvant_de_ghicit):
            if l == incercare:
                progres[i] = incercare
        print("Bravo! Litera este în cuvânt.")
    else:
        incercari_ramase -= 1
        print(f"Litera nu este în cuvânt. Îți mai rămân {incercari_ramase} încercări.")

    # Afișarea progresului și încercărilor rămase
    print("Progres:", " ".join(progres))
    print("Încercări rămase:", incercari_ramase)

#Final de joc
if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvântul era:", cuvant_de_ghicit)
