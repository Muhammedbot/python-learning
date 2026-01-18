# Day 22 - Datetime Module Complete

from datetime import datetime, timedelta, date
import time

print("="*70)
print("              DATETIME MASTERY - 5 PROJECTS")
print("="*70)

# ============================================
# PROJECT 1: TIME FORMATTER
# ============================================

def time_formatter():
    """Display current time in multiple formats"""
    print("\n" + "="*70)
    print("PROJECT 1: TIME FORMATTER")
    print("="*70)

    now = datetime.now()

    print("\nCurrent Date & Time in Different Formats:\n")

    print("1. Full:", now.strftime("%A, %B %d, %Y at %I:%M:%S %p"))
    print("2. Short:", now.strftime("%m/%d/%Y %H:%M"))
    print("3. Long:", now.strftime("%B %d, %Y"))
    print("4. ISO:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("5. Custom:", now.strftime("Today is %A, the %d of %B, %Y"))
    print("6. Time only:", now.strftime("%I:%M %p"))
    print("7. 24-hour:", now.strftime("%H:%M:%S"))

    print("\n" + "="*70)


# ============================================
# PROJECT 2: BIRTHDAY COUNTDOWN
# ============================================

def birthday_countdown():
    """Calculate days until next birthday"""
    print("\n" + "="*70)
    print("PROJECT 2: BIRTHDAY COUNTDOWN")
    print("="*70)

    print("\nEnter your birthday:")

    try:
        month = int(input("Month (1-12): "))
        day = int(input("Day (1-31): "))

        today = date.today()

        # Get next birthday
        birthday_this_year = date(today.year, month, day)

        if birthday_this_year < today:
            # Birthday already passed this year
            next_birthday = date(today.year + 1, month, day)
        else:
            next_birthday = birthday_this_year

        # Calculate days until birthday
        days_until = (next_birthday - today).days

        print("\n" + "-"*70)
        print(f"Your next birthday: {next_birthday.strftime('%A, %B %d, %Y')}")
        print(f"Days until birthday: {days_until} days")

        if days_until == 0:
            print("\n🎉🎂 HAPPY BIRTHDAY TODAY! 🎂🎉")
        elif days_until == 1:
            print("\n🎉 Your birthday is TOMORROW! 🎉")
        elif days_until <= 7:
            print(f"\n🎈 Your birthday is THIS WEEK! Only {days_until} days!")
        elif days_until <= 30:
            print(f"\n🎂 Your birthday is THIS MONTH! {days_until} days to go!")
        else:
            weeks = days_until // 7
            print(f"\n⏰ {days_until} days = {weeks} weeks until your birthday!")

        print("-"*70)

    except ValueError:
        print("❌ Invalid date! Please enter numbers.")
    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# PROJECT 3: AGE CALCULATOR
# ============================================

def age_calculator():
    """Calculate exact age"""
    print("\n" + "="*70)
    print("PROJECT 3: EXACT AGE CALCULATOR")
    print("="*70)

    print("\nEnter your birth date:")

    try:
        year = int(input("Year (e.g., 2000): "))
        month = int(input("Month (1-12): "))
        day = int(input("Day (1-31): "))

        birth_date = date(year, month, day)
        today = date.today()

        # Calculate age
        age_years = today.year - birth_date.year

        # Adjust if birthday hasn't occurred this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1

        # Calculate exact days lived
        days_lived = (today - birth_date).days

        # Calculate months
        age_months = (today.year - birth_date.year) * 12 + today.month - birth_date.month
        if today.day < birth_date.day:
            age_months -= 1

        # Next birthday
        next_birthday = date(today.year, birth_date.month, birth_date.day)
        if next_birthday < today:
            next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
        days_to_birthday = (next_birthday - today).days

        print("\n" + "-"*70)
        print("YOUR AGE BREAKDOWN:")
        print("-"*70)
        print(f"Birth Date: {birth_date.strftime('%A, %B %d, %Y')}")
        print(f"Today: {today.strftime('%A, %B %d, %Y')}")
        print()
        print(f"🎂 You are {age_years} years old")
        print(f"📅 Or {age_months} months old")
        print(f"⏰ Or {days_lived:,} days old")
        print(f"⏱️  Or {days_lived * 24:,} hours old")
        print(f"⚡ Or {days_lived * 24 * 60:,} minutes old")
        print()
        print(f"🎈 Next birthday in {days_to_birthday} days")
        print("-"*70)

    except ValueError:
        print("❌ Invalid date! Check your input.")
    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# PROJECT 4: CODING TIME TRACKER
# ============================================

def coding_tracker():
    """Track how long you've been coding"""
    print("\n" + "="*70)
    print("PROJECT 4: CODING TIME TRACKER")
    print("="*70)

    print("\nWhen did you start learning to code?")

    try:
        year = int(input("Year (e.g., 2026): "))
        month = int(input("Month (1-12): "))
        day = int(input("Day (1-31): "))

        start_date = date(year, month, day)
        today = date.today()

        # Calculate time coding
        days_coding = (today - start_date).days
        weeks_coding = days_coding // 7
        months_coding = (today.year - start_date.year) * 12 + today.month - start_date.month

        print("\n" + "-"*70)
        print("YOUR CODING JOURNEY:")
        print("-"*70)
        print(f"Start Date: {start_date.strftime('%B %d, %Y')}")
        print(f"Today: {today.strftime('%B %d, %Y')}")
        print()
        print(f"💻 You've been coding for {days_coding} days!")
        print(f"📅 That's {weeks_coding} weeks")
        print(f"📆 Or about {months_coding} months")
        print()

        # Milestones
        if days_coding >= 365:
            years = days_coding // 365
            print(f"🏆 MILESTONE: {years} year(s) of coding! 🎉")
        elif days_coding >= 100:
            print("🏆 MILESTONE: 100+ days of coding! 💪")
        elif days_coding >= 30:
            print("🏆 MILESTONE: 30+ days! Keep going! 🚀")
        elif days_coding >= 7:
            print("🏆 MILESTONE: First week complete! 🔥")
        else:
            print(f"🌟 Day {days_coding} of your journey! Keep building!")

        print()
        print(f"At 4 hours/day, you've invested ~{days_coding * 4:,} hours!")
        print("-"*70)

    except ValueError:
        print("❌ Invalid date!")
    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# PROJECT 5: EVENT COUNTDOWN
# ============================================

def event_countdown():
    """Countdown to any future event"""
    print("\n" + "="*70)
    print("PROJECT 5: EVENT COUNTDOWN")
    print("="*70)

    # Predefined events
    today = date.today()

    # New Year
    new_year = date(today.year + 1, 1, 1)
    days_to_ny = (new_year - today).days

    # Valentine's Day
    valentines = date(today.year, 2, 14)
    if valentines < today:
        valentines = date(today.year + 1, 2, 14)
    days_to_valentines = (valentines - today).days

    # Christmas
    christmas = date(today.year, 12, 25)
    if christmas < today:
        christmas = date(today.year + 1, 12, 25)
    days_to_christmas = (christmas - today).days

    print("\n🎯 UPCOMING EVENTS:")
    print("-"*70)
    print(f"🎆 New Year {new_year.year}: {days_to_ny} days")
    print(f"💝 Valentine's Day: {days_to_valentines} days")
    print(f"🎄 Christmas: {days_to_christmas} days")
    print()

    # Custom event
    print("Or create your own countdown:")
    event_name = input("Event name: ")

    try:
        year = int(input("Year: "))
        month = int(input("Month (1-12): "))
        day = int(input("Day (1-31): "))

        event_date = date(year, month, day)
        days_until = (event_date - today).days

        if days_until < 0:
            print(f"\n❌ {event_name} already happened {abs(days_until)} days ago!")
        elif days_until == 0:
            print(f"\n🎉 {event_name} is TODAY! 🎉")
        else:
            weeks = days_until // 7
            months = days_until // 30

            print("\n" + "-"*70)
            print(f"⏰ COUNTDOWN TO: {event_name}")
            print("-"*70)
            print(f"Date: {event_date.strftime('%A, %B %d, %Y')}")
            print(f"Days: {days_until}")
            print(f"Weeks: {weeks}")
            print(f"Months: ~{months}")
            print("-"*70)

    except ValueError:
        print("❌ Invalid date!")
    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# BONUS: TIME SINCE PYTHON WAS CREATED
# ============================================

def python_age():
    """How old is Python?"""
    print("\n" + "="*70)
    print("BONUS: HOW OLD IS PYTHON?")
    print("="*70)

    # Python was first released on February 20, 1991
    python_birth = date(1991, 2, 20)
    today = date.today()

    days = (today - python_birth).days
    years = days // 365

    print(f"\n🐍 Python was created on {python_birth.strftime('%B %d, %Y')}")
    print(f"📅 Python is {years} years old!")
    print(f"⏰ That's {days:,} days of Python!")
    print()


# ============================================
# MAIN MENU
# ============================================

while True:
    print("\n" + "="*70)
    print("                  DATETIME PROJECTS MENU")
    print("="*70)
    print("1. ⏰ Time Formatter (see current time in many formats)")
    print("2. 🎂 Birthday Countdown (days until your birthday)")
    print("3. 📅 Age Calculator (exact age in years, months, days)")
    print("4. 💻 Coding Tracker (how long you've been coding)")
    print("5. 🎯 Event Countdown (countdown to any event)")
    print("6. 🐍 Python's Age (bonus!)")
    print("7. 🚪 Exit")
    print("="*70)

    choice = input("\nYour choice (1-7): ")

    if choice == "1":
        time_formatter()

    elif choice == "2":
        birthday_countdown()

    elif choice == "3":
        age_calculator()

    elif choice == "4":
        coding_tracker()

    elif choice == "5":
        event_countdown()

    elif choice == "6":
        python_age()

    elif choice == "7":
        print("\n" + "="*70)
        print("Thanks for exploring datetime!")
        print("Time is precious - use it well! ⏰")
        print("="*70)
        break

    else:
        print("\n❌ Invalid choice! Pick 1-7")
