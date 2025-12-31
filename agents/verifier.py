from tools.llm import llm

def verifier(state):
    response = llm.invoke([
        {
            "role": "user",
            "content": f"""
            Verify the following analysis for factual correctness.
            Remove hallucinations and keep it relevant to the topic: {state['topic']}

            Analysis:
            {state['analysis']}
            """
        }
    ])

    return {
        "topic": state["topic"],         
        "plan": state["plan"],           
        "analysis": state["analysis"],    
        "final_output": response.content,
        "titles": state["titles"] ,
        "links": state["links"] 
    }





