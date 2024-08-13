# URL Shortener API

The URL Shortener API is a simple web service that allows users to shorten long URLs into compact, easy-to-share links. The API provides endpoints to generate a shortened URL and retrieve the original URL using the shortened version.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [Running the Project Locally](#running-the-project-locally)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Shorten a long URL into a compact version.
- Redirect to the original URL using the shortened code.

## Project Structure

```
url-shortener/
│
├── alembic/                # Directory for Alembic migrations
│   ├── versions/           # Migration scripts
│   └── env.py              # Alembic environment configuration
│
├── app/                    # Main application directory
│   ├── __init__.py
│   ├── main.py             # Entry point for FastAPI application
│   ├── models.py           # SQLAlchemy models
│   ├── database.py         # Database connection and session management
│   ├── crud.py             # Database interaction logic
│   └── schemas.py          # Pydantic models for request and response bodies
│
├── .env                    # Environment variables (not included in version control)
├── .gitignore              # Git ignore rules
├── alembic.ini             # Alembic configuration file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Tech Stack

- Backend: FastAPI
- Database: PostgreSQL
- Migrations: Alembic
- Environment Management: python-dotenv
- ORM: SQLAlchemy
- ASGI server: Uvicorn

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL
- Git

### Clone the Repository

```bash
git clone https://github.com/kumarshivesh/url-shortener.git
cd url-shortener
```

### Create and Activate a Virtual Environment

```
python -m venv .venv
source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
```

### Install Dependencies

```
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in the root directory of the project and add the following variables:

```
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/url_shortener
```
Replace <username> and <password> with your PostgreSQL credentials.

## Database Setup

### 1. Create the Database:
Log in to your PostgreSQL shell and create a new database:
```
CREATE DATABASE url_shortener;
```

### 2. Run Migrations:
Apply the database migrations using Alembic:
```
alembic upgrade head
```


## Running the Project Locally


#### Run the FastAPI Application

```
uvicorn app.main:app --reload
```

The application will be running at http://localhost:8000.


## API Endpoints

### 1. Test the POST /shorten Endpoint
Purpose:
This endpoint accepts a long URL and returns a shortened URL.

Steps in Postman:

1. Open Postman and create a new POST request.

2. Enter the URL:
http://localhost:8000/shorten

3. Set the Request Body:

- Switch to the Body tab.
- Select raw and set the type to JSON.
- Enter the JSON payload with the URL you want to shorten. For example:
```
{
  "long_url": "https://www.example.com"
}
```
4. Send the Request:

- Click the Send button.
- You should receive a response containing the shortened URL, something like:
```
{
  "id": 1,
  "long_url": "https://www.example.com",
  "short_code": "abc123"
}
```

### 2. Test the GET /{short_code} Endpoint
Purpose:
This endpoint takes the short_code and redirects the user to the original long URL.

Steps in Postman:

1. Open Postman and create a new GET request.

2. Enter the URL:

Use the short_code returned from the previous POST request. For example:
```
http://localhost:8000/abc123
```
Replace abc123 with the actual short_code you received.

3. Send the Request:

- Click the Send button.

- Response: Redirects to the long URL in web browser. If using Postman, you may see the HTML content of the original page.


## License

This project is licensed under the MIT License. 



