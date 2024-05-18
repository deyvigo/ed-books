import pymysql
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".enviromentvars")

class Database:
  def __init__(self):
    db = self.connection()
    try:
      cursor = db.cursor()
      cursor.execute("""
        create table if not exists user
        (
          id_user   integer auto_increment primary key,
          username  varchar(30)  not null,
          password  varchar(100) not null,
          name      varchar(20)  not null,
          last_name varchar(20)  not null
        );
      """)
      cursor.execute("""
        create table if not exists book
        (
          id_book       integer auto_increment primary key,
          autor         varchar(60) not null,
          description   varchar(255) not null,
          url_img       varchar(255)
        );
      """)
    except Exception as e:
      print(f"Error durante la creación de las tablas: {e}")
    finally:
      db.close()

  def connection (self):
    db = pymysql.connections.Connection(
      host=os.getenv("DATABASE_HOST"),
      database=os.getenv("DATABASE_NAME"),
      user=os.getenv("DATABASE_USER"),
      password=os.getenv("DATABASE_PASSWORD"),
      port=3306,
      cursorclass=pymysql.cursors.DictCursor
    )
    return db
