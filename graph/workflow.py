"""LangGraph workflow definition."""

from langgraph.graph import END, START, StateGraph

from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from models.state import ResearchState
from agents.router_agent import RouterAgent
from agents.general_agent import GeneralAgent
from agents.safety_agent import SafetyAgent
from models.enums import CacheStatus
from agents.cache_agent import CacheAgent
research_agent = ResearchAgent()
writer_agent = WriterAgent()
router = RouterAgent()
general = GeneralAgent()
safety = SafetyAgent()
cache = CacheAgent()

def research_node(state: ResearchState) -> ResearchState:
    """Execute the research agent."""
    return research_agent.research(state)


def writer_node(state: ResearchState) -> ResearchState:
    """Execute the writer agent."""
    return writer_agent.write_report(state)

def router_node(state: ResearchState) -> ResearchState:
    """Execute the router agent."""
    return router.route(state)

def general_node(state: ResearchState) -> ResearchState:
    """Execute the general agent."""
    return general.respond(state)


def unsafe_node(state: ResearchState) -> ResearchState:
    """Execute the safety agent."""
    return safety.deny(state)

def route_query(state: ResearchState) -> str:
    """Determine the next node based on the router output."""

    return state["route"].value

def route_cache(state: ResearchState) -> str:
    print("CACHE STATUS:", state["cache_status"])

    if state["cache_status"] == CacheStatus.HIT:
        return "hit"

    return "miss"
def cache_node(state: ResearchState) -> ResearchState:
    """Execute the cache agent."""
    
    return cache.lookup(state)
def build_graph():
    """Build and compile the workflow graph."""

    graph = StateGraph(ResearchState)

    graph.add_node("router", router_node)
    graph.add_node("research", research_node)
    graph.add_node("writer", writer_node)
    graph.add_node("general", general_node)
    graph.add_node("unsafe", unsafe_node)
    graph.add_node("cache", cache_node)

    graph.add_edge(START, "router")

    graph.add_conditional_edges(
        "router",
        route_query,
        {
            "research": "cache",
            "general": "general",
            "unsafe": "unsafe",
        },
    )
    graph.add_conditional_edges(
    "cache",
    route_cache,
    {
        "hit": END,
        "miss": "research",
    },
    )
    graph.add_edge("research", "writer")

    graph.add_edge("writer", END)
    graph.add_edge("general", END)
    graph.add_edge("unsafe", END)

    return graph.compile()