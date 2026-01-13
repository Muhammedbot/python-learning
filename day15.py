# Day 15 - Coordinate Distance Calculator

import math

print("===== COORDINATE DISTANCE CALCULATOR =====")

# Store points as tuples (x, y coordinates)
points = []

def add_point():
    """Add a coordinate point"""
    print("\n--- Add Point ---")
    x = float(input("X coordinate: "))
    y = float(input("Y coordinate: "))
    name = input("Point name (e.g., A, B, Home): ")

    # Store as tuple with name
    point = (name, x, y)
    points.append(point)
    print(f"✅ Point {name} ({x}, {y}) added!")


def view_points():
    """View all points"""
    if len(points) == 0:
        print("\nNo points yet!")
    else:
        print("\n===== ALL POINTS =====")
        for i, point in enumerate(points, 1):
            name, x, y = point  # Unpack tuple!
            print(f"{i}. {name}: ({x}, {y})")


def calculate_distance():
    """Calculate distance between two points"""
    if len(points) < 2:
        print("\nNeed at least 2 points!")
        return

    print("\n--- Your Points ---")
    for i, point in enumerate(points, 1):
        name, x, y = point
        print(f"{i}. {name}")

    try:
        p1 = int(input("\nFirst point number: ")) - 1
        p2 = int(input("Second point number: ")) - 1

        if 0 <= p1 < len(points) and 0 <= p2 < len(points):
            # Unpack coordinates
            name1, x1, y1 = points[p1]
            name2, x2, y2 = points[p2]

            # Distance formula: √[(x2-x1)² + (y2-y1)²]
            distance = math.sqrt((x2 - x1)2 + (y2 - y1)2)

            print(f"\n📏 Distance from {name1} to {name2}:")
            print(f"   {round(distance, 2)} units")
        else:
            print("Invalid point numbers!")
    except:
        print("Invalid input!")


def find_origin_distance():
    """Find distance of all points from origin (0,0)"""
    if len(points) == 0:
        print("\nNo points yet!")
        return

    print("\n===== DISTANCE FROM ORIGIN (0,0) =====")
    origin = (0, 0)

    for point in points:
        name, x, y = point
        distance = math.sqrt(x2 + y2)
        print(f"{name}: {round(distance, 2)} units")


def midpoint():
    """Find midpoint between two points"""
    if len(points) < 2:
        print("\nNeed at least 2 points!")
        return

    print("\n--- Your Points ---")
    for i, point in enumerate(points, 1):
        name, x, y = point
        print(f"{i}. {name}")

    try:
        p1 = int(input("\nFirst point: ")) - 1
        p2 = int(input("Second point: ")) - 1

        if 0 <= p1 < len(points) and 0 <= p2 < len(points):
            name1, x1, y1 = points[p1]
            name2, x2, y2 = points[p2]

            # Midpoint formula: ((x1+x2)/2, (y1+y2)/2)
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2

            print(f"\n📍 Midpoint between {name1} and {name2}:")
            print(f"   ({round(mid_x, 2)}, {round(mid_y, 2)})")
        else:
            print("Invalid point numbers!")
    except:
        print("Invalid input!")
