import pandas as pd
from config import DB_CONFIG
from sqlalchemy import create_engine

if __name__ == "__main__":
    file_path = 'mini_dwh_project/data/sample.csv'
    #extract
    df = pd.read_csv(file_path)

    #transform
    df.columns = [col.strip().lower() for col in df.columns]

    #load
    url = url = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
              f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    engine = create_engine(url)
    df.to_sql("people", engine, if_exists='replace', index=False)
