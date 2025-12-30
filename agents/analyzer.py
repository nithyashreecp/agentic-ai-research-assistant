
from tools.llm import llm

def analyzer(state):
    summaries = state["papers"]
    memory = state.get("memory", [])

    response = llm.invoke([
        {
            "role": "user",
            "content": f"""
Analyze the research summaries below.
Use prior memory if relevant.

Memory:
{memory}

Summaries:
{summaries}
"""
        }
    ])

    return {
        "topic": state["topic"],          
        "plan": state["plan"],            
        "titles": state["titles"],         
        "analysis": response.content
    }







