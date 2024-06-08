inventory = dict()


menu = '''1. inventroy
2. buy from vendor
3. sell to customer
4. search by name
5. search by id
6. terminate
'''

def fill_inventory(inventory):
    id = input("enter id: ")
    name = input("enter name: ")
    price = float(input("enter price: "))
    quantity = int(input("enter quantitiy: "))

    if id in inventory:
        print(id , "already exits in the inventory.. updating")
    else:

        inventory[id] = {}
        inventory[id]["quantity"] = 0 

    inventory[id]["name"]= name
    inventory[id]["price"] = price
    inventory[id]["quantity"]+=quantity
    print("item added successfully")


def sell_to_customer(inventory):
    id = input("enter id: ")
    quantity = int(input("enter quantity: "))
    if id in inventory:
        if inventory[id]["quantity"] >= quantity:
            inventory[id]["quantity"] -= quantity
        else:
            print("that much quantitiy not avilable")
    else:
        print("item not found in inventory")

def print_item(item):
    for key , val in item.items():
        print(key , ":" , val) 

def search_by_name(inventory, name):
    flag = False
    for id in inventory:
        if inventory[id]["name"] == name:
            flag = True
            print_item(inventory[id])
    if not flag:
        print("no item found named",name)

def search_by_id(inventory,id):
    if id in inventory:
        print_item(inventory[id])
    else:
        print("id",id,"not found")
def print_inventory(inventory):
    if not inventory:
        print("inventory is empty.")
    print(inventory)


print(menu)
while True:
    option = int(input("enter option: "))
    if not option >= 1 and not option <= 6:
        print("enter valid option")
    else:
        if option == 1:
            print_inventory(inventory)
        elif option == 2:
            fill_inventory(inventory)
        elif option == 3:
            sell_to_customer(inventory)
        elif option==4:
            name = input("enter name: ")
            search_by_name(inventory , name)
        elif option==5:
            id = input("enter id: ")
            search_by_id(inventory, id)
        elif option == 6:
            print("terminating the program")
            exit()