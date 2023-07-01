class ZomatoChronicles:
    def __init__(self):
        self.menu = []
        self.orders = {}
        self.order_id = 1
    
    def add_dish(self, dish_id, dish_name, price):
        dish = {
            'dish_id': dish_id,
            'dish_name': dish_name,
            'price': price,
            'availability': True
        }
        self.menu.append(dish)
        print(f"Added '{dish_name}' to the menu.")

    def remove_dish(self, dish_id):
        for dish in self.menu:
            if dish['dish_id'] == dish_id:
                self.menu.remove(dish)
                print(f"Removed dish with ID '{dish_id}' from the menu.")
                break
        else:
            print(f"No dish found with ID '{dish_id}'.")

    def update_dish_availability(self, dish_id, availability):
        for dish in self.menu:
            if dish['dish_id'] == dish_id:
                dish['availability'] = availability
                print(f"Updated availability of dish with ID '{dish_id}' to {availability}.")
                break
        else:
            print(f"No dish found with ID '{dish_id}'.")

    def take_order(self, customer_name, dish_ids):
        order_items = []
        for dish_id in dish_ids:
            dish = next((dish for dish in self.menu if dish['dish_id'] == dish_id), None)
            if dish and dish['availability']:
                order_items.append(dish)
            else:
                print(f"Dish with ID '{dish_id}' is not available. Skipping...")
        
        if order_items:
            order = {
                'order_id': self.order_id,
                'customer_name': customer_name,
                'order_items': order_items,
                'status': 'received'
            }
            self.orders[self.order_id] = order
            self.order_id += 1
            print(f"Order {order['order_id']} received successfully.")

    def update_order_status(self, order_id, status):
        order = self.orders.get(order_id)
        if order:
            order['status'] = status
            print(f"Updated status of order {order_id} to '{status}'.")
        else:
            print(f"No order found with ID '{order_id}'.")
        
    def review_orders(self):
        if self.orders:
            for order_id, order in self.orders.items():
                print(f"Order ID: {order_id}")
                print(f"Customer Name: {order['customer_name']}")
                print("Order Items:")
                for item in order['order_items']:
                    print(f" - {item['dish_name']} (ID: {item['dish_id']})")
                print(f"Status: {order['status']}\n")
        else:
            print("No orders to review.")

    def run(self):
        print("Welcome to Zomato Chronicles: The Great Food Fiasco!")
        while True:
            print("\nPlease select an option:")
            print("1. Add a dish to the menu")
            print("2. Remove a dish from the menu")
            print("3. Update dish availability")
            print("4. Take a new order")
            print("5. Update order status")
            print("6. Review all orders")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")
            
            if choice == '1':
                dish_id = input("Enter the dish ID: ")
                dish_name = input("Enter the dish name: ")
                price = float(input("Enter the dish price: "))
                self.add_dish(dish_id, dish_name, price)
            elif choice == '2':
                dish_id = input("Enter the dish ID to remove: ")
                self.remove_dish(dish_id)
            elif choice == '3':
                dish_id = input("Enter the dish ID to update availability: ")
                availability = input("Enter the availability (True or False): ")
                self.update_dish_availability(dish_id, availability.lower() == 'true')
            elif choice == '4':
                customer_name = input("Enter customer name: ")
                dish_ids = input("Enter dish IDs (separated by commas): ").split(',')
                self.take_order(customer_name, dish_ids)
            elif choice == '5':
                order_id = input("Enter the order ID to update status: ")
                status = input("Enter the new status: ")
                self.update_order_status(int(order_id), status)
            elif choice == '6':
                self.review_orders()
            elif choice == '7':
                print("Exiting Zomato Chronicles. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the application
zomato_app = ZomatoChronicles()
zomato_app.run()
