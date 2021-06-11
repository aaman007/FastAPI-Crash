from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    token: str


class Token(BaseModel):
    id: int
    token: str
    user_id: int


user_list = {
    1: User(id=1, name='Mr. A', token='ABCD'),
    2: User(id=2, name='Mr. B', token='BCDE')
}

token_list = {
    'ABCD': Token(id=1, token='ABCD', user_id=1),
    'BCDE': Token(id=2, token='BCDE', user_id=2)
}
