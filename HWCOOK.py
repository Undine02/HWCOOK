# 1
cook_book = {}
with open('HWCOOK.txt', 'r', encoding='utf-8') as HWCOOK:
    for dish in HWCOOK:
        dishes = dish.strip()
        ingredients = int(HWCOOK.readline())
        dishes_list = []
        for ing in range(ingredients):
            ingredient_name, quantity, measure = HWCOOK.readline().split('|')
            dishes_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        cook_book[dishes] = dishes_list
        HWCOOK.readline()
print(cook_book)

# 3

def len_file(file1, file2, file3):
    with open(file1, encoding='utf8') as f:
        list1 = f.readlines()
    with open(file2, encoding='utf8') as f:
        list2 = f.readlines()
    with open(file3, encoding='utf8') as f:
        list3 = f.readlines()
    file_list = [list1, list2, list3]
    dict_file = {file1:list1, file2:list2, file3:list3}
    file_list.sort()
    file_list.reverse()
    with open('4.txt', 'a', encoding='utf8') as f:
        num =0
        for list in file_list:
            len_file = str(len(file_list[num]))
            num += 1
            if dict_file[file1] == list:
                f.write(f' \n {file1} \n')
            elif dict_file[file2] == list:
                f.write(f' \n {file2} \n')
            else: f.write(f' \n {file3} \n')
            f.write(f' {len_file} \n')
            for write in list:
                f.write(f' {write} ')

len_file('1.txt', '2.txt', '3.txt')

# 2

def get_shop_list_by_dishes(dishes, person_count, data = None):
    """
    :param dishes: список блюд из cook_book
    :param person_count: количество персон для кого мы будем готовить:
    :return: словарь с названием ингредиентов и его количества для блюда.
    типа
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
    """
    cook_dict = {}
    for dish in dishes:
        if dish in data:
            for ingress_diets in data[dish]:
                dict_ing = {}
                if ingress_diets['ingredient_name'] in cook_dict:
                    quantity = cook_dict[ingress_diets['ingredient_name']].get('quantity') + \
                               ingress_diets['quantity'] * person_count
                    cook_dict[ingress_diets['ingredient_name']].update(quantity=quantity)
                else:
                    dict_ing['measure'] = ingress_diets['measure']
                    dict_ing['quantity'] = ingress_diets['quantity'] * person_count
                    cook_dict[ingress_diets['ingredient_name']] = dict_ing
    return cook_dict

