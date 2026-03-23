import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

load_dotenv()

def get_engine() -> Engine:
    url = os.getenv("SUPABASE_URL")
    return create_engine(url)

if __name__ == "__main__":
    try:
        engine = get_engine()
        with engine.connect() as conn:
            print("Connection successful")
    except Exception as e:
        print(f"Connection failed: {e}")