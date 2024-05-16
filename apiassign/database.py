from sqlalchemy import create_engine,String,Column,Text,Boolean,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./blog.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()

class BlogDb(base):
    __tablename__ ='blogpost'
    postId = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String)
    Content = Column(Text)
    comment = Column(String,default=None)
    Like = Column(Boolean,default=False)

# from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient("mongodb+srv://lokeshiiitu:Lokesh1234@blog.ib8gcdz.mongodb.net/?retryWrites=true&w=majority&appName=blog")

# db = client["Blog_database"]

# # MongoDB Collection
# blog_collection = db["blog_posts"]

# class BlogDb:
#     @staticmethod
#     def create_post(title, content):
#         post_data = {
#             "title": title,
#             "content": content,
#             "comment": None,
#             "like": False
#         }
#         result = blog_collection.insert_one(post_data)
#         return result.inserted_id

#     @staticmethod
#     def get_post(post_id):
#         post_data = blog_collection.find_one({"_id": post_id})
#         return post_data

#     @staticmethod
#     def update_post(post_id, title, content):
#         updated_data = {"$set": {"title": title, "content": content}}
#         result = blog_collection.update_one({"_id": post_id}, updated_data)
#         return result.modified_count > 0

#     @staticmethod
#     def delete_post(post_id):
#         result = blog_collection.delete_one({"_id": post_id})
#         return result.deleted_count > 0

#     @staticmethod
#     def create_comment(post_id, comment):
#         result = blog_collection.update_one({"_id": post_id}, {"$set": {"comment": comment}})
#         return result.modified_count > 0

#     @staticmethod
#     def like_post(post_id, like):
#         result = blog_collection.update_one({"_id": post_id}, {"$set": {"like": like}})
#         return result.modified_count > 0
