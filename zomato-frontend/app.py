from flask import Flask, render_template, request

app = Flask(__name__)

menu = []
orders = []

@app.route('/')
def home():
    return render_template('menu.html', menu=menu)

@app.route('/add_dish', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        dish_id = request.form['dish_id']
        dish_name = request.form['dish_name']
        price = request.form['price']
        availability = request.form['availability']
        dish = {
            'dish_id': dish_id,
            'dish_name': dish_name,
            'price': price,
            'availability': availability
        }
        menu.append(dish)
        return 'Dish added successfully!'
    return render_template('add_dish.html')

@app.route('/remove_dish/<dish_id>', methods=['GET'])
def remove_dish(dish_id):
    for dish in menu:
        if dish['dish_id'] == dish_id:
            menu.remove(dish)
            return 'Dish removed successfully!'
    return 'Dish not found!'

@app.route('/update_availability/<dish_id>/<availability>', methods=['GET'])
def update_availability(dish_id, availability):
    for dish in menu:
        if dish['dish_id'] == dish_id:
            dish['availability'] = availability
            return 'Availability updated successfully!'
    return 'Dish not found!'

@app.route('/take_order', methods=['GET', 'POST'])
def take_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        dish_ids = request.form.getlist('dish_ids')
        order = {
            'customer_name': customer_name,
            'dish_ids': dish_ids,
            'status': 'received'
        }
        orders.append(order)
        return 'Order placed successfully!'
    return render_template('take_order.html', menu=menu)

@app.route('/update_status/<order_id>/<new_status>', methods=['GET'])
def update_status(order_id, new_status):
    for order in orders:
        if order['order_id'] == order_id:
            order['status'] = new_status
            return 'Order status updated successfully!'
    return 'Order not found!'

@app.route('/review_orders', methods=['GET'])
def review_orders():
    return render_template('review_orders.html', orders=orders)

@app.route('/exit', methods=['GET'])
def exit():
    return 'Exiting the application'

if __name__ == '__main__':
    app.run()
