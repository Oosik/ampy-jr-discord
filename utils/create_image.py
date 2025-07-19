import os
import bot_commands as cmd
from PIL import Image, ImageDraw, ImageFont

def create_image(command):
    """
    Generates an image containing text table derived from a command.

    Args:
        command (str): The command to generate the image for.

    Returns:
        str: The file path of the saved image.

    The function processes the command to generate a text table, 
    and uses this text to draw on an image. It calculates text bounding box
    dimensions to create a correctly sized image and saves it as a JPEG file.
    """

    if command == "apy":
        table = cmd.apy()
        table = table.get_string()
        table = table.replace('\U0001F680', 'B ')
    elif command == "price":
        table = cmd.price('amp-token')
        table = table.get_string()
    elif command == "tvl":
        table = cmd.tvl()
        table = table.get_string()
    elif command == "mc":
        table = cmd.mc('amp-token')
        table = table.get_string()
    elif command == "gas":
        table = cmd.gas()
        table = table.get_string()
    elif command == "price.anvil":
        table = cmd.price('anvil')
        table = table.get_string()
    elif command == "mc.anvil":
        table = cmd.mc('anvil')
        table = table.get_string()
		

    base_dir = os.path.dirname(__file__)
    font_path = os.path.join(base_dir, "..", "UbuntuMono-R.ttf")
        
    fnt = ImageFont.truetype(os.path.abspath(font_path), 30)
    
    ##
    ## create a blank image that we can measure the text bounding box
    img = Image.new('RGB', (1000, 1000), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    bbox = d.textbbox((0, 0), f'{table}', font=fnt)
    
    ##
    ## create the final image
    img = Image.new('RGB', (bbox[2] + 40, bbox[3] + 40), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.multiline_text((20, 20), f'{table}', font=fnt, fill=(0, 0, 0))

    img_path = os.path.join(base_dir, "..", f'img/{command}.jpg')
    img.save(img_path, 'JPEG')

    return img_path