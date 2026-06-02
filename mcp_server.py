from fastapi import FastAPI
import sqlite3

app = FastAPI()

DB_PATH = "student.db"


# TOOL 1: GET SCHEMA

@app.get("/get_schema")
def get_schema():

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    schema = {}

    for table in tables:
        table_name = table[0]

        cur.execute(f"PRAGMA table_info({table_name});")
        columns = cur.fetchall()

        schema[table_name] = [col[1] for col in columns]

    conn.close()

    return {"schema": schema}



# TOOL 2: RUN SQL

@app.post("/run_sql")
def run_sql(data: dict):

    query = data.get("query")

    # Prevent None query error
    if not query:
        return {"error": "Query is required"}

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        cur.execute(query)

        rows = cur.fetchall()

        columns = (
            [desc[0] for desc in cur.description]
            if cur.description
            else []
        )

        conn.commit()

        conn.close()

        return {
            "columns": columns,
            "rows": rows
        }

    except Exception as e:

        conn.close()

        return {"error": str(e)}