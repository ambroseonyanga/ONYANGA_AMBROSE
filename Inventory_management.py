
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
        "name": "Duracell AAA Batteries (4pk)",
        "price": 18000,
        "supplier": "PowerCell Supplies"
    },
    {
        "sku": "MED-PARA500",
        "name": "Paracetamol 500mg (100 tabs)",
        "price": 24000,
        "supplier": "MediLife Distributors"
    },
    {
        "sku": "YOG-YAKST500",
        "name": "Yakult Strawberry 500ml",
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
print(f"Items in stock  : \033[92m{len(stock)}\033[0m")
print(f"Items on order  : \033[92m{len(order)}\033[0m")
print("\nEnter your choice!")
print("\n1. Display a list of stock items")
print("2. Add an item to stock")
print("3. Update an item on stock")
print("4. Order an item")