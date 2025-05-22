def menu():
    global choice
    print(f"Items in stock  : \033[92m{len(stock)}\033[0m")
    print(f"Items on order  : \033[92m{len(order)}\033[0m")
    print("\n\033[92mMenu Items, choose number!\033[0m")
    print("1. Display a list of stock items")
    print("2. Add an item to stock")
    print("3. Update an item on stock")
    print("4. Order an item")
    choice = int(input("\033[92mYour choice?: \033[0m"))
print("\n\033[92mINVENTORY MANAGEMENT SYSTEM\033[0m\n")
stock = [
    {
        "sku": "MIL-APL1LTR",
        "name": "Apple Milk 1L",
        "price": 9000,
        "supplier": "FreshDairy Ltd"
    },
    {
        "sku": "BAT-DURAAA4P",
        "name": "Duracell AAA Batteries",
        "price": 18000,
        "supplier": "PowerCell Supplies"
    },
    {
        "sku": "MED-PARA500",
        "name": "Paracetamol 500mg",
        "price": 24000,
        "supplier": "MediLife Distributors"
    },
    {
        "sku": "YOG-YAKST500",
        "name": "Yakult Strawberry",
        "price": 6000,
        "supplier": "Yakult Kenya"
    },
    {
        "sku": "BIS-OREO123",
        "name": "Oreo Biscuits (123g)",
        "price": 4000,
        "supplier": "Mondelez Suppliers"
    }
]

order = []
# print(f"Items in stock  : \033[92m{len(stock)}\033[0m")
# print(f"Items on order  : \033[92m{len(order)}\033[0m")
# print("\n\033[92mMenu Items, choose number!\033[0m")
# print("1. Display a list of stock items")
# print("2. Add an item to stock")
# print("3. Update an item on stock")
# print("4. Order an item")
# choice = int(input("\033[92mYour choice?: \033[0m"))
menu()
if choice == 1:
    print(f"\033[92m{'SKU':<15} {'Name':<24} {'Price(UGX)':<12} {'Supplier'}\033[0m")
    for i in range(len(stock)):
        print(f"{stock[i]['sku']:<15} {stock[i]['name']:<24} {stock[i]['price']:<12} {stock[i]['supplier']}")