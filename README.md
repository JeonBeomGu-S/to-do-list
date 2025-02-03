# To-Do List API

A FastAPI-based To-Do List application with user authentication and task management.

## Features

- User registration and authentication (JWT-based)
- Task management (CRUD operations)
- Tagging system for tasks
- PostgreSQL database using SQLAlchemy

## Installation

1. Clone the repository  
   ```bash
    git clone <repository-url>
    cd toDoList
    ```
2. Create and activate a virtual environment
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database  
Ensure you have PostgreSQL installed and update the .env file with your database credentials.

5. Run the application
   ```bash
   uvicorn main:app --reload
   ```
   
## API Endpoints

### User
| Method | Request URL | Description                      |
|--------|-------------|----------------------------------|
| `POST` | `/signup`   | Register a new user              |  
| `POST` | `/login`    | Authenticate and get a JWT token |

### To-Do Management
| Method   | Request URL           | Description              |
|----------|-----------------------|--------------------------|
| `POST`   | `/todos/`             | Create a new task        |
| `GET`    | `/todos/`             | Retrieve all tasks       |
| `GET`    | `/todos/{todo_id}`    | Retrieve a specific task |
| `PUT`    | `/todos/{todo_id}`    | Update a task            |
| `DELETE` | `/todos/{todo_id}`    | Delete a task            |
| `GET`    | `/todos/tag/{tag_id}` | Retrieve a tasks by tag  |

### Tag
| Method   | Request URL      | Description       |
|----------|------------------|-------------------|
| `POST`   | `/tags/`         | Create a new tag  |
| `GET`    | `/tags/`         | Retrieve all tags |
| `PUT`    | `/tags/{tag_id}` | Update a tag      |
| `DELETE` | `/tags/{tag_id}` | Delete a tag      |

## Environment Variables

Create a .env file and add the following:  
```env
DATABASE_URL=postgresql://user:password@localhost/todo_db
JWT_SECRET_KEY=your_secret_key
HASH_ALGORITHM=HS256
```