from sqlmodel import SQLModel, Field, Session, create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings
from sqlalchemy.engine import URL
import time


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.database_username,
    password=settings.database_password,
    host=settings.database_hostname,
    port=int(settings.database_port),
    database=settings.database_name,
)

engine = create_engine(DATABASE_URL) 
        

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)



Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        
# only for documentation purposes we already conneced database using sqlalchemy
# while True:    
#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Raunak@123',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("connecting to database failed!")
#         print("Error: ",error )
#         time.sleep(2)
        

