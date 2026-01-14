# Day 16 - Inventory Management System

print("===== INVENTORY MANAGEMENT SYSTEM =====")
print()

# Dictionary to store inventory
# Structure: {"item_name": {"quantity": 10, "price": 25.50}}
inventory = {}


def add_item():
    """Add new item to inventory"""
    print("\n--- Add New Item ---")
    name = input("Item name: ").lower()

    if name in inventory:
        print(f"❌ {name.title()} already exists! Use 'Update' instead.")
        return

    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price per unit: $"))

        if quantity < 0 or price < 0:
            print("❌ Quantity and price must be positive!")
            return

        inventory[name] = {
            "quantity": quantity,
            "price": price
        }

        print(f"✅ Added {quantity} units of {name.title()} at ${price} each")

    except ValueError:
        print("❌ Invalid input! Please enter numbers.")


def view_inventory():
    """Display all items in inventory"""
    if len(inventory) == 0:
        print("\n📦 Inventory is empty!")
        return

    print("\n===== CURRENT INVENTORY =====")
    print(f"{'Item':<20} {'Quantity':<12} {'Price':<12} {'Total Value'}")
    print("-" * 60)

    total_value = 0

    for item_name, details in inventory.items():
        quantity = details["quantity"]
        price = details["price"]
        item_value = quantity * price
        total_value += item_value

        print(f"{item_name.title():<20} {quantity:<12} ${price:<11.2f} ${item_value:.2f}")

    print("-" * 60)
    print(f"{'TOTAL INVENTORY VALUE:':<44} ${total_value:.2f}")
    print()


def update_quantity():
    """Update item quantity (restock or sell)"""
    if len(inventory) == 0:
        print("\n📦 Inventory is empty!")
        return

    print("\n--- Update Quantity ---")
    name = input("Item name: ").lower()

    if name not in inventory:
        print(f"❌ {name.title()} not found in inventory!")
        return

    print(f"\nCurrent quantity of {name.title()}: {inventory[name]['quantity']}")
    print("1. Restock (add)")
    print("2. Sell (subtract)")

    choice = input("Choice (1-2): ")

    try:
        amount = int(input("Amount: "))

        if amount < 0:
            print("❌ Amount must be positive!")
            return

        if choice == "1":
            # Restock
            inventory[name]["quantity"] += amount
            print(f"✅ Added {amount} units. New quantity: {inventory[name]['quantity']}")

        elif choice == "2":
            # Sell
            if amount > inventory[name]["quantity"]:
                print(f"❌ Not enough stock! Only {inventory[name]['quantity']} available.")
                return

            inventory[name]["quantity"] -= amount
            revenue = amount * inventory[name]["price"]
            print(f"✅ Sold {amount} units. Revenue: ${revenue:.2f}")
            print(f"   Remaining quantity: {inventory[name]['quantity']}")

        else:
            print("❌ Invalid choice!")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")

def update_price():
    """Update item price"""
    if len(inventory) == 0:
        print("\n📦 Inventory is empty!")
        return

    print("\n--- Update Price ---")
    name = input("Item name: ").lower()

    if name not in inventory:
        print(f"❌ {name.title()} not found in inventory!")
        return

    print(f"Current price of {name.title()}: ${inventory[name]['price']:.2f}")

    try:
        new_price = float(input("New price: $"))

        if new_price < 0:
            print("❌ Price must be positive!")
            return

        old_price = inventory[name]["price"]
        inventory[name]["price"] = new_price

        change = ((new_price - old_price) / old_price) * 100
        print(f"✅ Price updated from ${old_price:.2f} to ${new_price:.2f}")
        print(f"   Change: {change:+.1f}%")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")


def remove_item():
    """Remove item from inventory"""
    if len(inventory) == 0:
        print("\n📦 Inventory is empty!")
        return

    print("\n--- Remove Item ---")
    name = input("Item name: ").lower()

    if name not in inventory:
        print(f"❌ {name.title()} not found in inventory!")
        return

    confirm = input(f"Remove {name.title()}? (yes/no): ").lower()

    if confirm == "yes":
        removed = inventory.pop(name)
        print(f"🗑️ Removed {name.title()} from inventory")
        print(f"   Had {removed['quantity']} units at ${removed['price']:.2f} each")
    else:
        print("❌ Cancelled")


def search_item():
    """Search for items"""
    if len(inventory) == 0:
        print("\n📦 Inventory is empty!")
        return

    print("\n--- Search Items ---")
    search_term = input("Search for: ").lower()

    found = []
    for item_name in inventory:
        if search_term in item_name:
            found.append(item_name)

    if len(found) == 0:
        print(f"❌ No items found matching '{search_term}'")
    else:
        print(f"\n--- Found {len(found)} item(s) ---")
        for item in found:
            details = inventory[item]
            print(f"\n{item.title()}")
            print(f"  Quantity: {details['quantity']}")
            print(f"  Price: ${details['price']:.2f}")
            print(f"  Value: ${details['quantity'] * details['price']:.2f}")


def low_stock_alert():
    """Show items with low stock"""
    if len(inventory) == 0:
        print("\n📦 Inventory is empty!")
        return

    try:
        threshold = int(input("\nLow stock threshold: "))

        low_stock = []
        for item_name, details in inventory.items():
            if details["quantity"] <= threshold:
                low_stock.append(item_name)

        if len(low_stock) == 0:
            print(f"✅ No items below {threshold} units!")
        else:
            print(f"\n⚠️ LOW STOCK ALERT ({len(low_stock)} items)")
            print("-" * 50)
            for item in low_stock:
                details = inventory[item]
                print(f"{item.title()}: {details['quantity']} units (Price: ${details['price']:.2f})")

    except ValueError:
        print("❌ Invalid input!")


        def calculate_stats():
            """Calculate inventory statistics"""
            if len(inventory) == 0:
                print("\n📦 Inventory is empty!")
                return

            print("\n===== INVENTORY STATISTICS =====")

            # Total items
            total_items = len(inventory)
            print(f"Total different items: {total_items}")

            # Total units
            total_units = sum([details["quantity"] for details in inventory.values()])
            print(f"Total units in stock: {total_units}")

            # Total value
            total_value = sum([details["quantity"] * details["price"] for details in inventory.values()])
            print(f"Total inventory value: ${total_value:.2f}")

            # Average price
            avg_price = sum([details["price"] for details in inventory.values()]) / total_items
            print(f"Average item price: ${avg_price:.2f}")

            # Most expensive item
            most_expensive = max(inventory.items(), key=lambda x: x[1]["price"])
            print(f"\nMost expensive: {most_expensive[0].title()} (${most_expensive[1]['price']:.2f})")

            # Cheapest item
            cheapest = min(inventory.items(), key=lambda x: x[1]["price"])
            print(f"Cheapest: {cheapest[0].title()} (${cheapest[1]['price']:.2f})")

            # Highest quantity
            highest_stock = max(inventory.items(), key=lambda x: x[1]["quantity"])
            print(f"\nHighest stock: {highest_stock[0].title()} ({highest_stock[1]['quantity']} units)")

            # Lowest quantity
            lowest_stock = min(inventory.items(), key=lambda x: x[1]["quantity"])
            print(f"Lowest stock: {lowest_stock[0].title()} ({lowest_stock[1]['quantity']} units)")
            
        # Main menu
        while True:
            print("\n" + "="*50)
            print("        INVENTORY MANAGEMENT SYSTEM")
            print("="*50)
            print("1. Add new item")
            print("2. View inventory")
            print("3. Update quantity (restock/sell)")
            print("4. Update price")
            print("5. Remove item")
            print("6. Search items")
            print("7. Low stock alert")
            print("8. Statistics")
            print("9. Exit")
            print("="*50)

            choice = input("\nChoice (1-9): ")

            if choice == "1":
                add_item()
            elif choice == "2":
                view_inventory()
            elif choice == "3":
                update_quantity()
            elif choice == "4":
                update_price()
            elif choice == "5":
                remove_item()
            elif choice == "6":
                search_item()
            elif choice == "7":
                low_stock_alert()
            elif choice == "8":
                calculate_stats()
            elif choice == "9":
                print("\n📦 Goodbye! Inventory saved in memory.")
                break
            else:
                print("\n❌ Invalid choice! Pick 1-9.")
