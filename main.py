from flask import Flask, request, jsonify
from num2words import num2words

app = Flask(__name__)

@app.route('/numero-in-lettere', methods=['GET'])
def numero_in_lettere():
    numero = request.args.get('numero')
    try:
        # Converti il numero in float
        numero = float(numero)
        
        # Separare la parte intera e quella decimale
        parte_intera = int(numero)
        parte_decimale = int(round((numero - parte_intera) * 100))
        
        # Converti la parte intera in lettere
        lettere = num2words(parte_intera, lang='it')
        
        # Formatta il risultato
        risultato = {lettere} / {parte_decimale:02d}
        
        return jsonify(risultato)
    except Exception as e:
        return jsonify({"errore": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
