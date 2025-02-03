from fastapi import APIRouter

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def create_todo():
    return {"msg": "/todos(post)"}

@router.get("/")
def get_todo_list():
    return {"msg": "/todos(get)"}

@router.get("/{todo_id}")
def get_todo():
    return {"msg": "/todos/{todo_id}(get)"}

@router.put("/{todo_id}")
def update_todo():
    return {"msg": "/todos/{todo_id}(put)"}

@router.delete("/{todo_id}")
def delete_todo():
    return {"msg": "/todos/{todo_id}(delete)"}


@router.get("/tag/{tag_id}")
def get_todo_list_by_tag():
    return {"msg": "/todos/tag/{tag_id}(get)"}