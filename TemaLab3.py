meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

contor_comenzi = {"papanasi": 0, "ceafa": 0, "guias": 0}

# Procesarea comenzilor 
print("Comenzi:")
while studenti and comenzi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    
    # Afisarea comenzii
    print(f"{student} a comandat {comanda}.")
    
    # Eliminare tava din stiva
    if tavi:
        tavi.pop()
    
    # Adaugare comanda in istoric
    istoric_comenzi.append(comanda)
    contor_comenzi[comanda] += 1

# Inventar
print("\nInventar:")
print(f"S-au comandat {contor_comenzi['guias']} guias, {contor_comenzi['ceafa']} ceafa, {contor_comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")

# Stocuri 
print(f"Mai este ceafa: {'ceafa' in meniu and contor_comenzi['ceafa'] < meniu.count('ceafa')}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu and contor_comenzi['papanasi'] < meniu.count('papanasi')}.")
print(f"Mai sunt guias: {'guias' in meniu and contor_comenzi['guias'] < meniu.count('guias')}.")

# Finante
# Calculăm încasările totale
incasari = sum(contor_comenzi[produs] * pret for produs, pret in preturi)
print(f"\nCantina a încasat: {incasari} lei.")

# Produse <7 lei
produse_ieftine = [item for item in preturi if item[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_ieftine}.")
