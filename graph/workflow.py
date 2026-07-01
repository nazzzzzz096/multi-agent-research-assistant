"""LangGraph workflow definition."""

from langgraph.graph import END, START, StateGraph

from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from models.state import ResearchState

research_agent = ResearchAgent()
writer_agent = WriterAgent()


def research_node(state: ResearchState) -> ResearchState:
    """Execute the research agent."""
    return research_agent.research(state)


def writer_node(state: ResearchState) -> ResearchState:
    """Execute the writer agent."""
    return writer_agent.write_report(state)


def build_graph():
    """Build and compile the workflow graph."""

    graph = StateGraph(ResearchState)

    graph.add_node("research", research_node)
    graph.add_node("writer", writer_node)

    graph.add_edge(START, "research")
    graph.add_edge("research", "writer")
    graph.add_edge("writer", END)

    return graph.compile()