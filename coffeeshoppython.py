# ## ordering drinks + tables
# print("Welcome to Haala's book store and cafe\n")



books = [
    {
      'title':'The gruffalo',
      'author':'julia donaldson', 
      'price': 4.99,
    },
    {
        'title': 'the rainbow fish',
        'author':'marcus pfister',
        'price':4.99,
    }
]
 
orders = []

# ----------------- MENU -----------------
def book_menu():
    print("\n Book menu XD:\n")
    i = 1
    for book in books:
        
        print(f"{i}. {book ['title']} by {book['author']}   £ {book['price']}")
        i+=1
    print()
# book_menu()

##ordering books
def book_order():
    book_menu()
    choice = input("choose a book 1 or 2 \nwhat book would you like?:\n")
    if choice == '1':
        orders.append(books[0])
        print("You've ordered:", books [0]['title'])
       
    elif choice == '2':
        orders.append(books[1])
        print("You've ordered:", books [1]['title'])
        
    else:
        print("invalid choice")
    
def view_orders():
    if not orders:
        print("\nYour basket is empty.")
    else:
        print("\n--- Your Order ---")
        total = 0
        for i, item in enumerate(orders, start=1):
            print(f"{i}. {item.get('title', item.get('name'))} - £{item['price']:.2f}")
            total += item['price']
        print(f"\nTotal: £{total:.2f}")

def order_beverage():
    beverages = {
        "Coffee": 2.50,
        "Tea": 2.00,
        "Soda": 1.50,
        "Juice": 3.00
    }
    
    print("\nAvailable Beverages:")
    for i, (name, price) in enumerate(beverages.items(), start=1):
        print(f"{i}. {name} - £{price:.2f}")

    try:
        choice = int(input("\nChoose a beverage (number): "))
        if 1 <= choice <= len(beverages):
            selected = list(beverages.keys())[choice - 1]
            orders.append({"name": selected, "price": beverages[selected]})
            print(f"Added: {selected} (£{beverages[selected]:.2f})")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a number.")
##recipt
import datetime

def save_order():
    if not orders:
        print("No orders to save!")
        return
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = sum(item['price'] for item in orders)
    
    with open("orders.txt", "a") as file:  # "a" = append mode
        file.write(f"\n=== Order ({timestamp}) ===\n")
        for item in orders:
            name = item.get('title', item.get('name', 'Unknown Item'))
            file.write(f"- {name}: £{item['price']:.2f}\n")
        file.write(f"Total: £{total:.2f}\n")
    
    print(f"Order saved to 'orders.txt' (Total: £{total:.2f})")

##clear basket
def clear_basket():
    orders.clear()
    print("Basket cleared!")  
#loop on showing the option on the books
while True:
    print("\n1.show menu of books \n 2.order books\n 3.view order\n 4.order a drink:)\n 5.clear basket\n 6.add to basket\n 7.quit")
    choice=input("\nchoose 1 or 2 or  3 or 4 or 5 or 6 or 7:\n")
    if choice == "1":
         book_menu()
    elif choice == "2":
         book_order()
    elif choice == "3":
         view_orders()
    elif choice == "4":
         order_beverage()
    elif choice =="5":
        clear_basket()
    elif choice == "6":
        save_order()
    elif choice =="7":
        print("enjoy your day XD")
        break
    else:
        print("invalid try again")
        break
