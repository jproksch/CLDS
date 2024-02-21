class Controller:
    """
    Die Controller-Klasse im MVC-Framework, die für die Koordination zwischen der View und dem Model verantwortlich ist.
    Sie reagiert auf Benutzeraktionen, holt Daten vom Model und aktualisiert die View.
    """

    def __init__(self, model, view):
        """
        Der Konstruktor der Controller-Klasse.

        Args:
            model (Model): Die Instanz der Model-Klasse, die die Geschäftslogik enthält.
            view (View): Die Instanz der View-Klasse, die die Benutzeroberfläche definiert.
        """
        self.model = model  # Referenz auf das Model speichern
        self.view = view    # Referenz auf die View speichern
        self.view.connect_controller(self)  # Verbindung zwischen View und Controller herstellen

    def process_input(self):
        """
        Verarbeitet die Eingabe des Benutzers, indem der Text aus der View geholt, an das Model gesendet
        und das Ergebnis von der Model-Klasse empfangen wird. Das Ergebnis wird dann in der View dargestellt.
        """
        # Holen des Textes aus der View
        input_text = self.view.get_input_text()
        # Senden des Textes an das Model und Empfangen der Antwort
        result = self.model.checkSprache(input_text)
        # Darstellen des Ergebnisses in der View
        self.view.set_result_text(result)

    def reset_input(self):
        """
        Setzt die Eingabefelder der View zurück, indem der Inhalt der Textfelder gelöscht wird.
        """
        # Löschen des Inhalts der Eingabe- und Ergebnistextfelder
        self.view.input_text_edit.clear()
        self.view.result_text_edit.clear()

    def close_app(self):
        """
        Schließt die Anwendung, indem das Hauptfenster geschlossen wird.
        """
        # Schließen des Hauptfensters der Anwendung
        self.view.close()
