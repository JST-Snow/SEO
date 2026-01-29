import urllib.request
from html.parser import HTMLParser

# Вставь ссылку на сайт, который хочешь проверить
url = "https://www.google.com"

class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self.current_tag = ""

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == "meta":
            dict_attrs = dict(attrs)
            if dict_attrs.get("name") == "description":
                self.description = dict_attrs.get("content")

    def handle_data(self, data):
        if self.current_tag == "title":
            self.title = data

# Запуск проверки
try:
    print(f"--- Анализ сайта: {url} ---")
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    
    parser = SEOParser()
    parser.feed(html)

    print(f"Заголовок (Title): {parser.title}")
    print(f"Описание (Description): {parser.description}")
except Exception as e:
    print(f"Ошибка: {e}")
