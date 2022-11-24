from serpapi import GoogleSearch

params = {
  "q": "jeans buy",
  "location": "Austin, Texas, United States",
  "hl": "en",
  "gl": "us",
  "tbm": "shop",
  "api_key": "b2bbaacdf95234778b4aeefe981e23d97e838b5a65cd47b48994a5a46070020f"
}

search = GoogleSearch(params)
results = search.get_dict()
shopping_results = results["shopping_results"]
print(shopping_results)