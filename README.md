# AURORA – Autonomous Agentic AI Research Assistant

AURORA is a fully autonomous, multi-agent research assistant designed to support exploratory research in emerging scientific domains.  
The system decomposes the research process into specialized agents that plan, retrieve, analyze, verify, and reflect on academic knowledge while maintaining long-term memory.

---

## 1. Motivation

Research in emerging domains is often fragmented, time-consuming, and repetitive.  
Researchers must manually search papers, synthesize findings, verify correctness, and often repeat similar analyses across sessions.

AURORA aims to reduce this burden by:
- Automating research planning and execution
- Integrating external academic knowledge
- Verifying analysis correctness
- Persisting knowledge across runs using long-term memory

---

## 2. Key Idea

Instead of a single monolithic AI model, AURORA uses a **multi-agent architecture**, where each agent performs a specific cognitive role.  
Agents are orchestrated deterministically using **LangGraph**, ensuring structured and explainable execution.

---

## 3. System Architecture

The system follows a linear, verifiable agent pipeline:

**Planner → Researcher → Analyzer → Verifier → Reflector**

### Agent Responsibilities

1. **Planner Agent**
   - Interprets the research topic
   - Decides analysis depth and overall research strategy

2. **Researcher Agent**
   - Retrieves relevant academic papers using the arXiv API
   - Extracts paper titles and summaries

3. **Analyzer Agent**
   - Synthesizes insights from retrieved research
   - Performs comparative and thematic analysis

4. **Verifier Agent**
   - Validates factual correctness
   - Removes hallucinations
   - Ensures topic relevance

5. **Reflector Agent**
   - Refines the verified analysis
   - Stores high-quality insights into long-term memory

---

## 4. Memory System

AURORA uses a **persistent vector-based memory** to enable learning across sessions.

- Vector Store: Pinecone (serverless)
- Embeddings: SentenceTransformers (all-MiniLM-L6-v2)
- Retrieval: Semantic similarity search
- Storage Trigger: Final verified analysis

This allows the system to reuse prior knowledge when related topics are queried in the future.

---

## 5. Technology Stack

- **Frontend**: Streamlit
- **Agent Orchestration**: LangGraph
- **Language Model**: LLaMA-3.1-8B via Groq API
- **Academic Source**: arXiv API
- **Vector Database**: Pinecone
- **Embeddings**: SentenceTransformers
- **Environment Management**: python-dotenv

---

## 6. Project Structure

agentic-ai-research-assistant/
│
├── agents/
│ ├── planner.py
│ ├── researcher.py
│ ├── analyzer.py
│ ├── verifier.py
│ └── reflector.py
│
├── graph/
│ └── research_graph.py
│
├── memory/
│ └── pinecone_store.py
│
├── tools/
│ └── llm.py
│
├── app.py
├── requirements.txt
└── README.md

---

## 7. How to Run Locally

Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/agentic-ai-research-assistant.git
cd agentic-ai-research-assistant

Step 2: Install Dependencies
```bash
pip install -r requirements.txt

Step 3: Configure Environment Variables
Create a .env file in the project root:
        GROQ_API_KEY=your_groq_api_key
        PINECONE_API_KEY=your_pinecone_api_key
        PINECONE_INDEX=aurora-memory

Step 4: Run the Application
streamlit run app.py

---

## 8. Live Deployment

Live Application URL:
https://agentic-ai-research-assistant-j7w8eckjmuwejspbdc3jr.streamlit.app

---

## 9. Example Workflow

-User inputs a research topic
-System retrieves relevant prior memory (if available)
-Planner agent defines the research strategy
-Researcher agent retrieves academic papers
-Analyzer agent synthesizes insights
-Verifier agent validates factual correctness
-Reflector agent refines and stores knowledge
-Final structured analysis is presented to the user
---
