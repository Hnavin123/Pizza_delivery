
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker



engine = create_engine('postgresql://postgres:abc123@localhost:5432/pizza_delivery', echo=True)


Base = declarative_base()

Session = sessionmaker(bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()





