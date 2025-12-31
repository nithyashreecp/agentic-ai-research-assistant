# agents/researcher.py
import arxiv

def researcher(state):
    topic = state["topic"]

    search = arxiv.Search(query=topic, max_results=5)
    papers = list(search.results())

    summaries = []
    titles = []
    links = []

    for p in papers:
        titles.append(p.title)
        summaries.append(p.summary)
        links.append(p.entry_id)  

    return {
        "topic": topic,
        "plan": state["plan"],
        "memory": state.get("memory", []),
        "papers": summaries,
        "titles": titles,
        "links": links
    }




