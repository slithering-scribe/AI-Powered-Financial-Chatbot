# AI-Powered Financial Chatbot (2025)  
# KI-gesteuerter Finanz-Chatbot (2025)

---

## Overview / Überblick

**English:**  
This project was developed as part of my Forage Virtual Internship. The AI-Powered Financial Chatbot integrates and interprets financial data from 10-K and 10-Q reports by extracting datasets from the EDGAR database. I performed comprehensive exploratory data analysis (EDA) using Python and Pandas, generated an analysis report, and leveraged the insights to design, develop, and deploy a chatbot on a local host server using Flask.

**Deutsch:**  
Dieses Projekt wurde im Rahmen meines Forage Virtual Internship entwickelt. Der KI-gesteuerte Finanz-Chatbot integriert und interpretiert Finanzdaten aus 10-K- und 10-Q-Berichten, indem Datensätze aus der EDGAR-Datenbank extrahiert werden. Ich habe eine umfassende explorative Datenanalyse (EDA) mit Python und Pandas durchgeführt, einen Analysebericht erstellt und die gewonnenen Erkenntnisse genutzt, um einen Chatbot zu entwerfen, zu entwickeln und mithilfe von Flask auf einem lokalen Server bereitzustellen.

- **Dataset Source / Datensatzquelle:** [EDGAR](https://www.sec.gov/edgar.shtml)

---

## Key Features / Hauptfunktionen

- **Data Extraction & EDA / Datenauswertung und EDA:**  
  Extracted financial data from EDGAR and performed exploratory data analysis using Python and Pandas to uncover key insights from 10-K and 10-Q reports.  
  Extrahierte Finanzdaten aus der EDGAR-Datenbank und führte mit Python und Pandas eine explorative Datenanalyse durch, um wesentliche Erkenntnisse aus 10-K- und 10-Q-Berichten zu gewinnen.

- **Insight Report Generation / Erstellung eines Analyseberichts:**  
  Generated a comprehensive analysis report that highlighted critical financial trends and patterns.  
  Erstellte einen umfassenden Analysebericht, der wichtige finanzielle Trends und Muster hervorhebt.

- **Chatbot Development & Deployment / Chatbot-Entwicklung und -Bereitstellung:**  
  Developed an AI-powered chatbot using Flask that interprets and responds to financial queries based on the extracted data, and deployed it on a local host server.  
  Entwickelte einen KI-gesteuerten Chatbot mithilfe von Flask, der Finanzabfragen basierend auf den extrahierten Daten interpretiert und beantwortet, und stellte ihn auf einem lokalen Server bereit.

---

## Installation / Installation

1. **Clone the Repository / Repository klonen:**

   ```bash
   git clone https://github.com/yourusername/ai-financial-chatbot.git
   cd ai-financial-chatbot
   ```

2. **Create and Activate a Virtual Environment / Virtuelle Umgebung erstellen und aktivieren:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use: `env\Scripts\activate`
   ```

3. **Install Dependencies / Abhängigkeiten installieren:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / Anwendung

1. **Run the Chatbot Server / Chatbot-Server starten:**

   ```bash
   flask run
   ```

2. **Access the Chatbot / Chatbot aufrufen:**  
   Open your web browser and navigate to `http://localhost:5000` to interact with the chatbot.

3. **Review the Analysis Report / Analysebericht ansehen:**  
   Refer to the generated analysis report (included in the `reports/` directory) for insights derived from the financial data.

---

## Project Structure / Projektstruktur

```
ai-financial-chatbot/
├── data/                 # Scripts and raw data extracted from EDGAR / Skripte und Rohdaten von EDGAR
├── notebooks/            # Jupyter Notebooks for EDA and report generation / Jupyter Notebooks für EDA und Berichtserstellung
├── models/               # (Optional) Models or scripts related to data processing / Modelle oder Skripte zur Datenverarbeitung
├── reports/              # Analysis report and findings / Analysebericht und Erkenntnisse
├── app.py                # Flask application for the chatbot / Flask-Anwendung für den Chatbot
├── requirements.txt      # Required Python packages / Erforderliche Python-Pakete
└── README.md             # Project documentation / Projektdokumentation
```

---

## Contributions / Mitwirken

**English:**  
Contributions are welcome! If you have suggestions, improvements, or bug reports, please open an issue or submit a pull request.

**Deutsch:**  
Beiträge sind willkommen! Wenn Sie Vorschläge, Verbesserungen oder Fehlerberichte haben, eröffnen Sie bitte ein Issue oder senden Sie einen Pull Request.

---

## License / Lizenz

This project is licensed under the MIT License.  
Dieses Projekt ist unter der MIT-Lizenz lizenziert.

---

## Final Note / Abschließende Hinweise

Harness the power of AI to demystify financial data and drive smarter decision-making in finance!  
Nutzen Sie die Kraft von KI, um Finanzdaten zu entschlüsseln und fundierte Entscheidungen im Finanzwesen zu treffen!
