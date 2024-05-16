from typing import Optional
from pydantic import BaseModel

class blog(BaseModel):
    title:str
    content: str

class getblog(BaseModel):
    postid:int =1

class comment(BaseModel):
    postid:int = 1
    comment:str

class like(BaseModel):
    postid:int = 1
    like:bool