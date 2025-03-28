import requests
import wget  # pip install wget
from zipfile import ZipFile
from bs4 import BeautifulSoup

def get_url_paths(url, ext=''):
    # Verificar a disponibilidade do site
    response = requests.get(url)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    
    # Extraindo os links que terminam com .pdf
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [node.get('href') for node in soup.find_all('a') if node.get('href') and node.get('href').endswith(ext)]
    return parent


def main():
    # Acesso ao site
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/"
    ext = '.pdf'
    links = []

    result = get_url_paths(url, ext)
    for file in result:
        # Extraindo os links que possuem "Anexo"
        if "Anexo" in file:
            links.append(file)
            print(file)

    # Baixar os arquivos PDF
    i = 1  
    with ZipFile("Anexos.zip","w") as zip:
        for link in links:
            filename = "Anexo" + str(i) + ".pdf" 
            zip.write(wget.download(link, filename))
            i += 1  


if __name__ == '__main__':
    main()
