# researcher.py
import arxiv

def researcher(state):
    topic = state["topic"]

    search = arxiv.Search(query=topic, max_results=5)
    papers = list(search.results())

    summaries = [p.summary for p in papers]
    titles = [p.title for p in papers]

    return {
        "topic": state["topic"],          
        "plan": state["plan"],           
        "memory": state.get("memory", []),
        "papers": summaries,
        "titles": titles
    }




