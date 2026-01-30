# Junior Backend Developer Interview Assessment

A comprehensive, practical interview kit for assessing junior backend developers. Tests real-world skills through debugging, business logic implementation, and API development.

## 🎯 Purpose

This repository contains a complete interview simulation for junior backend developer roles. It assesses:
- Debugging existing code
- Implementing business logic from specifications
- Database modeling and migrations
- REST API development with FastAPI
- Working with databases (SQLAlchemy, PostgreSQL)

## 📁 Repository Structure

```
FastAPI-Junior-Interview/
├── main.py                 # FastAPI application with sample endpoints
├── tasks.py                # Debugging and business logic tasks
├── models.py               # Database models (partial - Category missing)
├── config.py               # App settings from .env
├── database.py             # Database configuration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables template
└── test-data.sql           # Sample data for testing
```

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/einar1991/FastAPI-Junior-Interview
cd FastAPI-Junior-Interview
```

### 2. Create Virtual Environment
```bash
python -m venv .venv

# Activate on Windows:
.venv\Scripts\activate

# Activate on macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. Create a PostgreSQL database
2. Edit `.env` with your database credentials:
   ```
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=postgres
    DB_PASS=postgres
    DB_NAME=online_shop_db
   ```
3. Execute the test-data.sql script to fill the database.
   ```bash
   psql -U postgres -d online_shop_db -f test-data.sql
   ```
Or use your preferred PostgreSQL client to run the SQL file.

### 5. Run the Application
```bash
# Option 1: Using main.py
python main.py

# Option 2: Using uvicorn directly
uvicorn main:app --reload --port 8080
```

The API will be available at `http://localhost:8080`
Documentation (Swagger UI): `http://localhost:8080/docs`

## 📋 Interview Structure

### Part 1: Debugging & Business Logic (tasks.py)
1. **Debugging Task**: Fix `find_user_by_email` function
2. **Business Logic**: Implement `UserActionHistory` class methods

### Part 2: Backend Development (main.py)
1. **Database Modeling**: Add missing `Category` model
2. **API Endpoint 1**: Implement `GET /products` with JOIN and pagination
3. **API Endpoint 2**: Implement `POST /orders` with stock validation

## 🧪 Testing Your Solution

1. Run the application
2. Open Swagger UI at `http://localhost:8080/docs`
3. Test your endpoints interactively
4. Verify database changes via your preferred PostgreSQL client

## 📝 Interview Questions

Theoretical questions and timing guidelines are available in the `solutions` branch:
```bash
git checkout solutions
```
Or view directly on GitHub: [Questions and Assessment Guide](https://github.com/einar1991/FastAPI-Junior-Interview/blob/solutions/README.md)

## 🔧 Troubleshooting

### Common Issues:
1. **Database connection errors**: Verify `.env` credentials and that PostgreSQL is running
2. **Import errors**: Ensure virtual environment is activated and dependencies installed
3. **Port already in use**: Change port in `main.py` or use `--port` flag with uvicorn


## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 🤝 Contributing

Found an issue or have suggestions? Please open an Issue or Pull Request.

## 📄 [License](https://github.com/einar1991/FastAPI-Junior-Interview/blob/main/LICENSE)


---

## 💡 Tips for Candidates

- Read the existing code carefully - it contains patterns to follow
- Test your endpoints using Swagger UI
- Consider edge cases and error handling
- Ask clarifying questions if requirements are unclear
