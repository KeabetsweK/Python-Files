def add_item():
    food_name = input("What is your food name? ")
    quantity = int(input("Enter the number of food items")

    with open("grocery.txt","w") as file:
        file.write(food_name + " , " + quantity "\n")
        file.close()
    print("Food item added.")

def view_item():

        file = open("grocery.txt","r")
        for line in file:
            print(line)

def search_items():
    user_input = input("What would you like to search for? ")
    while True:
        if user_input == " ":
            print("Item found,quantity is ....")
        elif food_name == " ":
             print("Item not found.")
        else:
            ("")



