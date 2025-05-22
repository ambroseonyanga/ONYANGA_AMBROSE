def menu():
    global choice
    print("\033[92mDASHBOARD\033[0m")
    print(f"Items in stock  : \033[92m{len(stock)}\033[0m")
    print(f"Items on order  : \033[92m{len(order)}\033[0m")
    print("\n\033[92mMenu Items, choose number!\033[0m")
    print("1. Display a list of stock items")
    print("2. Add an item to stock")
    print("3. Update an item on stock")
    print("4. Order an item")
    choice = int(input("\033[92mYour choice?: \033[0m"))
    if choice == 1:
        print("\033[92mLIST OF STOCK ITEMS\033[0m")
        print(f"\033[92m{'SKU':<15} {'Name':<24} {'Price(UGX)':<12} {'Supplier'}\033[0m")
        for i in range(len(stock)):
            print(f"{stock[i]['sku']:<15} {stock[i]['name']:<24} {stock[i]['price']:<12} {stock[i]['supplier']}")
        print("\n")
        menu()
    elif choice == 2:
        sku = input("Enter the Item SKU: ")
        name = input("Enter the Item Name: ")
        ch = True
        while ch == True:
            try:
                price = int(input("Enter the Item Price: "))
                ch = False
            except:
                print("\033[91mPlease, enter the price in digits!\033[0m")
                ch = True
        supplier = input("Enter the Item Supplier: ")
        stock.append({"sku": sku, "name": name, "price": price, "supplier": supplier})
        print("\n\033[92mItem added to Stock successfully!\033[0m")
        menu()
    elif choice == 3:
        sku1 = input("Enter the SKU of the stock item to update: ")
        for i in range(len(stock)):
            if sku1 in stock[i].values():
                break
            i = len(stock)
        if i != len(stock):
            sku = input("Enter the new SKU of the item: ")
            name = input("Enter the new Name of the item: ")
            price = int(input("Enter the new Price of the item: "))
            supplier = input("Enter the new Supplier of the item: ")
            stock[i] = {"sku": sku, "name": name, "price": price, "supplier": supplier}
            print("\n\033[92mStock Item updated successfully!\033[0m\n")
            menu()           
        else:
            print("\033[91m\nSorry, an item with that SKU does not exist!\033[0m")
            menu()
    else:
        print("\033[91mWrong choice, try again!\033[0m")
        menu()
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
menu()