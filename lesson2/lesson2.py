import random
from time import sleep

import requests
from bs4 import BeautifulSoup

import json
import csv
import lxml


#код страницы
# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
#
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

#запись страницы в файл
# with open('index.html', 'w') as file:
#     file.write(src)

# #чтение файла
# with open('index.html') as file:
#     src = file.read()
#
# all_catigories_dict = {}
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')

# #пробегаемся по списку циклом
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = 'http://health-diet.ru' + item.get('href')
#     #print(f'{item_text}: {item_href}')
#
#     all_catigories_dict[item_text] = item_href
#
# #сохраним словарь  в JSON файл **** ОЧЕНЬ ВАЖНО *******
# with open('all_catigories_dict.json', 'w') as file:
#     json.dump(all_catigories_dict,file, indent=4, ensure_ascii=False)

#загрузим наш файл в переменную all_categories в формате JSON
with open('all_catigories_dict.json') as file:
   all_catigories = json.load(file)
   #print(all_catigories)

#создаем цикл со сбором данных со страницы
iteration_count = int(len(all_catigories)) - 1
count = 0
print(f'Всего итераций: {iteration_count}')

for category_name, category_href in all_catigories.items():

    #создадим список из символов которые хотим изменить
    rep = [", ", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')
    #print(category_name)

    #переходим к запросам на странице раскоментируй заголовки!!!!
    req = requests.get(url=category_href, headers=headers)
    src = req.text

    #сохраним нашу страницу под именем category в новую папку DATA которую создадим
    with open(f'data/{count}_{category_name}.html', 'w') as file:
        file.write(src)

    with open(f'data/{count}_{category_name}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    #проверка таблицы на наличие таблицы с продуктами
    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue

    # собираем заголовки таблицы
    table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    protein = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    #print(carbohydrates)


    with open(f'data/{count}_{category_name}.csv', 'w', encoding='UTF-8') as file:
        winter = csv.writer(file)
        winter.writerow(
            (
                product,
                calories,
                protein,
                fats,
                carbohydrates
            )
        )


    #собираем данные продуктов
    products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

    product_info = []
    for item in products_data:
        product_tds = item.find_all('td')

        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        protein = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        #print(protein)

        product_info.append(
            {
                'Title': title,
                'Calories': calories,
                'Protein': protein,
                'Fats': fats,
                'Carbohydrates': carbohydrates
            }
        )

        with open(f'data/{count}_{category_name}.csv', 'a', encoding='UTF-8') as file:
            winter = csv.writer(file)
            winter.writerow(
                (
                    title,
                    calories,
                    protein,
                    fats,
                    carbohydrates
                )
            )

    with open(f'data/{count}_{category_name}.json', 'a', encoding='UTF-8') as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1

    print(f'Итерация {count}. {category_name} записана...')
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print('Работа завершена')
        break

    print(f'Осталось итераций: {iteration_count}')
    sleep(random.randrange(2, 4))


#ВСЁ!!!!








