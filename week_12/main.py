"""
main.py
Week 12 - Tutorial 12: Computer Lab Monitoring System

Uses:
- for loop   -> to check a fixed number of computers (inside lab_monitor.py)
- while loop -> to repeat the monitoring process until the technician stops
- functions  -> each responsibility is separated into its own function
- modules    -> lab_monitor.py holds the core logic, main.py drives the program
"""

from lab_monitor import check_computers, count_available, display_status


def main():
    monitoring = True

    while monitoring:
        computers = check_computers()
        available = count_available(computers)
        display_status(computers, available)

        choice = input("\nPerform another monitoring cycle? (Y/N): ").strip().upper()
        if choice != "Y":
            monitoring = False
            print("\nMonitoring stopped by technician. Goodbye!")


if __name__ == "__main__":
    main()