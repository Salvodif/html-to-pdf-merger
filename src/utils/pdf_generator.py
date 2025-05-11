def generate_pdf(cleaned_html_content, output_pdf_path):
    from weasyprint import HTML

    # Convert the cleaned HTML content to a PDF
    HTML(string=cleaned_html_content).write_pdf(output_pdf_path)