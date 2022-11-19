from models import Base
from session import session

if __name__ == '__main__':

    session1 = session()
    Base.metadata.create_all(session1.get_bind())

    article = session1.query('articles').get(1)
    for hashtag in article:
        print(hashtag.hashtag)

