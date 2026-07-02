"""Application entry point."""

from graph.workflow import build_graph
from models.state import ResearchState
from models.enums import Route, CacheStatus

def main() -> None:
    """Run the research workflow."""

    topic = input("Enter a research topic: ")

    state: ResearchState = {
    "topic": topic,
    "research_notes": "",
    "report": "",
    "route": Route.RESEARCH,
    "cache_status":CacheStatus.MISS,
    }

    graph = build_graph()

    result = graph.invoke(state)
    print(result)
    print("\n")
    print(result["report"])


if __name__ == "__main__":
    main()