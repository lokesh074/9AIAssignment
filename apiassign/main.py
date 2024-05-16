from fastapi import FastAPI,HTTPException,Depends
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import database,schema
import crud

database.base.metadata.create_all(bind=database.engine)
app = FastAPI(
    title="Blog API"
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/Blog")
async def write_blog(blogtext:schema.blog,db = Depends(get_db)):
    Post_ID = crud.Blog.create_post(db,blogtext)
    if Post_ID==0:
        return JSONResponse(content={"Error":"Unable to Store content","PostID": Post_ID})
    else:
        return JSONResponse(content={"Status":"Content Added","PostID": Post_ID})

@app.post("/getpost")
async def get_blog(id:schema.getblog,db = Depends(get_db)):
    Post = crud.Blog.get_post(db,id.postid)
    # print(Post)
    if not Post:
        return JSONResponse(content={"Error":"Unable to Get content"})
    else:
        return {"Your Post":Post}

@app.post("/comment")
async def create_comment(com:schema.comment,db = Depends(get_db)):
    comment = crud.Blog.create_comment(db,com.postid,com.comment)
    return comment

@app.post("/delete")
async def deleteblog(id:schema.getblog,db = Depends(get_db)):
    delete_post = crud.Blog.delete_post(db,id.postid)
    return delete_post

@app.post("/like")
async def write_blog(lik:schema.like,db = Depends(get_db)):
    like_post = crud.Blog.like_post(db,lik.postid,lik.like)
    return like_post

# from fastapi import FastAPI, HTTPException
# from database import BlogDb

# app = FastAPI(title="Blog API")

# @app.post("/Blog")
# async def write_blog(title: str, content: str):
#     post_id = BlogDb.create_post(title=title.strip().lower(), content=content.strip())
#     if post_id:
#         return {"Status": "Content Added", "PostID": str(post_id)}
#     else:
#         raise HTTPException(status_code=500, detail="Unable to Store content")

# @app.post("/getpost")
# async def get_blog(post_id: str):
#     post_data = BlogDb.get_post(post_id)
#     if post_data:
#         return {"Your Post": post_data}
#     else:
#         raise HTTPException(status_code=404, detail="Post not found")

# @app.post("/comment")
# async def create_comment(post_id: str, comment: str):
#     if BlogDb.create_comment(post_id, comment):
#         return {"message": "Comment updated successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Post not available")

# @app.post("/delete")
# async def delete_blog(post_id: str):
#     if BlogDb.delete_post(post_id):
#         return {"message": "Post deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Post not available")

# @app.post("/like")
# async def like_blog(post_id: str, like: bool):
#     if BlogDb.like_post(post_id, like):
#         return {"message": "Like updated successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Post not available")

