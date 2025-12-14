from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///orders.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class OrderDB(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    side = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    status = Column(String)

Base.metadata.create_all(engine)
