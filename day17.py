# Day 17 - Complete Review: Personal Management System
# Combines: Variables, Functions, Loops, Lists, Dictionaries, Tuples, Files

import os
from datetime import datetime

print("="*60)
print("     PERSONAL MANAGEMENT SYSTEM")
print("     Everything You've Learned in One App!")
print("="*60)

# ============================================
# GLOBAL DATA STRUCTURES
# ============================================

contacts = []      # List of contact dictionaries
todos = []         # List of to-do dictionaries
expenses = []      # List of expense dictionaries
notes = []         # List of note dictionaries

# File names for persistence
CONTACTS_FILE = "pms_contacts.txt"
TODOS_FILE = "pms_todos.txt"
EXPENSES_FILE = "pms_expenses.txt"
NOTES_FILE = "pms_notes.txt"


# ============================================
# PART 1: CONTACT MANAGER
# ============================================

def load_contacts():
    """Load contacts from file - DEMONSTRATES: Files, Lists, Dictionaries"""
    global contacts
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split("|")
                        if len(parts) == 3:
                            contact = {
                                "name": parts[0],
                                "phone": parts[1],
                                "email": parts[2]
                            }
                            contacts.append(contact)
            print(f"✅ Loaded {len(contacts)} contacts")
        except:
            print("⚠️ Error loading contacts")


def save_contacts():
    """Save contacts to file - DEMONSTRATES: Files, Loops"""
    try:
        with open(CONTACTS_FILE, "w") as file:
            for contact in contacts:
                file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")
        return True
    except:
        return False


def add_contact():
    """Add new contact - DEMONSTRATES: Dictionaries, Input, Validation"""
    print("\n--- Add Contact ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    if save_contacts():
        print(f"✅ Added {name}")


def view_contacts():
    """View all contacts - DEMONSTRATES: Loops, Conditionals, String Formatting"""
    if len(contacts) == 0:
        print("\n📱 No contacts yet!")
        return

    print("\n===== YOUR CONTACTS =====")
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f"   📞 {contact['phone']}")
        print(f"   📧 {contact['email']}")


def search_contacts():
    """Search contacts - DEMONSTRATES: String Methods, Conditionals"""
    search = input("\nSearch for: ").lower()
    found = []

    for contact in contacts:
        if (search in contact['name'].lower() or 
            search in contact['phone'] or 
            search in contact['email'].lower()):
            found.append(contact)

    if len(found) == 0:
        print("❌ No contacts found!")
    else:
        print(f"\n--- Found {len(found)} contact(s) ---")
        for contact in found:
            print(f"• {contact['name']} - {contact['phone']}")


def contact_manager():
    """Contact manager menu - DEMONSTRATES: While loops, Functions"""
    while True:
        print("\n" + "="*40)
        print("CONTACT MANAGER")
        print("="*40)
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contacts")
        print("4. Back to main menu")

        choice = input("\nChoice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice!")

# ============================================
# PART 2: TO-DO LIST MANAGER
# ============================================

def load_todos():
    """Load todos from file"""
    global todos
    if os.path.exists(TODOS_FILE):
        try:
            with open(TODOS_FILE, "r") as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split("|")
                        if len(parts) == 3:
                            todo = {
                                "task": parts[0],
                                "priority": parts[1],
                                "done": parts[2] == "True"
                            }
                            todos.append(todo)
            print(f"✅ Loaded {len(todos)} tasks")
        except:
            print("⚠️ Error loading todos")


def save_todos():
    """Save todos to file"""
    try:
        with open(TODOS_FILE, "w") as file:
            for todo in todos:
                file.write(f"{todo['task']}|{todo['priority']}|{todo['done']}\n")
        return True
    except:
        return False


def add_todo():
    """Add new task - DEMONSTRATES: Dictionaries, Lists"""
    print("\n--- Add Task ---")
    task = input("Task: ")
    print("Priority: 1=Low, 2=Medium, 3=High")
    priority = input("Priority (1-3): ")

    if priority not in ["1", "2", "3"]:
        priority = "2"

    priority_names = {"1": "Low", "2": "Medium", "3": "High"}

    todo = {
        "task": task,
        "priority": priority_names[priority],
        "done": False
    }

    todos.append(todo)
    if save_todos():
        print("✅ Task added!")


def view_todos():
    """View all tasks - DEMONSTRATES: Loops, Conditionals, Emojis"""
    if len(todos) == 0:
        print("\n✅ No tasks! You're all clear!")
        return

    print("\n===== YOUR TASKS =====")

    # Separate by priority - DEMONSTRATES: Filtering
    high = [t for t in todos if t['priority'] == "High" and not t['done']]
    medium = [t for t in todos if t['priority'] == "Medium" and not t['done']]
    low = [t for t in todos if t['priority'] == "Low" and not t['done']]
    completed = [t for t in todos if t['done']]

    if high:
        print("\n🔴 HIGH PRIORITY:")
        for i, task in enumerate(high, 1):
            print(f"  {i}. {task['task']}")

    if medium:
        print("\n🟡 MEDIUM PRIORITY:")
        for i, task in enumerate(medium, 1):
            print(f"  {i}. {task['task']}")

    if low:
        print("\n🟢 LOW PRIORITY:")
        for i, task in enumerate(low, 1):
            print(f"  {i}. {task['task']}")

    if completed:
        print(f"\n✅ COMPLETED ({len(completed)}):")
        for task in completed[:3]:  # Show only first 3
            print(f"  • {task['task']}")


def complete_todo():
    """Mark task as complete - DEMONSTRATES: List Indexing, Boolean"""
    if len(todos) == 0:
        print("\nNo tasks!")
        return

    print("\n--- Your Tasks ---")
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo['done'] else "⬜"
        print(f"{i}. {status} {todo['task']}")

    try:
        num = int(input("\nComplete which task? "))
        if 1 <= num <= len(todos):
            todos[num-1]['done'] = True
            if save_todos():
                print(f"✅ Completed: {todos[num-1]['task']}")
        else:
            print("Invalid number!")
    except:
        print("Invalid input!")


def todo_manager():
    """To-do manager menu"""
    while True:
        print("\n" + "="*40)
        print("TO-DO LIST MANAGER")
        print("="*40)
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Back to main menu")

        choice = input("\nChoice: ")

        if choice == "1":
            add_todo()
        elif choice == "2":
            view_todos()
        elif choice == "3":
            complete_todo()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice!")

# ============================================
# PART 3: EXPENSE TRACKER
# ============================================

def load_expenses():
    """Load expenses from file"""
    global expenses
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, "r") as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split("|")
                        if len(parts) == 4:
                            expense = {
                                "name": parts[0],
                                "amount": float(parts[1]),
                                "category": parts[2],
                                "date": parts[3]
                            }
                            expenses.append(expense)
            print(f"✅ Loaded {len(expenses)} expenses")
        except:
            print("⚠️ Error loading expenses")


def save_expenses():
    """Save expenses to file"""
    try:
        with open(EXPENSES_FILE, "w") as file:
            for expense in expenses:
                file.write(f"{expense['name']}|{expense['amount']}|{expense['category']}|{expense['date']}\n")
        return True
    except:
        return False


def add_expense():
    """Add new expense - DEMONSTRATES: Float, Datetime, Dictionaries"""
    print("\n--- Add Expense ---")
    name = input("Expense name: ")

    try:
        amount = float(input("Amount: $"))
    except:
        print("Invalid amount!")
        return

    print("Categories: food, transport, bills, shopping, other")
    category = input("Category: ").lower()

    # Get current date - DEMONSTRATES: Datetime module
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    if save_expenses():
        print(f"✅ Added ${amount} expense")


def view_expenses():
    """View all expenses - DEMONSTRATES: Calculations, String Formatting"""
    if len(expenses) == 0:
        print("\n💰 No expenses yet!")
        return

    print("\n===== YOUR EXPENSES =====")

    total = 0
    for expense in expenses:
        total += expense['amount']
        print(f"• {expense['name']}: ${expense['amount']:.2f} ({expense['category']}) - {expense['date']}")

    print(f"\n💵 TOTAL: ${total:.2f}")


def expense_stats():
    """Expense statistics - DEMONSTRATES: Advanced Calculations, Dictionaries"""
    if len(expenses) == 0:
        print("\nNo expenses yet!")
        return

    print("\n===== EXPENSE STATISTICS =====")

    # Total - DEMONSTRATES: Sum, List Comprehension
    total = sum([e['amount'] for e in expenses])
    print(f"Total spent: ${total:.2f}")

    # By category - DEMONSTRATES: Dictionary Building
    by_category = {}
    for expense in expenses:
        cat = expense['category']
        if cat in by_category:
            by_category[cat] += expense['amount']
        else:
            by_category[cat] = expense['amount']

    print("\nBy Category:")
    for category, amount in by_category.items():
        percentage = (amount / total) * 100
        print(f"  {category.title()}: ${amount:.2f} ({percentage:.1f}%)")

    # Biggest expense - DEMONSTRATES: Max function
    if expenses:
        biggest = max(expenses, key=lambda x: x['amount'])
        print(f"\nBiggest expense: {biggest['name']} (${biggest['amount']:.2f})")


def expense_tracker():
    """Expense tracker menu"""
    while True:
        print("\n" + "="*40)
        print("EXPENSE TRACKER")
        print("="*40)
        print("1. Add expense")
        print("2. View expenses")
        print("3. Statistics")
        print("4. Back to main menu")
        choice = input("\nChoice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_stats()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice!")

# ============================================
# PART 4: NOTES/DIARY
# ============================================

def load_notes():
    """Load notes from file"""
    global notes
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, "r") as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split("|", 2)  # Split only twice
                        if len(parts) == 3:
                            note = {
                                "title": parts[0],
                                "date": parts[1],
                                "content": parts[2]
                            }
                            notes.append(note)
            print(f"✅ Loaded {len(notes)} notes")
        except:
            print("⚠️ Error loading notes")


def save_notes():
    """Save notes to file"""
    try:
        with open(NOTES_FILE, "w") as file:
            for note in notes:
                # Replace | in content to avoid issues
                content = note['content'].replace("|", "¦")
                file.write(f"{note['title']}|{note['date']}|{content}\n")
        return True
    except:
        return False


def add_note():
    """Add new note - DEMONSTRATES: Multi-line input, Datetime"""
    print("\n--- New Note ---")
    title = input("Note title: ")
    print("Note content (press Enter twice to finish):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    content = "\n".join(lines)
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    note = {
        "title": title,
        "date": date,
        "content": content
    }

    notes.append(note)
    if save_notes():
        print("✅ Note saved!")


def view_notes():
    """View all notes - DEMONSTRATES: String Manipulation"""
    if len(notes) == 0:
        print("\n📝 No notes yet!")
        return

    print("\n===== YOUR NOTES =====")
    for i, note in enumerate(notes, 1):
        print(f"\n{i}. {note['title']}")
        print(f"   Date: {note['date']}")
        # Show first 50 characters of content
        preview = note['content'][:50]
        if len(note['content']) > 50:
            preview += "..."
        print(f"   Preview: {preview}")


def read_note():
    """Read full note - DEMONSTRATES: Indexing, Error Handling"""
    if len(notes) == 0:
        print("\nNo notes!")
        return

    view_notes()

    try:
        num = int(input("\nRead which note? "))
        if 1 <= num <= len(notes):
            note = notes[num-1]
            print(f"\n{'='*50}")
            print(f"Title: {note['title']}")
            print(f"Date: {note['date']}")
            print(f"{'='*50}")
            print(note['content'])
            print(f"{'='*50}")
        else:
            print("Invalid number!")
    except:
        print("Invalid input!")


def notes_manager():
    """Notes manager menu"""
    while True:
        print("\n" + "="*40)
        print("NOTES & DIARY")
        print("="*40)
        print("1. Write new note")
        print("2. View all notes")
        print("3. Read note")
        print("4. Back to main menu")

        choice = input("\nChoice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            read_note()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice!")


# ============================================

# ============================================
# PART 5: DASHBOARD & STATISTICS
# ============================================

def show_dashboard():
    """Show overview dashboard - DEMONSTRATES: All Concepts Together"""
    print("\n" + "="*60)
    print("                    DASHBOARD")
    print("="*60)

    # Contacts summary
    print(f"\n📱 CONTACTS: {len(contacts)} saved")
    if contacts:
        print(f"   Latest: {contacts[-1]['name']}")

    # Tasks summary - DEMONSTRATES: Filtering with List Comprehension
    pending = [t for t in todos if not t['done']]
    completed = [t for t in todos if t['done']]
    print(f"\n✅ TASKS: {len(pending)} pending, {len(completed)} completed")
    if pending:
        high_priority = [t for t in pending if t['priority'] == "High"]
        if high_priority:
            print(f"   ⚠️ {len(high_priority)} high priority tasks!")

    # Expenses summary - DEMONSTRATES: Calculations
    if expenses:
        total = sum([e['amount'] for e in expenses])
        print(f"\n💰 EXPENSES: ${total:.2f} total")
        print(f"   {len(expenses)} transactions")
        avg = total / len(expenses)
        print(f"   Average: ${avg:.2f}")
    else:
        print(f"\n💰 EXPENSES: No expenses tracked yet")

    # Notes summary
    print(f"\n📝 NOTES: {len(notes)} saved")
    if notes:
        print(f"   Latest: {notes[-1]['title']}")

    # Overall stats - DEMONSTRATES: Tuples for multiple returns
    total_items = len(contacts) + len(todos) + len(expenses) + len(notes)
    print(f"\n{'='*60}")
    print(f"Total items managed: {total_items}")
    print(f"{'='*60}")


# ============================================
# PART 6: MAIN PROGRAM
# ============================================

def load_all_data():
    """Load all data from files - DEMONSTRATES: Functions calling functions"""
    print("\nLoading your data...")
    load_contacts()
    load_todos()
    load_expenses()
    load_notes()
    print("✅ All data loaded!\n")


def main_menu():
    """Main menu - DEMONSTRATES: While loops, Functions, Menu systems"""
    print("\nWelcome to your Personal Management System!")

    # Load all data at start
    load_all_data()

    while True:
        print("\n" + "="*60)
        print("                    MAIN MENU")
        print("="*60)
        print("1. 📱 Contact Manager")
        print("2. ✅ To-Do List")
        print("3. 💰 Expense Tracker")
        print("4. 📝 Notes & Diary")
        print("5. 📊 Dashboard")
        print("6. 🚪 Exit")
        print("="*60)

        choice = input("\nYour choice (1-6): ")

        if choice == "1":
            contact_manager()
        elif choice == "2":
            todo_manager()
        elif choice == "3":
            expense_tracker()
        elif choice == "4":
            notes_manager()
        elif choice == "5":
            show_dashboard()
        elif choice == "6":
            print("\n" + "="*60)
            print("Thank you for using Personal Management System!")
            print("All your data has been saved automatically.")
            print("="*60)
            break
        else:
            print("\n❌ Invalid choice! Please pick 1-6.")


# ============================================
# RUN THE PROGRAM
# ============================================

if 'name' == "main":
    main_menu()
