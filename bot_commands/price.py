import prettytable as pt
from utils import run_curl
from utils.helpers import get_coingecko_key

def price(token_id):
    """
    Grabs price, volume, high, low, 24H change, ATH, and ATL metrics for a given token ID and returns a formatted string containing a table of the metrics.

    Parameters
    ----------
    token_id : str
        The ID of the token to query.

    Returns
    -------
    str
        A formatted string containing a table of the metrics.
    """
    ##
    ## URL for the API
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
    table.add_row(['Price', '${:,.6f}'.format(data[0]['current_price'])])
    table.add_row(['24H Volume', '${:,.0f}'.format(data[0]['total_volume'])])
    table.add_row(['High 24H', '${:,.6f}'.format(data[0]['high_24h'])])
    table.add_row(['Low 24H', '${:,.6f}'.format(data[0]['low_24h'])])
    table.add_row(['24H Change', '{:,.2f}'.format(data[0]['price_change_percentage_24h']) + '%'])
    table.add_row(['ATH', '${:,.6f}'.format(data[0]['ath'])])
    table.add_row(['ATL', '${:,.6f}'.format(data[0]['atl'])])

    return table