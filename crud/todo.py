from sqlalchemy.orm import Session

from models import Todo, TodoTag
from schemas.todo import TodoCreate, TodoUpdate


def create_todo(db: Session, todo_data: TodoCreate):
    print(TodoCreate)
    new_todo = Todo(
        user_id = todo_data.user_id,
        title = todo_data.title,
        description = todo_data.description,
        due_date = todo_data.due_date,
        priority = todo_data.priority,
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

def get_all_todos(db: Session, user_id: int):
    todo_list = db.query(Todo).filter(user_id == Todo.user_id).order_by(Todo.due_date).all()
    return todo_list

def get_todo_by_id(db: Session, todo_id: int, user_id: int):
    todo = db.query(Todo).filter(todo_id == Todo.id, user_id == Todo.user_id).first()
    if not todo:
        return None
    return todo

def update_todo(db: Session, todo_id: int, todo_data: TodoUpdate, user_id: int):
    todo = db.query(Todo).filter(todo_id == Todo.id, user_id == Todo.user_id).first()
    if not todo:
        return None

    for key, value in todo_data.model_dump().items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)

    return todo

def delete_todo(db: Session, todo_id: int, user_id: int):
    todo = db.query(Todo).filter(todo_id == Todo.id, user_id == Todo.user_id).first()

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return todo
