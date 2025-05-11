# 🛠️ PDF & HTML Toolkit Suite

Questo repository contiene una suite di script Python progettati per la manipolazione di file PDF e la conversione di contenuti HTML in PDF.

---

## 🌟 Funzionalità Principali

*   📄 **Split PDF (`split_pdf.py`)**: Divide un file PDF in un intervallo di pagine specificato dall'utente.
*   🌐 **HTML to PDF Converter (`main.py` e `utils/`)**:
    *   🔗 **HTML Merger (`utils/html_merger.py`)**: Unisce più file HTML da una directory specificata in un unico documento HTML.
    *   ✨ **Background Remover (`utils/background_remover.py`)**: Rimuove stili di background e attributi `style` da un contenuto HTML, utile per una stampa pulita.
    *   📝 **PDF Generator (`utils/pdf_generator.py`)**: Converte il contenuto HTML pulito in un file PDF utilizzando WeasyPrint.

---

## 📂 Struttura del Progetto
```
.
├── split_pdf.py           # Script per dividere i PDF
├── main.py                # Script principale per il workflow HTML -> PDF
├── utils/
│   ├── __init__.py
│   ├── html_merger.py       # Modulo per unire file HTML
│   ├── background_remover.py # Modulo per pulire l'HTML
│   └── pdf_generator.py     # Modulo per generare PDF da HTML
└── README.md              # Questo file
```

---

## ⚙️ Prerequisiti e Installazione

1.  **Python**: Assicurati di avere Python 3.6+ installato.
2.  **Librerie Python**: Installa le dipendenze necessarie. Puoi creare un file `requirements.txt` con il seguente contenuto:
    ```txt
    PyPDF2
    beautifulsoup4
    WeasyPrint
    ```
    E poi installarle con:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Dipendenze WeasyPrint**: WeasyPrint ha dipendenze di sistema (come Pango, Cairo, GDK-PixBuf) che devono essere installate. Consulta la [documentazione ufficiale di WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation) per istruzioni specifiche per il tuo sistema operativo.

---

## 🚀 Utilizzo

### 1. Dividere un File PDF (`split_pdf.py`)

Questo script permette di estrarre un intervallo di pagine da un file PDF esistente.

**Esecuzione:**

*   **Tramite argomento da linea di comando:**
    ```bash
    python split_pdf.py "percorso/del/tuo/file.pdf"
    ```
    Lo script chiederà poi la pagina iniziale e finale.

*   **Fornendo il percorso interattivamente:**
    ```bash
    python split_pdf.py
    ```
    Lo script chiederà di inserire il percorso del file PDF, e successivamente la pagina iniziale e finale.

Il file PDF risultante sarà salvato nella stessa directory dello script con un nome del tipo `NOMEFILEORIGINALE_pages_INIZIO_to_FINE.pdf`.

### 2. Convertire HTML in PDF (`main.py`)

Questo script orchestra il processo di unione di più file HTML, pulizia degli stili di background e successiva conversione in un unico file PDF.

**Configurazione:**

1.  **Modifica `main.py`**:
    Apri `main.py` e modifica la variabile `html_directory` per puntare alla directory contenente i tuoi file HTML:
    ```python
    # Define the directory containing HTML files
    html_directory = 'PERCORSO/ALLA/TUA/CARTELLA/HTML'
    ```
2.  **Modifica `utils/html_merger.py` (Opzionale)**:
    Se i tuoi file HTML utilizzano una codifica diversa da `latin-1`, modifica la linea:
    ```python
    with open(file_path, 'r', encoding='latin-1') as file: # Cambia 'latin-1' se necessario
    ```

**Esecuzione:**

```bash
python main.py
```

Lo script produrrà un file `Nome file.pdf` (o il nome specificato in `output_pdf_path` dentro `main.py`) nella directory principale del progetto.

---

## 📝 Note Importanti

*   **Codifica File HTML**: Lo script `html_merger.py` attualmente usa la codifica `latin-1` per leggere i file HTML. Se i tuoi file usano una codifica differente (es. `utf-8`), assicurati di aggiornare la funzione `open()` nello script.
*   **Rimozione Stili**: `background_remover.py` è abbastanza aggressivo nel rimuovere tutti gli attributi `style` e i tag `<style>`. Questo è ottimo per la pulizia, ma potrebbe rimuovere stili desiderati se non sono legati al background.
*   **Percorsi Assoluti/Relativi**: Per `html_directory` in `main.py`, è consigliabile usare percorsi assoluti o percorsi relativi allo script `main.py` per evitare ambiguità.

---

## 💡 Possibili Miglioramenti

*   Aggiungere argomenti da linea di comando a `main.py` per specificare la directory HTML e il file PDF di output.
*   Migliorare la robustezza della rimozione degli stili in `background_remover.py` per essere più selettivo.
*   Aggiungere opzioni di personalizzazione per la generazione del PDF (es. margini, orientamento) in `pdf_generator.py`.
*   Implementare logging più dettagliato.
*   Aggiungere test unitari.

---

## 📜 Licenza

Questo progetto è rilasciato sotto la Licenza MIT. Vedi il file `LICENSE` (se presente) per maggiori dettagli. *(Nota: dovresti aggiungere un file LICENSE al tuo repo, ad esempio scegliendo tra le opzioni di GitHub quando crei il repo o aggiungendolo manualmente)*

---

## 🤝 Contribuire

I contributi sono benvenuti! Se hai suggerimenti o vuoi migliorare il codice, sentiti libero di:
1.  Forkare il repository.
2.  Creare un nuovo branch (`git checkout -b feature/AmazingFeature`).
3.  Committare le tue modifiche (`git commit -m 'Add some AmazingFeature'`).
4.  Pushare al branch (`git push origin feature/AmazingFeature`).
5.  Aprire una Pull Request.

---

## 🙏 Ringraziamenti (Opzionale)

*   Grazie ai creatori delle librerie PyPDF2, BeautifulSoup4, e WeasyPrint.
*   ... (altri ringraziamenti se necessario)

---