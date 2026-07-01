"""Application entry point."""

from llm.gemini_client import GeminiClient


def main() -> None:
    """Run a simple Gemini test."""

    llm = GeminiClient()

    response = llm.generate(
        "Explain what an AI agent is in three sentences."
    )

    print(response)


if __name__ == "__main__":
    main()