1. Purpose of the Application

As part of the IT Support team at City University Malaysia, students frequently report technical issues such as LMS login problems, WiFi connectivity issues, printer malfunctions, and password reset requests. Before a technician can investigate any issue, a helpdesk ticket must first be created.

This application is a simple Ticket Registration System that allows a student to submit an IT support ticket. The system captures the student's details and the issue description, lets the student select a priority level, automatically assigns a technician based on that priority, and then displays a formatted ticket summary.

2. Tech Stack
Language: Python 3
Structure: Modular Python programming (separate files for logic and presentation)
Modules:
main.py – Entry point of the program; coordinates ticket creation and display.
ticket.py – Contains create_ticket(), which collects user input and builds the ticket record, including automatic technician assignment.
display.py – Contains display_ticket(), which formats and prints the ticket summary to the console.
No external libraries are required; only Python's built-in input() and print() functions are used.
3. How to Use
Make sure Python 3 is installed on your machine.
Clone/download the week_9 directory containing main.py, ticket.py, display.py, and this README.md.
Open a terminal and navigate into the week_9 directory:
   cd week_9
Run the program:
   python3 main.py
When prompted, enter the following details:
Student Name
Student ID
Issue description
Location
Priority level (High, Medium, or Low)
The program will automatically assign a technician based on the priority level:
High → Ahmad
Medium → Siti
Low → Ali
A formatted helpdesk ticket summary will be displayed, showing the ticket status as Pending.
Example Run
=== IT Helpdesk Ticket ===
Student Name : izzad
Student ID  : 12345678910
Issue        : blue screen pc
Location    : lab 101 level 1
Priority (High/Medium/Low): High

========== HELPDESK TICKET ==========
Student Name : izzad
Student ID   : 12345678910
Issue        : blue screen pc
Location     : lab 101 level 1
Priority     : High
Technician   : Ahmad
Status       : Pending
======================================
4. Demonstration

Record a short screen recording (video or GIF) showing:

Running python3 main.py
Entering sample ticket details
The final formatted ticket output

Attach or link the recording here once completed.