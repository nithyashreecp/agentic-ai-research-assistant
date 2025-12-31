import streamlit as st
from graph.research_graph import build_graph
from memory.pinecone_store import retrieve_similar

# PAGE CONFIG 
st.set_page_config(
    page_title="AURORA – Autonomous Research AI",
    layout="wide"
)

#  SIDEBAR 
with st.sidebar:
    st.markdown("### 🧠 AURORA")
    st.caption("Autonomous Research System")

    st.markdown("---")

    st.markdown("**🧩 Active Agents**")
    st.markdown("""
    - Planner Agent  
    - Researcher Agent  
    - Analyzer Agent 
    - Verifier Agent 
    - Reflector Agent  
    """)

    st.markdown("---")

    st.markdown("**🗂 Memory System**")
    st.markdown("""
    - Vector Store: Pinecone  
    - Embeddings: SentenceTransformers  
    - Retrieval: Semantic Similarity  
    """)

    st.markdown("---")
    st.caption("Designed for emerging scientific domains")

# MAIN HEADER 
st.markdown(
    """
    <div style="text-align:center; padding-top:20px;">
        <h1>🧠 AURORA</h1>
        <h4>Autonomous Understanding & Research Orchestrator for Advanced Science</h4>
        <p style="opacity:0.8;">
        A fully autonomous, memory-augmented agentic research system
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

#  INPUT 
topic = st.text_input("🔬 Enter a research topic", placeholder="e.g., AI for climate modeling")

if st.button("🚀 Run Autonomous Research"):
    graph = build_graph()

    # Retrieve memory
    with st.spinner("🔍 Retrieving prior knowledge from long-term memory..."):
        memory_context = retrieve_similar(topic, top_k=3)

    # Run agents
    with st.spinner("🧠 Agents are reasoning autonomously..."):
        result = graph.invoke({
            "topic": topic,
            "memory": memory_context
        })

    st.markdown("---")

    #  MEMORY 
    st.subheader("🗂 Prior Knowledge Used")
    if memory_context:
        for m in memory_context:
            st.markdown(f"- {m}")
    else:
        st.markdown("_No relevant prior memory found._")

    st.markdown("---")

    #  PLAN 
    st.subheader("📌 Research Plan")
    st.write(result["plan"])

    st.markdown("---")

    #  ANALYSIS 
    st.subheader("📊 Final Analysis")
    st.write(result["final_output"])

    st.markdown("---")

    # SOURCES 
    st.subheader("📚 Papers Referenced")

    if "links" in result and result["links"]:
    for title, link in zip(result["titles"], result["links"]):
        st.markdown(f"- [{title}]({link})")
    else:
    st.markdown("_No paper links available._")






