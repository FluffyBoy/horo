import requests
from bs4 import BeautifulSoup

def get_horo (url = "https://horo.mail.ru/prediction/virgo/today/"):
    
    # подготавливаем части запроса серверу о том,что хотим получить и кто мы
    st_accept = "text/html" 
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
    # заголовки запроса на сервер
    headers = {
       "Accept": st_accept,
       "User-Agent": st_useragent
    }

    # отправляем запрос с заголовками по нужному адресу
    page = requests.get(url, headers)
    # считываем текст HTML-документа
    src = page.text
    # выбираем парсер (его отдельно ставить надо)
    parser = 'lxml'
    #готовим суп
    soup = BeautifulSoup(src, parser)

    # параметры цели (надо уточнять для твоего парсера)
    target_teg = 'div'
    target_class = 'article__item article__item_alignment_left article__item_html'

    # считываем целевой текст
    target_element = soup.find(target_teg , class_ = target_class)

    # разбиваем блок на абзацы
    paragraphs = target_element.find_all('p')

    string = ''
    # складываем абзацы в строку
    for p in paragraphs:
        string +=  '\t' + p.text + '\n'
        
    return string

if __name__ == '__main__':
    message = get_horo()
    print(message)
