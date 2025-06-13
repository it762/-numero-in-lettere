from flask import Flask, request, jsonify
from num2words import num2words

app = Flask(__name__)

@app.route('/numero-in-lettere', methods=['GET'])
def numero_in_lettere():
    numero = request.args.get('numero')
    try:       
        numero = float(numero)
        numero_intero = int(numero)
        lettere = num2words(numero_intero, lang='it')

        return jsonify({"numero": numero, "lettere": lettere})
    except Exception as e:
        return jsonify({"errore": str(e)}), 400

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=10000)