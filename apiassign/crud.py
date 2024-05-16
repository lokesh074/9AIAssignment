from database import *
import database
class Blog:
    @staticmethod
    def create_post(db,blogpost):
        try:
           post = BlogDb(title=blogpost.title.strip().lower(),Content=blogpost.content.strip())
           db.add(post)
           db.flush()
           blog_id = post.postId
           db.commit()
           db.refresh(post)
           print("Blog added successfully")
           return blog_id
        except Exception as e:
            print("Error when inserting blog content:",e)
            db.rollback()
            blog_id = 0            
            return blog_id

    @staticmethod
    def get_post(db,post_id):
        try:
           post_data = db.query(database.BlogDb).filter(database.BlogDb.postId==post_id).first()
           return post_data

        except Exception as e:
            print("Error in get post function :: ",e)
            db.rollback()
            # return HTTPException(status_code=404, detail="Post not found")

    @staticmethod
    def update_post(db,post_id,title,content):
        data = db.query(database.BlogDb).filter(database.BlogDb.postId==post_id).first()
        if data.postId!=0 or data.postId!=None:
            data.title = title.strip()
            data.Content = content
            return {"message": "Post updated successfully"}
        else:
            return {"message": "Post is not available"}

    @staticmethod
    def delete_post(db,post_id):
        try:
            post = db.query(database.BlogDb).filter(database.BlogDb.postId == post_id).first()
            if post:
                db.delete(post)
                db.commit()
                return {"message": "Post deleted successfully"}
            else:
                return {"message": "Post is not available"}
        except Exception as e:
            db.rollback()
            return {"message": "Post is not available"}
            # raise HTTPException(status_code=500, detail=f"Error deleting post: {e}")


    @staticmethod
    def create_comment(db,post_id,comment):
        try:
            data = db.query(database.BlogDb).filter(database.BlogDb.postId == post_id).first()
            
            if data:
               data.comment = comment.strip()
            #    print(data.comment)
               db.commit()
               print("updated comment")
               return {"message": "comment updated successfully"}
            else:
                return {"message": "Post is not available"}

        except Exception as e:
            db.rollback()
            return {"message": "Post is not available"}


    @staticmethod
    def like_post(db,post_id,Like):
        db.query(database.BlogDb).filter(database.BlogDb.postId == post_id).update({'Like': Like})
        db.commit()
        return {"message": "Like updated successfully"}
