# Technical Decisions Documentation

## 1. Architecture Pattern: Layered Architecture
I chose to separate the application into 4 distinct layers:
- **UI Layer (Flet):** Handles user interaction only. No logic allowed here.
- **Service Layer:** Contains business logic and acts as a bridge.
- **Model Layer:** Enforces data validation (Data Integrity).
- **Database Layer:** Manages connections and raw SQL queries.

**Reason:** This ensures "Separation of Concerns", making the code testable, maintainable, and scalable.

## 2. GUI Framework: Flet
**Reason:** Flet allows building modern, responsive UIs using Python without needing frontend languages (HTML/CSS/JS). It is fast for prototyping and supports hot-reload.

## 3. Database: SQLite
**Reason:** Since this is a local desktop application, SQLite is the best choice because it requires no server setup (Serverless) and is built into Python.

## 4. Testing: Pytest
**Reason:** Pytest provides a simple syntax for writing tests and powerful features like `fixtures` (which I used for in-memory database testing) and helpful error reporting.