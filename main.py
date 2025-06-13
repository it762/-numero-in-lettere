from flask import Flask, Response
from num2words import num2words

app = Flask(__name__)

@app.route('/numero-in-lettere/<numero>', methods=['GET'])
def numero_in_lettere(numero):
    try:
        numero = float(numero)
        parte_intera = int(numero)
        parte_decimale = int(round((numero - parte_intera) * 100))
        
        lettere = num2words(parte_intera, lang='it')
        risultato = f"{lettere} / {parte_decimale:02d}"
        
        return Response(risultato, mimetype='text/plain')
    except Exception as e:
        return Response(f"Errore: {str(e)}", status=400, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
