#Valdez, John Kenneth C.
#CS1202

game_library = {
    "Donkey Kong": {"quantity": 3, "rental_cost": 2},
    "Super Mario Bros": {"quantity": 5, "rental_cost": 3},
    "Tetris": {"quantity": 2, "rental_cost": 1}
}

account = {}

admin_acc = "admin"
admin_pass = "adminpass"

    
def create_account():
    username = input("\nEnter a username: ")
    if username == '':
        print("Dont keep it blank.")
        return
    password = input("Enter a Password: ")
    if password == '':
        print("Dont keep it blank.")
        return
    if username in account:
        print("\nUsername Already Exist !!") # to check whether the account is already exist
        return
    balance()
    account[username] = {"password": password, "balance":money, "points": 0, "inventory": []} #with this the created account will  be save in empty account dictionary
    print("\nUser registered successfully.")

def balance_update(username):
    deposit = (input("\nDeposit a balance: $"))
    if deposit == '': 
        print("Cancelled...\n")
        main()
    else:
        try:
            deposit = float(deposit)
            account[username]["balance"] += deposit # to add a new balance to its own user account
            print("\nYour balance now is updated !!")
            main(username)
        except:
            print("\nPlease Enter a valid input\n")
            return 
        
def balance():
    global money
    money = (input("\nDeposit a Balance (Keep it blank to cancel): $"))
    if money == '':
        print("Cancelled...\n")
        log_in_menu()
    else:
        try:
            money = float(money) # to convert the input value into a float and also to handle the error
        except:
            print("\nPlease enter a valid input.\n")
            balance()
 
def login():
    username = input("Enter a username: ")
    password = input("Enter your password: ")
    if username == '':
        print("Dont keep it blank.")
        return
    if username in account and account[username]["password"] == password: 
        print("\nLogin successful.")
        return main(username)
    if username == admin_acc and password == admin_pass:
        print("\nAdmin login successful.")
        return admin_power()
    else:
        print("\nInvalid username or password. Please try again.")
        return log_in_menu()

def display():
    print("\n\n~ Library ~")
    for count, (game, info) in enumerate(game_library.items(),start=1): # i use for loop and enumerate to put a number in my dictionary so it not messy.
        print(f"{count}. {game}")
        print(f"Cost: ${info['rental_cost']}")
        print(f"Available: {info['quantity']}")

def display_games():
    print("\n\n~ Library ~")
    for count, (game, info) in enumerate(game_library.items(),start=1):
        print(f"{count}. {game}")
        print(f"Cost: ${info['rental_cost']}")
        print(f"Available: {info['quantity']}")
    exit = input("\nEnter to exit: ")
    if exit == '':
        print("")
        return

def admin_power():
    display()
    choice = (input("Choose you want to edit: "))
    if choice == '':
        print("Cancelled..")
        return log_in_menu()
    else:
        try :
            choice = int(choice)
            if choice >= 1 and choice <= len(game_library):
                game = list(game_library.keys())[choice - 1]
                quantity = int(input("Enter new quantity: "))
                rental_cost = float(input("Enter new rental cost: $"))
                game_library[game]["quantity"] = quantity
                game_library[game]["rental_cost"] = rental_cost
                display()
                print("Game details updated successfully.")
                return log_in_menu()
            else:
                    print("\nInvalid choice!!.")
                    return admin_power()
        except:
            print("\nInvalid Input !!.")
            return admin_power()

def rent_game(username):
    global available_games
    display()
    available_games = list(game_library.keys())  # i make list available_game as a variable from game_library of keys using built in function list.
    # Variable to track if the game is successfully rented
    game_rented = False

    while not game_rented:
        choice = (input("\nEnter the number of the game you want to rent: "))
        if choice == '':
            print("\nCancelled...\n")
            return main()
        else:
            try:
                choice = int(choice)
                if 1 <= choice <= len(available_games):
                    title = available_games[choice - 1]
                    if game_library[title]["quantity"] > 0:
                        rental_cost = game_library[title]["rental_cost"]
                        if account[username]["balance"] >= rental_cost or account[username]["points"] >= rental_cost: # to check if the user have sufficient balance to rent
                            rent_choice = input(f"Do you want to rent '{title}' for ${rental_cost}? (Y/N): ").strip().lower()
                            if rent_choice == 'y':
                                if account[username]["balance"] >= rental_cost:
                                    account[username]["balance"] -= rental_cost
                                else:
                                    account[username]["points"] -= rental_cost
                                account[username]["inventory"].append(title) # in this after the user rent the game, the game will be transfer to user account.
                                game_library[title]["quantity"] -= 1
                                # Points
                                account[username]["points"] += rental_cost // 2 #i use floor division for points as to get he nearest whole number
                                print("\nGame rented successfully.")
                                game_rented = True  # Set the flag to True to exit the loop
                            else:
                                print("\nRenting cancelled.")
                                break  # Break out of the loop if renting is cancelled
                        else:
                            print("\nInsufficient balance or points to rent the game.")
                            break
                    else:
                        print("\nSorry, this game is currently out of stock.")
                        break
                else:
                    print("\nInvalid choice. Please enter a number within the range.")
                    break
            except:
                print("\nInvalid input. Please enter a number.")
                break
        
def redeem(username, available_games):
    if account[username]["points"] >= 3: # to check whether the user have enough balance to use
        while True:
            rent_choice = input("\nYou have enough points to rent.\nDo you want to redeem a game using your points? (Y / N): ")
            if rent_choice.lower() == 'y':
                display()
                try:
                    rent_pick = int(input("\nEnter the number of the game you want to rent: "))
                    if 1 <= rent_pick <= len(available_games): #To check if the user input from the choices
                        title = available_games[rent_pick - 1] # i made another variable for the rent pick, because counting in dictionary starting at 0.
                        if game_library[title]["quantity"] > 0: # To check whether the game is available 
                            rental_cost = game_library[title]["rental_cost"]
                            account[username]["inventory"].append(title) # in this after the user rent the game, the game will be transfer to user account. 
                            game_library[title]["quantity"] -= 1
                            # Point deduction
                            account[username]["points"] -= 3
                            print("\nGame rented successfully using points.")
                            break
                        else:
                            print("\nSorry, this game is currently unavailable.")
                            break
                    else:
                        print("\nInvalid choice. Please enter a number from the choices.")
                        break
                except:
                    print("\nInvalid input. Please enter a number.")
                break
            elif rent_choice.lower() == 'n':
                break
            else:
                print("\nInvalid choice. Please enter (Y for yes) (N for no).")
                break
            
def return_game(username):
    if account[username]['inventory']:
        print("\nGames in your inventory: ")
        for count, game in enumerate(account[username]['inventory'], start=1):
            print(f"{count}. {game}")
        while True:
            choice = int(input("\nEnter the number of the game you want to return: "))
            if choice == '':
                print("Cancelled...\n")
                return main()
            else:
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(account[username]['inventory']):
                        title = account[username]['inventory'][choice - 1]
                        if title in account[username]["inventory"]:
                            account[username]["inventory"].remove(title)
                            game_library[title]["quantity"] += 1
                            print("\nGame returned successfully.")
                            break  # Break out of the loop after successfully returning the game
                        else:
                            print("\nYou don't have this game in your inventory.")
                            break
                    else:
                        print("\nInvalid input. Please enter a number within the range.")
                        break
                except:
                    print("\nInvalid input. Please enter a number.")
                    break
    else:
        print("\nYour inventory is empty.")
        


def main(username):
    while True:
        print(f"Welcome {username}")
        print(f"Balance: $ {account[username]['balance']}")
        print(f"Points: $ {account[username]['points']}")
        print("\n1. Rent a Game")
        print("2. Return a Game")
        print("3. View Availale games")
        print("4. Add Balance")
        print("5. Redeem")
        print("6. Log Out")
      
        try:
            choice = str(input("\nEnter your choice (1-6): "))
            if choice == '1':
                rent_game(username)
            elif choice == '2':
                return_game(username)
            elif choice == '3':
                display_games()
            elif choice == '4':
                balance_update(username)
            elif choice == '5':
                redeem(username, available_games)  
            elif choice == '6':
                print("Logging out... \n")
                log_in_menu()
            else:
                print("\nInvalid choice")
        except:
            print("\nYou dont have enough balance.\n")


def log_in_menu():
    while True:
        print("Welcome to Rental Game")
        print("1. Log in")
        print("2. Register")
        print("3. Exit")
        choice = (input("\nEnter your choice (1-3): "))
        if choice == '':
            return log_in_menu()
        else:
            try:
                choice = int(choice)
                if choice == 1:
                    login()
                elif choice == 2:
                    create_account()
                elif choice == 3:
                    print("\nExiting the program... BYE")
                    break
                else:
                    print("\nInvalid choice")
            except:
                print("\nPlease Input a number.")

if __name__ == "__main__":
    log_in_menu()
                    
        

                 
       
           
