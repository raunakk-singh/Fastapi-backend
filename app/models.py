from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,select
from sqlalchemy.orm import column_property,relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

from .database import Base


class Votes(Base):
  __tablename__='votes'
  post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
  user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)


class Post(Base):
  __tablename__="posts"
  
  id=Column(Integer,primary_key=True,nullable=False)
  title=Column(String,nullable=False)
  content=Column(String,nullable=False)
  published=Column(Boolean,server_default="TRUE",nullable=False)
  created_at=Column(TIMESTAMP(timezone=True),nullable=False, server_default=func.now())
  owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
  votes=column_property(
      select(func.count(Votes.post_id))
      .where(Votes.post_id==id)
      .correlate_except(Votes)
      .scalar_subquery()
  )

  owner=relationship("User")

class User(Base):
  __tablename__='users'
  id=Column(Integer,primary_key=True,nullable=False)
  email=Column(String,nullable=False,unique=True)
  password=Column(String,nullable=False)
  published=Column(Boolean,server_default='TRUE',nullable=False)
  created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())
  phone_no=Column(String)

  