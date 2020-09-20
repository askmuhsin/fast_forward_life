import requests

req_url = 'http://localhost:65481/api/search'

def search(search_query, req_url=req_url, top_k=2):
    r = requests.post(req_url, json={
        'top_k': top_k, 'data': [search_query]
    })
    res = r.json()
    return res


def get_matches_info(search_query):
    res = search(search_query)
    return result['search']['docs'][0]['matches']
