import datetime

books = [
    {'title': 'The Gruffalo', 'author': 'Julia Donaldson', 'price': 4.99},
    {'title': 'The Rainbow Fish', 'author': 'Marcus Pfister', 'price': 4.99}
]

orders = []

def book_menu():
    print("\n--- Book Menu ---")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} by {book['author']} - £{book['price']:.2f}")
    print()

def book_order():
    book_menu()
    choice = input("Choose a book by number: ")
    if choice.isdigit() and 1 <= int(choice) <= len(books):
        selected_book = books[int(choice) - 1]
        orders.append(selected_book)
        print(f"You've ordered: {selected_book['title']}")
    else:
        print("Invalid choice. Please try again.")

def view_orders():
    if not orders:
        print("\nYour basket is empty.")
        return

    print("\n--- Your Order ---")
    total = 0
    for i, item in enumerate(orders, start=1):
        name = item.get('title') or item.get('name', 'Unknown Item')
        price = item['price']
        print(f"{i}. {name} - £{price:.2f}")
        total += price
    print(f"\nTotal: £{total:.2f}")

def order_beverage():
    beverages = {
        "Coffee": 2.50,
        "Tea": 2.00,
        "Soda": 1.50,
        "Juice": 3.00
    }

    print("\n--- Available Beverages ---")
    for i, (name, price) in enumerate(beverages.items(), start=1):
        print(f"{i}. {name} - £{price:.2f}")

    choice = input("Choose a beverage by number: ")
    if choice.isdigit() and 1 <= int(choice) <= len(beverages):
        selected = list(beverages.keys())[int(choice) - 1]
        orders.append({"name": selected, "price": beverages[selected]})
        print(f"Added: {selected} (£{beverages[selected]:.2f})")
    else:
        print("Invalid choice. Please enter a number corresponding to a beverage.")

def save_order():
    if not orders:
        print("No orders to save!")
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = sum(item['price'] for item in orders)

    with open("orders.txt", "a") as file:
        file.write(f"\n=== Order ({timestamp}) ===\n")
        for item in orders:
            name = item.get('title') or item.get('name', 'Unknown Item')
            file.write(f"- {name}: £{item['price']:.2f}\n")
        file.write(f"Total: £{total:.2f}\n")

    print(f"Order saved to 'orders.txt' (Total: £{total:.2f})")

def clear_basket():
    orders.clear()
    print("Basket cleared!")

def main():
    while True:
        print("""
--- Main Menu ---
1. Show book menu
2. Order a book
3. View your order
4. Order a drink
5. Clear basket
6. Save order (add to basket)
7. Quit
""")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            book_menu()
        elif choice == "2":
            book_order()
        elif choice == "3":
            view_orders()
        elif choice == "4":
            order_beverage()
        elif choice == "5":
            clear_basket()
        elif choice == "6":
            save_order()
        elif choice == "7":
            print("Enjoy your day! 😊")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    print("Welcome to Haala's Bookstore and Cafe!\n")
    main()
