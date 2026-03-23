import pandas as pd
from db import get_engine
from llm import generate_sql
from validator import is_safe_query

def run_query(question: str, conversation_history: list = []) -> tuple[str, pd.DataFrame]:
    sql = generate_sql(question, conversation_history)

    if sql == "CANNOT_ANSWER":
        raise ValueError("This question cannot be answered from the database. Try asking something data-specific like 'what is the total revenue by category?'")

    if not is_safe_query(sql):
        raise ValueError(f"Unsafe query blocked: {sql}")

    engine = get_engine()
    with engine.connect() as conn:
        df = pd.read_sql(sql, conn)
    return sql, df


if __name__ == "__main__":
    question = "What were the total sales by region?"
    sql, df = run_query(question)
    print(f"Generated SQL:\n{sql}\n")
    print(f"Results:\n{df}")