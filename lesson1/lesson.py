#pip install beatifulsoup4

from bs4 import BeautifulSoup



with open('index.html') as file:
    src = file.read()
# print(src)


soup = BeautifulSoup(src, 'lxml')

# title = soup.title
# print(title.text)

#*************.find() - метод берет первый заголовок ******************
#************* .find_all() - метод берет все и создает список ********************

# page_h1 = soup.find('h1')
# print(page_h1)
#
# page_all_h1 = soup.find_all('h1')
# print(page_all_h1)
#
# for item in page_all_h1:
#     print(item.text)

# user_name = soup.find('div', class_='user__name')
# print(user_name.text.strip())

# user_name = soup.find('div', class_='user__name').find('span').text
# # print(user_name)

# user_name = soup.find('div', {'class': 'user__name'}).find('span').text
# print(user_name)

# user_name = soup.find(class_='user__info').find_all('span')
# print(user_name)
#
#  for item in user_name:
#      print(item.text)
#
# print(user_name[2].text)

# social_links = soup.find(class_='social__networks').find('ul').find_all('a')
# print(social_links)

# all_a = soup.find_all('a')
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get('href')
#     print(f'{item_text}: {item_url}')


#****************** .find_parent()
#****************** .find_parents() - метод родителей элементов

# post_div = soup.find(class_='post__text').find_parent()
# print(post_div)

# post_div = soup.find(class_='post__text').find_parent('div', 'user__post')
# print(post_div)


# post_divs = soup.find(class_='post__text').find_parents('div', 'user__post')
# print(post_divs)

#***************** .next_lement
#***************** .previos.element
next_el = soup.find(class_='post__title').next_element.next_element.text
print(next_el)

next_el = soup.find(class_='post__title').find_next().text
print(next_el)