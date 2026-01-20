# Day 23 - File Operations & Automation

import os
import shutil
from datetime import datetime
from pathlib import Path

print("="*70)
print("           FILE ORGANIZER & AUTOMATION TOOL")
print("="*70)

# File type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
    'Presentations': ['.ppt', '.pptx', '.key', '.odp'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'],
    'Executables': ['.exe', '.msi', '.app', '.dmg', '.deb', '.rpm'],
    'Others': []  # Everything else
}


# ============================================
# PROJECT 1: FILE SCANNER
# ============================================

def scan_folder():
    """Scan and list all files in a folder"""
    print("\n" + "="*70)
    print("PROJECT 1: FILE SCANNER")
    print("="*70)

    folder_path = input("\nEnter folder path (or press Enter for current folder): ").strip()

    if not folder_path:
        folder_path = "."

    if not os.path.exists(folder_path):
        print(f"❌ Folder '{folder_path}' does not exist!")
        return

    print(f"\n📂 Scanning: {os.path.abspath(folder_path)}")
    print("-"*70)

    files = []
    folders = []

    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if os.path.isfile(item_path):
                files.append(item)
            elif os.path.isdir(item_path):
                folders.append(item)

        print(f"\n📁 Folders: {len(folders)}")
        if folders:
            for folder in folders[:10]:  # Show first 10
                print(f"   • {folder}")
            if len(folders) > 10:
                print(f"   ... and {len(folders) - 10} more")

        print(f"\n📄 Files: {len(files)}")
        if files:
            for file in files[:10]:  # Show first 10
                size = os.path.getsize(os.path.join(folder_path, file))
                size_mb = size / (1024 * 1024)
                print(f"   • {file} ({size_mb:.2f} MB)")
            if len(files) > 10:
                print(f"   ... and {len(files) - 10} more")

        print("-"*70)

    except PermissionError:
        print("❌ Permission denied! Cannot access this folder.")
    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# PROJECT 2: FILE TYPE ANALYZER
# ============================================

def analyze_file_types():
    """Analyze what types of files are in a folder"""
    print("\n" + "="*70)
    print("PROJECT 2: FILE TYPE ANALYZER")
    print("="*70)

    folder_path = input("\nEnter folder path (or press Enter for current): ").strip()

    if not folder_path:
        folder_path = "."

    if not os.path.exists(folder_path):
        print(f"❌ Folder does not exist!")
        return

    print(f"\n📊 Analyzing: {os.path.abspath(folder_path)}")
    print("-"*70)

    # Count files by category
    category_counts = {category: 0 for category in FILE_TYPES.keys()}
    total_files = 0

    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if os.path.isfile(item_path):
                total_files += 1
                file_ext = os.path.splitext(item)[1].lower()

                # Find category
                categorized = False
                for category, extensions in FILE_TYPES.items():
                    if file_ext in extensions:
                        category_counts[category] += 1
                        categorized = True
                        break

                if not categorized:
                    category_counts['Others'] += 1

        print(f"\n📈 ANALYSIS RESULTS:")
        print("-"*70)
        print(f"Total files: {total_files}\n")

        # Show results
        for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                percentage = (count / total_files) * 100
                bar = "█" * int(percentage / 5)
                print(f"{category:<15} {count:>4} files ({percentage:>5.1f}%) {bar}")

        print("-"*70)

    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# PROJECT 3: FILE ORGANIZER
# ============================================

def organize_files():
    """Organize files into folders by type"""
    print("\n" + "="*70)
    print("PROJECT 3: FILE ORGANIZER")
    print("="*70)

    folder_path = input("\nEnter folder path to organize: ").strip()

    if not folder_path:
        folder_path = "."

    if not os.path.exists(folder_path):
        print(f"❌ Folder does not exist!")
        return

    print(f"\n⚠️  WARNING: This will move files into organized folders!")
    print(f"📂 Target: {os.path.abspath(folder_path)}")
    confirm = input("\nContinue? (yes/no): ").lower()

    if confirm != "yes":
        print("❌ Cancelled!")
        return

    print("\n🔄 Organizing files...")
    print("-"*70)

    moved_count = 0

    try:
        # Get all files
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        for file in files:
            file_path = os.path.join(folder_path, file)
            file_ext = os.path.splitext(file)[1].lower()

            # Find category
            target_category = 'Others'
            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    target_category = category
                    break

            # Create category folder if doesn't exist
            category_folder = os.path.join(folder_path, target_category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
                print(f"✅ Created folder: {target_category}")

            # Move file
            destination = os.path.join(category_folder, file)

            # Handle duplicates
            if os.path.exists(destination):
                name, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination):
                    new_name = f"{name}_{counter}{ext}"
                    destination = os.path.join(category_folder, new_name)
                    counter += 1

            shutil.move(file_path, destination)
            moved_count += 1
            print(f"📁 Moved: {file} → {target_category}/")

        print("-"*70)
        print(f"✅ Successfully organized {moved_count} files!")
        print("-"*70)

    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# PROJECT 4: BULK FILE RENAMER
# ============================================

def bulk_rename():
    """Rename multiple files at once"""
    print("\n" + "="*70)
    print("PROJECT 4: BULK FILE RENAMER")
    print("="*70)

    folder_path = input("\nEnter folder path: ").strip()

    if not folder_path:
        folder_path = "."

    if not os.path.exists(folder_path):
        print(f"❌ Folder does not exist!")
        return

    # Show files
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("❌ No files in this folder!")
        return

    print(f"\n📄 Found {len(files)} files")
    for i, file in enumerate(files[:10], 1):
        print(f"   {i}. {file}")
    if len(files) > 10:
        print(f"   ... and {len(files) - 10} more")

    print("\nRename options:")
    print("1. Add prefix (e.g., 'IMG_' → IMG_file.jpg)")
    print("2. Add suffix (e.g., '_backup' → file_backup.jpg)")
    print("3. Sequential numbering (file_001.jpg, file_002.jpg...)")

    choice = input("\nChoice (1-3): ")

    if choice == "1":
        prefix = input("Enter prefix: ")

        confirm = input(f"\n⚠️  Rename {len(files)} files with prefix '{prefix}'? (yes/no): ").lower()
        if confirm != "yes":
            print("❌ Cancelled!")
            return

        renamed = 0
        for file in files:
            old_path = os.path.join(folder_path, file)
            new_name = prefix + file
            new_path = os.path.join(folder_path, new_name)

            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                renamed += 1

        print(f"✅ Renamed {renamed} files!")

    elif choice == "2":
        suffix = input("Enter suffix (before extension): ")

        confirm = input(f"\n⚠️  Rename {len(files)} files with suffix '{suffix}'? (yes/no): ").lower()
        if confirm != "yes":
            print("❌ Cancelled!")
            return

        renamed = 0
        for file in files:
            name, ext = os.path.splitext(file)
            new_name = f"{name}{suffix}{ext}"

            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)

            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                renamed += 1

        print(f"✅ Renamed {renamed} files!")

    elif choice == "3":
        base_name = input("Enter base name (e.g., 'photo'): ")

        confirm = input(f"\n⚠️  Rename {len(files)} files sequentially? (yes/no): ").lower()
        if confirm != "yes":
            print("❌ Cancelled!")
            return

        renamed = 0
        for i, file in enumerate(files, 1):
            ext = os.path.splitext(file)[1]
            new_name = f"{base_name}_{i:03d}{ext}"

            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)

            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                renamed += 1

        print(f"✅ Renamed {renamed} files!")


# ============================================
# PROJECT 5: FILE STATISTICS
# ============================================

def file_statistics():
    """Show detailed folder statistics"""
    print("\n" + "="*70)
    print("PROJECT 5: FILE STATISTICS")
    print("="*70)

    folder_path = input("\nEnter folder path: ").strip()

    if not folder_path:
        folder_path = "."

    if not os.path.exists(folder_path):
        print(f"❌ Folder does not exist!")
        return

    print(f"\n📊 Analyzing: {os.path.abspath(folder_path)}")
    print("-"*70)

    try:
        total_files = 0
        total_folders = 0
        total_size = 0
        largest_file = ("", 0)
        smallest_file = ("", float('inf'))

        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if os.path.isfile(item_path):
                total_files += 1
                size = os.path.getsize(item_path)
                total_size += size

                if size > largest_file[1]:
                    largest_file = (item, size)
                if size < smallest_file[1]:
                    smallest_file = (item, size)

            elif os.path.isdir(item_path):
                total_folders += 1

        # Convert sizes
        total_size_mb = total_size / (1024 * 1024)
        total_size_gb = total_size / (1024 * 1024 * 1024)

        print("\n📈 STATISTICS:")
        print("-"*70)
        print(f"Total Files: {total_files}")
        print(f"Total Folders: {total_folders}")
        print()
        print(f"Total Size: {total_size_mb:.2f} MB ({total_size_gb:.2f} GB)")

        if total_files > 0:
            avg_size = total_size / total_files
            avg_size_mb = avg_size / (1024 * 1024)
            print(f"Average File Size: {avg_size_mb:.2f} MB")
            print()
            print(f"Largest File: {largest_file[0]} ({largest_file[1] / (1024*1024):.2f} MB)")
            print(f"Smallest File: {smallest_file[0]} ({smallest_file[1] / 1024:.2f} KB)")

        print("-"*70)

    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# MAIN MENU
# ============================================

print("\n💡 TIP: This tool works best with a test folder!")
print("   Create a 'test_folder' with some files to practice safely.")

while True:
    print("\n" + "="*70)
    print("              FILE AUTOMATION MENU")
    print("="*70)
    print("1. 🔍 Scan Folder (list all files)")
    print("2. 📊 Analyze File Types (what's in the folder)")
    print("3. 📁 Organize Files (sort by type)")
    print("4. ✏️  Bulk Rename (rename many files at once)")
    print("5. 📈 File Statistics (sizes, counts, etc.)")
    print("6. 🚪 Exit")
    print("="*70)

    choice = input("\nYour choice (1-6): ")

    if choice == "1":
        scan_folder()

    elif choice == "2":
        analyze_file_types()

    elif choice == "3":
        organize_files()

    elif choice == "4":
        bulk_rename()

    elif choice == "5":
        file_statistics()

    elif choice == "6":
        print("\n" + "="*70)
        print("Thanks for using File Automation Tool!")
        print("Automate the boring stuff! 🚀")
        print("="*70)
        break

    else:
        print("\n❌ Invalid choice! Pick 1-6")
