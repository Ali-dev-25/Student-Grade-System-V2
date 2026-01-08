# Student Grade System 

A Desktop Application to manage student grades, calculate averages, and export reports to Excel. Built with **Python** & **Flet** using a **Layered Architecture**.

## Features
- **Add Students:** With real-time validation for IDs and phone numbers.
- **View Grades:** Auto-calculates GPA and grade status (Excellent, Good, etc.).
- **Excel Export:** Generates formatted Excel reports with one click.
- **Data Safety:** Prevents duplicate IDs and invalid grades.

## Project Structure
```text
Student-Grade-System-V2/
│
├── .github/                        # GitHub Actions & CI/CD
│   └── workflows/
│       └── python-app.yml          # CI Pipeline configuration (Automated Tests)
│
├── src/                            # Application Source Code
│   ├── __init__.py                 # Package initializer
│   │
│   ├── database/                   # Database Layer
│   │   ├── __init__.py
│   │   └── db_manager.py           # Connection management, Tables & Constraints
│   │
│   ├── models/                     # Data Models Layer
│   │   ├── __init__.py
│   │   └── student.py              # Student Data Class + Validation Logic
│   │
│   ├── services/                   # Service Layer (Business Logic)
│   │   ├── __init__.py
│   │   └── student_service.py      # Core logic: Add, Fetch, & Excel Export
│   │
│   └── ui/                         # User Interface Layer
│       ├── __init__.py
│       └── main_window.py          # Main GUI, Widgets & Event Handling
│
├── tests/                          # Unit Tests (15 Tests)
│   ├── __init__.py
│   ├── test_models.py              # Tests for Data Validation & Rules
│   ├── test_service.py             # Tests for Database Operations & Constraints
│   └── test_export.py              # Tests for Excel File Generation
│
├── main.py                         # Application Entry Point
├── requirements.txt                # Dependencies (flet, openpyxl, pytest)
├── README.md                       # Project Documentation & Diagrams
├── TECHNICAL_DECISIONS.md          # Architectural & Technical Decisions
└── .gitignore                      # Files to ignore (e.g __pycache__)

## Installation and Usage
   git clone https://github.com/YourUsername/Student-Grade-System-V2.git
cd Student-Grade-System-V2

## How to Run

1- install Requirements
   pip install -r requirements.txt

2- Run the App
    python main.py

## How to Test
- to run the 15 automated tests:
    pytest

## Aouther
   Ali AL-Hatami

```markdown
## Database Diagram

```mermaid
erDiagram
    STUDENTS {
        string std_id PK "7 digits, Unique"
        string name "Not Null"
        string email
        string phone "9 digits"
        int web_design "0-100"
        int info_sec "0-100"
        int comm_tech "0-100"
        int data_struct "0-100"
        int wireless_net "0-100"
        int comm_skill "0-100"
    }
