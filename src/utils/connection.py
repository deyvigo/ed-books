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
        create table if not exists autor
        (
          id_autor  int auto_increment
            primary key,
          name      varchar(200) null
        );
      """)
      cursor.execute("""
        create table if not exists book
        (
          id_book     int auto_increment
            primary key,
          id_autor    int  null,
          description text not null,
          url_img     text not null,
          constraint book_autor_id_autor_fk
            foreign key (id_autor) references autor (id_autor)
        );
      """)
      cursor.execute("""
        create table if not exists genre
        (
          id_genre   int auto_increment
            primary key,
          genre_name varchar(100) null
        );
      """)
      cursor.execute("""
        create table if not exists book_genre
        (
          id_book_genre int auto_increment
            primary key,
          id_book       int not null,
          id_genre      int not null,
          constraint book_genre_book_id_book_fk
            foreign key (id_book) references book (id_book),
          constraint book_genre_genre_id_genre_fk
            foreign key (id_genre) references genre (id_genre)
        );
      """)
      cursor.execute("""
        create table if not exists user
        (
          id_user  int auto_increment
            primary key,
          username varchar(30) not null,
          password varchar(70) not null,
          name     varchar(30) not null
        );
      """)
      cursor.execute("""
        create table if not exists book_user
        (
          id_book_user int auto_increment
            primary key,
          id_book      int not null,
          id_user      int not null,
          constraint book_user_book_id_book_fk
            foreign key (id_book) references book (id_book),
          constraint book_user_user_id_user_fk
            foreign key (id_user) references user (id_user)
        );
      """)
      cursor.execute("""
        create table if not exists friend
        (
          id_friend    int auto_increment
            primary key,
          id_applicant int               not null,
          id_receiver  int               not null,
          is_accept    tinyint default 0 not null,
          constraint friend_user_id_user_fk
            foreign key (id_applicant) references user (id_user),
          constraint friend_user_id_user_fk_2
            foreign key (id_receiver) references user (id_user)
        );
      """)
      cursor.execute("""
        create table if not exists post
        (
          id_post      int auto_increment
            primary key,
          id_user_post int          not null,
          id_book      int          not null,
          content      varchar(500) not null,
          constraint post_book_id_book_fk
            foreign key (id_book) references book (id_book),
          constraint post_user_id_user_fk
            foreign key (id_user_post) references user (id_user)
        );
      """)
      cursor.execute("""
        create table if not exists comment
        (
          id_comment     int auto_increment
            primary key,
          id_post        int          not null,
          id_user_coment int          not null,
          comment        varchar(500) not null,
          constraint comment_post_id_post_fk
            foreign key (id_post) references post (id_post),
          constraint comment_user_id_user_fk
            foreign key (id_user_coment) references user (id_user)
        );
      """)
      cursor.execute("""
        create table if not exists comment_user
        (
          id_comment_user int auto_increment
            primary key,
          id_comment      int not null,
          id_user         int null,
          constraint comment_user_comment_id_comment_fk
            foreign key (id_comment) references comment (id_comment),
          constraint comment_user_user_id_user_fk
            foreign key (id_user) references user (id_user)
        );
      """)
      cursor.execute("""
        create table if not exists post_user
        (
          id_post_user int auto_increment
            primary key,
          id_post      int not null,
          id_user      int not null,
          constraint post_user_post_id_post_fk
            foreign key (id_post) references post (id_post),
          constraint post_user_user_id_user_fk
            foreign key (id_user) references user (id_user)
        );
      """)
      print("Las tablas de crearon satisfactoriamente.")
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
