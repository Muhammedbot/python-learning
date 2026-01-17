# Day 21 - Expense Tracker with JSON (Week 3 Finale!)

import json
import os
from datetime import datetime

print("="*70)
print("              EXPENSE TRACKER - WEEK 3 PROJECT")
print("="*70)

# File to store expenses
EXPENSES_FILE = "expenses.json"

# Load expenses from JSON file
def load_expenses():
    """Load expenses from JSON file"""
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, "r") as file:
                expenses = json.load(file)
                print(f"✅ Loaded {len(expenses)} expenses from file")
                return expenses
        except json.JSONDecodeError:
            print("⚠️ Expense file corrupted. Starting fresh.")
            return []
        except Exception as e:
            print(f"⚠️ Error loading expenses: {e}")
            return []
    else:
        print("📝 No expense file found. Starting fresh!")
        return []


# Save expenses to JSON file
def save_expenses(expenses):
    """Save expenses to JSON file"""
    try:
        with open(EXPENSES_FILE, "w") as file:
            json.dump(expenses, file, indent=2)
        return True
    except Exception as e:
        print(f"❌ Error saving expenses: {e}")
        return False


# Add new expense
def add_expense(expenses):
    """Add a new expense"""
    print("\n" + "="*70)
    print("ADD NEW EXPENSE")
    print("="*70)

    try:
        # Get expense name
        name = input("\nExpense name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return expenses

        # Get amount
        while True:
            try:
                amount = float(input("Amount ($): "))
                if amount <= 0:
                    print("❌ Amount must be positive!")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number!")

        # Get category
        print("\nCategories:")
        print("1. Food & Dining")
        print("2. Transportation")
        print("3. Bills & Utilities")
        print("4. Shopping")
        print("5. Entertainment")
        print("6. Healthcare")
        print("7. Other")

        category_choice = input("\nChoose category (1-7) or type custom: ")

        categories = {
            "1": "Food & Dining",
            "2": "Transportation",
            "3": "Bills & Utilities",
            "4": "Shopping",
            "5": "Entertainment",
            "6": "Healthcare",
            "7": "Other"
        }

        if category_choice in categories:
            category = categories[category_choice]
        else:
            category = category_choice.strip().title()

        # Get date (or use today)
        use_today = input("\nUse today's date? (yes/no): ").lower()

        if use_today == "yes" or use_today == "y":
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            date = input("Enter date (YYYY-MM-DD): ")

        # Optional note
        note = input("Add note (optional): ").strip()

        # Create expense
        expense = {
            "name": name,
            "amount": amount,
            "category": category,
            "date": date,
            "note": note if note else ""
        }

        expenses.append(expense)

        if save_expenses(expenses):
            print("\n✅ Expense added successfully!")
            print(f"💰 {name}: ${amount:.2f} ({category})")
        else:
            print("⚠️ Expense added but failed to save!")

        return expenses

    except KeyboardInterrupt:
        print("\n⚠️ Cancelled")
        return expenses
    except Exception as e:
        print(f"❌ Error: {e}")
        return expenses

def export_report(expenses):
    """Export expenses to a readable text file"""
    if len(expenses) == 0:
        print("\n💸 No expenses to export!")
        return

    print("\n" + "="*70)
    print("EXPORT REPORT")
    print("="*70)

    filename = f"expense_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    try:
        with open(filename, "w") as file:
            file.write("="*70 + "\n")
            file.write("              EXPENSE TRACKER REPORT\n")
            file.write(f"              Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*70 + "\n\n")

            # Category Breakdown
            file.write("CATEGORY BREAKDOWN\n")
            file.write("-" * 20 + "\n")

            cat_summary = {}
            for expense in expenses:
                cat = expense['category']
                if cat not in cat_summary:
                    cat_summary[cat] = []
                cat_summary[cat].append(expense)

            for cat in sorted(cat_summary.keys()):
                cat_expenses = cat_summary[cat]
                cat_total = sum([e['amount'] for e in cat_expenses])

                file.write(f"{cat}:\n")
                file.write(f"  Count: {len(cat_expenses)} | Total: ${cat_total:,.2f}\n\n")

                for expense in cat_expenses:
                    file.write(f"  • {expense['name']}: ${expense['amount']:.2f} ({expense['date']})\n")

                file.write("\n")

            # All expenses
            file.write("="*70 + "\n")
            file.write("ALL EXPENSES\n")
            file.write("="*70 + "\n\n")

            for i, expense in enumerate(expenses, 1):
                file.write(f"{i}. {expense['name']}\n")
                file.write(f"   Amount: ${expense['amount']:.2f}\n")
                file.write(f"   Category: {expense['category']}\n")
                file.write(f"   Date: {expense['date']}\n")
                if expense['note']:
                    file.write(f"   Note: {expense['note']}\n")
                file.write("\n")

        print(f"✅ Report exported to: {filename}")
    except Exception as e:
        print(f"❌ Export failed: {e}")

def view_all_expenses(expenses):
    """View all tracked expenses"""
    if len(expenses) == 0:
        print("\n💸 No expenses yet!")
        return

    print("\n" + "="*70)
    print("ALL EXPENSES")
    print("="*70)

    total = 0
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")
        print(f"   Category: {expense['category']} | Date: {expense['date']}")
        if expense['note']:
            print(f"   Note: {expense['note']}")
        total += expense['amount']

    print("\n" + "="*70)
    print(f"💰 Grand Total: ${total:,.2f}")
    print("="*70)

def search_expenses(expenses):
    """Search expenses by name or category"""
    if len(expenses) == 0:
        print("\n💸 No expenses yet!")
        return

    print("\n" + "="*70)
    print("SEARCH EXPENSES")
    print("="*70)

    search_term = input("\nSearch for (name or category): ").lower().strip()

    if not search_term:
        print("❌ Please enter a search term!")
        return

    # Search
    results = []

    for expense in expenses:
        if (search_term in expense['name'].lower() or 
            search_term in expense['category'].lower() or
            (expense['note'] and search_term in expense['note'].lower())):
            results.append(expense)

    if len(results) == 0:
        print(f"\n❌ No expenses found matching '{search_term}'")
    else:
        print(f"\n✅ Found {len(results)} expense(s):")
        print("-" * 70)

        total = 0
        for i, expense in enumerate(results, 1):
            print(f"\n{i}. {expense['name']} - ${expense['amount']:.2f}")
            print(f"   Category: {expense['category']} | Date: {expense['date']}")
            if expense['note']:
                print(f"   Note: {expense['note']}")
            total += expense['amount']

        print("\n" + "="*70)
        print(f"💰 Total in search results: ${total:,.2f}")
        print("="*70)

def view_by_category(expenses):
    """Group and view expenses by category"""
    if not expenses:
        print("\n💸 No expenses yet!")
        return

    categories = {}
    for expense in expenses:
        cat = expense['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(expense)

    print("\n" + "="*70)
    print("EXPENSES BY CATEGORY")
    print("="*70)

    for cat in sorted(categories.keys()):
        cat_expenses = categories[cat]
        cat_total = sum(e['amount'] for e in cat_expenses)
        print(f"\n📁 {cat.upper()} (${cat_total:.2f})")
        print("-" * 30)
        for e in cat_expenses:
            print(f"• {e['name']}: ${e['amount']:.2f} ({e['date']})")

def monthly_summary(expenses):
    """Show expenses grouped by month"""
    if not expenses:
        print("\n💸 No expenses yet!")
        return

    months = {}
    for expense in expenses:
        try:
            # Extract month/year from date string
            date_obj = datetime.strptime(expense['date'], "%Y-%m-%d")
            month_key = date_obj.strftime("%B %Y")
        except ValueError:
            month_key = "Unknown Date"

        if month_key not in months:
            months[month_key] = 0
        months[month_key] += expense['amount']

    print("\n" + "="*70)
    print("MONTHLY SUMMARY")
    print("="*70)

    for month, total in months.items():
        print(f"📅 {month}: ${total:,.2f}")

def show_statistics(expenses):
    """Show high-level expense statistics"""
    if not expenses:
        print("\n💸 No expenses yet!")
        return

    amounts = [e['amount'] for e in expenses]
    total = sum(amounts)
    avg = total / len(expenses)
    highest = max(expenses, key=lambda x: x['amount'])

    print("\n" + "="*70)
    print("EXPENSE STATISTICS")
    print("="*70)
    print(f"📊 Total expenses: {len(expenses)}")
    print(f"💰 Total spent: ${total:,.2f}")
    print(f"📈 Average expense: ${avg:,.2f}")
    print(f"🔥 Highest expense: {highest['name']} (${highest['amount']:.2f})")

def delete_expense(expenses):
    """Delete an expense by its index"""
    if not expenses:
        print("\n💸 No expenses to delete!")
        return expenses

    view_all_expenses(expenses)
    try:
        idx = int(input("\nEnter index to delete (or 0 to cancel): "))
        if idx == 0:
            return expenses
        if 1 <= idx <= len(expenses):
            deleted = expenses.pop(idx - 1)
            save_expenses(expenses)
            print(f"\n✅ Deleted: {deleted['name']}")
        else:
            print("\n❌ Invalid index!")
    except ValueError:
        print("\n❌ Please enter a valid number!")

    return expenses



# Main program
print("\n🌐 Loading expenses...\n")
expenses = load_expenses()

while True:
    print("\n" + "="*70)
    print("                    EXPENSE TRACKER MENU")
    print("="*70)
    print("1. 💰 Add new expense")
    print("2. 📋 View all expenses")
    print("3. 📂 View by category")
    print("4. 📅 Monthly summary")
    print("5. 🔍 Search expenses")
    print("6. 📊 Show statistics")
    print("7. 🗑️  Delete expense")
    print("8. 📤 Export report")
    print("9. 🚪 Exit")
    print("="*70)

    choice = input("\nYour choice (1-9): ")

    if choice == "1":
        expenses = add_expense(expenses)

    elif choice == "2":
        view_all_expenses(expenses)

    elif choice == "3":
        view_by_category(expenses)

    elif choice == "4":
        monthly_summary(expenses)

    elif choice == "5":
        search_expenses(expenses)

    elif choice == "6":
        show_statistics(expenses)

    elif choice == "7":
        expenses = delete_expense(expenses)

    elif choice == "8":
        export_report(expenses)

    elif choice == "9":
        print("\n" + "="*70)
        print("Thanks for using Expense Tracker!")
        print(f"Total expenses tracked: {len(expenses)}")
        if len(expenses) > 0:
            total = sum([e['amount'] for e in expenses])
            print(f"Total amount: ${total:,.2f}")
        print("="*70)
        break

    else:
        print("\n❌ Invalid choice! Pick 1-9")
