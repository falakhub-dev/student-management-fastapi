
import sqlite3

from fastapi import APIRouter, HTTPException
from langchain_ollama import ChatOllama
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["AI Query"])

# Initialize the local LLM using Ollama
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


class QueryRequest(BaseModel):
    question: str


@router.post("/query-students")
def ask_student_database(payload: QueryRequest):
    try:
        # 1. Fetch all records from the SQLite database
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        # Get column names
        column_names = [
            desc[0] for desc in cursor.description
        ]

        conn.close()

        # 2. Format database records as text context
        context_data = (
            f"Columns: {column_names}\n"
            "Data Rows:\n"
            + "\n".join(str(row) for row in rows)
        )

        # 3. Create a prompt with database context
        prompt = f"""You are a helpful assistant.
Use the following database records to answer
the user's question. Answer only using the
provided records. If the answer is not available,
say that the information is not available.

Database Context:
{context_data}

User Question: {payload.question}

Answer:"""

        # 4. Invoke the local language model
        response = llm.invoke(prompt)

        answer_text = (
            response.content
            if hasattr(response, "content")
            else str(response)
        )

        # 5. Return the answer
        return {
            "question": payload.question,
            "answer": answer_text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
