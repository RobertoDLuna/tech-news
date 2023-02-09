import requests
import time

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)  # espera 1 segundo para uma nova requisição
        if response.status_code != 200:
            return None
        return response.text  # retorna todo o html da página
    except requests.Timeout:  # trata do timeout caso o tempo seja excedido
        return None


# testando manualmente
print(fetch("https://www.tecmundo.com.br/mais-lidas"))


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
