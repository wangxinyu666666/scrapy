from sqlalchemy import Column, String , DateTime, Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


def db_connect():
     #    return create_engine('sqlite:///./sqlalchemy.db?charset=utf-8',echo = True)

     return create_engine("mysql+pymysql://root:9855zzy@localhost/wangxinyu?charset=utf8", max_overflow=5)  # 定义一个指向sqlalchemy.db数据库的引擎
def create_articless_table(engine):
    DeclarativeBase.metadata.create_all(engine)
class Article(DeclarativeBase):
     __tablename__ = 'articless'

     id= Column(Integer, primary_key=True)
     title = Column('title',String(200))
     link = Column('link',String(100))
     desc = Column('desc',String(20000))