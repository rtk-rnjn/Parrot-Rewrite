from __future__ import annotations

import random

import discord
from discord import app_commands
from discord.ext import commands

from bot.core import Parrot

CONFESSIONS_CHANNEL_ID = 1464576360558362750
GUILD_ID = 776415524056727582


class ConfessionModal(discord.ui.Modal, title="Anonymous Confession"):
    confession = discord.ui.TextInput(
        label="Your Confession",
        style=discord.TextStyle.paragraph,
        placeholder="Type your anonymous confession here...",
        required=True,
        max_length=1950,
    )

    async def on_submit(self, interaction: discord.Interaction[Parrot]) -> None:
        channel = interaction.client.get_channel(CONFESSIONS_CHANNEL_ID)
        if channel is None:
            await interaction.response.send_message("Confessions channel not found.", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)
        random_adjective = interaction.client.assets.random_adjective.title()
        random_noun = random.choice(interaction.client.assets.nouns).title()
        name = f"{random_adjective} {random_noun}"
        embed = discord.Embed(
            title=f"Confession by {name}",
            description=self.confession.value,
            color=discord.Color.purple(),
            timestamp=discord.utils.utcnow(),
        )
        if isinstance(channel, discord.abc.Messageable):
            await channel.send(embed=embed)
        await interaction.followup.send(f"Your confession has been sent anonymously as `{name}`!", ephemeral=True)


class ConfessionCommands(commands.Cog):
    """Commands related to confessions."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="confess", description="Make an anonymous confession.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def confess(self, interaction: discord.Interaction) -> None:
        """Make an anonymous confession."""
        modal = ConfessionModal()
        await interaction.response.send_modal(modal)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """Listen for messages in the confessions channel and delete non-embed messages."""
        if message.channel.id != CONFESSIONS_CHANNEL_ID:
            return

        if message.author.bot:
            return

        if await self.bot.is_owner(message.author):
            return

        COMMAND = "</confess:1464579894192373903>"

        if not message.embeds:
            await message.delete(delay=0)
            await message.channel.send(
                f"{message.author.mention}, please use the {COMMAND} command to make anonymous confessions.", delete_after=10
            )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ConfessionCommands(bot), guilds=[discord.Object(id=GUILD_ID)])
