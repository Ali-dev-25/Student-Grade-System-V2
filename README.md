# Student Grade System V2

A robust Desktop Application built with **Python** and **Flet** to manage student records, calculate GPAs, and generate Excel reports. This project is engineered using **Layered Architecture** to ensure clean code, scalability, and data integrity.

---

## Key Features
### 1. Robust Architecture
The project follows a strict **Layered Architecture** (Separation of Concerns):
- **UI Layer:** Handles user interaction (Flet).
- **Service Layer:** Bridges the UI and Database, handling business logic.
- **Model Layer:** Enforces data validation rules.
- **Database Layer:** Manages SQLite connections securely using Context Managers.

### 2. Data Integrity & Validation
- **Real-time Validation:** Prevents invalid inputs before they reach the database.
- **Constraints:**
  - Student ID & Phone must be exactly **9 digits**.
  - Grades must be between **0 and 100**.
  - Prevents duplicate Student IDs.

### 3. Professional Excel Export
- Generates formatted `.xlsx` reports using `openpyxl`.
- **Auto-fit Columns:** Automatically adjusts column width based on content.
- Opens the file automatically after export.



### 4. Automated Testing (CI/CD)
- **15 Unit Tests** covering Models, Services, and Export logic using `pytest`.
- **GitHub Actions:** Automatically runs tests on every push to ensure code stability.

---

## Project Structure
```
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
```

## Installation and Usage
   git clone https://github.com/YourUsername/Student-Grade-System-V2.git
cd Student-Grade-System-V2

## Install Dependencies
1- install Requirements
   pip install -r requirements.txt

## Run the Application
2- Run the App
    python main.py

## How to Test
- to run the 15 automated tests:
    pytest
```
 Expected Output
       tests/test_modles.py .....  [33%]
tests/test_service.py ..... [66%]
tests/test_export.py .....  [100%]
================= 15 passed in 0.xxs =================
```

## Database Diagram
```
- just one table in the System
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
```
### CI/CD (GitHub Actions)
- This repository is configured with GitHub Actions. Every push to the main branch automatically runs the test suite to ensure no regressions are introduced.

## Auther
- Ali AL-Hatami
  Software Engineering Student | Python Developer

GitHub: Ali-dev-25
Project Type: Technical Assessment


