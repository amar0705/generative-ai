class Snack:
    def __init__(self, snack_id, snack_name, price, availability):
        self.snack_id = snack_id
        self.snack_name = snack_name
        self.price = price
        self.availability = availability


class Canteen:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, snack):
        self.inventory.append(snack)
        print(f"Snack {snack.snack_name} added to inventory.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print(f"Snack {snack.snack_name} removed from inventory.")
                return
        print("Snack not found in inventory.")

    def update_snack_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print(f"Snack {snack.snack_name} availability updated.")
                return
        print("Snack not found in inventory.")

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    self.sales_records.append(snack)
                    snack.availability = "no"
                    print(f"Snack {snack.snack_name} sold.")
                    return
                else:
                    print("Snack is not available for sale.")
                    return
        print("Snack not found in inventory.")

    def print_inventory(self):
        print("Current Snack Inventory:")
        for snack in self.inventory:
            print(f"Snack ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}, Availability: {snack.availability}")

    def print_sales_records(self):
        print("Sales Records:")
        for snack in self.sales_records:
            print(f"Snack ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}")


def main():
    canteen = Canteen()

    while True:
        print("\n--- Canteen Management System ---")
        print("1. Add Snack to Inventory")
        print("2. Remove Snack from Inventory")
        print("3. Update Snack Availability")
        print("4. Sell Snack")
        print("5. View Inventory")
        print("6. View Sales Records")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            snack_id = input("Enter Snack ID: ")
            snack_name = input("Enter Snack Name: ")
            price = float(input("Enter Snack Price: "))
            availability = input("Is Snack Available? (yes/no): ")

            snack = Snack(snack_id, snack_name, price, availability)
            canteen.add_snack(snack)

        elif choice == "2":
            snack_id = input("Enter Snack ID: ")
            canteen.remove_snack(snack_id)

        elif choice == "3":
            snack_id = input("Enter Snack ID: ")
            availability = input("Update Snack Availability (yes/no): ")
            canteen.update_snack_availability(snack_id, availability)

        elif choice == "4":
            snack_id = input("Enter Snack ID: ")
            canteen.sell_snack(snack_id)

        elif choice == "5":
            canteen.print_inventory()

        elif choice == "6":
            canteen.print_sales_records()

        elif choice == "0":
            print("Exiting Canteen Management System...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
