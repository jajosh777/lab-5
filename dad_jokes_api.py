import requests

DAD_JOKE_API_URL = 'https://icanhazdadjoke.com/'

DAD_JOKE_SEARCH_URL = f'{DAD_JOKE_API_URL}/search'

def main():
    
    jokes = search_dad_jokes('cow')
    pass

def search_dad_jokes (search_term, page=1, limit=20):

    
    query_params = {
        'page': page,
        'limit': limit,
        'term': search_term
    }

    
    header_params = {
    'Accept': 'application/json'
    }

    
    print(f'Searching for dad jokes containing "{search_term}"...', end='') 
    resp_msg = requests.get(DAD_JOKE_SEARCH_URL, params=query_params, headers=header_params)

    
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        jokes_list = [j['joke'] for j in body_dict['results']]
        return jokes_list
    else:
        print("failure")
        print (f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

def get_random_dad_joke():
    
    header_params = {
    'Accept': 'application/json'
    }

    
    print('Getting a random dad joke...', end='')
    resp_msg = requests.get (DAD_JOKE_API_URL, headers=header_params)

    
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        return body_dict['joke']
    else:
        print("failure")
        print (f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

if __name__ == "__main__":
    main()