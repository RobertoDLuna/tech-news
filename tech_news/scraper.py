from parsel import Selector
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


# Requisito 2
def scrape_updates(html_content):
    data_selector = Selector(html_content)
    link_news = data_selector.css("a.cs-overlay-link::attr(href)").getall()
    return link_news


# Requisito 3
def scrape_next_page_link(html_content):
    css_selector = "a.next::attr(href)"  # endereço do botão next
    html_page = Selector(text=html_content)  # carrega a pag html
    url_next_page = html_page.css(
        css_selector
    ).get()  # retorna o primeiro elemento encontrado
    return url_next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
