import discord, utils

class ImageUI(discord.ui.View):

    def __init__(self, the_command):
        """
        Parameters
        ----------
        the_command : Command
            The command object that this UI should work with.
        ctx : Context
            The context that this UI was created in.
        """
        super().__init__()
        self.the_command = the_command

    @discord.ui.button(label="Ugly? View image instead.", style=discord.ButtonStyle.primary, custom_id="view_image_button")
    
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        """
        Called when the button on the UI is pressed.

        Parameters
        ----------
        interaction: discord.Interaction
            The interaction object that triggered this function.
        button: discord.ui.Button
            The button that was pressed.

        Returns
        -------
        None

        Notes
        -----
        This function disables the button and edits the message it was a part of.
        It then creates an image using utils.create_image() and sends it in the same channel as the message.
        """
        button.disabled = True
        await interaction.response.edit_message(view=self)

        img = utils.create_image(self.the_command)
        file = discord.File(img, filename=f"{self.the_command}.jpg")
        
        # await message.delete()
        await interaction.message.edit(content=None,attachments=[file], view=None)