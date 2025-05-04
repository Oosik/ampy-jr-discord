import prettytable as pt
from utils import run_curl

def apy():
    
    """
    Grabs the 7D and 30D APYs for all flexa collateral pools.

    Returns:
        str: A formatted string containing a table of the pools and their
            respective APYs.
    """
    url = 'https://api.flexa.co/collateral_pools'

    ##
    ## create table
    ## setup columns and alignment
    table = pt.PrettyTable(['Pool', '7D', '30D', '🚀'])
    table.align['Pool'] = 'l'
    table.align['7D'] = 'r'
    table.align['30D'] = 'r'
    table.align['🚀'] = 'c'
    table.padding_width = 0

    ##
    ## attempt to get data from API
    ## if it fails, return error message
    data = run_curl(url)
    
    if 'Status' in data and data['Status'] == 'Error':
        return data['Message']
    
    ##
    ## create table
    for pool in data['data']:
        name = pool['entity']['name']
        if name == 'Nighthawk Wallet':
            name = 'Nighthawk'
            
        apy_short = pool['reward_rate']['7_day']['label']
        apy_long = pool['reward_rate']['30_day']['label']
        
        if pool['boosted']:
            boost = 'X'
        else:
            boost = ' '
        
        table.add_row([name, apy_short, apy_long, boost])

    return table