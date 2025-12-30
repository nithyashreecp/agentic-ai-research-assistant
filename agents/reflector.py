from tools.llm import llm
from memory.pinecone_store import store_text
import uuid

def reflector(state):
    topic = state["topic"]
    analysis = state["analysis"]

    response = llm.invoke([
        {
            "role": "user",
            "content": f"""
You are a reflection agent.

Improve the following analysis.
Ensure it is concise, accurate, and clearly structured.

Topic: {topic}

Analysis:
{analysis}
"""
        }
    ])

    final_output = response.content

    # STORE INTO PINECONE
    doc_id = f"{topic}-{uuid.uuid4()}"
    store_text(
        text=f"Topic: {topic}\n\n{final_output}",
        doc_id=doc_id
    )

    return {
        "topic": topic,
        "plan": state["plan"],
        "analysis": analysis,
        "final_output": final_output,
        "titles": state["titles"]
    }
