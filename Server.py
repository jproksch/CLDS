# Importieren der notwendigen Module aus Flask, langdetect und iso639
from flask import Flask, request, jsonify
from langdetect import detect, detect_langs
from iso639 import languages

# Erstellen einer Flask-Anwendung
app = Flask(__name__)

# Dekorator, der die Route '/lg' definiert.
# Diese Route wird aufgerufen, wenn eine GET-Anfrage an den Server gesendet wird.
@app.route('/lg')
def textToSearch():
    # Die GET-Parameter werden abgerufen. 
    # 'id' ist der Name des Parameters, der den zu analysierenden Text enthält.
    text = request.args.get("id")

    # Verwendung von 'detect' aus langdetect, um den Sprachcode des Textes zu ermitteln.
    short_lang = detect(text)
    #print(short_lang)

    # 'detect_langs' gibt eine Liste von Sprachen mit ihren Wahrscheinlichkeiten zurück.
    prob = detect_langs(text)

    # Initialisierung einer Variablen, die angibt, ob das Ergebnis zuverlässig ist.
    prob_value = False

    # Überprüfung, ob die Wahrscheinlichkeit der erkannten Sprache größer als 0,5 ist.
    # Wenn ja, wird 'prob_value' auf True gesetzt.
    if prob[0].prob > 0.5:
        prob_value = True

    # Verwendung des iso639-Pakets, um den vollen Namen der Sprache anhand des Sprachcodes zu erhalten.
    sprachname = languages.get(alpha2=short_lang).name

    # Zerstückelt die Probability und entfernt das {de:}0....
    value = str(prob[0]).split(":")
    # Erstellen eines Dictionaries, das die Daten für die JSON-Antwort enthält.
    data = {
        "reliable": prob_value,     # Zuverlässigkeit der Spracherkennung
        "language": sprachname,     # Voller Name der erkannten Sprache
        "short": short_lang,        # Kurzcode der erkannten Sprache
        "prob": value[1]  # Wahrscheinlichkeiten der erkannten Sprachen als String-Liste
    }
    #print(data)

    return data

# Wenn dieses Skript als Hauptprogramm ausgeführt wird, startet der Flask-Server.
if __name__ == '__main__':
    app.run(debug=False)  # Der Debug-Modus ist ausgeschaltet
