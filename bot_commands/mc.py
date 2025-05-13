import prettytable as pt
from utils import run_curl
from utils.helpers import get_coingecko_key

def mc(token_id):
    """
    Grabs market cap metrics for the given token ID.

    Parameters
    ----------
    token_id : str
        The ID of the token to query.

    Returns
    -------
    str
        A formatted string containing a table of the metrics.
    """
    url = f'https://api.coingecko.com/api/v3/coins/markets?ids={token_id}&vs_currency=usd'
    url = get_coingecko_key(url)

    ##
    ## create table
    ## setup columns and alignment
    table = pt.PrettyTable(['Metric', 'Value'])
    table.align['Metric'] = 'l'
    table.align['Value'] = 'r'
    table.padding_width = 1
    
    ##
    ## attempt to get data from API
    ## if it fails, return error message
    data = run_curl(url)
    
    if 'Status' in data and data['Status'] == 'Error':
        return data['Message']

    ##
    ## create table
    table.add_row(['Rank', '{:,.0f}'.format(data[0]['market_cap_rank'])])
    table.add_row(['Market Cap', '${:,.0f}'.format(data[0]['market_cap'])])
    table.add_row(['24h Change', '{:,.0f}'.format(data[0]['market_cap_change_24h'])])

    return table