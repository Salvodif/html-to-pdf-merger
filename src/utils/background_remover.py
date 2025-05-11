def remove_background(html_content):
    from bs4 import BeautifulSoup

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove background styles
    for style in soup.find_all('style'):
        style.decompose()

    for element in soup.find_all(True):  # True matches all tags
        if 'style' in element.attrs:
            del element.attrs['style']
        if 'background' in element.attrs:
            del element.attrs['background']

    # Return the cleaned HTML content
    return str(soup)