import os
from utils.html_merger import merge_html_files
from utils.background_remover import remove_background
from utils.pdf_generator import generate_pdf

def main():
    # Define the directory containing HTML files
    html_directory = 'C:\My Web Sites\Carimo STh III\www.carimo.it\somma-teologica'
    
    # Step 1: Merge HTML files
    merged_html = merge_html_files(html_directory)
    
    # Step 2: Remove background from the merged HTML
    cleaned_html = remove_background(merged_html)
    
    # Step 3: Generate PDF from the cleaned HTML
    output_pdf_path = 'Carimo - STh II-II.pdf'
    generate_pdf(cleaned_html, output_pdf_path)
    
    print(f"PDF generated successfully at {output_pdf_path}")

if __name__ == "__main__":
    main()