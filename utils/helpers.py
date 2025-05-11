import requests, sys
from config.settings import get_env


def is_dev():
    """
    Checks if the bot is running in dev mode or not.
    """
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        return True
        
    return False



def run_curl(url, headers=None):
    """
    Make a GET request to the given URL and return a JSON response.
    
    Parameters
    ----------
    url : str
        The URL to query.
    headers : dict
        A dictionary of headers to pass to the request.
    
    Returns
    -------
    data : dict
        A dictionary of the JSON response, or {'Status': 'Error', 'Message': <error message>} if the request fails.
    """
    
    ##
    ## attempt to get data from API
    ## if it fails, return error message
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {'Status': 'Error', 'Message': 'Error: likely due to rate limiting, sit tight for 2 minutes & try again.'}

    ##
    ## check for 200 response
    # response.status_code = 403
    if response.status_code != 200:
        return {'Status': 'Error', 'Message': f"Error fetching data from API. Status: {response.status_code}. Please alert an admin."}
    
    ##
    ## parse the JSON response
    data = response.json()
    return data


def get_coingecko_key(url):
    """
    Appends the CoinGecko API key to the URL if not in development mode.

    Parameters
    ----------
    url : str
        The URL to which the API key should be appended.

    Returns
    -------
    str
        The original URL if in development mode, otherwise the URL appended with the CoinGecko API key.
    """
    if (is_dev()):
        return url
    else:
        return url + '&x_cg_demo_api_key=' + get_env('COINGECKO_KEY')

def get_alchemy_key():
    """
    Retrieves the Alchemy API key from the environment variables.

    Returns
    -------
    str
        The Alchemy API key from the environment variables.
    """
    return get_env('ALCHEMY_KEY')

def get_etherscan_key():
    """
    Retrieves the Etherscan API key from the environment variables.

    Returns
    -------
    str
        The Etherscan API key from the environment variables.
    """
    return get_env('ETHERSCAN_KEY')