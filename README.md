# NATURAL-LANGUAGE-TEXT-TO-SQL-USING-MCP.
client name: internal company POC


cursor = connection.cursor() is used in Python database programming.
It creates a cursor object from the database connection.
Simple Meaning:
A cursor is like a helper/tool that allows Python to:
run SQL queries
fetch data from database
insert/update/delete records
Without a cursor, you cannot execute SQL commands.



# mcp_server.py :
creates a API using FastAPI and SQLite.
It has 2 API endpoints:

1. `/get_schema`

   * Connects to the database
   * Gets all table names
   * Fetches column names of each table
   * Returns database schema in JSON format

2. `/run_sql`

   * Accepts an SQL query from user
   * Executes the query on database
   * Returns query result (columns + rows)
   * Handles errors using `try-except`

Main components:

* `sqlite3.connect()` → connects to database
* `cursor()` → executes SQL queries
* `fetchall()` → gets all data
* `commit()` → saves changes
* `close()` → closes database connection safely


# mcp_client.py : 
This is a complete **Text-to-SQL AI application** built using Streamlit, FastAPI, SQLite, and Google Gemini AI.

## What it does:

User asks question in normal English like:
Show all students with marks greater than 90
The AI agent:

1. Gets database schema using API
2. Understands tables and columns
3. Generates SQL query
4. Executes SQL using API
5. Returns answer + SQL + table data in UI

---

## Main Parts

### 1. Environment Setup

Loads API key using `.env`

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


---

### 2. API Tool Functions

Calls backend FastAPI APIs:

* `/get_schema` → fetch database structure
* `/run_sql` → execute SQL query

---

### 3. MCP Agent

`mcp_agent(question)` is the brain of the system.

It:

* sends prompt to Gemini
* asks model to use tools
* executes tool calls
* retries on SQL errors
* returns final result

This is similar to an AI Agent / MCP workflow.

---

### 4. JSON Parsing

`safe_parse_json()` safely converts AI response text into JSON.

---

### 5. Data Formatting

Converts SQL output into Pandas DataFrame.

pd.DataFrame()

---

### 6. Streamlit UI

Creates frontend interface:

* input box
* submit button
* answer display
* SQL display
* data table display



## Overall Flow

User Question
     ↓
Gemini AI Agent
     ↓
Get Schema API
     ↓
Generate SQL
     ↓
Run SQL API
     ↓
Show Result in Streamlit

This is a simple AI-powered Text-to-SQL system using MCP-style tool calling architecture.

| Library               | Purpose       |
| --------------------- | ------------- |
| `streamlit`           | UI            |
| `requests`            | API calls     |
| `pandas`              | DataFrame     |
| `json`                | JSON handling |
| `dotenv`              | Load API keys |
| `google.generativeai` | Gemini model  |


Client Request
      ↓
Receive SQL Query
      ↓
Connect Database
      ↓
Execute Query
      ↓
Fetch Rows
      ↓
Return JSON Response
