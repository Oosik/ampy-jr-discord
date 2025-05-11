import os
from dotenv import load_dotenv
import utils.helpers as helpers

load_dotenv()


def get_token():
    """
    Returns the bot token based on the current environment.

    Returns
    -------
    str
        The token for either the development or production environment.
    """
    if (helpers.is_dev()):
        return os.getenv('DEV_TOKEN')
    else:
        return os.getenv('PROD_TOKEN')
    

    
def get_guild_id():
    """
    Returns the guild ID for the bot.
    
    Returns
    -------
    int
        The guild ID.
    """
    if (helpers.is_dev()):
        return os.getenv('DEV_GUILD')
    else:
        return os.getenv('PROD_GUILD')

def get_env(value):
    """
    Retrieves the value of an environment variable.

    Parameters
    ----------
    value : str
        The name of the environment variable to retrieve.

    Returns
    -------
    str
        The value of the environment variable, or None if the variable does not exist.
    """
    return os.getenv(value)