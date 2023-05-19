import datetime
import re
import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# Путь к драйверу
driver_path = 'Путь к драйверу вашего браузера'

# Создание объекта сервиса для драйвера
service = Service(driver_path)

# Создание экземпляра браузера Firefox
options = webdriver.FirefoxOptions()  # подставьте свой браузер
options.add_argument("--headless")
driver = webdriver.Firefox(service=service, options=options)  # подставьте свой браузер

# Открытие страницы
stepik_id = 87654321  # пропишите нужный id
url = f'https://stepik.org/users/{stepik_id}'
driver.get(url)

# Ожидание загрузки таблицы или нужных элементов
wait = WebDriverWait(driver, 10)
tables = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'graph')))

# Общее количество элементов в таблице активности
count = 348

# Итерация по таблицам
for table in tables:
    # Поиск элементов в таблице
    table_cols = table.find_elements(By.CLASS_NAME, "graph-domain")

    # Итерация по колонкам таблицы
    for col in table_cols:
        if count == 0:  # выход из цикла после перебора всех ячеек
            break

        try:
            # Извлечение информации из ячеек
            cells = col.find_elements(By.XPATH, './/*[contains(@class, "graph-rect")]')

            for cell in cells:
                # Наведение курсора на ячейку, чтобы появилась всплывающая информация
                webdriver.ActionChains(driver).move_to_element(cell).perform()
                # Ожидание появления всплывающей подсказки
                tooltip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ch-tooltip')))
                tooltip_text = tooltip.text
                # Обработка полученной информации
                # Извлечение даты и количества задач из tooltip_text
                date_match = re.search(r'(\w+ \d{1,2}, \d{4})', tooltip_text)
                problems_match = re.search(r'problems solved – (\d+)', tooltip_text)

                if date_match and problems_match:
                    # Получение значений из регулярных выражений
                    date_str = date_match.group(1)
                    problems_solved = problems_match.group(1)

                    # Преобразование даты в требуемый формат
                    date_obj = datetime.datetime.strptime(date_str, '%B %d, %Y')
                    formatted_date = date_obj.strftime('%d %B, %Y')
                    count -= 1
                    print(f'Осталось: {count}')
                    if int(problems_solved) > 0:
                        # Запись данных в JSON файл
                        if os.path.isfile('data.txt'):
                            with open('data.txt', 'a', encoding='utf-8') as f:
                                print(f'Дата: {formatted_date}, Решено задач: {problems_solved}', file=f)
                        else:
                            with open('data.txt', 'w', encoding='utf-8') as f:
                                print(f'Дата: {formatted_date}, Решено задач: {problems_solved}', file=f)

        except TimeoutException:
            # Обработка исключения, когда всплывающая подсказка не появляется в течение тайм-аута
            print("Нет больше ячеек. Выход...")
            break

# Закрытие браузера
driver.quit()
