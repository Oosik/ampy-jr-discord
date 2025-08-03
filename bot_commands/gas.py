import prettytable as pt
from utils import run_curl
from utils.helpers import get_etherscan_key

def gas():
    """
    Grabs the current gas numbers (fast, proposed, and safe) and sends them in a formatted string.

    Returns
    -------
    str
        A formatted string containing a table of the metrics.
    """
    ##
    ## URL for the API
    url = f'https://api.etherscan.io/v2/api?chainid=1&module=gastracker&action=gasoracle&apikey={get_etherscan_key()}' 

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
    table.add_row(['Fast', '{:,.2f} gwei'.format(float(data['result']['FastGasPrice']))])
    table.add_row(['Proposed', '{:,.2f} gwei'.format(float(data['result']['ProposeGasPrice']))])
    table.add_row(['Safe', '{:,.2f} gwei'.format(float(data['result']['SafeGasPrice']))])

    return table