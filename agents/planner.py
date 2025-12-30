from tools.llm import llm

def planner(state):
    topic = state["topic"]

    response = llm.invoke([
        {
            "role": "user",
            "content": f"""
You are a planning agent.

Given the research topic: "{topic}"

Decide:
- whether prior memory is useful (yes/no)
- what analysis depth is needed (basic / detailed)

Return in JSON:
{{
  
  "analysis_depth": "basic" or "detailed",
  "plan": "short plan"
}}
"""
        }
    ])

    return {
        "topic": topic,        
        "plan": response.content 
    }




