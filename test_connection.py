from sqlalchemy import create_engine
from config import DB_CONFIG

def test_connection():
    try:
        url = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
              f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        engine = create_engine(url)
        print("connected to DB")
    except Exception as e:
        print("failed connection", e)

test_connection()