from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTextEdit, QWidget

class View(QMainWindow):
    """
    Die View Klasse des MVC-Frameworks, die für die Darstellung der Benutzeroberfläche verantwortlich ist.
    Sie zeigt Widgets an, die vom Benutzer interagiert werden können, und präsentiert Daten, die vom Controller verarbeitet werden.
    """

    def __init__(self):
        """
        Konstruktor der View Klasse, der die Benutzeroberfläche initialisiert.
        """
        # Initialisierung der Basisklasse QMainWindow
        super().__init__()
        # Aufruf der UI-Setup Methode
        self.init_ui()

    def init_ui(self):
        """
        Initialisiert die Benutzeroberfläche und legt das Layout und die Widgets der Anwendung fest.
        """
        # Festlegen des Fenstertitels
        self.setWindowTitle("My Language Tool")
        # Festlegen der Fenstergröße
        self.resize(600, 500)

        # Erstellen der Labels, TextEdit Felder und Buttons
        self.label1 = QLabel("Please provide your text here:")
        self.label2 = QLabel("Here is your result:")
        self.start_btn = QPushButton("Start")
        self.reset_btn = QPushButton("Reset")
        self.close_btn = QPushButton("Close")
        self.input_text_edit = QTextEdit()
        self.result_text_edit = QTextEdit()

        # Erstellen der Layouts
        main_layout = QVBoxLayout()
        btns_layout = QHBoxLayout()

        # Hinzufügen der Widgets zum Hauptlayout
        main_layout.addWidget(self.label1)
        main_layout.addWidget(self.input_text_edit)
        main_layout.addWidget(self.label2)
        main_layout.addWidget(self.result_text_edit)

        # Hinzufügen der Buttons zum Button-Layout
        btns_layout.addWidget(self.start_btn)
        btns_layout.addWidget(self.reset_btn)
        btns_layout.addWidget(self.close_btn)

        # Integrieren des Button-Layouts in das Hauptlayout
        main_layout.addLayout(btns_layout)

        # Erstellen eines zentralen Widgets und Zuweisen des Hauptlayouts
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def get_input_text(self):
        """
        Gibt den aktuell im Input TextEdit eingegebenen Text zurück.

        Returns:
            str: Der Text, den der Benutzer eingegeben hat.
        """
        return self.input_text_edit.toPlainText()

    def set_result_text(self, data):
        """
        Setzt den im Result TextEdit angezeigten Text. Verarbeitet und formatiert das Ergebnis als HTML,
        um die Darstellung wie im gegebenen Beispielbild zu ermöglichen.

        Args:
            data (dict): Ein Dictionary, das die Sprachprüfergebnisse enthält.
        """
        # Überprüfen, ob das Ergebnis ein Dictionary ist und entsprechend formatieren
        if isinstance(data, dict):
            # Werte aus dem Dictionary holen und umwandeln
            reliable = 'yes' if data.get('reliable') else 'no'
            language = data.get('language', 'Unknown')
            probability = float(data.get('prob', 0)) * 100  # Konvertieren zu Prozent

            # HTML-String für das Ergebnis erstellen
            html_content = f"""
            <p>reliable: <b>{reliable}</b></p>
            <p>language: <b>{language}</b></p>
            <p>probability: <b>{probability:.2f}%</b></p>
            """
            # Setzen des HTML-Inhalts im Ergebnis-TextEdit
            self.result_text_edit.setHtml(html_content)
        else:
            # Wenn es kein Dictionary ist, wird der Text direkt gesetzt
            self.result_text_edit.setPlainText(data)

    def connect_controller(self, controller):
        """
        Verbindet die Controller-Aktionen mit den Signalen der UI-Elemente, sodass Benutzerinteraktionen behandelt werden können.

        Args:
            controller: Eine Instanz des Controllers, der die Logik der Anwendung verarbeitet.
        """
        # Verbinden der Klick-Signale der Buttons mit den entsprechenden Controller-Methoden
        self.start_btn.clicked.connect(controller.process_input)
        self.reset_btn.clicked.connect(controller.reset_input)
        self.close_btn.clicked.connect(controller.close_app)
