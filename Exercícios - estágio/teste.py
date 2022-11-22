for x in listaTamanhos:
        if x not in lista2:
        lista2.append(x)




items = [
    {
        'code': 0,
        'name': 'coca cola',
        'price': 5
    },
    {
        'code': 1,
        'name': 'cadbury',
        'price': 10
    },
    {
        'code': 2,
        'name': 'chips',
        'price': 2
    },
]

is_quit = False
item = ''

while is_quit == False:
    print("Welcome to the vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("Enter the code number of the item you want to get: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Great, {item['name']} will cost you {item['price']} dollars")

        price = int(input(f"Enter {item['price']} dollars to purchase: "))
        if price == item['price']:
            print(f"Thank you for buying here is your {item['name']}")
        else:
            print(f"Please enter only {item['price']} dollars")

    query = input("To quit the machine enter q and to continue buying enter anything: ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')
