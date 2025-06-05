from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

# Încarcă datele din fișierul JSON
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Salvează datele în fișierul JSON
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    produse = load_data()
    return render_template('index.html', produse=produse)

@app.route('/adauga', methods=['POST'])
def adauga():
    produse = load_data()
    try:
        id_nou = request.form.get('id', '').strip()
        nume_nou = request.form.get('nume', '').strip()
        cantitate_nou = request.form.get('cantitate', '').strip()
        pret_nou = request.form.get('pret', '').strip()
        if not (id_nou.isdigit() and cantitate_nou.isdigit() and pret_nou.isdigit() and nume_nou):
            return "Date invalide", 400
        produs_nou = {
            "id": int(id_nou),
            "nume": nume_nou,
            "cantitate": int(cantitate_nou),
            "pret": int(pret_nou)
        }
        produse.append(produs_nou)
        save_data(produse)
        return redirect('/')
    except Exception as e:
        return f"Eroare la adăugare: {e}", 400

@app.route('/sterge', methods=['POST'])
def sterge():
    id_str = request.form.get('id', '').strip()
    if not id_str.isdigit():
        return "ID invalid sau lipsă", 400
    id_de_sters = int(id_str)
    produse = load_data()
    produse = [p for p in produse if p['id'] != id_de_sters]
    save_data(produse)
    return redirect('/')

@app.route('/editeaza', methods=['POST'])
def editeaza():
    id_str = request.form.get('id', '').strip()
    nume_nou = request.form.get('nume', '').strip()
    cantitate_nou = request.form.get('cantitate', '').strip()
    pret_nou = request.form.get('pret', '').strip()
    if not (id_str.isdigit() and cantitate_nou.isdigit() and pret_nou.isdigit() and nume_nou):
        return "Date invalide", 400
    id_modif = int(id_str)
    produse = load_data()
    for produs in produse:
        if produs['id'] == id_modif:
            produs['nume'] = nume_nou
            produs['cantitate'] = int(cantitate_nou)
            produs['pret'] = int(pret_nou)
            break
    save_data(produse)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
