# Day 27 - Email Automation System

from datetime import datetime

print("="*60)
print("        EMAIL AUTOMATION SYSTEM")
print("="*60)

# ============================================
# EMAIL FUNCTIONS
# ============================================

def send_email(to, subject, message):
    """Send an email (simulated)"""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create email object
    email = {
        'to': to,
        'subject': subject,
        'message': message,
        'timestamp': timestamp,
        'status': 'sent'
    }

    # Display it
    print("\n" + "="*60)
    print("📧 EMAIL SENT!")
    print("="*60)
    print(f"To: {email['to']}")
    print(f"Subject: {email['subject']}")
    print(f"Time: {email['timestamp']}")
    print("-"*60)
    print(f"Message:\n{email['message']}")
    print("="*60)

    # Save to file
    save_to_sent(email)

    return True


def save_to_sent(email):
    """Save email to sent items"""

    with open("sent_emails.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{'='*60}\n")
        file.write(f"To: {email['to']}\n")
        file.write(f"Subject: {email['subject']}\n")
        file.write(f"Time: {email['timestamp']}\n")
        file.write(f"Status: {email['status']}\n")
        file.write(f"Message:\n{email['message']}\n")


def send_welcome_email(name, email):
    """Send welcome email to new user"""

    subject = f"Welcome {name}!"

    message = f"""
Hello {name}!

Welcome to our service! We're excited to have you on board.

Your account has been created successfully.

If you have any questions, feel free to reply to this email.

Best regards,
The Team
    """

    return send_email(email, subject, message)


def send_reminder_email(email, task, due_date):
    """Send task reminder email"""

    subject = f"Reminder: {task}"

    message = f"""
Hi there!

This is a reminder about your task:

Task: {task}
Due Date: {due_date}

Don't forget to complete it on time!

Best regards,
Task Manager
    """

    return send_email(email, subject, message)


def send_report_email(email, data):
    """Send daily report email"""

    subject = "Daily Report"

    message = f"""
Daily Activity Report

Date: {datetime.now().strftime("%Y-%m-%d")}

Summary:
{data}

This is an automated report.
    """

    return send_email(email, subject, message)


def send_bulk_email(recipients, subject, message):
    """Send email to multiple people"""

    print(f"\n📨 Sending to {len(recipients)} recipients...")

    sent_count = 0

    for recipient in recipients:
        success = send_email(recipient, subject, message)
        if success:
            sent_count += 1

    print(f"\n✅ Sent to {sent_count}/{len(recipients)} recipients!")


# ============================================
# MENU SYSTEM
# ============================================

def show_menu():
    """Display email automation menu"""

    while True:
        print("\n" + "="*60)
        print("        EMAIL AUTOMATION MENU")
        print("="*60)
        print("1. Send Simple Email")
        print("2. Send Welcome Email")
        print("3. Send Reminder Email")
        print("4. Send Report Email")
        print("5. Send Bulk Email")
        print("6. View Sent Emails")
        print("7. Exit")
        print("="*60)

        choice = input("Choose (1-7): ")

        if choice == "1":
            # Simple email
            to = input("To: ")
            subject = input("Subject: ")
            message = input("Message: ")
            send_email(to, subject, message)

        elif choice == "2":
            # Welcome email
            name = input("User name: ")
            email = input("User email: ")
            send_welcome_email(name, email)

        elif choice == "3":
            # Reminder email
            email = input("Email: ")
            task = input("Task: ")
            due_date = input("Due date: ")
            send_reminder_email(email, task, due_date)

        elif choice == "4":
            # Report email
            email = input("Email: ")
            data = input("Report data: ")
            send_report_email(email, data)

        elif choice == "5":
            # Bulk email
            print("\nEnter recipients (one per line, 'done' to finish):")
            recipients = []
            while True:
                email = input("Email: ")
                if email.lower() == 'done':
                    break
                recipients.append(email)

            subject = input("Subject: ")
            message = input("Message: ")

            send_bulk_email(recipients, subject, message)

        elif choice == "6":
            # View sent emails
            try:
                with open("sent_emails.txt", "r", encoding="utf-8") as file:
                    print("\n" + "="*60)
                    print("        SENT EMAILS")
                    print("="*60)
                    print(file.read())
            except FileNotFoundError:
                print("\n📭 No emails sent yet!")

        elif choice == "7":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice!")


# ============================================
# RUN THE PROGRAM
# ============================================

print("\n🚀 Email Automation System Ready!")
print("💡 This is a simulator - no real emails are sent")
print("📁 All emails are saved to sent_emails.txt\n")

show_menu()



# Email templates
TEMPLATES = {
    'birthday': """
Happy Birthday {name}! 🎉

Wishing you an amazing day filled with joy and happiness!

Best wishes,
Your Friends
    """,

    'invoice': """
Invoice for {name}

Amount Due: ${amount}
Due Date: {due_date}

Please pay by the due date.

Thank you!
    """,

    'meeting': """
Meeting Reminder

Hi {name},

This is a reminder about our meeting:
Date: {date}
Time: {time}
Location: {location}

See you there!
    """
}

def send_from_template(template_name, email, **kwargs):
    """Send email using a template"""

    if template_name not in TEMPLATES:
        print("❌ Template not found!")
        return

    message = TEMPLATES[template_name].format(**kwargs)
    subject = f"{template_name.title()} Notification"

    return send_email(email, subject, message)

# Use it
send_from_template(
    'birthday',
    'friend@email.com',
    name='Ahmed'
)
