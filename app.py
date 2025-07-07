from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

books = [
    {'title': 'The gruffalo', 'author': 'julia donaldson', 'price': 4.99},
    {'title': 'the rainbow fish', 'author': 'marcus pfister', 'price': 4.99},
]

beverages = {
    "Coffee": 2.50,
    "Tea": 2.00,
    "Soda": 1.50,
    "Juice": 3.00
}

orders = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def book_menu():
    return render_template('menu.html', books=books)

@app.route('/order_book', methods=['POST'])
def order_book():
    book_index = int(request.form['book_index'])
    orders.append(books[book_index])
    return redirect(url_for('view_orders'))

@app.route('/order_beverage', methods=['POST'])
def order_beverage():
    drink = request.form['drink']
    if drink in beverages:
        orders.append({'name': drink, 'price': beverages[drink]})
    return redirect(url_for('view_orders'))

@app.route('/view_orders')
def view_orders():
    total = sum(item['price'] for item in orders)
    return render_template('order.html', orders=orders, total=total)

@app.route('/clear')
def clear():
    orders.clear()
    return redirect(url_for('view_orders'))

@app.route('/save_order')
def save_order():
    if not orders:
        return redirect(url_for('view_orders'))

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = sum(item['price'] for item in orders)

    with open("orders.txt", "a") as file:
        file.write(f"\n=== Order ({timestamp}) ===\n")
        for item in orders:
            name = item.get('title', item.get('name', 'Unknown Item'))
            file.write(f"- {name}: £{item['price']:.2f}\n")
        file.write(f"Total: £{total:.2f}\n")

    return render_template("receipt.html", total=total)

if __name__ == '__main__':
    app.run(debug=True)
