import re

FORBIDDEN = ["insert", "update", "delete", "drop", "alter", "truncate", "exec", "execute", "create"]

def is_safe_query(sql: str) -> bool:
    cleaned = sql.strip().lower()

    # Strip SQL comments before checking
    cleaned = re.sub(r'--.*', '', cleaned)
    cleaned = re.sub(r'/\*.*?\*/', '', cleaned, flags=re.DOTALL)

    # Must start with SELECT or WITH (CTEs)
    if not cleaned.startswith("select") and not cleaned.startswith("with"):
        return False

    # Must not contain forbidden keywords
    for keyword in FORBIDDEN:
        if re.search(rf"\b{keyword}\b", cleaned):
            return False

    return True