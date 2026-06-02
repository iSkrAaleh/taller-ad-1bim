from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# conexcion exacta al contenedor PostgreSQL
DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5434/universidad_db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
