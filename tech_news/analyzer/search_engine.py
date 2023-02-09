from tech_news.database import search_news
import datetime

# Requisito 7


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})

    list_news = [(new["title"], new["url"]) for new in news]

    return list_news


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.date.fromisoformat(date).strftime("%d/%m/%Y")
        news = search_news({"timestamp": date})
        list_news = [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")
    return list_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
