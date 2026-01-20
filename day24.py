# Day 24 - Scheduled Tasks & Automation

import time
from datetime import datetime, timedelta
import threading

print("="*70)
print("         SCHEDULED TASKS - AUTOMATION ON AUTOPILOT")
print("="*70)


# ============================================
# PROJECT 1: COUNTDOWN TIMER
# ============================================

def countdown_timer():
    """Execute code after a delay"""
    print("\n" + "="*70)
    print("PROJECT 1: COUNTDOWN TIMER")
    print("="*70)

    try:
        seconds = int(input("\nRun task after how many seconds? "))

        print(f"\n⏳ Task scheduled to run in {seconds} seconds...")
        print("Waiting...")

        # Wait
        time.sleep(seconds)

        # Execute task
        print("\n" + "="*70)
        print("🔔 DING! TIME'S UP!")
        print("="*70)
        print("✅ Task executed!")
        print(f"⏰ Executed at: {datetime.now().strftime('%I:%M:%S %p')}")

    except ValueError:
        print("❌ Please enter a valid number!")


# ============================================
# PROJECT 2: INTERVAL REPEATER
# ============================================

def interval_repeater():
    """Repeat task every X seconds"""
    print("\n" + "="*70)
    print("PROJECT 2: INTERVAL REPEATER")
    print("="*70)

    try:
        interval = int(input("\nRepeat every how many seconds? "))
        times = int(input("How many times? "))

        print(f"\n⏰ Task will run {times} times, every {interval} seconds")
        print("Press Ctrl+C to stop early")
        print("-"*70)

        for i in range(1, times + 1):
            # Execute task
            current_time = datetime.now().strftime('%I:%M:%S %p')
            print(f"\n🔔 Run #{i}/{times} at {current_time}")
            print(f"✅ Task executed successfully!")

            # Wait before next run (except after last run)
            if i < times:
                print(f"⏳ Waiting {interval} seconds until next run...")
                time.sleep(interval)

        print("\n" + "="*70)
        print(f"✅ All {times} tasks completed!")
        print("="*70)

    except ValueError:
        print("❌ Please enter valid numbers!")
    except KeyboardInterrupt:
        print("\n\n⏹️ Stopped by user!")


# ============================================
# PROJECT 3: SPECIFIC TIME SCHEDULER
# ============================================

def specific_time_scheduler():
    """Run task at specific time"""
    print("\n" + "="*70)
    print("PROJECT 3: SPECIFIC TIME SCHEDULER")
    print("="*70)

    print(f"\n⏰ Current time: {datetime.now().strftime('%I:%M:%S %p')}")
    print("\nSchedule a task to run at a specific time:")

    try:
        hour = int(input("Hour (0-23, e.g., 14 for 2 PM): "))
        minute = int(input("Minute (0-59): "))

        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            print("❌ Invalid time!")
            return

        # Calculate target time
        now = datetime.now()
        target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        # If time already passed today, schedule for tomorrow
        if target_time <= now:
            target_time += timedelta(days=1)

        # Calculate wait time
        wait_seconds = (target_time - now).total_seconds()
        wait_minutes = wait_seconds / 60
        wait_hours = wait_minutes / 60

        print(f"\n✅ Task scheduled for: {target_time.strftime('%I:%M %p on %A, %B %d')}")
        print(f"⏳ Wait time: {int(wait_hours)}h {int(wait_minutes % 60)}m {int(wait_seconds % 60)}s")

        # For demo, let's just wait 5 seconds instead of real time
        print("\n💡 DEMO MODE: Waiting 5 seconds instead of real time...")
        time.sleep(5)

        print("\n" + "="*70)
        print("🔔 SCHEDULED TASK RUNNING!")
        print("="*70)
        print(f"⏰ Executed at: {datetime.now().strftime('%I:%M:%S %p')}")
        print("✅ Task completed!")

    except ValueError:
        print("❌ Please enter valid numbers!")


# ============================================
# PROJECT 4: POMODORO TIMER
# ============================================

def pomodoro_timer():
    """Work/break reminder (25 min work, 5 min break)"""
    print("\n" + "="*70)
    print("PROJECT 4: POMODORO TIMER")
    print("="*70)

    print("\n🍅 Pomodoro Technique:")
    print("   • Work for 25 minutes")
    print("   • Break for 5 minutes")
    print("   • Repeat!")

    try:
        sessions = int(input("\nHow many pomodoro sessions? "))

        # For demo: 1 second = 1 minute
        work_time = 5  # 5 seconds = demo of 25 minutes
        break_time = 2  # 2 seconds = demo of 5 minutes

        print(f"\n✅ Starting {sessions} pomodoro sessions!")
        print("💡 DEMO MODE: Using shorter times for testing")
        print(f"   Work time: {work_time} seconds (represents 25 min)")
        print(f"   Break time: {break_time} seconds (represents 5 min)")
        print("-"*70)

        for i in range(1, sessions + 1):
            # Work session
            print(f"\n🔔 POMODORO #{i}/{sessions}")
            print("💼 WORK TIME! Focus on your task!")
            print(f"⏰ Started: {datetime.now().strftime('%I:%M:%S %p')}")

            time.sleep(work_time)

            print(f"✅ Work session complete!")

            # Break (except after last session)
            if i < sessions:
                print(f"\n☕ BREAK TIME! Rest for {break_time} seconds...")
                time.sleep(break_time)
                print("✅ Break complete! Ready for next session!")

        print("\n" + "="*70)
        print(f"🎉 ALL {sessions} POMODORO SESSIONS COMPLETE!")
        print("Great work! 💪")
        print("="*70)

    except ValueError:
        print("❌ Please enter a valid number!")
    except KeyboardInterrupt:
        print("\n\n⏹️ Pomodoro stopped!")


# ============================================
# PROJECT 5: DAILY TASKS SCHEDULER
# ============================================

def daily_tasks_scheduler():
    """Schedule multiple daily tasks"""
    print("\n" + "="*70)
    print("PROJECT 5: DAILY TASKS SCHEDULER")
    print("="*70)

    print("\n📅 Schedule your daily tasks!")

    tasks = []

    while True:
        print("\n" + "-"*70)
        task_name = input("Task name (or 'done' to finish): ")

        if task_name.lower() == 'done':
            break

        try:
            hour = int(input("Hour (0-23): "))
            minute = int(input("Minute (0-59): "))

            if 0 <= hour <= 23 and 0 <= minute <= 59:
                tasks.append({
                    'name': task_name,
                    'hour': hour,
                    'minute': minute,
                    'time_str': f"{hour:02d}:{minute:02d}"
                })
                print(f"✅ Added: {task_name} at {hour:02d}:{minute:02d}")
            else:
                print("❌ Invalid time!")

        except ValueError:
            print("❌ Invalid input!")

    if not tasks:
        print("\n❌ No tasks scheduled!")
        return

    # Sort tasks by time
    tasks.sort(key=lambda x: (x['hour'], x['minute']))

    # Display schedule
    print("\n" + "="*70)
    print("YOUR DAILY SCHEDULE:")
    print("="*70)

    for i, task in enumerate(tasks, 1):
        time_12h = datetime.strptime(task['time_str'], '%H:%M').strftime('%I:%M %p')
        print(f"{i}. {time_12h} - {task['name']}")

    print("="*70)

    # Save to file
    try:
        with open("daily_schedule.txt", "w") as file:
            file.write("DAILY TASK SCHEDULE\n")
            file.write("="*70 + "\n\n")

            for task in tasks:
                time_12h = datetime.strptime(task['time_str'], '%H:%M').strftime('%I:%M %p')
                file.write(f"{time_12h} - {task['name']}\n")

        print("\n✅ Schedule saved to: daily_schedule.txt")
        print("💡 You can use this schedule to set up real automated tasks!")

    except Exception as e:
        print(f"❌ Error saving schedule: {e}")


# ============================================
# PROJECT 6: WATER REMINDER
# ============================================

def water_reminder():
    """Remind to drink water every X minutes"""
    print("\n" + "="*70)
    print("PROJECT 6: WATER REMINDER")
    print("="*70)

    print("\n💧 Stay hydrated! Set up water drinking reminders.")

    try:
        interval_minutes = int(input("Remind every how many minutes? "))
        total_reminders = int(input("How many reminders? "))

        # For demo: use seconds instead of minutes
        interval_seconds = 3  # Demo: 3 seconds instead of actual minutes

        print(f"\n✅ Water reminder set!")
        print(f"💡 DEMO MODE: Reminding every {interval_seconds} seconds")
        print(f"   (In real use: every {interval_minutes} minutes)")
        print(f"🔔 Will remind {total_reminders} times")
        print("-"*70)

        for i in range(1, total_reminders + 1):
            print(f"\n💧 REMINDER #{i}/{total_reminders}")
            print("="*70)
            print("🚰 TIME TO DRINK WATER!")
            print("💪 Stay hydrated, stay healthy!")
            print(f"⏰ {datetime.now().strftime('%I:%M:%S %p')}")
            print("="*70)

            if i < total_reminders:
                print(f"\n⏳ Next reminder in {interval_seconds} seconds...")
                time.sleep(interval_seconds)

        print("\n✅ All reminders complete!")
        print("💧 Great job staying hydrated! 💪")

    except ValueError:
        print("❌ Please enter valid numbers!")
    except KeyboardInterrupt:
        print("\n\n⏹️ Reminders stopped!")


# ============================================
# BONUS: TASK HISTORY TRACKER
# ============================================

def log_task(task_name):
    """Log completed tasks with timestamp"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open("task_history.txt", "a") as file:
        file.write(f"{timestamp} - {task_name}\n")


def view_task_history():
    """View all completed tasks"""
    print("\n" + "="*70)
    print("TASK HISTORY")
    print("="*70)

    try:
        with open("task_history.txt", "r") as file:
            history = file.read()

        if history:
            print(history)
        else:
            print("No task history yet!")

    except FileNotFoundError:
        print("No task history yet!")


# ============================================
# MAIN MENU
# ============================================

while True:
    print("\n" + "="*70)
    print("              SCHEDULED TASKS MENU")
    print("="*70)
    print("1. ⏱️  Countdown Timer (run after X seconds)")
    print("2. 🔁 Interval Repeater (run every X seconds)")
    print("3. ⏰ Specific Time Scheduler (run at exact time)")
    print("4. 🍅 Pomodoro Timer (work/break cycles)")
    print("5. 📅 Daily Tasks Scheduler (plan your day)")
    print("6. 💧 Water Reminder (hydration alerts)")
    print("7. 📜 View Task History")
    print("8. 🚪 Exit")
    print("="*70)

    choice = input("\nYour choice (1-8): ")

    if choice == "1":
        countdown_timer()

    elif choice == "2":
        interval_repeater()

    elif choice == "3":
        specific_time_scheduler()

    elif choice == "4":
        pomodoro_timer()

    elif choice == "5":
        daily_tasks_scheduler()

    elif choice == "6":
        water_reminder()

    elif choice == "7":
        view_task_history()

    elif choice == "8":
        print("\n" + "="*70)
        print("Thanks for using Task Scheduler!")
        print("Automate everything! 🚀")
        print("="*70)
        break

    else:
        print("\n❌ Invalid choice! Pick 1-8")
