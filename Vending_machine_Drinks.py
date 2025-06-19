import csv


class SuperShop:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def import_form_csv(cls):
        with open("super_shop.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            SuperShop(
                name=item.get("Name"),
                price=float(item.get("Price")),
                quantity=float(item.get("Quantity"))
            )

    @staticmethod
    def customer(Item_no):
        final_price = 0
        with open("super_shop.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            if item.get("Item_no") == str(Item_no):
                quantity = int(input("Please Enter the Quantity you would like to buy: "))
                if int(item["Quantity"]) >= quantity:
                    price = int(quantity) * int(item["Price"])
                    final_price += price

                    item["Quantity"] = str(int(item["Quantity"]) - int(quantity))

                    # Update the CSV file with the modified items
                    with open("super_shop.csv", "w", newline='') as file:
                        fieldnames = ["Item_no", "Name", "Price", "Quantity"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        if file.tell() == 0:
                            writer.writeheader()
                        writer.writerows(items)
                else:
                    print("Sorry! Out of stock.")
        return f"\n{final_price} bdt"

    @classmethod
    def interface(cls):
        print()
        print("Welcome to Soft Drinking Center.\nThis is the list of the drinks and the prices.\n")
        with open("super_shop.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        num = 1
        for item in items:
            print(f"{int(num)}.{item.get('Name')} - {item.get('Price')} bdt")
            num += 1

        while True:
            print()
            order = int(input("Which one you would like to take? please select the item no : "))
            print(SuperShop.customer(order))
            print()
            print("Would you like to shop more?\n1.Yes\n2.No")
            response = int(input("Please select your choice: "))
            if response == 1:
                continue
            if response == 2:
                print("\nThank you for your shopping. ")
                break

            else:
                print("Sorry! Wrong option.")
                quit()


SuperShop.interface()
