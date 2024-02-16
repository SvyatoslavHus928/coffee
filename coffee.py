menu = {
    "кава Еспресо": {
        "number": 1,
        "price": 25,
    },
    "кава Латте": {
        "number": 2,
        "price": 30,
    },

    "кава Капучино": {
        "number": 3,
        "price": 35,
    },
    "кава Американо": {
        "number": 4,
        "price": 40,
    },
    "кава Лунго": {
        "number": 5,
        "price": 38,
    },
    "кава Ірландська": {
        "number": 5,
        "price": 44,
    },

}
def print_menu():
    for item, info in menu.items():
        print(f"{info['number']}. {item}: {info['price']} грн")


def process_order():
    order = {}
    while True:
        item = input("Введіть номер кави (або '=' для завершення): ")
        if item == "=":
            break

        if item not in menu:
            print("Неіснуючий номер кави.")
            continue

        quantity = int(input("Введіть кількість: "))
        order[item] = quantity
    return order


def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item]["price"] * quantity
    return total


def print_receipt(order, total):
    print("=== Квитанція ===")
    for item, quantity in order.items():
        info = menu[item]
        print(f"{info['number']}. {item}: {quantity} x {info['price']} грн = {info['price'] * quantity} грн")
    print(f"Загальна вартість: {total} грн")


def add_item(name, price):
    if name in menu:
        print(f"Кава з назвою '{name}' вже існує.")
        return

    menu[name] = {"number": len(menu) + 1, "price": price}


while True:
    print_menu()
    order = process_order()
    total = calculate_total(order)
    print_receipt(order, total)

    answer = input("Хочете додати нову каву до меню? (y/n): ")

    if answer.lower() == "y":
        name = input("Введіть назву нової кави: ")
        price = float(input("Введіть ціну нової кави: "))

        add_item(name, price)

    again = input("Бажаєте зробити ще одне замовлення? (y/n): ")
    if again.lower() != "y":
        break