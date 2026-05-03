print("\n♨️ WELCOME TO JAVA JUNCTION ☕")
print("============================")
# this function should diplay the menu  
def show_menu(menu):
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - KSh {value[1]}")
    print("0. Checkout")

# Function that takes order from user

def take_order(menu):
    cart = []
    total = 0

    while True:
        show_menu(menu)
        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice in menu:
            item, price = menu[choice]

            qty = int(input(f"How many {item}? "))
            cart.append((item, price, qty))
            total += price * qty

            print(f"{qty} x {item} added to cart.")
        else:
            print("Invalid choice")

    return cart, total

# calculates the bill
def calculate_total(total):
    tip_percent = float(input("Enter tip percentage (e.g. 10 for 10%): "))
    tip = tip_percent / 100

    final_total = total + (total * tip)
    return final_total, tip_percent

#receipt generated
def print_receipt(cart, subtotal, final_total, tip_percent):
    print("\n🧾 --- RECEIPT ---")
    
    for item, price, qty in cart:
        print(f"{item} x{qty} - KSh {price * qty}")

    tip_amount = subtotal * tip_percent / 100

    print(f"\nSubtotal: KSh {subtotal}")
    print(f"Tip ({tip_percent}%): KSh {round(tip_amount, 2)}")
    print(f"Total Bill: KSh {round(final_total, 2)}")

# The menu is put as a dictionary
menu = {
    1: ("Black Coffee", 800),
    2: ("Milk Tea (Chai)", 1000),
    3: ("Cappuccino", 1800),
    4: ("Hot Chocolate", 1050),
    5: ("Fresh Lemon Tea", 1020),
    6: ("Iced Coffee", 1500),
    7: ("Fresh Juice (Mango/Passion)", 1030),
    8: ("Mandazi (2 pcs)", 250),
    9: ("Samosa (Beef/Vegetable)", 370),
    10: ("Sausage (Smokie)", 460)
}

#Final part
cart, subtotal = take_order(menu)

if cart:
    final_total, tip_percent = calculate_total(subtotal)
    print_receipt(cart, subtotal, final_total, tip_percent)
else:
    print("No items ordered.Please make your order!")


"""
This is the basic logic behind it
Bill=(input("How much is the bill? "))
Tip = 0.1
Total_Bill=float(Bill) + (float(Bill)*float(Tip))
print("The total bill is: " +str(Total_Bill))
"""