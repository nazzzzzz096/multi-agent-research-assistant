from tools.tavily_search import TavilySearchProvider

search = TavilySearchProvider()

result = search.search("Latest AI trends")

print(result)