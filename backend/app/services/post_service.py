from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.database import get_db
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate

class PostService:
    # 초기자
    def __init__(self, db:AsyncSession):
        self.db = db
        
    # 저장기능 - apis/post.py의 create함수에서 호출함
    async def post_create(self, pp: PostCreate):
        # 이미 인자인 post에 저장할 값들이 들어온 상태다.
        # post변수에 있는 값들을 테이블모델(Post)에 저장하자!
        create_post = Post(title=pp.title, content=pp.content, author_id=pp.author)
        self.db.add(create_post) # db세션에 위의 값을 등록
        await self.db.commit() # db에 적용
        await self.db.refresh(create_post) # db에 적용된 내용과 일치시킨다.(id, create_at, status) 들어옴
        return create_post
    
def get_post_service(db: AsyncSession = Depends(get_db)) : # PostService를 생성하여 반환하는 것이 목적이다.    
    return PostService(db)