# 🚀 Natural Language Text-to-SQL Using MCP

Transform plain English questions into SQL queries using the power of AI, Large Language Models (LLMs), and the Model Context Protocol (MCP).

## 📖 Overview

**Natural Language Text-to-SQL Using MCP** is an AI-powered application that enables users to interact with databases using natural language instead of writing SQL manually.

The system interprets user questions, understands database schema context through MCP, generates optimized SQL queries, executes them, and returns human-readable results.

### Example

**User Input**

```text
Show all employees whose salary is greater than 50000
```

**Generated SQL**

```sql
SELECT * 
FROM Employee
WHERE salary > 50000;
```

---

## ✨ Features

* 🧠 Natural Language to SQL Conversion
* 🔗 MCP (Model Context Protocol) Integration
* 🤖 LLM-Powered Query Generation
* 📊 Database Schema Understanding
* ⚡ Real-Time SQL Execution
* 🛡️ SQL Validation and Error Handling
* 📈 Structured Query Results
* 🔍 Context-Aware Query Generation
* 🏗️ Scalable and Modular Architecture

---

## 🏛️ System Architecture

```text
User Query
    │
    ▼
Natural Language Input
    │
    ▼
MCP Server
    │
    ▼
LLM Processing Layer
    │
    ▼
SQL Query Generation
    │
    ▼
Database Execution
    │
    ▼
Result Formatting
    │
    ▼
User Response
```

---

## 🛠️ Tech Stack

| Technology                  | Purpose             |
| --------------------------- | ------------------- |
| Python                      | Core Development    |
| MCP                         | Context Management  |
| LangChain                   | LLM Orchestration   |
| OpenAI / LLM APIs           | Query Generation    |
| SQL                         | Database Operations |
| SQLite / MySQL / PostgreSQL | Data Storage        |
| FastAPI                     | API Development     |
| Streamlit                   | User Interface      |

---

## 📂 Project Structure

```text
NATURAL-LANGUAGE-TEXT-TO-SQL-USING-MCP/
│
├── app/
│   ├── agents/
│   ├── database/
│   ├── prompts/
│   ├── tools/
│   └── services/
│
├── data/
│
├── tests/
│
├── requirements.txt
├── README.md
└── main.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/NATURAL-LANGUAGE-TEXT-TO-SQL-USING-MCP.git
```

### Navigate to Project

```bash
cd NATURAL-LANGUAGE-TEXT-TO-SQL-USING-MCP
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python main.py
```

---

## 🎯 Use Cases

* Business Intelligence
* Data Analytics
* Database Exploration
* Enterprise Reporting
* Educational SQL Learning
* Self-Service Data Querying
* AI-Powered Data Assistants

---

## 📸 Sample Queries

### Query 1

```text
List all customers from Pune.
```

Generated SQL:

```sql
SELECT *
FROM Customers
WHERE city = 'Pune';
```

### Query 2

```text
Show top 5 highest paid employees.
```

Generated SQL:

```sql
SELECT *
FROM Employee
ORDER BY salary DESC
LIMIT 5;
```

### Query 3

```text
Count total orders placed this month.
```

Generated SQL:

```sql
SELECT COUNT(*)
FROM Orders
WHERE MONTH(order_date)=MONTH(CURRENT_DATE);
```

---

## 🔮 Future Enhancements

* Multi-Database Support
* Query Visualization
* Interactive Dashboard
* Voice-to-SQL Interface
* Fine-Tuned SQL Models
* Query Optimization Engine
* Role-Based Access Control
* Advanced Analytics Integration

---

## 🏆 Learning Outcomes

This project demonstrates:

* Generative AI Applications
* Large Language Models (LLMs)
* Prompt Engineering
* Model Context Protocol (MCP)
* Natural Language Processing (NLP)
* SQL Query Generation
* Database Integration
* AI Agent Development

---

## 👨‍💻 Author

**Gahininath Wagh**

* Python Developer
* AI & Machine Learning Enthusiast
* Generative AI Developer

GitHub: https://github.com/Gahininat

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐛 Report issues
* 🤝 Contribute improvements

---

## 📜 License

company

---

### "Making Databases Conversational with AI and MCP" 🚀
