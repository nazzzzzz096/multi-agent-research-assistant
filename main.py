"""Application entry point."""

from graph.workflow import build_graph
from models.state import ResearchState


def main() -> None:
    """Run the research workflow."""

    topic = input("Enter a research topic: ")

    state: ResearchState = {
    "topic": topic,
    "research_notes": "",
    "report": "",
    }

    graph = build_graph()

    result = graph.invoke(state)

    print("\n")
    print(result["report"])


if __name__ == "__main__":
    main()