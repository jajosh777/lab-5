import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = 'AF6YvHf4gn4-iCa_xDbNwJ1NPGdpgXRy'

def main():
    paste_url = post_new_paste('Whatever paste', 'a bunch of crap')
    pass

def post_new_paste(title, body_text, expiration='10M', listed=True):
    """Creates a new public PasteBin paste
    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): How long the paste will last. (See https://pastebin.com/doc_api). Defaults to '10M'.
        listed (bool, optional): Whatever the past is listed or not. Defaults to True.
    Returns:
        str: URL of the new paste. None if unsuccessful.
    """

    # Create dictionary of parameter values
    params = {
    'api_dev_key': DEVELOPER_API_KEY,
    'api_option': 'paste',
    'api_paste_code': body_text,
    'api_paste_name': title,
    'api_paste_expire_date': expiration,
    'api_paste_private': 0 if listed else 1

    }

    # Send the POST request to the PasteBin API
    print("Posting new paste to PasteBin...", end='')
    resp_msg = requests.post(API_POST_URL, data=params)

    # Check if paste was created successfully
    if resp_msg.ok:
        print('success')
        # print(f'URL of new paste: {resp_msg.text}')
        return resp_msg.text
    else:
        print("failure")
        print (f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

    pass

if __name__ == "__main__":
    main()