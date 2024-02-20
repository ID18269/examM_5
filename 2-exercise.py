import requests
from bs4 import BeautifulSoup
import os
import concurrent.futures

def download_page(url):
    page = requests.get(url)
    return page.text

def save_page(page, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(page)

def main():
    base_url = 'https://tilshunos.com/sinonims/'
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('https://tilshunos.com/sinonims/'):
            links.append(href)

    os.makedirs('sinonimlar', exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i, link in enumerate(links):
            future = executor.submit(download_page, link)
            futures.append((future, f'sinonimlar/sahifa_{i}.html'))

        for future, file_name in futures:
            page = future.result()
            save_page(page, file_name)
            print(f'{file_name} saqlandi')

if __name__ == '__main__':
    main()
    
