from dotenv import load_dotenv
import streamlit as st
import os
import requests
import json
import pandas as pd
import google.generativeai as genai


# Load ENV

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

BASE_URL = "http://127.0.0.1:8000"


# MCP CLIENT TOOLS (HTTP)

def get_schema_tool():
    res = requests.get(f"{BASE_URL}/get_schema")
    return res.json()["schema"]

def run_sql_tool(query):
    res = requests.post(f"{BASE_URL}/run_sql", json={"query": query})
    return res.json()

TOOLS = {
    "get_schema": get_schema_tool,
    "run_sql": run_sql_tool
}


# JSON PARSER

def safe_parse_json(text):
    try:
        return json.loads(text)
    except:
        try:
            start = text.find("{")
            end = text.rfind("}") + 1
            return json.loads(text[start:end])
        except:
            return None

# FORMAT

def format_df(result):
    return pd.DataFrame(result["rows"], columns=result["columns"])


# MCP AGENT (CLIENT SIDE)

def mcp_agent(question):

    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    messages = [{
        "role": "user",
        "parts": [f"""
You are a TRUE MCP agent.

TOOLS (via API):
- get_schema
- run_sql(query)

Return ONLY JSON:

{{
  "action": "...",
  "arguments": {{}},
  "reason": "..."
}}

FINAL:
{{
  "action": "final",
  "arguments": {{
    "answer": "...",
    "sql": "..."
  }}
}}

Rules:
- Call get_schema first
- Then generate SQL
- Then call run_sql
- Retry max 3 times
- If column missing → explain

Question:
{question}
"""
        ]
    }]

    retry_count = 0
    last_error = None
    last_result = None
    last_sql = None

# Runs agent loop maximum 8 times.

# Why?
# Because AI may need multiple steps:

# get schema
# generate SQL
# execute SQL
# retry if error
# produce final answer


# {
#   "action": "final",
#   "arguments": {
#     "answer": "3 students found",
#     "sql": "SELECT * FROM STUDENT"
#   }
# }

    for _ in range(8):

        response = model.generate_content(messages)
        raw = response.text.strip()

        print("LLM:", raw)

        data = safe_parse_json(raw)
        if not data:
            return "❌ JSON parsing failed"

        action = data.get("action")

        # ---------------- TOOL CALL ----------------
        if action in TOOLS:

            if action == "get_schema":
                result = TOOLS[action]()

            elif action == "run_sql":
                query = data["arguments"].get("query")
                last_sql = query

                result = TOOLS[action](query)

                if "error" in result:
                    retry_count += 1
                    last_error = result["error"]

                    if retry_count >= 3:
                        return f"❌ Failed: {last_error}"

                else:
                    last_result = result

            messages.append({"role": "model", "parts": [raw]})
            messages.append({
                "role": "user",
                "parts": [f"Tool result: {json.dumps(result)} | Error: {last_error}"]
            })

        # ---------------- FINAL ----------------
        elif action == "final":

            answer = data["arguments"].get("answer")
            sql = data["arguments"].get("sql", last_sql)

            if last_result:
                df = format_df(last_result)
                return answer, sql, df

            return answer

    return "❌ Agent failed"



# STREAMLIT UI

st.set_page_config(page_title="TEXT TO SQL", layout="wide")
st.header("NATURAL LANGUAGE TEXT TO SQL")

question = st.text_input("Ask your question:")

if st.button("Submit"):

    result = mcp_agent(question)

    if isinstance(result, tuple):
        answer, sql, df = result

        st.subheader("🧠 Answer")
        st.write(answer)

        st.subheader("💻 SQL")
        st.code(sql)

        st.subheader("📊 Data")
        st.dataframe(df)

    else:
        st.write(result)


# User Question
#       ↓
# Gemini AI
#       ↓
# Choose Tool
#       ↓
# Call API Tool
#       ↓
# Get Result
#       ↓
# Generate Final Answer