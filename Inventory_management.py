def menu():
    print("\033[92;1mDASHBOARD\033[0m") #Extra characters exists to color the text
        
    # The following code is to display items on the dashboard such as in stock and on order!
    print(f"Items in stock  : \033[92m{len(stock)}\033[0m")
    print(f"Items on order  : \033[92m{len(order)}\033[0m") 
       
    # This is the menu that a user can choose
    print("\n\033[92mMenu Items, choose number!\033[0m")
    print("1. Display a list of stock items")
    print("2. Add an item to stock")
    print("3. Update an item on stock")
    print("4. Order an item")
    try: 
        choice = int(input("\033[92mYour choice?: \033[0m"))
    except:
        print("\033[91mPlease enter choice number instead!\033[0m")
        menu()    
    #Conditional statements that shows the program how to proceed
    if choice == 1:
        # Displaying the list of stock items
        print("\033[92mLIST OF STOCK ITEMS\033[0m")
        print(f"\033[92m{'SKU':<15} {'Name':<24} {'Price(UGX)':<12} {'Supplier'}\033[0m")
        for i in range(len(stock)):
            print(f"{stock[i]['sku']:<15} {stock[i]['name']:<24} {stock[i]['price']:<12} {stock[i]['supplier']}")
        print("\n")
    elif choice == 2:
        # Adding an item to stock
        print("\033[92mAdding an item to stock\033[0m")
        sku = input("Enter the Item SKU: ")
        name = input("Enter the Item Name: ")
        
        # Here I handled errors of when a user enters price which are not integers
        ch = True
        while ch == True:
            try:
                price = int(input("Enter the Item Price: "))
                ch = False
            except:
                print("\033[91mPlease, enter the price in digits!\033[0m")
        supplier = input("Enter the Item Supplier: ")
        stock.append({"sku": sku, "name": name, "price": price, "supplier": supplier})
        print("\n\033[92mItem added to Stock successfully!\033[0m")
    elif choice == 3:
        # Updating an item on stock!
        print("\033[92mUpdating an item on stock!\033[0m")
        sku1 = input("Enter the SKU of the stock item to update: ")
        for i in range(len(stock)):
            if sku1 in stock[i].values():
                break
            i = len(stock)
        if i != len(stock):
            sku = input("Enter the new SKU of the item: ")
            name = input("Enter the new Name of the item: ")
            ch = True
            while ch == True:
                try:
                    price = int(input("Enter the new Price of the item: "))
                    ch = False
                except:
                    print("\033[91mPlease, enter the price in digits!\033[0m")
                    ch = True
            supplier = input("Enter the new Supplier of the item: ")
            stock[i] = {"sku": sku, "name": name, "price": price, "supplier": supplier}
            print("\n\033[92mStock Item updated successfully!\033[0m\n")          
        else:
            print("\033[91m\nSorry, an item with that SKU does not exist!\033[0m")
    elif choice == 4:        
        # This is the logic for ordering an item. Notice the dashboard changes accordingly        
        sku = input("Enter the SKU of the item you want to order: ")
        for i in range(len(stock)):
            if sku in stock[i].values():
                break
            i = len(stock)
        if i != len(stock):
            order.append({"sku": stock[i]["sku"], "name": stock[i]["name"], "price": stock[i]["price"], "supplier": stock[i]["supplier"]})
            del stock[i]
            print("\n\033[92mItem ordered successfully\033[0m")
        else:
            print("\033[91mSorry, that item is out of stock\033[0m")        
    else:
        print("\033[91mWrong choice, try again!\033[0m")
    menu()
print("\n\033[92;1mINVENTORY MANAGEMENT SYSTEM\033[0m\n")

# Below are hard coded stock items for demonstration purposes!
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
    }
]

order = [{
        "sku": "BIS-OREO123",
        "name": "Oreo Biscuits (123g)",
        "price": 4000,
        "supplier": "Mondelez Suppliers"
    }]
menu()