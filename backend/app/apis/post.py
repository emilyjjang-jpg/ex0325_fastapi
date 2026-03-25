from fastapi import APIRouter, Depends, HTTPException
from app.models.post import Post
from app.schemas.post import PostCreate, PostResponse, PostUpdate
from app.services.post_service import PostService, get_post_service

router = APIRouter()

@router.post("/create", response_model=PostResponse,
          summary="게시물 저장기능",
          description="저장할 자원(title, content)을 인자로 전달하여 저장한다.") # posts게시물 저장
async def create(post: PostCreate, ps: PostService = Depends(get_post_service)): # 서비스객체가 강제로 주입되야 함
    new_post = await ps.post_create(post)
    if new_post is None:
        raise HTTPException(status_code=404, detail='게시물 저장실패')
    return new_post
