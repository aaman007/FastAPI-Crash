from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional

from models.books import book_list, Book
from models.users import user_list, token_list

app = FastAPI()


@app.get('/user-info')
def retrieve_user(token: str, user_id: Optional[int] = None):
    user = None if not user_id else user_list.get(user_id)
    token = token_list.get(token)
    token_user = token and user_list.get(token.user_id)

    if not token or (user and token_user != user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid Token or User ID'
        )
    return {'user': token_user}


@app.get('/books')
def list_books():
    _books = []
    for key in book_list.keys():
        _books.append(book_list[key])
    return {'books': _books}


@app.get('/books/{pk}')
def retrieve_book(pk: int = Path(None, description='Book Id', gt=0)):
    if pk in book_list:
        return {'book': book_list[pk]}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post('/books/')
def create_book(book: Book):
    if book.id in book_list:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='ID already exists'
        )
    book_list[book.id] = book
    return {'book': book}


@app.put('/books/{pk}')
def update_book(pk: int, book: Book):
    if pk not in book_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    elif book.id != pk:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='ID can not be modified'
        )
    book_list[pk] = book
    return {'book': book}


@app.delete('/books/{pk}')
def delete_book(pk: int):
    if pk not in book_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    del book_list[pk]
    return {'status': 'deleted'}


# To run the application
# uvicorn app:app --reload

