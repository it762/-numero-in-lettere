from flask import Flask, jsonify
from num2words import num2words

app = Flask(__name__)

@app.route('/numero-in-lettere/<numero>', methods=['GET'])
def numero_in_lettere(numero):
    try:
        numero = float(numero)
        parte_intera = int(numero)
        parte_decimale = int(round((numero - parte_intera) * 100))
        
        lettere = num2words(parte_intera, lang='it')
        risultato = {
            "valore": f"{lettere} / {parte_decimale:02d}"
        }
        return jsonify(risultato)
    except Exception as e:
        return jsonify({"errore": str(e)}), 400