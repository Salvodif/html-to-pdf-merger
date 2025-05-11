from PyPDF2 import PdfReader, PdfWriter
import os

def ask_page_number(prompt, max_page):
    """Chiede all'utente un numero di pagina con validazione"""
    while True:
        try:
            page = int(input(prompt))
            if 1 <= page <= max_page:
                return page
            print(f"Errore: inserisci un numero tra 1 e {max_page}")
        except ValueError:
            print("Errore: inserisci un numero valido")

def split_pdf(input_path):
    """
    Divide un PDF da una pagina iniziale a una finale
    
    :param input_path: Percorso del file PDF da dividere
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Il file {input_path} non esiste")
    
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    
    print(f"\nFile PDF caricato: {os.path.basename(input_path)}")
    print(f"Pagine totali: {total_pages}")
    
    start_page = ask_page_number(
        f"Inserisci la pagina di INIZIO (1-{total_pages}): ",
        total_pages
    )
    
    end_page = ask_page_number(
        f"Inserisci la pagina di FINE ({start_page}-{total_pages}): ",
        total_pages
    )
    
    if end_page < start_page:
        print("\nAttenzione: la pagina finale è minore di quella iniziale")
        print("Imposto automaticamente la pagina finale uguale a quella iniziale")
        end_page = start_page
    
    writer = PdfWriter()
    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])
    
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = f"{base_name}_pages_{start_page}_to_{end_page}.pdf"
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    
    print(f"\n✅ PDF creato con successo: {output_path}")
    print(f"📄 Pagine incluse: da {start_page} a {end_page}")

if __name__ == "__main__":
    import sys
    
    print("🛠️ PDF Splitter - Dividi un PDF da pagina a pagina")
    
    if len(sys.argv) == 2:
        input_pdf = sys.argv[1]
    else:
        input_pdf = input("\nInserisci il percorso del file PDF: ").strip('"')
    
    try:
        split_pdf(input_pdf)
    except Exception as e:
        print(f"\n❌ Errore: {str(e)}")
        sys.exit(1)