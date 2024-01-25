from bs4 import BeautifulSoup
import requests

# Загрузка веб-страницы
url = 'http://127.0.0.1:8000/'
response = requests.get(url)
html = response.text

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Поиск всех тегов формы на странице
forms = soup.find_all('form')

# Обход найденных форм и выполнение необходимых действий
for form in forms:

    for input_tag in form.find_all('input'):
        print(input_tag.get('name'))
    # Получение информации о форме
    form_action = form.get('action')
    form_method = form.get('method')

    # Дополнительная обработка формы...
    # Например, отправка данных или извлечение полей формы

    # Пример вывода информации о форме
    print('Form Action:', form_action)
    print('Form Method:', form_method)
    print('---')