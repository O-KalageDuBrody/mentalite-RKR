from flask import *

app = Flask(__name__)

gestionnaire = {
    'TFerragu': {
        'nom': 'Ferragu',
        'prenom': 'Thomas',
        'age': 25,
        'notes': {
            'Maths': [12, 14],
            'NSI': [14, 17, 15],
            'Physique': [20, 20]
        }
    },
    'BLéa': {
        'nom': 'Léa',
        'prenom': 'BARBERON',
        'age': 25,
        'notes': {
            'Maths': [20, 14],
            'NSI': [20, 14, 20, 20],
            'Physique': []
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html', eleves=gestionnaire)

@app.route('/eleve/<id>')
def eleve(id):
    eleve = gestionnaire.get(id, None)
    if eleve:
        return render_template('eleve.html', eleve=eleve)
    return "Élève non trouvé", 404

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        id = request.form['id']
        nom = request.form['nom']
        prenom = request.form['prenom']
        age = int(request.form['age'])
        gestionnaire[id] = {
            'nom': nom,
            'prenom': prenom,
            'age': age,
            'notes': {}
        }
        return redirect(url_for('index'))
    return render_template('ajouter.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
