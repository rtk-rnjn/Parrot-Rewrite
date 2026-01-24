from __future__ import annotations

import random

import discord
from discord import app_commands
from discord.ext import commands

from bot.core import Parrot

CONFESSIONS_CHANNEL_ID = 1464576360558362750
GUILD_ID = 776415524056727582


class ConfessionModal(discord.ui.Modal, title="Anonymous Confession"):
    name = discord.ui.TextInput(
        label="Your Anonymous Name (Optional)",
        style=discord.TextStyle.short,
        placeholder="Leave blank for a random name",
        required=False,
        max_length=50,
    )

    confession = discord.ui.TextInput(
        label="Your Confession",
        style=discord.TextStyle.paragraph,
        placeholder="Type your anonymous confession here...",
        required=True,
        max_length=3900,
        min_length=20,
    )

    def __init__(self, *, text: str, random_name: str) -> None:
        super().__init__(timeout=None)
        self.text = text
        self.confession.default = text

        self.random_name = random_name
        self.name.default = random_name

    async def on_submit(self, interaction: discord.Interaction[Parrot]) -> None:
        channel = interaction.client.get_channel(CONFESSIONS_CHANNEL_ID)
        if channel is None:
            await interaction.response.send_message("Confessions channel not found.", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)

        embed = discord.Embed(
            title=f"Confession by {self.name.value or self.random_name}",
            description=self.confession.value,
            color=discord.Color.purple(),
            timestamp=discord.utils.utcnow(),
        )
        if isinstance(channel, discord.abc.Messageable):
            await channel.send(embed=embed)
        await interaction.followup.send(
            f"Your confession has been sent anonymously as `{self.name.value or self.random_name}`!", ephemeral=True
        )


class ConfessionCommands(commands.Cog):
    """Commands related to confessions."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.locked = False
        self.locked_reason = "Maintenance"

    @app_commands.command(name="confess", description="Make an anonymous confession.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    @app_commands.checks.cooldown(1, 10 * 60, key=lambda i: (i.user.id))
    async def confess(
        self, interaction: discord.Interaction[Parrot], *, text: str = commands.parameter(description="Your anonymous confession.")
    ) -> None:
        """Make an anonymous confession."""

        random_adjective = interaction.client.assets.random_adjective.title()
        random_noun = random.choice(interaction.client.assets.nouns).title()
        name = f"{random_adjective} {random_noun}"

        if self.locked:
            await interaction.response.send_message(
                f"The confession system is currently locked. Please try again later.\nReason: **{self.locked_reason}**", ephemeral=True
            )
            return

        modal = ConfessionModal(text=text, random_name=name)
        await interaction.response.send_modal(modal)

    @confess.error
    async def confess_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        """Handle errors for the confess command."""
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                f"You are on cooldown. Please wait {int(error.retry_after)} seconds before using this command again.", ephemeral=True
            )
            return

        await interaction.response.send_message(
            "An unexpected error occurred while processing your confession. Please try again later.", ephemeral=True
        )

    @app_commands.command(name="confession rules", description="View the rules for making confessions.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def confession_rules(self, interaction: discord.Interaction) -> None:
        """View the rules for making confessions."""
        rules = (
            "1. Strictly DO NOT SHARE personal information (yours or others'). This includes names, locations, contact details, etc.\n",
            "2. Confessions must be respectful and non-offensive. Hate speech, harassment, or discriminatory content will not be tolerated.\n",
            "3. No spam or promotional content. Confessions should be genuine and meaningful.\n",
            "4. This is not anonymous general chat. Keep confessions relevant and appropriate for the community.\n",
            "5. The moderators reserve the right to remove any confession that violates these rules or is deemed inappropriate.\n",
        )
        embed = discord.Embed(
            title="Confession Rules", description=rules, color=discord.Color.blue(), timestamp=discord.utils.utcnow()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="confession lock", description="Lock the confession system.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lock_confessions(
        self,
        interaction: discord.Interaction,
        *,
        reason: str = commands.parameter(default="Maintenance", description="Reason for locking confessions."),
    ) -> None:
        """Lock the confession system."""
        self.locked = True
        self.locked_reason = reason
        await interaction.response.send_message(f"The confession system has been locked.\nReason: **{reason}**", ephemeral=True)

    @app_commands.command(name="confession unlock", description="Unlock the confession system.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    @app_commands.checks.has_permissions(manage_channels=True)
    async def unlock_confessions(self, interaction: discord.Interaction) -> None:
        """Unlock the confession system."""
        self.locked = False
        self.locked_reason = "Maintenance"
        await interaction.response.send_message("The confession system has been unlocked.", ephemeral=True)

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

        if not message.content.strip():
            return

        await message.delete(delay=0)
        if self.locked:
            return

        await message.channel.send(
            f"{message.author.mention}, please use the {COMMAND} command to make anonymous confessions.", delete_after=10
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ConfessionCommands(bot), guilds=[discord.Object(id=GUILD_ID)])
