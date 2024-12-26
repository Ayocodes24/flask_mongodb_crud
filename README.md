# Flask MongoDB CRUD Application

A simple CRUD (Create, Read, Update, Delete) application using Flask and MongoDB. This application provides user authentication using JWT and integrates with Postman for API testing.

## Prerequisites

- Docker
- Docker Compose
- Postman

## Project Structure
.
├── app.py                 # Main application file
├── config.py              # Configuration settings
├── Dockerfile             # Docker image configuration
├── docker-compose.yml     # Docker Compose setup
├── resources/             # API resource files
│   ├── user.py            # User-related CRUD operations
│   ├── auth.py            # Authentication and authorization endpoints
├── models/                # Data models
│   └── user.py            # User model for password hashing
├── utils/                 # Utility functions
│   ├── validators.py      # Input validation logic
│   ├── auth_middleware.py # Middleware for token validation
├── static/                # Static files (if any)
└── README.md              # Project README


## Setup and Running the Application

### Clone the Repository

git clone https://github.com/yourusername/flask-mongodb-crud.git
cd flask-mongodb-crud


### Create a .env file and add the following environment variables:
- SECRET_KEY=your_secret_key
- MONGO_URI=mongodb://mongo:27017/flaskdb

### docker-compose up --build

--The application will be available at http://localhost:5000

### Testing the API with Postman

 Register a User
- **URL**: `POST http://localhost:5000/register`
- **Method**: `POST`
- **Body** (raw JSON):
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
  }

Continue executing all the commands with correct methods using postman

