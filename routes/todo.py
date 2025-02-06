from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from crud.todo import create_todo, get_all_todos, get_todo_by_id, update_todo, delete_todo, get_all_todos_by_tag
from crud.user import get_current_user_id
from database.db import get_db
from schemas.todo import TodoCreate, TodoUpdate

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = Depends(OAuth2PasswordBearer(tokenUrl="token"))

@router.post("/")
def post_todo(todo_data: TodoCreate, db: Session = Depends(get_db)):
    new_todo = create_todo(db=db, todo_data=todo_data)
    return {"msg": "Created todo successfully!", "todo": new_todo}


@router.get("/")
def get_todo_list(db: Session = Depends(get_db), token: str = oauth2_scheme):
    user_id = get_current_user_id(db, token)
    todo_list = get_all_todos(db=db, user_id=user_id)
    return {"msg": "Retrieved todo list successfully!", "todo_list": todo_list}

@router.get("/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db), token: str = oauth2_scheme):
    user_id = get_current_user_id(db=db, token=token)
    todo = get_todo_by_id(db=db, todo_id=todo_id, user_id=user_id)
    if todo is None:
        return {"msg": "Cannot find todo"}
    return {"msg": "Retrieved todo detail successfully!", "todo": todo}

@router.put("/{todo_id}")
def put_todo(todo_id: int, todo_data: TodoUpdate, db: Session = Depends(get_db), token: str = oauth2_scheme):
    user_id = get_current_user_id(db=db, token=token)
    todo = update_todo(db=db, todo_id=todo_id, todo_data=todo_data, user_id=user_id)
    if todo is None:
        return {"msg": "Cannot update todo"}
    return {"msg": "todo is updated successfully!", "updated_todo": todo}

@router.delete("/{todo_id}")
def handle_delete_todo(todo_id: int, db: Session = Depends(get_db), token: str = oauth2_scheme):
    user_id = get_current_user_id(db=db, token=token)
    todo = delete_todo(db=db, todo_id=todo_id, user_id=user_id)
    return {"msg": "todo is deleted successfully", "deleted_todo": todo}

@router.get("/tag/{tag_id}")
def get_todo_list_by_tag():
    return {"msg": "/todos/tag/{tag_id}(get)"}