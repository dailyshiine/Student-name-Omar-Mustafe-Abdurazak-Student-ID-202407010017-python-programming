"""
lab_monitor.py
Module for the Computer Lab Monitoring System (Week 12 - Tutorial 12)

Responsibilities:
- check_computers()  -> collect the status of every computer in the lab
- count_available()  -> count how many computers are marked as Available
- display_status()   -> print a formatted lab status report
"""


def check_computers():
    """Prompt the user to classify each of the 5 computers, return the list."""
    computers = []  # initial value

    # iterate & check for 5 computers
    for number in range(1, 6):
        status = input(f"Computer {number} Status (A/U/M): ").strip().upper()

        # prompt the user to classify each computer to either
        # A - Available, U - Used, M - Maintenance
        while status not in ("A", "U", "M"):
            print("Invalid input. Please enter A, U, or M.")
            status = input(f"Computer {number} Status (A/U/M): ").strip().upper()

        computers.append(status)

    return computers


def count_available(computers):
    """Count how many computers in the list are marked 'A' (Available)."""
    available = 0  # initial value

    for status in computers:
        if status == "A":
            available += 1

    return available


def display_status(computers, available):
    """Print a formatted lab status report."""
    print("\n========== LAB STATUS ==========")

    for number in range(len(computers)):
        print(f"Computer {number + 1}: {computers[number]}")

    print("---------------------------------")
    print(f"Available Computers: {available}")
    print("=================================")