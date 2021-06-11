from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str


book_list = {
    1: Book(id=1, title='Lord of the Rings', author='Mr. A'),
    2: Book(id=2, title='The Hobbit', author='Mr. B'),
    3: Book(id=3, title='Harry Potter', author='Mr. C'),
}
