from urllib.parse import quote
import requests

class Model:
    """
    Die Model-Klasse im MVC-Framework, die für die Interaktion mit der externen API zur Sprachprüfung verantwortlich ist.
    Sie sendet eine Anfrage an eine API und empfängt die Antwort, welche dann im gewünschten Format zurückgegeben wird.
    """

    def checkSprache(self, text):
        """
        Sendet den zu prüfenden Text an eine API und gibt die Antwort zurück.
        Verwendet URL-Encoding, um sicherzustellen, dass der Text korrekt über die URL übermittelt wird.

        Args:
            text (str): Der Text, dessen Sprache geprüft werden soll.

        Returns:
            dict: Ein Dictionary, das die Antwort der API enthält, wenn die Anfrage erfolgreich war.
            str: Eine Fehlermeldung mit dem Statuscode, wenn die Anfrage fehlgeschlagen ist.
        """
        # URL-Encoding des Textes, um ihn als Parameter in der URL zu verwenden
        encoded_text = quote(text)
        # Erstellen der vollständigen URL für die API-Anfrage
        request_url = f"http://127.0.0.1:5000/lg?id={encoded_text}"
        # Durchführung der GET-Anfrage an die API
        api_answer = requests.get(request_url)

        # Überprüfen des Statuscodes der Antwort
        if api_answer.status_code == 200:
            # Umwandeln der JSON-Antwort in ein Python-Dictionary
            response_data = api_answer.json()
            # Rückgabe der verarbeiteten Daten
            return response_data
        else:
            # Rückgabe einer Fehlermeldung mit dem Statuscode
            return f"Fehler bei der Anfrage: Statuscode {api_answer.status_code}"
