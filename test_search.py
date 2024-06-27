import requests

def google_search(api_key, cse_id, query, num_results=10):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'num': num_results
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    API_KEY = 'xyz'
    CSE_ID = 'e4daef1ee50734449'
    query = 'Soeldner Consult Landing Zone'
    results = google_search(API_KEY, CSE_ID, query)

    for i, item in enumerate(results.get('items', [])):
        print(f"Result {i+1}:")
        print(f"Title: {item['title']}")
        print(f"Snippet: {item['snippet']}")
        print(f"Link: {item['link']}")
        print()
te
