from fastapi import APIRouter

router = APIRouter(
    prefix="/tags",
    tags=["tags"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def create_tag():
    return {"msg": "/tags(post)"}

@router.get("/")
def get_tag_list():
    return {"msg": "/tags(get)"}

@router.put("/{tag_id}")
def update_todo():
    return {"msg": "/tags/{tag_id}(put)"}

@router.delete("/{tag_id}")
def delete_todo():
    return {"msg": "/tags/{tag_id}(delete)"}

