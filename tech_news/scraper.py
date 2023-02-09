from parsel import Selector
import requests
import time
import re
from tech_news.database import create_news

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
    data_selector = Selector(html_content)
    all_summary = ""
    first_summary = data_selector.css("div.entry-content > p").get()
    list_texts = Selector(first_summary).css("p *::text").getall()

    for itens in list_texts:
        all_summary += itens

    dict_news = {
        "url": data_selector.css(
            "head > link[rel=canonical]::attr(href)"
        ).get(),
        "title": data_selector.css("h1.entry-title::text").get().strip(),
        "timestamp": data_selector.css("li.meta-date::text").get(),
        "writer": data_selector.css("a.fn::text").get(),
        "reading_time": int(
            re.sub(
                "[^0-9]",
                "",
                data_selector.css("li.meta-reading-time::text").get(),
            )
        ),
        "summary": all_summary.strip(),
        "category": data_selector.css("span.label::text").get(),
    }

    return dict_news


# Requisito 5
def get_tech_news(amount):
    scraper = "https://blog.betrybe.com"
    count = 0
    list_news = []

    while count < amount:
        get_infos = fetch(scraper)
        get_url = scrape_updates(get_infos)
        for url in get_url:
            content = fetch(url)
            list_news.append(scrape_news(content))
            count += 1
            if count == amount:
                break
        scraper = scrape_next_page_link(get_infos)

    create_news(list_news)

    return list_news
