from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route("/contact/")
def MaPremiereAPI():
    # Affiche le fichier HTML à la place du texte brut
    return render_template("contact.html")
@app.route('/tawarano/')
def meteo():
    # Remplacez l'URL si nécessaire, mais l'exercice utilise la version sample
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    
    # Parcourt la liste des prévisions (clé 'list' dans la réponse JSON)
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        # Extraction de la température et conversion de Kelvin en °C
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 
        
        # Ajout des données filtrées au tableau de résultats
        results.append({'Jour': dt_value, 'temp': temp_day_value})
        
    # Retourne les résultats au format JSON
    return jsonify(results=results)
@app.route("/rapport/")
def mongraphique():
    # Flask cherche automatiquement le fichier dans le dossier 'templates'
    return render_template("graphique.html")
@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")
  
  
if __name__ == "__main__":
  app.run(debug=True)
