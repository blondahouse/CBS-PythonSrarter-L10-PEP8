# 1. show available

# 2. add some product
# input name, any string without checks
# input quantity, non-negative integer (if name exists just sum to existent quantity, if 0 - just change price)
# input price (if name exists just change price)

# 3. extract a product
# input name, check if exists
# input quantity, check if it is no more than available


def str_in_range(message):
    while True:
        input_string = input(message)
        if input_string in product_names_list:
            return input_string
        else:
            continue


def float_non_negative(message):
    while True:
        input_string = input(message)
        try:
            if float(input_string) < 0:
                raise ValueError
        except ValueError:
            continue
        else:
            return float(input_string)


def int_non_negative(message):
    while True:
        input_string = input(message)
        try:
            if int(input_string) < 0:
                raise ValueError
        except ValueError:
            continue
        else:
            return int(input_string)


def int_non_negative_max_limit(message, max_limit):
    while True:
        input_string = input(message)
        try:
            if int(input_string) <= 0 or int(input_string) > max_limit:
                raise ValueError
        except ValueError:
            continue
        else:
            return int(input_string)


def print_products_header():
    print(f'\t|{"Name":^30}|{"Quantity":^30}|{"Price":^30}|')


def print_products_delimiter():
    print(f'\t|{"":-^30}|{"":-^30}|{"":-^30}|')


def print_products(products_list):
    for i in products_list:
        print(f'\t|    '
              f'{i[0][0:22] if len(i[0]) < 23 else i[0][0:19] + "...":<26}|{i[1]:^30}|{"$" + str(round(i[2],2)):^30}|')


def print_menu():
    print(f'\t|{"1. Add/change product":^30}|'
          f'{"2. Extract product" if len(available_products_list) else "":^30}'
          f'|{"0. Exit":^30}|')


available_products_list = [('pen', 5, 1.99),
                           ('pencil', 8, .99),
                           ('notebook', 13, 2.99),
                           ('eraser', 21, .49)]

while True:
    product_names_list = []
    for product in available_products_list:
        product_names_list.append(product[0])

    print()
    print_products_delimiter()
    print_products_header()
    print_products_delimiter()
    print_products(available_products_list)
    print_products_delimiter()
    print_menu()
    print_products_delimiter()
    while True:
        action_input = input('Enter action number: ')
        try:
            if int(action_input) not in range(3 if len(available_products_list) else 2):
                raise ValueError
        except ValueError:
            continue
        else:
            if not int(action_input):
                exit()
            else:
                action_input = int(action_input)
                break
    match action_input:
        case 1:
            product_name = input('Enter product name: ')
            product_quantity = int_non_negative('Enter product number (non-negative integer): ')
            product_price = float_non_negative('Enter product price (non-negative number with decimal point): ')
            if product_name in product_names_list:
                product_index = product_names_list.index(product_name)
                new_product_tuple = (product_name,
                                     product_quantity + available_products_list[product_index][1],
                                     product_price)
                available_products_list[product_index] = new_product_tuple
            else:
                available_products_list.insert(0, (product_name, product_quantity, product_price))
        case 2:
            product_name = str_in_range('Enter existent product name: ')
            product_index = product_names_list.index(product_name)
            product_quantity = int_non_negative_max_limit('Enter product number (non-negative integer): ',
                                                          available_products_list[product_index][1])
            if product_quantity == available_products_list[product_index][1]:
                del available_products_list[product_index]
            else:
                new_product_tuple = (product_name,
                                     available_products_list[product_index][1] - product_quantity,
                                     available_products_list[product_index][2])
                available_products_list[product_index] = new_product_tuple
