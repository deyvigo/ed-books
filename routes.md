```js

```

GET /friends?id=<id_user\>
```js
// response
{
  "data": [
    {
      "id_friend": 14
    },
  ]
}
```

POST /login
```js
// body
{
  "username": "dgomez",
  "password": "123456"
}
// response
{
  "access_token": "...",
  "id": 21,
  "name": "Deyvi Gomez",
  "username": "dgomez"
}
```


POST /user
```js
{
  "username": "dgomez",
  "password": "123456",
  "name": "Deyvi Gomez"
}
```

GET /user
```js
{
  "data": [
    {
      "id_user": 1,
      "name": "John Doe",
      "username": "jdoe"
    },
  ]
}
```

GET /genre
```js
{
  "data": [
    {
      "genre_name": "juvenile fiction",
      "id_genre": 1
    },
  ]
}
```

GET /friends/recommended/<id_user\>
```js
{
  "data": [
    {
      "id_user": 2,
      "name": "Alice Smith",
      "username": "asmith"
    },
  ]
}
```

GET /search/book/genre/<genre_name\>
```js
{
  "books": [
    {
      "author": [
        {
          "id_author": 4,
          "name": "Gabriel García Márquez"
        }
      ],
      "description": "...",
      "genres": [
        {
          "genre_name": "fiction",
          "id_genre": 6
        }
      ],
      "id_book": 1,
      "title": "Todos los cuentos",
      "url_img": "http://books.google.com/books/content?id=ojJjBgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
  ]
}
```