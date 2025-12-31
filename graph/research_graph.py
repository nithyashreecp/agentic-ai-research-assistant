from langgraph.graph import StateGraph

from agents.planner import planner
from agents.researcher import researcher
from agents.analyzer import analyzer
from agents.verifier import verifier
from agents.reflector import reflector


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("planner", planner)
    graph.add_node("researcher", researcher)
    graph.add_node("analyzer", analyzer)
    graph.add_node("verifier", verifier)
    graph.add_node("reflector", reflector)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "analyzer")
    graph.add_edge("analyzer", "verifier")
    graph.add_edge("verifier", "reflector")

    graph.set_finish_point("reflector")

    return graph.compile()




