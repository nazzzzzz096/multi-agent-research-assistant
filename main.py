"""Application entry point."""

from agents.research_agent import ResearchAgent


def main() -> None:
    """Run the research agent."""
    topic = input("Enter a research topic: ")

    researcher = ResearchAgent()

    result = researcher.research(topic)

    print("\n")
    print("=" * 80)
    print(result)
    print("=" * 80)


if __name__ == "__main__":
    main()