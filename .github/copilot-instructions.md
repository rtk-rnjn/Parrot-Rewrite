### Create a Minimal Discord Bot with discord.py

Source: https://discordpy.readthedocs.io/en/stable/quickstart

This Python code demonstrates how to create a basic Discord bot using the discord.py library. It sets up default intents, enables the message content intent, and defines event handlers for when the bot is ready and when a message is received. The bot responds with 'Hello!' when it detects a message starting with '$hello'. It requires a Discord bot token to run.

```python
# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('your token here')
```

--------------------------------

### Run Python Script on Windows

Source: https://discordpy.readthedocs.io/en/stable/quickstart

Command to execute a Python script named 'example_bot.py' using the Python 3 interpreter on Windows.

```bash
$ py -3 example_bot.py
```

--------------------------------

### Run Python Script on Other Systems

Source: https://discordpy.readthedocs.io/en/stable/quickstart

Command to execute a Python script named 'example_bot.py' using the Python 3 interpreter on non-Windows systems (e.g., Linux, macOS).

```bash
$ python3 example_bot.py
```

--------------------------------

### Handle Discord Onboarding Events

Source: https://discordpy.readthedocs.io/en/stable/

These events relate to the Discord onboarding feature, allowing new members to be guided through server setup. They cover creating, updating, and deleting onboarding prompts and configurations.

```python
discord.Guild.onboarding() -> discord.Onboarding
```

```python
discord.AuditLogAction.onboarding_create
```

```python
discord.AuditLogAction.onboarding_update
```

```python
discord.AuditLogAction.onboarding_prompt_create
```

```python
discord.AuditLogAction.onboarding_prompt_update
```

```python
discord.AuditLogAction.onboarding_prompt_delete
```

--------------------------------

### Using setup_hook in discord.py Client Subclass

Source: https://discordpy.readthedocs.io/en/stable/migrating

This example shows how to use the `setup_hook()` method, introduced in discord.py v2.0, by subclassing `discord.Client`. The `setup_hook()` method is executed after logging in but before connecting to the Discord gateway, suitable for asynchronous setup tasks.

```Python
import discord

class MyClient(discord.Client):
    async def setup_hook(self):
        print('This is asynchronous!')

client = MyClient()
client.run(TOKEN) # TOKEN should be defined
```

--------------------------------

### Python - Asynchronous Extension Setup

Source: https://discordpy.readthedocs.io/en/stable/migrating

Demonstrates the change in extension setup functions from synchronous to asynchronous in discord.py v2.0. The `setup` function now needs to be a coroutine and `bot.add_cog` must be awaited.

```Python
# before
def setup(bot):
    bot.add_cog(MyCog(bot))

# after
async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

--------------------------------

### Install discord.py with Voice Support

Source: https://discordpy.readthedocs.io/en/stable/intro

Installs discord.py along with the necessary dependencies for voice support using pip.

```shell
python3 -m pip install -U discord.py[voice]
```

--------------------------------

### Manage App Command Installs

Source: https://discordpy.readthedocs.io/en/stable/

Controls the installation parameters for application commands, specifying where and how they can be installed within a Discord server. This includes options for guilds and users.

```Python
discord.app_commands.AppCommand.allowed_installs
discord.app_commands.Command.allowed_installs
discord.app_commands.ContextMenu.allowed_installs
discord.app_commands.Group.allowed_installs
commands.Bot.allowed_installs
discord.app_commands.allowed_installs()
```

--------------------------------

### Configure Bot Setup Hooks and Logging in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details the `setup_hook` method for both `discord.Client` and `commands.Bot`, which is used for asynchronous setup tasks. It also includes the utility for setting up logging.

```python
discord.Client.setup_hook()
commands.Bot.setup_hook()
discord.utils.setup_logging()
```

--------------------------------

### Install discord.py (Python 3)

Source: https://discordpy.readthedocs.io/en/stable/intro

Installs or upgrades the discord.py library using pip for Python 3. This is the standard installation command.

```shell
python3 -m pip install -U discord.py
```

--------------------------------

### Discord App Info Custom Install URL

Source: https://discordpy.readthedocs.io/en/stable/

Provides a custom URL for installing an application.

```python
discord.AppInfo.custom_install_url
```

--------------------------------

### Python: Start a task after the bot is ready

Source: https://discordpy.readthedocs.io/en/stable/ext/tasks/index

This example shows how to ensure a background task only starts after the bot has successfully connected and is ready. The `before_printer` method uses `await self.bot.wait_until_ready()` to pause execution until the bot is ready, then the `printer` task begins.

```Python
from discord.ext import tasks, commands\n\nclass MyCog(commands.Cog):\n    def __init__(self, bot):\n        self.index = 0\n        self.bot = bot\n        self.printer.start()\n\n    def cog_unload(self):\n        self.printer.cancel()\n\n    @tasks.loop(seconds=5.0)\n    async def printer(self):\n        print(self.index)\n        self.index += 1\n\n    @printer.before_loop\n    async def before_printer(self):\n        print('waiting...')\n        await self.bot.wait_until_ready()\n
```

--------------------------------

### Example Context Menu Commands - discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides examples of creating context menu commands for reacting to messages and banning users. These demonstrate the usage of the @discord.app_commands.context_menu decorator.

```Python
@app_commands.context_menu()
async def react(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message('Very cool message!', ephemeral=True)

@app_commands.context_menu()
async def ban(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f'Should I actually ban {user}...', ephemeral=True)
```

--------------------------------

### Setup Discord Logging Manually

Source: https://discordpy.readthedocs.io/en/stable/logging

Provides a way to set up discord.py's logging configuration without using Client.run(), using the discord.utils.setup_logging() function.

```python
import discord

discord.utils.setup_logging()

# or, for example
discord.utils.setup_logging(level=logging.INFO, root=False)
```

--------------------------------

### Get Short Documentation

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Gets the short documentation string for the command. This is typically the 'brief' attribute or the first line of the 'help' attribute if 'brief' is empty.

```python
_property _short_doc
```

--------------------------------

### Starting and Stopping Tasks and Clients in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to start and stop asynchronous tasks and the Discord client using discord.py. This includes methods for `tasks.Loop`, `discord.Client`, and `commands.Bot`.

```python
client.start()
# Starting the Discord client

bot.start()
# Starting the bot

tasks.Loop.start()
# Starting a loop task

tasks.Loop.stop()
# Stopping a loop task

view.stop()
# Stopping a UI view
```

--------------------------------

### Add support for user-installable apps

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enables user-installable applications, allowing users to install apps directly. This adds attributes to commands and context menus to control installation, along with new enums and interaction methods.

```Python
from discord.app_commands import app_commands
import discord

# New attributes for installation control
app_commands.Command.allowed_installs: list[str]
app_commands.AppCommand.allowed_installs: list[str]
app_commands.ContextMenu.allowed_installs: list[str]

# New decorators for installation
app_commands.allowed_installs()
app_commands.guild_install()
app_commands.user_install()

# New enum for installation type
class AppInstallationType:
    guild: str
    user: str

# New interaction attributes
Interaction.context: discord.InteractionContext
Interaction.is_guild_integration(): bool
Interaction.is_user_integration(): bool

```

--------------------------------

### Discord.py Example Cog with Special Methods

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

An example of a Discord.py cog demonstrating the implementation of various special methods for customization and event handling, including custom naming.

```Python
class MyCog(commands.Cog, name='Example Cog'):
    def cog_unload(self):
        print('cleanup goes here')

    def bot_check(self, ctx):
        print('bot check')
        return True

    def bot_check_once(self, ctx):
        print('bot check once')
        return True

    async def cog_check(self, ctx):
        print('cog local check')
        return await ctx.bot.is_owner(ctx.author)

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    async def cog_before_invoke(self, ctx):
        print('cog local before: {0.command.qualified_name}'.format(ctx))

    async def cog_after_invoke(self, ctx):
        print('cog local after: {0.command.qualified_name}'.format(ctx))

    @commands.Cog.listener()
    async def on_message(self, message):
        pass
```

--------------------------------

### Install discord.py on Windows

Source: https://discordpy.readthedocs.io/en/stable/intro

Installs or upgrades the discord.py library using pip for Python 3 on Windows systems, using the 'py' launcher.

```shell
py -3 -m pip install -U discord.py
```

--------------------------------

### Define Hybrid Command Groups and Sub-commands

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

This example shows how to create hybrid command groups and sub-commands using `Bot.hybrid_group()`. The `tag` group has a `fallback` command named `get` for direct invocation, and a `create` sub-command.

```Python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.hybrid_group(fallback="get")
async def tag(ctx, name):
    await ctx.send(f"Showing tag: {name}")

@tag.command()
async def create(ctx, name):
    await ctx.send(f"Created tag: {name}")

# Remember to sync your CommandTree for slash commands to appear
# await bot.tree.sync()

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Asynchronous Bot Setup Hook

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

A coroutine to set up the bot asynchronously after login but before WebSocket connection. Overwrite this to perform custom setup. It's called once in `login()` before any events are dispatched.

```Python
async def _setup_hook():
    # Perform asynchronous setup here
    pass
```

--------------------------------

### MinimalHelpCommand: Get Opening Note

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns the help command's opening note, primarily useful for internationalization (i18n). The default implementation provides instructions on how to get more information about commands or categories.

```Python
def get_opening_note():
    """Returns help command’s opening note. This is mainly useful to override for i18n purposes.
    The default implementation returns
    Use `{prefix}{command_name} [command]` for more info on a command.
    You can also use `{prefix}{command_name} [category]` for more info on a category.

    Returns
    -------
    str
        The help command opening note.
    """
    pass
```

--------------------------------

### Install Voice Dependencies on Debian-based Linux

Source: https://discordpy.readthedocs.io/en/stable/intro

Installs the required system-level dependencies (libffi, libnacl, python3-dev) for voice support on Debian-based Linux distributions using apt.

```shell
$ apt install libffi-dev libnacl-dev python3-dev
```

--------------------------------

### Discord Onboarding Prompt Types

Source: https://discordpy.readthedocs.io/en/stable/

Enumerates the different types of prompts that can be used within Discord's onboarding feature to guide new members.

```python
discord.OnboardingPromptType
```

```python
discord.OnboardingPrompt
```

```python
discord.OnboardingPromptOption
```

--------------------------------

### Create and Load a Discord.py Extension

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/extensions

This snippet demonstrates how to create a basic Discord.py extension with a 'hello' command and the required 'setup' function to add it to the bot. It also shows how to load this extension using 'Bot.load_extension()'.

```Python
from discord.ext import commands

@commands.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.display_name}.')

async def setup(bot):
    bot.add_command(hello)

# To load this extension:
# await bot.load_extension('hello')
```

--------------------------------

### Handle No Entry Point Error in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This exception is raised when a discord.py extension module lacks the required `setup` entry point function. It inherits from ExtensionError and includes the extension name.

```Python
class NoEntryPointError(ExtensionError):
    """An exception raised when an extension does not have a `setup` entry point function.

    This inherits from `ExtensionError`
    """
    pass

```

--------------------------------

### Get Activity Creation Timestamp

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds `Activity.created_at` to retrieve the timestamp when an activity was started. This is useful for tracking the duration or start time of user activities.

```Python
activity.created_at
```

--------------------------------

### Generate Discord OAuth2 Install URL

Source: https://discordpy.readthedocs.io/en/stable/

Generates a URL to install an application to a Discord guild using OAuth2. This function requires the client ID and can optionally include scopes and permissions.

```python
discord.utils.oauth_url(client_id: int, *, scopes: Sequence[str] = ..., permissions: discord.Permissions = ..., redirect_uri: str | None = ..., **params) -> str
```

--------------------------------

### Python Context Menu Decorator Example

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates how to create a context menu command using the `@context_menu()` decorator in discord.py. This example shows a basic context menu for messages.

```Python
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.context_menu(name="Show Message Info")
async def show_message_info(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(f"Message content: {message.content}")

@client.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {client.user}')

client.run('YOUR_BOT_TOKEN')
```

--------------------------------

### discord.py Allowed Installs Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

The allowed_installs decorator specifies the contexts (guilds and users) where a command can be installed. Discord manages this installation server-side, and the decorator does not trigger error handlers. It is ignored in subcommands due to Discord limitations. Available since version 2.4.

```Python
@app_commands.command()
@app_commands.allowed_installs(guilds=False, users=True)
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in users by default!')
```

--------------------------------

### discord.py User Install Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

The user_install decorator indicates that a command should be installed for users. This installation is managed server-side by Discord, and the decorator does not trigger error handlers. It is ignored in subcommands due to a Discord limitation. Available since version 2.4.

```Python
@app_commands.command()
@app_commands.user_install()
async def my_user_install_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in users by default!')
```

--------------------------------

### Running Discord Bots and Commands

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of running Discord bots using the `run()` method for both `discord.Client` and `commands.Bot`. It also includes a function for running converters.

```python
discord.Client.run()
commands.Bot.run()
commands.run_converters()
```

--------------------------------

### Get Short Documentation of discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Gets the "short" documentation of a command. By default, this is the `brief` attribute. If that is empty, the first line of the `help` attribute is used instead.

```python
_property _short_doc
```

--------------------------------

### Get Subscription Current Period

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the start and end dates of the current subscription period.

```python
discord.Subscription.current_period_end
discord.Subscription.current_period_start
```

--------------------------------

### AppInstallationType Class in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Represents the installation location of an application command. It indicates whether the integration is a guild install or a user install. New in version 2.4.

```python
class AppInstallationType:
    guild: bool
    user: bool
```

--------------------------------

### Discord Integration Type Configuration

Source: https://discordpy.readthedocs.io/en/stable/

Configuration related to OAuth2 install parameters for Discord integrations, allowing customization of the installation process.

```python
discord.IntegrationTypeConfig.oauth2_install_params
```

--------------------------------

### Setup Bot Logging

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Configures the root logger for the bot. By default, only the library logger ('discord') is set up. Setting this to True also sets up the root logger.

```Python
client.setup_logging(True) # Sets up the root logger as well
```

--------------------------------

### Greedy Converter Example

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Demonstrates the use of the `Greedy` converter to consume multiple arguments for one parameter. In this example, `Greedy[int]` collects all integer arguments until a non-integer is encountered, which is then assigned to the `reason` parameter.

```Python
from discord.ext import commands

@commands.command()
async def test(ctx, numbers: commands.Greedy[int], reason: str):
    await ctx.send("numbers: {}, reason: {}".format(numbers, reason))
```

--------------------------------

### discord.py: Running the Client (Old vs. New)

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_async

Demonstrates the change in how to run the discord.py client. Previously, login and run were separate calls. In newer versions, client.run() takes the token directly and handles the event loop.

```Python
client.login('token')
client.run()
```

```Python
client.run('token')
```

--------------------------------

### Get Root Parent of discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the root parent of this command. If the command has no parents, it returns `None`. For example, in commands `?a b c test`, the root parent is `a`.

```python
_property _root_parent
```

--------------------------------

### Get Parents of discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the parents of this command. If the command has no parents, it returns an empty list. For example, in commands `?a b c test`, the parents are `[c, b, a]`.

```python
_property _parents
```

--------------------------------

### Example Parameter Description - discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates describing a command parameter using the @discord.app_commands.describe decorator, specifying the description for the 'member' parameter.

```Python
@app_commands.command(description='Bans a member')
@app_commands.describe(member='the member to ban')
async def ban(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f'Banned {member}')
```

--------------------------------

### Get Qualified Name of discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the fully qualified command name, including the full parent name and the command name itself. For example, in `?one two three`, the qualified name would be `one two three`.

```python
_property _qualified_name
```

--------------------------------

### Get Full Parent Name of discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the fully qualified parent command name, which is the base command name required to execute it. For example, in `?one two three`, the parent name would be `one two`.

```python
_property _full_parent_name
```

--------------------------------

### Discord.py: Session Start Limits and Total Children Count

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access session start limits and the total count of children for UI views and modals.

```python
session_start_limits.total
view.total_children_count
modal.total_children_count
```

--------------------------------

### Approximate User Install Count in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds `AppInfo.approximate_user_install_count` to provide an approximate count of user installs for an application.

```Python
Add `AppInfo.approximate_user_install_count` (GH-9915)
```

--------------------------------

### Basic Discord Bot Event Handling

Source: https://discordpy.readthedocs.io/en/stable/intro

A simple discord.py bot example that logs in, prints a message when ready, and prints incoming messages. Requires the 'message_content' intent.

```python
# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')
```

--------------------------------

### DefaultHelpCommand Methods

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Outlines the methods available in the DefaultHelpCommand class for generating and formatting help messages, including retrieving command signatures, sending paginated output, and adding command details.

```python
def shorten_text(text: str) -> str
def get_ending_note() -> str
def get_command_signature(command: Command) -> str
def add_indented_commands(commands: Sequence[Command], *, heading: str, max_size: Optional[int] = None)
def add_command_arguments(command: Command)
async def send_pages()
def add_command_formatting(command)
```

--------------------------------

### Discord.py: Get Prompt

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves an onboarding prompt by its ID. This method is part of the discord.Onboarding class.

```python
discord.Onboarding.get_prompt()
```

--------------------------------

### Discord Onboarding and Select Option Description

Source: https://discordpy.readthedocs.io/en/stable/

Provides access to the description attribute for OnboardingPromptOption and SelectOption, used in onboarding flows and select menus.

```python
discord.OnboardingPromptOption.description
discord.SelectOption.description
```

--------------------------------

### Fix cchardet Installation with Speed Extras

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Prevents the `cchardet` library from being installed on Python versions 3.10 and above when the `speed` extras are used. This avoids unnecessary dependency installations for newer Python versions.

```Python
# Conceptual change in setup.py or pyproject.toml
# The fix involves conditional installation logic based on Python version and extras.

# Example (conceptual, in setup.py):
# install_requires = [...] 
# extras_require = {
#     'speed': ['cchardet', ...]
# }
# 
# # Logic to conditionally include cchardet based on sys.version_info
# if sys.version_info >= (3, 10):
#     extras_require['speed'].remove('cchardet')

# This is a build/packaging configuration change.
```

--------------------------------

### Discord.py: Get Opening Note

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the opening note for help messages. This is relevant for MinimalHelpCommand.

```python
commands.MinimalHelpCommand.get_opening_note()
```

--------------------------------

### discord.py Guild Install Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

The guild_install decorator signifies that a command is intended for installation within guilds. Discord handles this installation process server-side, and the decorator does not invoke error handlers. Due to Discord limitations, it has no effect on subcommands. Available since version 2.4.

```Python
@app_commands.command()
@app_commands.guild_install()
async def my_guild_install_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in guilds by default!')
```

--------------------------------

### Discord.py ChannelSelect Example

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This example demonstrates how to create a `ChannelSelect` component within a discord.py view. The callback function receives the interaction and the `ChannelSelect` object, and it sends a message mentioning the first selected channel.

```python
class MyView(discord.ui.LayoutView):
    action_row = discord.ui.ActionRow()

    @action_row.select(cls=ChannelSelect, channel_types=[discord.ChannelType.text])
    async def select_channels(self, interaction: discord.Interaction, select: ChannelSelect):
        return await interaction.response.send_message(f'You selected {select.values[0].mention}')
```

--------------------------------

### Get Command by Name in discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a `Command` from the internal list of commands, which can also be used to get aliases. The name can be fully qualified (e.g., `'foo bar'`) to get a subcommand. Returns `None` if not found.

```python
get_command(_name_ , _/_)
```

--------------------------------

### Implement Custom Help Command in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Demonstrates how to create a custom help command by subclassing discord.py's MinimalHelpCommand. This example shows how to override get_command_signature and how to bind the custom help command to a cog.

```python
class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command
```

--------------------------------

### Fetch Session Start Limits in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds `AutoShardedClient.fetch_session_start_limits()` to retrieve information about session start limits for auto-sharded clients.

```Python
Add `AutoShardedClient.fetch_session_start_limits()` (GH-10007)
```

--------------------------------

### Discord Onboarding Prompts and Role IDs

Source: https://discordpy.readthedocs.io/en/stable/

Details attributes for onboarding prompts, including whether fields are required and the role IDs associated with prompt options.

```python
discord.OnboardingPrompt.required
discord.OnboardingPromptOption.role_ids
discord.OnboardingPromptOption.roles
```

--------------------------------

### Using Discord Select Menus and String Options in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to work with Discord's UI components, specifically select menus and string options for application commands, using discord.py.

```python
app_command_option_type.string
# Representing a string option type for commands

component_type.string_select
# Representing a string select menu component type
```

--------------------------------

### Discord.py: Managing Guild Templates

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of accessing guild templates and generating them using the 'templates()' method.

```python
guild.templates()
ui_item.template
```

--------------------------------

### Managing Stage Instances and Channels in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of interacting with Stage Instances and Stage Channels in discord.py. This covers creating, deleting, updating instances, and accessing stage-related permissions and messages.

```python
guild.stage_channels
# Accessing stage channels within a guild

stage_channel.speakers
# Accessing speakers in a stage channel

client.stage_instances
# Accessing stage instances via the client
```

--------------------------------

### Create a Discord.py Extension with Teardown

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/extensions

This snippet illustrates creating a Discord.py extension that includes both a 'setup' function for when the extension is loaded and a 'teardown' function for when it is unloaded. The 'teardown' function is called when the extension is removed from the bot.

```Python
async def setup(bot):
    print('I am being loaded!')

async def teardown(bot):
    print('I am being unloaded!')
```

--------------------------------

### Advanced Onboarding and Permissions in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet highlights 'OnboardingMode.advanced' for advanced onboarding configurations and 'Permissions.advanced()' for checking advanced permission sets.

```Python
discord.OnboardingMode.advanced
discord.Permissions.advanced()
```

--------------------------------

### Range Constraint for Integer Input

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides an example of using the app_commands.Range annotation to enforce that an integer parameter in an application command must be within a specified range. The example shows how to define the command with a constrained integer input.

```Python
import discord
from discord import app_commands

@app_commands.command()
async def range_command(interaction: discord.Interaction, value: app_commands.Range[int, 10, 12]):
    await interaction.response.send_message(f'Your value is {value}', ephemeral=True)
```

--------------------------------

### Discord.py Cog with Before and After Invoke Hooks

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

An example of a Discord.py cog implementing `cog_before_invoke` and `cog_after_invoke` methods to manage context data and log command completion.

```Python
class MyCog(commands.Cog):
    async def cog_before_invoke(self, ctx):
        ctx.secret_cog_data = 'foo'

    async def cog_after_invoke(self, ctx):
        print('{0.command} is done...'.format(ctx))

    @commands.command()
    async def foo(self, ctx):
        await ctx.send(ctx.secret_cog_data)
```

--------------------------------

### Discord.py: Get Option

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a specific option from an onboarding prompt. This method is part of the discord.OnboardingPrompt class.

```python
discord.OnboardingPrompt.get_option()
```

--------------------------------

### Get POSIX-like Signature for Help

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns a POSIX-like signature string, which is useful for displaying help messages for commands in a clear and concise format.

```Python
command.signature
```

--------------------------------

### Handling Discord Voice Client and Audio Streams in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of interacting with the Discord voice client and audio streams, including accessing the audio source and stream properties.

```python
voice_client.source
# Accessing the audio source of a voice client

pc_maudio.stream
# Accessing the stream of a PCM audio object
```

--------------------------------

### Fix context install decorators in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Ensures that context install decorators in discord.py explicitly restrict commands, improving command security and behavior.

```python
Fix context install decorators to explicitly restrict commands
```

--------------------------------

### Create and Activate Virtual Environment

Source: https://discordpy.readthedocs.io/en/stable/intro

Demonstrates the process of creating a Python virtual environment named 'bot-env' and activating it on a Linux/macOS system.

```shell
$ cd your-bot-source
$ python3 -m venv bot-env
$ source bot-env/bin/activate
```

--------------------------------

### Default Settings and Values in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of default settings and values for various Discord.py components, including commands, parameters, message references, and intents. Understanding defaults is key for proper configuration.

```python
import discord
import commands

# Default parameter value
default_param = discord.app_commands.Parameter.default

# Default bucket type for commands
default_bucket = commands.BucketType.default

# Default message reference type
default_ref = discord.MessageReferenceType.default

# Default intents
default_intents = discord.Intents.default()
```

--------------------------------

### Get Single Element from AsyncIterator in Python

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Illustrates how to retrieve a single element from an AsyncIterator using the get() method, similar to discord.utils.find() or discord.utils.get().

```Python
my_last_message = await channel.history().get(author=client.user)
```

--------------------------------

### Get Current UTC Time in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to get the current Coordinated Universal Time (UTC) using the discord.py utilities module.

```python
discord.utils.utcnow()
```

--------------------------------

### Range Converter Example

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Illustrates how to use the `Range` converter to enforce constraints on argument values. This example restricts the `value` parameter to be an integer between 10 and 12 (inclusive). If the input is outside this range or not an integer, an appropriate error is raised.

```Python
from discord.ext import commands

@bot.command()
async def range(ctx: commands.Context, value: commands.Range[int, 10, 12]):
    await ctx.send(f'Your value is {value}')
```

--------------------------------

### Discord.py Command Tree and Context Menu Commands

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates the usage of discord.app_commands.CommandTree for managing application commands, including context menu commands. It covers creating, syncing, and handling these commands.

```Python
import discord
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync commands globally
        await self.tree.sync()

        # Sync commands to a specific guild
        # guild = discord.Object(id=YOUR_GUILD_ID)
        # await self.tree.sync(guild=guild)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

# Example of a context menu command
@app_commands.context_menu(name='Report Message')
async def report_message(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(f'Thanks for reporting {message.author}\'s message!', ephemeral=True)

intents = discord.Intents.default()
client = MyClient(intents=intents)
# client.run('YOUR_BOT_TOKEN')

# Example of accessing context from a command tree
# The 'context' attribute is typically available within interaction handlers
# For example, within an interaction callback:
# async def some_command_callback(interaction: discord.Interaction):
#     command_context = interaction.client.tree.context # This might not be directly accessible like this
#     # The context is usually implicitly handled by the framework

```

--------------------------------

### Prepare Help Command in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to prepare the help command for a discord.py bot. The `prepare_help_command()` method allows for customization of the help command's behavior and output.

```Python
await commands.HelpCommand.prepare_help_command(self, ctx, *, check_ratelimit=True)
```

--------------------------------

### Get Discovery Splash Image URL

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `Guild.discovery_splash_url` to get the URL of the guild's discovery splash image. This asset is used in the server discovery feature.

```Python
guild.discovery_splash_url
```

--------------------------------

### Create Discord Template

Source: https://discordpy.readthedocs.io/en/stable/

Enables the creation of a server template from an existing guild, which can be used to quickly set up new servers.

```python
await discord.Guild.create_template()
```

--------------------------------

### Discord Command Names and Parameters

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of accessing the 'name' attribute for commands and parameters within the discord.py command framework.

```python
print(commands.Command.name)
print(commands.Parameter.name)
```

--------------------------------

### Discord Intents and Permissions

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of using 'none()' methods for Discord Intents and Permissions to create objects with no specified intents or permissions.

```python
discord.Intents.none()
discord.Permissions.none()
```

--------------------------------

### Example Docstring Parameter Description - discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Shows an alternative method for describing command parameters using docstrings, specifically the 'Parameters' section in a NumPy-style format.

```Python
@app_commands.command()
async def ban(interaction: discord.Interaction, member: discord.Member):
    """Bans a member

    Parameters
    ----------
    member: discord.Member
        the member to ban
    """
    await interaction.response.send_message(f'Banned {member}')
```

--------------------------------

### Discord.py: Welcome Screen and Widgets

Source: https://discordpy.readthedocs.io/en/stable/

Details functionalities related to guild welcome screens and server widgets. This includes accessing welcome channels and retrieving widget information.

```python
discord.WebhookType
discord.WelcomeScreen.welcome_channels
discord.Guild.welcome_screen()
discord.WelcomeChannel
discord.WelcomeScreen
discord.Widget
discord.Guild.widget()
discord.AuditLogDiff.widget_channel
discord.Guild.widget_channel
discord.AuditLogDiff.widget_enabled
discord.Guild.widget_enabled
discord.WidgetChannel
discord.WidgetMember
```

--------------------------------

### Discord OnboardingPromptOption Roles

Source: https://discordpy.readthedocs.io/en/stable/

The roles associated with an onboarding prompt option.

```python
discord.OnboardingPromptOption.roles
```

--------------------------------

### discord.py Commands Extension

Source: https://discordpy.readthedocs.io/en/stable/index

The discord.ext.commands extension provides a framework for creating bots with commands, simplifying command handling and argument parsing.

```Python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# bot.run('YOUR_TOKEN')
```

--------------------------------

### Working with Discord Spotify Integration in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to integrate and retrieve information about users' Spotify activities using discord.py, including the Spotify class itself.

```python
discord.Spotify
# Represents a user's Spotify activity
```

--------------------------------

### Apply Discord Logging to Root Logger

Source: https://discordpy.readthedocs.io/en/stable/logging

Configures the discord.py client to apply its logging configuration to the root logger by setting root_logger=True in Client.run().

```python
client.run(token, log_handler=handler, root_logger=True)
```

--------------------------------

### Discord Client Login

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates the 'login' method for discord.py clients, used to establish a connection to Discord.

```python
import discord

# Logging in the client
# Assuming 'client' is a discord.Client object
# await client.login('YOUR_BOT_TOKEN')
```

--------------------------------

### Fetch Guilds into a List

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This example shows how to fetch guilds with a limit of 150 and collect them into a Python list using an asynchronous list comprehension.

```Python
guilds = [guild async for guild in client.fetch_guilds(limit=150)]
```

--------------------------------

### Get Command Signature

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns a POSIX-like signature string for the command, which is useful for generating help messages.

```python
_property _signature
```

--------------------------------

### Discord Help Command DM Help

Source: https://discordpy.readthedocs.io/en/stable/

Manages DM help settings for DefaultHelpCommand and MinimalHelpCommand.

```python
commands.DefaultHelpCommand.dm_help
commands.MinimalHelpCommand.dm_help
commands.DefaultHelpCommand.dm_help_threshold
commands.MinimalHelpCommand.dm_help_threshold
```

--------------------------------

### MinimalHelpCommand: Get Destination

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns the Messageable where the help command will be output. By default, this returns the context's channel. This method can be overridden for custom behavior.

```Python
def get_destination():
    """Returns the `Messageable` where the help command will be output.

    You can override this method to customise the behaviour.
    By default this returns the context’s channel.

    Returns
    -------
    abc.Messageable
        The destination where the help command will be output.
    """
    pass
```

--------------------------------

### Get Soundboard Sound by ID

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a soundboard sound using its ID. New in version 2.5.

```python
get_soundboard_sound(_id_ , _/_)
```

--------------------------------

### Discord.py: Get User

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a user by their ID. This can be called on discord.Client or commands.Bot.

```python
discord.Client.get_user()
commands.Bot.get_user()
```

--------------------------------

### Registering Events with asyncio in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_async

Demonstrates how to register event handlers in discord.py, showing the transition from basic function definitions to using `@asyncio.coroutine` or `async def` for compatibility with asyncio.

```Python
import asyncio

# Before (requires @asyncio.coroutine if client.event is used)
@client.event
def on_message(message):
    pass

# After (using @asyncio.coroutine)
@client.event
@asyncio.coroutine
def on_message(message):
    pass

# After (using async def in Python 3.5+)
@client.event
async def on_message(message):
    pass

# Using the utility decorator for easier registration
@client.async_event
def on_message(message):
    pass
```

--------------------------------

### Discord SessionStartLimits Reset After

Source: https://discordpy.readthedocs.io/en/stable/

Specifies the duration after which session start limits are reset.

```python
discord.SessionStartLimits.reset_after
```

--------------------------------

### Discord Channel Types

Source: https://discordpy.readthedocs.io/en/stable/

Shows examples of Discord channel type constants, including 'news' and 'news_thread'.

```python
discord.ChannelType.news
discord.ChannelType.news_thread
```

--------------------------------

### Get Signature of discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the signature of a discord.py command.

```python
_property _signature
```

--------------------------------

### Discord.py: Get Prefix

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the prefix for commands. This method is available on commands.Bot.

```python
commands.Bot.get_prefix()
```

--------------------------------

### Cog Lifecycle: Loading and Unloading

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Illustrates the `cog_load` and `cog_unload` methods, which are special asynchronous methods called when a cog is loaded or unloaded, respectively. Useful for setup and cleanup tasks.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        print(f'Cog {self.qualified_name} loaded.')

    async def cog_unload(self):
        print(f'Cog {self.qualified_name} unloaded.')
```

--------------------------------

### Discord.py: Get Sticker

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a sticker by its ID. This can be called on discord.Client or commands.Bot.

```python
discord.Client.get_sticker()
commands.Bot.get_sticker()
```

--------------------------------

### Discord.py Permissions and Connection Handling

Source: https://discordpy.readthedocs.io/en/stable/

Details Discord permissions, specifically the 'connect' permission, and methods related to establishing and managing connections for voice channels and other connectable endpoints.

```Python
import discord
from discord.ext import commands
import asyncio

# --- Permissions Example ---
# You can check permissions for a member in a specific channel
# async def check_connect_permission(member: discord.Member, channel: discord.VoiceChannel):
#     permissions = channel.permissions_for(member)
#     if permissions.connect:
#         print(f'{member.name} can connect to {channel.name}')
#     else:
#         print(f'{member.name} cannot connect to {channel.name}')

# --- Connection Methods ---

# bot = commands.Bot(command_prefix='!')

# @bot.command()
# async def connect_to_voice(ctx):
#     if ctx.author.voice:
#         channel = ctx.author.voice.channel
#         try:
#             # Check if the bot has permission to connect
#             if ctx.guild.me.guild_permissions.connect:
#                 await channel.connect() # discord.VoiceChannel.connect()
#                 await ctx.send(f'Connected to {channel.name}')
#             else:
#                 await ctx.send('I do not have permission to connect to this voice channel.')
#         except discord.ClientException as e:
#             await ctx.send(f'Error connecting: {e}')
#     else:
#         await ctx.send('You are not in a voice channel.')

# @bot.command()
# async def disconnect_from_voice(ctx):
#     if ctx.voice_client:
#         await ctx.voice_client.disconnect() # discord.VoiceClient.disconnect()
#         await ctx.send('Disconnected from voice channel.')
#     else:
#         await ctx.send('I am not connected to a voice channel.')

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Get Cog Name of discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the name of the cog to which this command belongs, if any.

```python
_property _cog_name
```

--------------------------------

### Iterate and Print Guild Names

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This example demonstrates how to asynchronously iterate through guilds fetched with a limit of 150 and print the name of each guild.

```Python
async for guild in client.fetch_guilds(limit=150):
    print(guild.name)
```

--------------------------------

### Activate Virtual Environment on Windows

Source: https://discordpy.readthedocs.io/en/stable/intro

Shows how to activate a Python virtual environment named 'bot-env' on a Windows system using the batch script.

```shell
$ bot-env\Scripts\activate.bat
```

--------------------------------

### Discord Command Descriptions

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to provide descriptions for application commands, groups, and parameters in Discord.py. Clear descriptions enhance user experience and command discoverability.

```python
import discord

# Describing an app command
@discord.app_commands.describe(name='The user to greet')
async def greet(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'Hello {name}!')

# App command description attribute
app_command_description = discord.app_commands.AppCommand.description

# Parameter description attribute
parameter_description = discord.app_commands.Parameter.description
```

--------------------------------

### Discord.py: Get Guild

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a guild by its ID. This can be called on discord.Client or commands.Bot.

```python
discord.Client.get_guild()
commands.Bot.get_guild()
```

--------------------------------

### Discord Onboarding Prompt Dropdown

Source: https://discordpy.readthedocs.io/en/stable/

Specifies the dropdown prompt type for Discord onboarding.

```python
discord.OnboardingPromptType.dropdown
```

--------------------------------

### Accessing Discord Entitlement Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to access entitlement information, specifically the start time of an entitlement, using discord.py.

```python
entitlement.starts_at
# Getting the start timestamp of an entitlement
```

--------------------------------

### Getting Active Invites

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `Client.invites_from()` to fetch currently active invites within a server.

```Python
await client.invites_from(guild)
```

--------------------------------

### Discord.py: Integration and Intent Management

Source: https://discordpy.readthedocs.io/en/stable/

This snippet details attributes and methods related to Discord integrations and intents. It covers properties for install parameters, integration IDs, and enabling specific intents for the Discord client or bot.

```python
discord.AppInfo.install_params
discord.StageChannel.instance
discord.AppCommandOptionType.integer
discord.Integration
discord.AuditLogAction.integration_create
discord.AuditLogAction.integration_delete
discord.RawIntegrationDeleteEvent.integration_id
discord.RoleTags.integration_id
discord.AuditLogAction.integration_update
discord.IntegrationAccount
discord.IntegrationApplication
discord.Intents.integrations
discord.Guild.integrations()
discord.IntegrationTypeConfig
discord.Intents
discord.Client.intents
commands.Bot.intents
```

--------------------------------

### Discord.py: Get Listeners

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves all listeners registered with a cog. This method is available on commands.Cog.

```python
commands.Cog.get_listeners()
```

--------------------------------

### Discord.py: Get Thread

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a thread by its ID. This can be called on discord.ForumChannel, discord.Guild, or discord.TextChannel.

```python
discord.ForumChannel.get_thread()
discord.Guild.get_thread()
discord.TextChannel.get_thread()
```

--------------------------------

### Discord.py: Get Task

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a task from a loop. This method is part of the tasks.Loop class.

```python
tasks.Loop.get_task()
```

--------------------------------

### Utilizing Discord Permissions in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of checking and utilizing Discord permissions within discord.py, such as permissions for speaking or managing stages.

```python
permissions.speak
# Checking if the 'speak' permission is enabled

permissions.stage_moderator()
# Checking for stage moderator permissions
```

--------------------------------

### Create Application Command - discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Creates an application command from a regular function. Parameters like name, description, nsfw, auto_locale_strings, and extras can be configured. Defaults are provided for most parameters.

```Python
@discord.app_commands.command(_*_ , _name =..._, _description =..._, _nsfw =False_, _auto_locale_strings =True_, _extras =..._)
    
Creates an application command from a regular function.
```

--------------------------------

### Load Extension in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Loads a Python extension module into the discord.py bot. Extensions contain commands, cogs, or listeners and require a global `setup` function as their entry point. This function is a coroutine and requires the extension name and optionally a package name for relative imports.

```Python
await bot._load_extension(name, package=None)
```

--------------------------------

### Discord.py: Get Role

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a role from a guild by its ID. This can be called on discord.Guild or discord.Member.

```python
discord.Guild.get_role()
discord.Member.get_role()
```

--------------------------------

### Add Member Premium Since Attribute

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds Member.premium_since to determine when a member started boosting a guild.

```Python
member.premium_since
```

--------------------------------

### Using constructed custom converter instance

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates that a custom converter class can be used either by directly referencing the class or by creating an instance of it. Both approaches are functionally equivalent for basic usage.

```Python
@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

# is the same as...

@bot.command()
async def slap(ctx, *, reason: Slapper()): # Note the parentheses here
    await ctx.send(reason)
```

--------------------------------

### Discord.py: Get Max Size

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the maximum size for help messages. This is relevant for MinimalHelpCommand.

```python
commands.MinimalHelpCommand.get_max_size()
```

--------------------------------

### Discord.py: Get Commands

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves all commands available in a command tree or a cog. This can be called on discord.app_commands.CommandTree or commands.Cog.

```python
discord.app_commands.CommandTree.get_commands()
commands.Cog.get_commands()
```

--------------------------------

### Get Current Loop Information

Source: https://discordpy.readthedocs.io/en/stable/

Returns the current iteration number of a looping task.

```python
tasks.Loop.current_loop
```

--------------------------------

### Make Web Requests with aiohttp

Source: https://discordpy.readthedocs.io/en/stable/faq

Shows how to make an asynchronous HTTP GET request to a specified URL using the `aiohttp` library. It handles the response status and parses the JSON content if the request is successful.

```Python
async with aiohttp.ClientSession() as session:
    async with session.get('http://aws.random.cat/meow') as r:
        if r.status == 200:
            js = await r.json()
```

--------------------------------

### Manage Guild Settings and Permissions with discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet covers functionalities for managing guild settings, including onboarding, welcome screens, widgets, and member pruning. It also touches upon permission checks and enabling/disabling features within the guild context.

```python
discord.Guild.edit_onboarding()
discord.Guild.edit_welcome_screen()
discord.Guild.edit_widget()
discord.Guild.estimate_pruned_members()
discord.AuditLogDiff.enable_emoticons
discord.StreamIntegration.enable_emoticons
discord.AuditLogDiff.enabled
discord.AutoModRule.enabled
discord.BotIntegration.enabled
commands.Command.enabled
discord.Integration.enabled
discord.Onboarding.enabled
discord.StreamIntegration.enabled
discord.WelcomeScreen.enabled
discord.AutoModRule.exempt_channel_ids
```

--------------------------------

### Get Cooldown Retry After Time in discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the amount of seconds before a command can be tried again. The `ctx` parameter is positional-only.

```python
get_cooldown_retry_after(_ctx_ , _/_)
```

--------------------------------

### Customizing Flag Syntax with Delimiter and Prefix

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Provides examples of customizing the flag syntax using `delimiter` and `prefix` arguments in the `FlagConverter` class. This includes POSIX-like and Windows-like syntaxes.

```Python
# --hello world syntax
class PosixLikeFlags(commands.FlagConverter, delimiter=' ', prefix='--'):
    hello: str


# /make food
class WindowsLikeFlags(commands.FlagConverter, prefix='/', delimiter=''):
    make: str

```

--------------------------------

### Get Item ID

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Retrieves the unique identifier for a UI component. The ID is optional and is used internally by Discord.

```python
item_id = item.id
```

--------------------------------

### Create aiohttp ClientSession for Requests

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Demonstrates the recommended way to make HTTP requests using aiohttp v2.0 or higher by creating and managing a `aiohttp.ClientSession`. This replaces older helper functions like `aiohttp.get`.

```Python
async with aiohttp.ClientSession() as sess:
    async with sess.get('url') as resp:
        # work with resp
```

--------------------------------

### Create a Discord Select Menu

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates how to create a discord.ui.Select component with custom options. This includes setting a placeholder, minimum and maximum values, and adding options with labels, values, and descriptions.

```Python
import discord

options = [
    discord.SelectOption(label="Option 1", description="This is the first option.", emoji="1️⃣"),
    discord.SelectOption(label="Option 2", description="This is the second option.", emoji="2️⃣", default=True),
    discord.SelectOption(label="Option 3", description="This is the third option.", emoji="3️⃣")
]

select_menu = discord.ui.Select(
    placeholder="Choose an option...",
    min_values=1,
    max_values=1,
    options=options
)
```

--------------------------------

### Getting Banned Members

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Provides the `Client.get_bans()` method to retrieve a list of banned members from a server.

```Python
await client.get_bans(guild)
```

--------------------------------

### Discord.py: Get Parameter

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a specific parameter from a command. This method is part of the discord.app_commands.Command class.

```python
discord.app_commands.Command.get_parameter()
```

--------------------------------

### Discord.py Context Menu Commands and Conversions

Source: https://discordpy.readthedocs.io/en/stable/

Details the creation and usage of context

--------------------------------

### Define a Basic Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates how to define a simple command using the `@bot.command()` decorator. The command takes a context and an argument, and sends the argument back to the channel.

```Python
import discord
from discord.ext import commands

# Assuming 'bot' is an instance of commands.Bot
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)
```

--------------------------------

### Discord.py: Get Shard

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the shard ID for a given guild. This method is available on discord.AutoShardedClient.

```python
discord.AutoShardedClient.get_shard()
```

--------------------------------

### Login to Discord Client

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Logs the discord.py client into the Discord API using the provided token. This coroutine also calls the `setup_hook()` after successful login. It raises `LoginFailure` for invalid credentials and `HTTPException` for other HTTP-related errors.

```Python
await bot._login(token)
```

--------------------------------

### Discord App Command Autocomplete Functionality

Source: https://discordpy.readthedocs.io/en/stable/

This section details how to implement autocomplete for application commands in Discord.py. It covers setting up autocomplete for arguments, parameters, and interactions, allowing users to get suggestions as they type.

```python
discord.app_commands.Argument.autocomplete
discord.app_commands.Parameter.autocomplete
discord.InteractionType.autocomplete
discord.app_commands.Command.autocomplete()
discord.app_commands.Transformer.autocomplete()
discord.app_commands.autocomplete()
discord.InteractionResponse.autocomplete()
discord.InteractionResponseType.autocomplete_result
```

--------------------------------

### Working with Embed Providers and Prompts

Source: https://discordpy.readthedocs.io/en/stable/

Details the `provider` attribute for embeds and attributes related to prompts in onboarding and auto-moderation presets in discord.py.

```Python
discord.Embed.provider
```

```Python
discord.AutoModPresets.profanity
```

```Python
discord.AuditLogDiff.prompts
```

```Python
discord.Onboarding.prompts
```

--------------------------------

### Discord.py: Get Context

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the context for a given message or interaction. This method is available on commands.Bot.

```python
commands.Bot.get_context()
```

--------------------------------

### Discord.py: Get Flags

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves flags for a command converter. This method is part of the commands.FlagConverter class.

```python
commands.FlagConverter.get_flags()
```

--------------------------------

### Discord.py: Get Member

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a member from a guild by their ID. This method is specific to the discord.Guild object.

```python
discord.Guild.get_member()
```

--------------------------------

### Accessing Discord User and Member Flags for Onboarding in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to check flags related to user and member onboarding processes within discord.py.

```python
member_flags.started_home_actions
# Checking if a member has started home actions during onboarding
```

--------------------------------

### Set Discord Log Level to DEBUG

Source: https://discordpy.readthedocs.io/en/stable/logging

Configures the discord.py client to log messages at the DEBUG level and directs them to a file handler.

```python
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Assume client refers to a discord.Client subclass...
client.run(token, log_handler=handler, log_level=logging.DEBUG)
```

--------------------------------

### Get Stage Instance by ID

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a stage instance using its stage channel ID. New in version 2.0.

```python
get_stage_instance(_id_ , _/_)
```

--------------------------------

### discord.py: Prepare Help Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

A low-level coroutine to prepare the help command before execution. Useful for setting up state in subclasses. The default implementation does nothing. Called within the help command callback. Access invocation context via HelpCommand.context.

```Python
async def _prepare_help_command(self, ctx, command=None, /):
    """Prepares the help command before it does anything."""
    # Custom preparation logic here
```

--------------------------------

### Add Guild Premium Subscription Count

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces Guild.premium_subscription_count to get the number of members boosting a guild.

```Python
guild.premium_subscription_count
```

--------------------------------

### Example Parameter Renaming - discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Illustrates renaming a command parameter from 'the_member_to_ban' to 'member' for display in the Discord UI using the @discord.app_commands.rename decorator.

```Python
@app_commands.command()
@app_commands.rename(the_member_to_ban='member')
async def ban(interaction: discord.Interaction, the_member_to_ban: discord.Member):
    await interaction.response.send_message(f'Banned {the_member_to_ban}')
```

--------------------------------

### Accessing Guild and User Information

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of accessing various attributes related to guilds and users, such as preferred locale, premium subscription details, and public flags.

```Python
discord.AuditLogDiff.preferred_locale
```

```Python
discord.Guild.preferred_locale
```

```Python
discord.Guild.premium_progress_bar_enabled
```

```Python
discord.Guild.premium_subscriber_role
```

```Python
discord.Guild.premium_subscribers
```

```Python
discord.Guild.premium_subscription_count
```

```Python
discord.PartialInviteGuild.premium_subscription_count
```

```Python
discord.SystemChannelFlags.premium_subscriptions
```

```Python
discord.Guild.premium_tier
```

```Python
discord.UserFlags.premium_promo_dismissed
```

```Python
discord.ClientUser.public_flags
```

```Python
discord.Member.public_flags
```

```Python
discord.TeamMember.public_flags
```

```Python
discord.User.public_flags
```

```Python
discord.WidgetMember.public_flags
```

--------------------------------

### Discord AppCommandThread Equality and Hashing

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates how to check for equality (==) and inequality (!=) between AppCommandThread objects, and how to get the hash of a thread object.

```python
x == y

Checks if two thread are equal. 

x != y

Checks if two thread are not equal. 

hash(x)

Returns the thread’s hash.
```

--------------------------------

### Define Commands with decorators

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates the use of decorators like commands.command() and discord.app_commands.command() to define bot commands and application commands respectively.

```python
from discord.ext import commands
from discord import app_commands

# Example for prefix commands:
# @commands.command(name='ping')
# async def ping_command(ctx):
#     await ctx.send('Pong!')

# Example for slash commands:
# @app_commands.command(name='hello')
# async def hello_command(interaction: discord.Interaction):
#     await interaction.response.send_message('Hello!')
```

--------------------------------

### Discord.py: Get Emoji

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves an emoji by its ID or name. This can be called on discord.Client, commands.Bot, or discord.Guild.

```python
discord.Client.get_emoji()
commands.Bot.get_emoji()
discord.Guild.get_emoji()
```

--------------------------------

### Get Channel from Context (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns the channel object associated with the command in the discord.py context. This is a shorthand for accessing `Message.channel`.

```python
context.channel

```

--------------------------------

### Fetch Stage Instance with Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Gets a StageInstance object for a given stage channel ID. Requires the `channel_id` as an integer argument.

```Python
await bot.fetch_stage_instance(111222333444)
```

--------------------------------

### Voice Connection and Playback Redesign in Python

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Contrasts the old method of joining voice channels and creating players with the new approach using VoiceChannel.connect() and VoiceClient.play() for audio playback.

```Python
vc = await client.join_voice_channel(channel)
player = vc.create_ffmpeg_player('testing.mp3', after=lambda: print('done'))
player.start()

player.is_playing()
player.pause()
player.resume()
player.stop()
# ...
```

```Python
vc = await channel.connect()
vc.play(discord.FFmpegPCMAudio('testing.mp3'), after=lambda e: print('done', e))
vc.is_playing()
vc.pause()
vc.resume()
vc.stop()
```

--------------------------------

### Discord.py: Get Cog

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a specific cog by its name from the bot. This method is available on commands.Bot.

```python
commands.Bot.get_cog()
```

--------------------------------

### Working with Status and Activity in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to set and retrieve user status and activity information using discord.py. This includes attributes for activity state, status display types, and Spotify integration.

```python
activity.state
# Getting the state of an activity

activity.status_display_type
# Getting the display type of a status

spotify.start()
# Starting a Spotify activity
```

--------------------------------

### Get Root Parent

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the top-level parent group of the command. Returns None if the command is not part of any group hierarchy.

```python
_property _root_parent
```

--------------------------------

### Get User by ID

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a user from Discord using their ID. The ID parameter is positional-only since version 2.0.

```python
get_user(_id_ , _/_)
```

--------------------------------

### Get Unique Commands in discord.py Group

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns a unique set of commands without aliases that are registered within a group.

```python
_property _commands
```

--------------------------------

### Discord.py Before Invoke Hooks

Source: https://discordpy.readthedocs.io/en/stable/

Defines methods to be executed before a command or task is invoked. These hooks are useful for pre-execution checks or setup.

```python
discord.Client.before_identify_hook()
commands.Bot.before_identify_hook()
commands.Bot.before_invoke()
commands.Command.before_invoke()
commands.Group.before_invoke()
commands.HybridCommand.before_invoke()
commands.HybridGroup.before_invoke()
commands.before_invoke()
tasks.Loop.before_loop()
```

--------------------------------

### Set Discord Client Activity Status

Source: https://discordpy.readthedocs.io/en/stable/faq

Shows how to initialize a discord.Client with a specific activity status, such as 'playing a game', using the `activity` parameter.

```python
client = discord.Client(activity=discord.Game(name='my game'))
```

--------------------------------

### Discord.py: Get Ending Note

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the ending note for help messages. This is relevant for DefaultHelpCommand and MinimalHelpCommand.

```python
commands.DefaultHelpCommand.get_ending_note()
commands.MinimalHelpCommand.get_ending_note()
```

--------------------------------

### Add Emoji url_as

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Provides a method to get emoji URLs in different formats. Requires discord.py.

```python
Add `Emoji.url_as()` (GH-6162)
```

--------------------------------

### Manage Select Menus and Options in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates the usage of select menus and their associated components within Discord interactions. This includes creating select menus, defining options, and handling user selections, which are key for interactive bot commands.

```python
discord.ui.Select
discord.ComponentType.select
discord.ui.ActionRow.select()
discord.ui.select()
discord.SelectDefaultValue
discord.SelectDefaultValueType
discord.SelectMenu
discord.SelectOption
```

--------------------------------

### Get Cog Description

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Details the `description` attribute, which typically holds the cleaned docstring of the cog class, providing a textual description.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    """This cog handles music playback commands."""
    def __init__(self, bot):
        self.bot = bot

    def get_cog_description(self):
        return self.description
```

--------------------------------

### Accessing Discord Integration Application Summary in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to retrieve the summary or description of an integration application using discord.py.

```python
integration_application.summary
# Getting the summary of an integration application
```

--------------------------------

### Discord.py: Get Stage Instance

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a stage instance by its ID. This can be called on discord.Client, commands.Bot, or discord.Guild.

```python
discord.Client.get_stage_instance()
commands.Bot.get_stage_instance()
discord.Guild.get_stage_instance()
```

--------------------------------

### Python: Simplified Late Binding with Author Shortcut

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Illustrates a simplified approach to late binding using the `commands.Author` shortcut for the default parameter.

```Python
@bot.command()
async def wave(ctx, to: discord.User = commands.Author):
    await ctx.send(f'Hello {to.mention} :wave:')
```

--------------------------------

### Access Application Information

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves and manages information related to the Discord application associated with the bot, including installation counts and application IDs. This is essential for understanding bot usage and integration.

```Python
discord.AppInfo
discord.PartialAppInfo
discord.Client.application
commands.Bot.application
discord.Message.application
discord.WebhookType.application
discord.Client.application_flags
commands.Bot.application_flags
discord.Activity.application_id
discord.app_commands.AppCommand.application_id
discord.app_commands.GuildAppCommandPermissions.application_id
discord.Client.application_id
discord.Entitlement.application_id
commands.Bot.application_id
discord.Interaction.application_id
discord.Message.application_id
discord.PartialIntegration.application_id
discord.RawIntegrationDeleteEvent.application_id
discord.SKU.application_id
discord.Client.application_info()
commands.Bot.application_info()
discord.EntitlementType.application_subscription
discord.ApplicationFlags
discord.AppInfo.approximate_guild_count
discord.PartialAppInfo.approximate_guild_count
discord.AppInfo.approximate_user_install_count
```

--------------------------------

### Using Coroutines with Client Methods in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_async

Shows how to correctly call methods on the discord.py Client that have been converted to coroutines. These methods must be awaited or yielded from.

```Python
# Before (direct call)
client.send_message(message.channel, 'Hello')

# After (using yield from)
yield from client.send_message(message.channel, 'Hello')

# After (using await in Python 3.5+)
await client.send_message(message.channel, 'Hello')
```

--------------------------------

### Discord.py Per-Command Before and After Invocation Hooks

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Shows how to define specific before and after invocation hooks for individual commands in Discord.py.

```Python
@bot.command()
async def foo(ctx):
    await ctx.send('foo')

@foo.before_invoke
async def before_foo_command(ctx):
    # do something before the foo command is called
    pass

@foo.after_invoke
async def after_foo_command(ctx):
    # do something after the foo command is called
    pass
```

--------------------------------

### Discord.py: Get Soundboard Sound

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a soundboard sound by its ID. This can be called on discord.Client, commands.Bot, or discord.Guild.

```python
discord.Client.get_soundboard_sound()
commands.Bot.get_soundboard_sound()
discord.Guild.get_soundboard_sound()
```

--------------------------------

### discord.py Command Hooks: @before_invoke

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Illustrates the use of the @before_invoke decorator in discord.py for registering a coroutine that executes before a command is called. This is suitable for setup tasks.

```python
@before_invoke
async def pre_command_hook(ctx):
    # Setup logic here
    pass
```

--------------------------------

### Discord.py: Get All Channels

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves all channels accessible by the bot. This method is available on both discord.Client and commands.Bot instances.

```python
discord.Client.get_all_channels()
commands.Bot.get_all_channels()
```

--------------------------------

### Working with Discord Message Components and Styles in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to use various message components in discord.py, including text input components and their associated styles.

```python
text_input.style
# Getting the style of a text input component
```

--------------------------------

### Discord.py: Get Tag

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a tag from a forum channel by its ID. This method is specific to the discord.ForumChannel object.

```python
discord.ForumChannel.get_tag()
```

--------------------------------

### Variable Arguments (*args)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to accept an arbitrary number of arguments using the `*args` syntax in a command. All arguments passed by the user are collected into a tuple.

```Python
import discord
from discord.ext import commands

# Assuming 'bot' is an instance of commands.Bot
@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')
```

--------------------------------

### Discord.py: Get Retry After

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the time in seconds until a cooldown is ready. This method is part of the discord.app_commands.Cooldown class.

```python
discord.app_commands.Cooldown.get_retry_after()
```

--------------------------------

### Discord Welcome Description

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the description attribute for WelcomeChannel and WelcomeScreen, related to welcome messages.

```python
discord.WelcomeChannel.description
discord.WelcomeScreen.description
```

--------------------------------

### Get Creation Date for Forum Order Type

Source: https://discordpy.readthedocs.io/en/stable/

Specifies the creation date as an ordering criterion for forum posts.

```python
discord.ForumOrderType.creation_date
```

--------------------------------

### discord.py Command Class Overview

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Provides an overview of the discord.py Command class, outlining its attributes and methods for implementing bot commands. This class is not manually created but generated via decorators.

```python
class discord.ext.commands.Command(_* args_, _** kwargs_)

Attributes:
  * aliases
  * brief
  * callback
  * checks
  * clean_params
  * cog
  * cog_name
  * cooldown
  * cooldown_after_parsing
  * description
  * enabled
  * extras
  * full_parent_name
  * help
  * hidden
  * ignore_extra
  * invoked_subcommand
  * name
  * parent
  * parents
  * qualified_name
  * require_var_positional
  * rest_is_raw
  * root_parent
  * short_doc
  * signature
  * usage

Methods:
  * async__call__
  * defadd_check
  * @after_invoke
  * @before_invoke
  * asynccan_run
  * defcopy
  * @error
  * defget_cooldown_retry_after
  * defhas_error_handler
  * defis_on_cooldown
  * defremove_check
  * defreset_cooldown
  * defupdate
```

--------------------------------

### Managing Subscriptions and SKUs in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to handle subscription-related information and SKUs (Stock Keeping Units) within discord.py. This includes accessing subscription status and SKU details.

```python
sku.subscriptions()
# Getting subscriptions for a SKU

role_tags.subscription_listing_id
# Accessing the subscription listing ID from role tags
```

--------------------------------

### Discord.py: Get Default

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the default value for a command parameter. This method is part of the commands.Parameter class.

```python
commands.Parameter.get_default()
```

--------------------------------

### Discord.py: Get All Members

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves all members of all guilds the bot is in. This method is available on both discord.Client and commands.Bot instances.

```python
discord.Client.get_all_members()
commands.Bot.get_all_members()
```

--------------------------------

### Write Discord Logs to a File

Source: https://discordpy.readthedocs.io/en/stable/logging

Configures the discord.py client to write logs to a specified file using a FileHandler. This overrides the default stderr output.

```python
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Assume client refers to a discord.Client subclass...
client.run(token, log_handler=handler)
```

--------------------------------

### Discord.py: Get Channel

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a specific channel by its ID. This can be called on discord.Client, commands.Bot, or discord.Guild objects.

```python
discord.Client.get_channel()
commands.Bot.get_channel()
discord.Guild.get_channel()
```

--------------------------------

### Working with Discord Application Command Options in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to define application command options, including string options and subcommand groups, using discord.py.

```python
app_command_option_type.subcommand
# Representing a subcommand option type

app_command_option_type.subcommand_group
# Representing a subcommand group option type
```

--------------------------------

### Get Cleaned Prefix (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the cleaned-up invoke prefix for a discord.py context. Mentions are formatted as '@name' instead of '<@id>'.

```python
context._clean_prefix

```

--------------------------------

### Get Cog Qualified Name

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Explains how to access the `qualified_name` attribute, which provides the cog's name as defined during its creation or loading.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_cog_name(self):
        return self.qualified_name
```

--------------------------------

### Get Clean Parameters

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a dictionary of command parameters, excluding the context and self parameters. This is useful for inspecting the command's signature.

```python
_property _clean_params
```

--------------------------------

### Get Application Commands Defined in a Cog

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Details the `get_app_commands()` method, which retrieves a list of application commands (slash commands and groups) defined within the cog.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='hello')
    async def hello_app(self, interaction: discord.Interaction):
        await interaction.response.send_message('Hello!')

    def get_cog_app_commands(self):
        return self.get_app_commands()
```

--------------------------------

### Discord.py Global Before and After Invocation Hooks

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Demonstrates how to register global hooks in Discord.py that execute before and after any command is invoked.

```Python
# global hooks:

@bot.before_invoke
async def before_any_command(ctx):
    # do something before a command is called
    pass

@bot.after_invoke
async def after_any_command(ctx):
    # do something after a command is called
    pass
```

--------------------------------

### Get Command Cooldown

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns the cooldown configuration for the command, or None if no cooldown is set. This property indicates when the command was last invoked.

```python
_property _cooldown
```

--------------------------------

### Get Cog Name

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the name of the cog to which this command belongs, if it is part of a cog. Returns None if the command is not associated with a cog.

```python
_property _cog_name
```

--------------------------------

### Get Guild by ID

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a guild (server) from Discord using its ID. The ID parameter is positional-only since version 2.0.

```python
get_guild(_id_ , _/_)
```

--------------------------------

### Get Cooldown for discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the cooldown configuration for a command, or `None` if no cooldown is registered. This property was added in version 2.0.

```python
_property _cooldown
```

--------------------------------

### Create Discord Stage Instance

Source: https://discordpy.readthedocs.io/en/stable/

Allows for the creation of a stage instance within a stage channel, used for live audio events and discussions.

```python
await discord.StageChannel.create_instance()
```

--------------------------------

### Get Sticker by ID

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a guild sticker using its ID. New in version 2.0. For standard stickers, use fetch_sticker() or fetch_premium_sticker_packs().

```python
get_sticker(_id_ , _/_)
```

--------------------------------

### Manage Discord Session IDs and Limits

Source: https://discordpy.readthedocs.io/en/stable/

Provides access to the session ID for voice clients and information about session start limits, which are relevant for managing real-time connections.

```python
discord.VoiceClient.session_id
discord.SessionStartLimits
```

--------------------------------

### Create and Manage Discord Media Galleries

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Shows how to create and manage a MediaGallery component for Discord UI. This includes adding, appending, inserting, removing, and clearing media items, with support for descriptions and spoilers.

```Python
import discord

# Example of creating a MediaGallery and adding items

# Assuming MediaGalleryItem is defined elsewhere
# gallery = discord.ui.MediaGallery(id=1)
# gallery.add_item(media="https://example.com/image.png", description="A sample image")
# gallery.append_item(item=discord.ui.MediaGalleryItem(media="attachment://file.txt"))
# gallery.insert_item_at(0, media="https://example.com/another.jpg")
# gallery.remove_item(item_to_remove)
# gallery.clear_items()

# Accessing attributes
# print(gallery.items)
# print(gallery.id)
```

--------------------------------

### Discord AppCommandThread String Representation

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Shows how to get the string representation of an AppCommandThread object, which typically returns the thread's name.

```python
str(x)

Returns the thread’s name.
```

--------------------------------

### Support guild onboarding in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds support for guild onboarding features in discord.py, enhancing community management capabilities.

```python
Add support for guild onboarding (GH-10226, GH-9260)
```

--------------------------------

### Get Emojis with discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the emojis available to the connected client. This property does not include emojis owned by the application; use `fetch_application_emoji()` for those.

```Python
property emojis:
    # The emojis that the connected client has.
    # Note: This does not include the emojis that are owned by the application. Use `fetch_application_emoji()` to get those.
    # Type: Sequence[`Emoji`]
    pass
```

--------------------------------

### Create Discord Permissions - Instant Invite

Source: https://discordpy.readthedocs.io/en/stable/

Represents the permission to create instant invites for channels.

```python
discord.Permissions.create_instant_invite
```

--------------------------------

### Discord.py: Access Reaction Information

Source: https://discordpy.readthedocs.io/en/stable/

Get information about a specific reaction on a message, including the emoji and the user who added it.

```Python
discord.Reaction
```

--------------------------------

### Discord.py: Get Message Reactions

Source: https://discordpy.readthedocs.io/en/stable/

Retrieve a list of all reactions present on a message. This allows you to see which emojis have been reacted with and by whom.

```Python
discord.Message.reactions
```

--------------------------------

### Get Users for Reactions and Events in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to retrieve users who have reacted to a message or are participating in scheduled events using discord.py.

```python
discord.Reaction.users()
discord.ScheduledEvent.users()
```

--------------------------------

### Discord.py: Get Message Reference

Source: https://discordpy.readthedocs.io/en/stable/

Access the message reference object, which indicates if a message is a reply to another message.

```Python
discord.Message.reference
```

--------------------------------

### Updating Event Signatures in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_async

Illustrates the changes in event handler signatures between discord.py v0.9.0 and v0.10.0. Many events now receive 'before' and 'after' arguments to provide context on the changes.

```Python
# Before v0.10.0
def on_channel_update(channel): pass
def on_member_update(member): pass
def on_status(member): pass
def on_server_role_update(role): pass
def on_voice_state_update(member): pass
def on_socket_raw_send(payload, is_binary): pass

# After v0.10.0
def on_channel_update(before, after): pass
def on_member_update(before, after): pass
def on_server_role_update(before, after): pass
def on_voice_state_update(before, after): pass
def on_socket_raw_send(payload): pass

# Note: on_status was removed and functionality merged into on_member_update.
```

--------------------------------

### Add zstd Gateway Compression

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Includes zstd gateway compression in the `speed` extras, which can be installed via `discord.py[speed]`. This can improve gateway performance.

```Python
Add zstd gateway compression to `speed` extras (GH-9947)
    
    * This can be installed using `discord.py[speed]`
```

--------------------------------

### Running discord.py Client with Custom Asyncio Loop

Source: https://discordpy.readthedocs.io/en/stable/migrating

This snippet demonstrates how to manually manage the asyncio event loop for a discord.py client, allowing for other asynchronous operations before starting the client. It uses `asyncio.run()` to execute the main asynchronous function.

```Python
import discord
import asyncio

client = discord.Client()

async def main():
    # do other async things
    await my_async_function() # Assuming my_async_function is defined elsewhere

    # start the client
    async with client:
        await client.start(TOKEN) # TOKEN should be defined

asyncio.run(main())
```

--------------------------------

### Get Current Command Context

Source: https://discordpy.readthedocs.io/en/stable/

Provides access to the current argument and parameter being processed within a command context.

```python
commands.Context.current_argument
commands.Context.current_parameter
```

--------------------------------

### Create and Add Items to a Discord UI Container

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates how to create a UI container with initial text display and outlines parameters for children, accent color, spoiler, and ID. It also details methods for adding, removing, and finding items within the container.

```Python
class MyView(ui.LayoutView):
    container = ui.Container(ui.TextDisplay('I am a text display on a container!'))
    # or you can use your subclass:
    # container = MyContainer()

# Parameters for ui.Container:
# children (`Item`) – The initial children of this container.
# accent_colour (Optional[Union[`Colour`, `int`]]) – The colour of the container. Defaults to `None`.
# accent_color (Optional[Union[`Colour`, `int`]]) – The color of the container. Defaults to `None`.
# spoiler (`bool`) – Whether to flag this container as a spoiler. Defaults to `False`.
# id (Optional[`int`]) – The ID of this component. This must be unique across the view.

# Methods:
# add_item(_item_): Adds an item to this container.
# remove_item(_item_): Removes an item from the container.
# find_item(_id_ , _/_): Gets an item with Item.id set as id, or None if not found.
```

--------------------------------

### Manage File Component Sizes and Attachments

Source: https://discordpy.readthedocs.io/en/stable/

Details how to get the size of file components and attachments, which is useful for handling file uploads and managing storage.

```python
discord.FileComponent.size
discord.Attachment.size
```

--------------------------------

### Working with Placeholders and Media Items

Source: https://discordpy.readthedocs.io/en/stable/

Details attributes used as placeholders for UI elements and media items, such as user selects and unfurled media, in discord.py.

```Python
discord.ui.UserSelect.placeholder
```

```Python
discord.UnfurledMediaItem.placeholder
```

```Python
discord.UnfurledMediaItem.proxy_url
```

--------------------------------

### discord.py Tasks Loop Methods

Source: https://discordpy.readthedocs.io/en/stable/ext/tasks/index

Methods for controlling the execution of a discord.py Tasks Loop. Includes starting, stopping, restarting, and managing exception types.

```python
import discord
from discord.ext import tasks

# Assuming 'my_loop' is an instance of tasks.Loop

# Start the loop
task = my_loop.start()

# Stop the loop gracefully
my_loop.stop()

# Cancel the loop immediately
my_loop.cancel()

# Restart the loop
my_loop.restart()

# Add exception types to handle
my_loop.add_exception_type(ValueError, TypeError)

# Clear all handled exception types
my_loop.clear_exception_types()

# Check if the loop is running
is_running = my_loop.is_running()

# Check if the loop is being cancelled
is_cancelling = my_loop.is_being_cancelled()

# Get the current iteration count
current_iteration = my_loop.current_loop

# Get the next scheduled iteration time
next_iter = my_loop.next_iteration

# Get the configured seconds interval
seconds_interval = my_loop.seconds

# Get the configured minutes interval
minutes_interval = my_loop.minutes

# Get the configured hours interval
hours_interval = my_loop.hours

# Get the configured specific times for iteration
loop_times = my_loop.time
```

--------------------------------

### Creating a Server

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enables the creation of new servers directly through the `Client.create_server()` method.

```Python
await client.create_server(name, **options)
```

--------------------------------

### Working with Discord Subscriptions and SKU Types in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to categorize SKUs and subscriptions using the `SKUType` enum in discord.py.

```python
sku_type.subscription_group
# Representing a subscription group SKU type
```

--------------------------------

### Get Commands Defined in a Cog

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Explains the `get_commands()` method, which returns a list of all standard text-based commands defined directly within the cog (excluding subcommands).

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    def get_cog_commands(self):
        return self.get_commands()
```

--------------------------------

### Unload Extensions and Translators in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of unloading cogs (extensions) from a bot and unloading translators in discord.py's application commands.

```python
await commands.Bot.unload_extension(bot, name)
await discord.app_commands.Translator.unload(translator)
```

--------------------------------

### Discord.py Mentionable Select Menus

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to use mentionable select menus, including accessing the component type and the select menu itself.

```Python
import discord

# Example of accessing the mentionable select component type
mentionable_select_type = discord.ComponentType.mentionable_select
print(mentionable_select_type)

# Example of creating a mentionable select menu
# mentionable_select = discord.ui.MentionableSelect()
# print(mentionable_select)
```

--------------------------------

### Get Associated App Command Group

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Explains the `app_command` attribute, which returns the associated application command group if the cog inherits from `GroupCog`.

```python
import discord
from discord.ext import commands

class MyGroupCog(commands.GroupCog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.qualified_name} is ready.')

    def get_associated_group(self):
        return self.app_command
```

--------------------------------

### Discord.py: Get Scheduled Event

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a scheduled event from a guild by its ID. This method is specific to the discord.Guild object.

```python
discord.Guild.get_scheduled_event()
```

--------------------------------

### Discord.py: Get Partial Messageable

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a partial messageable object by its ID. This method is available on discord.Client and commands.Bot.

```python
discord.Client.get_partial_messageable()
commands.Bot.get_partial_messageable()
```

--------------------------------

### Discord App Command Option Types and Permissions

Source: https://discordpy.readthedocs.io/en/stable/

Lists different option types for application commands and permission types related to roles.

```python
discord.AppCommandOptionType.role
discord.AppCommandPermissionType.role
```

--------------------------------

### Discord.py: Get Cooldown Tokens

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the number of tokens available for a cooldown. This method is part of the discord.app_commands.Cooldown class.

```python
discord.app_commands.Cooldown.get_tokens()
```

--------------------------------

### Discord.py: Get Member Named

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a member from a guild by their name or nickname. This method is specific to the discord.Guild object.

```python
discord.Guild.get_member_named()
```

--------------------------------

### Discord.py: Creating References for Messages

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to create message references for interaction messages, regular messages, partial messages, and webhook messages.

```python
interaction_message.to_reference()
message.to_reference()
partial_message.to_reference()
webhook_message.to_reference()
```

--------------------------------

### Get Guild from Context (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the guild object associated with the command in the discord.py context. Returns None if the guild information is not available.

```python
context.guild

```

--------------------------------

### Advanced Logging with Rotating File Handler

Source: https://discordpy.readthedocs.io/en/stable/logging

Sets up a custom logging configuration with a rotating file handler for discord.py, excluding HTTP requests from DEBUG level logging.

```python
import discord
import logging
import logging.handlers

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Assume client refers to a discord.Client subclass...
# Suppress the default configuration since we have our own
client.run(token, log_handler=None)
```

--------------------------------

### Discord.py: Get Channel or Thread

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a channel or a thread by its ID from a guild. This method is specific to the discord.Guild object.

```python
discord.Guild.get_channel_or_thread()
```

--------------------------------

### Create and Use a Discord.py Cog

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/cogs

Defines a 'Greetings' cog with a 'hello' command and an 'on_member_join' listener. It also shows how to manage the last mentioned member for context-aware responses. This cog subclasses `commands.Cog` and uses decorators for commands and listeners.

```Python
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member
```

--------------------------------

### Get Author from Context (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the author of the command invocation in the discord.py context. This can be either a User or a Member object, and is a shorthand for `Message.author`.

```python
context.author

```

--------------------------------

### Get All Guild Members

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns a generator yielding all Member objects the client can see across all guilds. This is equivalent to iterating through guilds and their members.

```python
for member in client._get_all_members():
    yield member
```

--------------------------------

### Discord.py: Get Destination

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the destination for help messages. This is relevant for help command implementations like DefaultHelpCommand, HelpCommand, and MinimalHelpCommand.

```python
commands.DefaultHelpCommand.get_destination()
commands.HelpCommand.get_destination()
commands.MinimalHelpCommand.get_destination()
```

--------------------------------

### Get Channel by ID

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a channel or thread using its ID. Returns None if not found. Handles GuildChannel, Thread, and PrivateChannel types.

```python
client.get_channel(id)
```

--------------------------------

### Discord.py: Get Command

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a specific command by its name. This can be called on discord.app_commands.CommandTree, discord.app_commands.Group, commands.Bot, commands.Group, commands.GroupMixin, or commands.HybridGroup.

```python
discord.app_commands.CommandTree.get_command()
discord.app_commands.Group.get_command()
commands.Bot.get_command()
commands.Group.get_command()
commands.GroupMixin.get_command()
commands.HybridGroup.get_command()
```

--------------------------------

### Specifying Intents for discord.py Client

Source: https://discordpy.readthedocs.io/en/stable/migrating

This code demonstrates the required change in discord.py v2.0 where the `intents` parameter is now mandatory when initializing a `discord.Client` or its subclasses. It shows the 'before' and 'after' syntax for setting intents.

```Python
# before
# client = discord.Client()

# after
import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)
```

--------------------------------

### Python: Advanced Converter for JoinDistance Class

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Provides an example of an advanced converter implementation for the `JoinDistance` class. This converter inherits from `commands.MemberConverter` and customizes the `convert` method to return a `JoinDistance` object.

```Python
class JoinDistance:
    def __init__(self, joined, created):
        self.joined = joined
        self.created = created

    @property
    def delta(self):
        return self.joined - self.created

class JoinDistanceConverter(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return JoinDistance(member.joined_at, member.created_at)

@bot.command()
async def delta(ctx, *, member: JoinDistanceConverter):
    is_new = member.delta.days < 100
    if is_new:
        await ctx.send("Hey you're pretty new!")
    else:
        await ctx.send("Hm you're not so new.")

```

--------------------------------

### Configure Specific Intents for Messages and Guilds

Source: https://discordpy.readthedocs.io/en/stable/intents

This example shows how to create an `Intents` object by explicitly enabling only 'messages' and 'guilds'. It also includes a commented-out option to enable 'reactions' if needed, and demonstrates passing these intents to `discord.Client` or `commands.Bot`.

```python
import discord

intents = discord.Intents(messages=True, guilds=True)
# If you also want reaction events enable the following:
# intents.reactions = True

# Somewhere else:
# client = discord.Client(intents=intents)
# or
# from discord.ext import commands
# bot = commands.Bot(command_prefix='!', intents=intents)
```

--------------------------------

### Python: Local Command Error Handling

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Provides an example of a local error handler for a discord.py command using the `@command.error` decorator to catch specific exceptions like `commands.BadArgument`.

```Python
@bot.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    await ctx.send(msg)

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')
```

--------------------------------

### Handle Discord Interaction Responses and Modals

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to respond to interactions by sending messages or modals, and how to manage permissions related to sending messages and threads.

```python
discord.InteractionResponse.send_message()
discord.InteractionResponse.send_modal()
discord.Permissions.send_messages
discord.Permissions.send_messages_in_threads
```

--------------------------------

### Discord.py: Get Redirect URIs

Source: https://discordpy.readthedocs.io/en/stable/

Retrieve the list of redirect URIs associated with an application. These are used for OAuth2 authorization flows.

```Python
discord.AppInfo.redirect_uris
```

```Python
discord.PartialAppInfo.redirect_uris
```

--------------------------------

### ext.commands: Allow relative paths for loading extensions via package keyword

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enhances the extension loading mechanism in `ext.commands` by allowing relative paths to be used with the `package` keyword argument. This simplifies loading extensions from subdirectories within a project.

```Python
from discord.ext import commands

# Example usage:
# bot.load_extension('my_cog', package='cogs.my_cog_package')

```

--------------------------------

### Working with Discord Message Types for Stage Events in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to identify different message types related to Discord stage events, such as stage start, end, and topic changes.

```python
message_type.stage_start
# Identifying a stage start message

message_type.stage_topic
# Identifying a message indicating a stage topic change
```

--------------------------------

### Handle Extension Failed Error in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Raised when a discord.py extension fails to load due to an error during module execution or the `setup` function. It inherits from ExtensionError and captures the original exception.

```Python
class ExtensionFailed(ExtensionError):
    """An exception raised when an extension failed to load during execution of the module or `setup` entry point.

    This inherits from `ExtensionError`
    """
    def __init__(self, name: str, original: Exception):
        self.name = name
        self.original = original
        super().__init__(f"Failed to load extension {name}\n{original!s}")

    name: str
        """The extension that had the error."""
    original: Exception
        """The original exception that was raised. You can also get this via the `__cause__` attribute."""

```

--------------------------------

### Configuring Command Prefixes and Help Commands in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to configure command prefixes and manage help command behavior in discord.py. This includes attributes for stripping prefixes and handling subcommand not found errors.

```python
bot.strip_after_prefix
# Whether to strip the prefix after command processing

help_command.subcommand_not_found()
# Handling cases where a subcommand is not found
```

--------------------------------

### Get Qualified Command Name

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the full name of the command, including all its parent group names. This represents the complete invocation path for the command.

```python
_property _qualified_name
```

--------------------------------

### Using Enumerations for Discord API Constants

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_async

Illustrates the use of enumerations in discord.py v0.10.0 for representing states like server regions, member statuses, and channel types, replacing string literals for better type safety.

```Python
# Before (using string literals)
server.region == 'us-west'
member.status == 'online'
channel.type == 'text'

# After (using enumerations)
server.region == discord.ServerRegion.us_west
member.status = discord.Status.online
channel.type == discord.ChannelType.text
```

--------------------------------

### Get Command Parents

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a list of the command's parent groups in order from closest to furthest. Returns an empty list if the command has no parents.

```python
_property _parents
```

--------------------------------

### Discord UI Item Definitions

Source: https://discordpy.readthedocs.io/en/stable/

References for Discord UI components, including base Item, DynamicItem, and MediaGallery components and their item collections.

```python
discord.ui.Item
```

```python
discord.ui.DynamicItem.item
```

```python
discord.MediaGalleryComponent.items
```

--------------------------------

### Get Emoji by ID

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a custom emoji from Discord using its ID. This function is positional-only for the ID parameter since version 2.0.

```python
get_emoji(_id_ , _/_)
```

--------------------------------

### Get All Guild Channels

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Provides a generator to iterate through all GuildChannel objects the client can access across all guilds. Permissions for each channel should be checked using abc.GuildChannel.permissions_for().

```python
for channel in client._get_all_channels():
    yield channel
```

--------------------------------

### Discord.py: Converting Assets and Emojis to Files

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to convert various Discord assets, such as attachments, emojis, and voice channel sound effects, into file objects.

```python
asset.to_file()
attachment.to_file()
emoji.to_file()
partial_emoji.to_file()
voice_channel_sound_effect.to_file()
```

--------------------------------

### Get Listeners Defined in a Cog

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Describes the `get_listeners()` method, which returns a list of (name, function) tuples for all event listeners registered within the cog.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.listener()
    async def on_ready(self):
        print('Bot is ready!')

    def get_cog_listeners(self):
        return self.get_listeners()
```

--------------------------------

### Getting Clean Message Content

Source: https://discordpy.readthedocs.io/en/stable/whats_new

The `Message.clean_content()` method returns a text version of the message content with mentions replaced by names.

```Python
clean_text = message.clean_content
```

--------------------------------

### Process Commands in on_message Event

Source: https://discordpy.readthedocs.io/en/stable/faq

Provides an example of how to properly handle the `on_message` event in discord.py when using the commands extension. It demonstrates calling `bot.process_commands(message)` to ensure commands are still processed after custom logic.

```Python
@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)
```

--------------------------------

### Generate Discord Bot Invite URL with discord.py

Source: https://discordpy.readthedocs.io/en/stable/discord

This snippet demonstrates how to dynamically generate an OAuth2 invite URL for a Discord bot at runtime using the `discord.utils.oauth_url()` function. It requires specifying the bot's scopes and permissions.

```Python
import discord

# Assuming you have a discord.Permissions object
permissions = discord.Permissions()
permissions.read_messages = True
permissions.send_messages = True

# Replace 'YOUR_CLIENT_ID' with your actual bot's client ID
# Replace ['bot'] with the desired scopes (e.g., ['applications.commands'] for slash commands)
invite_url = discord.utils.oauth_url('YOUR_CLIENT_ID', permissions=permissions, scopes=['bot'])

print(f'Invite URL: {invite_url}')
```

--------------------------------

### Get Cog by Name

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a Cog instance by its name. Returns None if the cog is not found. The name corresponds to the class name or the keyword argument used during creation.

```python
client.get_cog(name)
```

--------------------------------

### Utilizing Minimal Help Command and Range Errors in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section covers the use of a minimal help command and handling range errors in discord.py, including attributes for minimum values and loop minutes.

```python
minimal_help_command = commands.MinimalHelpCommand
range_error_minimum = commands.RangeError.minimum
loop_minutes = tasks.Loop.minutes
```

--------------------------------

### Get Cog from Context (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the cog object associated with the command in the current discord.py context. Returns None if the command is not part of a cog.

```python
context._cog

```

--------------------------------

### Get User Permissions from Context (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns the resolved permissions for the user who invoked the command within the current channel. This is a shorthand for `abc.GuildChannel.permissions_for()` or `Interaction.permissions`.

```python
context.permissions

```

--------------------------------

### Python - Asynchronous Extension Loading

Source: https://discordpy.readthedocs.io/en/stable/migrating

Illustrates how to load extensions asynchronously in discord.py v2.0. This can be done using `setup_hook` within a custom Bot class or within an `async with` block.

```Python
# before
bot.load_extension('my_extension')

# after using setup_hook
class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension('my_extension')

# after using async_with
async def main():
    async with bot:
        await bot.load_extension('my_extension')
        await bot.start(TOKEN)

asyncio.run(main())
```

--------------------------------

### Disable Discord.py Default Logging

Source: https://discordpy.readthedocs.io/en/stable/logging

Disables the default logging configuration provided by discord.py by passing None to the log_handler argument in Client.run().

```python
client.run(token, log_handler=None)
```

--------------------------------

### Discord.py: Get Ban Reason

Source: https://discordpy.readthedocs.io/en/stable/

Retrieve the reason provided when a member was banned from a guild. This is useful for tracking ban history.

```Python
discord.BanEntry.reason
```

--------------------------------

### Handle Discord Select Menu Interaction Callback

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides an example of an asynchronous callback function for a discord.ui.Select component. This callback is executed when a user makes a selection, receiving the interaction object.

```Python
import discord

class MySelect(discord.ui.Select):
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected: {self.values[0]}")

# Example usage within a View:
# view = discord.ui.View()
# view.add_item(MySelect())
# await interaction.response.send_message("Choose an option:", view=view)
```

--------------------------------

### MinimalHelpCommand: Get Ending Note

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns the help command's ending note, which is mainly useful for overriding for internationalization (i18n) purposes. The default implementation does nothing.

```Python
def get_ending_note():
    """Return the help command’s ending note. This is mainly useful to override for i18n purposes.
    The default implementation does nothing.

    Returns
    -------
    str
        The help command ending note.
    """
    pass
```

--------------------------------

### Discord Command Error Handling

Source: https://discordpy.readthedocs.io/en/stable/

Lists common exceptions related to command registration and execution, such as 'CommandAlreadyRegistered' and 'NoEntryPointError'.

```python
raise commands.CommandAlreadyRegistered()
raise commands.NoEntryPointError()
```

--------------------------------

### Discord.py: Get Connection Closed Reason

Source: https://discordpy.readthedocs.io/en/stable/

Access the reason why a WebSocket connection was closed. This is helpful for diagnosing connection issues.

```Python
discord.ConnectionClosed.reason
```

--------------------------------

### Configuring Argument and Select Menu Constraints in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section illustrates how to set minimum length and value constraints for arguments and select menus in discord.py. It covers attributes for command arguments, text input fields, and select menu options.

```python
argument_min_length = discord.app_commands.Argument.min_length
text_input_min_length = discord.TextInput.min_length
ui_text_input_min_length = discord.ui.TextInput.min_length
argument_min_value = discord.app_commands.Argument.min_value
parameter_min_value = discord.app_commands.Parameter.min_value
transformer_min_value = discord.app_commands.Transformer.min_value
select_menu_min_values = discord.SelectMenu.min_values
channel_select_min_values = discord.ui.ChannelSelect.min_values
mentionable_select_min_values = discord.ui.MentionableSelect.min_values
role_select_min_values = discord.ui.RoleSelect.min_values
select_min_values = discord.ui.Select.min_values
user_select_min_values = discord.ui.UserSelect.min_values
```

--------------------------------

### Create a Discord Modal with discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This example demonstrates how to create a custom modal using the discord.py library. It defines a Questionnaire modal with text input fields for name and answer, and an on_submit method to handle the user's response.

```python
import discord
from discord import ui

class Questionnaire(ui.Modal, title='Questionnaire Response'):
    name = ui.TextInput(label='Name')
    answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)
```

--------------------------------

### MinimalHelpCommand: Get Command Signature

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the signature portion of the help page for a given command. This method is useful for displaying command usage information and is positional-only since version 2.0.

```Python
def get_command_signature(command, /):
    """Retrieves the signature portion of the help page.

    Changed in version 2.0: `command` parameter is now positional-only.

    Parameters
    ----------
    command : Command
        The command to get the signature of.

    Returns
    -------
    str
        The signature for the command.
    """
    pass
```

--------------------------------

### Discord Opus Load Opus

Source: https://discordpy.readthedocs.io/en/stable/

Shows the 'load_opus' function for initializing the Opus library, which is necessary for voice support in discord.py.

```python
import discord

# Loading the Opus library
# discord.opus.load_opus()
```

--------------------------------

### Get Invite Code with discord.Invite.code

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the unique code for a Discord invite. This code is used to identify and join a specific server.

```python
from discord import Invite

# Example:
# invite: Invite = ... # Assume invite object is obtained
# invite_code = invite.code
# print(f"Invite code: {invite_code}")
```

--------------------------------

### Get Discord Object Converter

Source: https://discordpy.readthedocs.io/en/stable/

Provides a converter for Discord objects, allowing them to be easily retrieved or validated within commands or other functions.

```python
commands.ObjectConverter
```

--------------------------------

### Discord RPC Origins Configuration

Source: https://discordpy.readthedocs.io/en/stable/

Lists the origins allowed for Rich Presence communication for applications.

```python
discord.AppInfo.rpc_origins
discord.PartialAppInfo.rpc_origins
```

--------------------------------

### discord.py: Manual Event Loop Control

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_async

Shows how to manually control the event loop in discord.py using asyncio. This involves logging in, connecting, and managing the loop's execution and closure.

```Python
import discord
import asyncio

client = discord.Client()

@asyncio.coroutine
def main_task():
    yield from client.login('token')
    yield from client.connect()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main_task())
except:
    loop.run_until_complete(client.logout())
finally:
    loop.close()
```

--------------------------------

### Discord Autocomplete for Fruit Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides an example of an autocomplete callback function for a Discord slash command. The `fruit_autocomplete` function filters a list of fruits based on user input and returns matching choices.

```python
import discord
from discord import app_commands
from typing import List

async def fruit_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
    return [
        app_commands.Choice(name=fruit, value=fruit)
        for fruit in fruits if current.lower() in fruit.lower()
    ]

@app_commands.command()
@app_commands.autocomplete(fruit=fruit_autocomplete)
async def fruits(interaction: discord.Interaction, fruit: str):
    await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')
```

--------------------------------

### Get Help Command Destination (Python)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the `Messageable` destination where the help command's output will be sent. This method can be overridden to customize the destination, defaulting to the context's channel.

```python
def get_destination():
    """
    Returns the `Messageable` where the help command will be output.
    You can override this method to customise the behaviour.
    By default this returns the context’s channel.

    Returns
        The destination where the help command will be output.

    Return type:
        abc.Messageable
    """
    pass
```

--------------------------------

### Discord.py Invite and Select Menu Value Limits

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing properties for invite maximum uses and select menu maximum values.

```Python
import discord

# Example of accessing max uses for an invite
invite_max_uses = discord.Invite.max_uses
print(invite_max_uses)

# Example of accessing max values for a select menu
select_max_values = discord.SelectMenu.max_values
print(select_max_values)
```

--------------------------------

### Managing Discord Role Permissions and Select Menus

Source: https://discordpy.readthedocs.io/en/stable/

Covers attributes and components related to roles, including role requirements, role mentions, and role select menus. This is important for server administration and user interaction.

```python
discord.ChannelFlags.require_tag
discord.SelectMenu.required
discord.TextInput.required
discord.ui.ChannelSelect.required
discord.ui.MentionableSelect.required
discord.ui.RoleSelect.required
discord.ui.Select.required
discord.ui.TextInput.required
discord.ui.UserSelect.required
discord.Message.role_mentions
discord.ComponentType.role_select
```

--------------------------------

### Python: Schedule a task for a specific time daily

Source: https://discordpy.readthedocs.io/en/stable/ext/tasks/index

This example shows how to schedule a task to run once a day at a specific time using the `time` parameter in `@tasks.loop`. The `my_task` is set to run at 8:30 AM UTC daily.

```Python
import datetime\nfrom discord.ext import commands, tasks\n\utc = datetime.timezone.utc\n\n# If no tzinfo is given then UTC is assumed.\ntime = datetime.time(hour=8, minute=30, tzinfo=utc)\n\nclass MyCog(commands.Cog):\n    def __init__(self, bot):\n        self.bot = bot\n        self.my_task.start()\n\n    def cog_unload(self):\n        self.my_task.cancel()\n\n    @tasks.loop(time=time)\n    async def my_task(self):\n        print("My task is running!")\n
```

--------------------------------

### Shorthand for Login and Connect

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

A coroutine that serves as a shorthand for calling `login()` and `connect()`. It takes the authentication token and an optional reconnect flag.

```Python
await _start(_token_ , reconnect=True)
```

--------------------------------

### Get Command by Name

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a Command object from the internal command list using its name, including aliases. Supports fully qualified names for subcommands. Returns None if not found.

```python
client.get_command(name)
```

--------------------------------

### Accessing Platform and Activity Information

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access information about the platform and activity type associated with Discord users and activities, including playing status and sticker formats.

```Python
discord.Activity.platform
```

```Python
discord.Game.platform
```

```Python
discord.Streaming.platform
```

```Python
discord.ActivityType.playing
```

```Python
discord.StickerFormatType.png
```

--------------------------------

### Get Application Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Retrieves a specific application command from the command tree. It can fetch global commands or commands specific to a guild, and filter by command type.

```Python
get_command(_command_ , _/_ , _*_ , _guild=None_ , _type= <AppCommandType.chat_input: 1>_)
```

--------------------------------

### Get Full Parent Name

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the complete name of the command's parent hierarchy. This is the sequence of names needed to invoke the command through its parent groups.

```python
_property _full_parent_name
```

--------------------------------

### Working with Discord UI Layouts and Views in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to manage UI layout views and stop them when necessary using discord.py.

```python
ui_layout_view.stop()
# Stopping a UI layout view
```

--------------------------------

### Get Filesize Limit (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns the maximum allowed size in bytes for files uploaded within the guild or DM channel associated with the discord.py context.

```python
context._filesize_limit

```

--------------------------------

### discord.py: Guild Video Channel User Limit

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds `Guild.max_video_channel_users` to get the maximum number of users allowed in video channels.

```Python
max_users = guild.max_video_channel_users
```

--------------------------------

### Discord.py Help Commands and Range Errors

Source: https://discordpy.readthedocs.io/en/stable/

This section details attributes for using minimal help commands and handling range errors in discord.py, including minimum values and loop configurations.

```python
minimal_help_command = commands.MinimalHelpCommand
range_error_minimum = commands.RangeError.minimum
loop_minutes = tasks.Loop.minutes
```

--------------------------------

### Get Item Parent

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Returns the parent item of the current item, if it has one. This property is only available for items that are children of other items, introduced in version 2.6.

```python
parent_item = item.parent
```

--------------------------------

### Get Parent of Command Group

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Retrieves the parent object of a command group. This property is useful for navigating the command hierarchy within the discord.py framework.

```Python
parent_group = group._root_parent
```

--------------------------------

### Customizing Flag Name and Default Value

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to customize a flag's name and default value using the `commands.flag()` function. This example maps the 'members' attribute to a 'member' flag with an empty list as the default.

```Python
from typing import List

class BanFlags(commands.FlagConverter):
    members: List[discord.Member] = commands.flag(name='member', default=lambda ctx: [])

```

--------------------------------

### Working with UI Component Styles in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to set and retrieve the styles for UI components like Buttons and TextInputs in discord.py. This includes using predefined style constants.

```python
button.style
# Getting the style of a button

text_input.style
# Getting the style of a text input
```

--------------------------------

### Get Item's Associated View

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides access to the underlying View object that manages this UI item. This allows for interaction with the broader UI context.

```python
associated_view = item.view
```

--------------------------------

### Discord.py: Get Command Signature

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the signature of a command. This is available on specific help command implementations like DefaultHelpCommand, HelpCommand, and MinimalHelpCommand.

```python
commands.DefaultHelpCommand.get_command_signature()
commands.HelpCommand.get_command_signature()
commands.MinimalHelpCommand.get_command_signature()
```

--------------------------------

### Get Command Prefix with commands.Bot.command_prefix

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the prefix used to invoke commands for the bot. This can be a string or a callable that returns a list of prefixes.

```python
from discord.ext import commands

# Example:
# bot = commands.Bot(command_prefix='!')
# print(f"Bot command prefix: {bot.command_prefix}")
```

--------------------------------

### Configure discord.py Client with Intents

Source: https://discordpy.readthedocs.io/en/stable/intents

Demonstrates how to configure the discord.py client to handle Discord API changes related to intents, specifically for the `on_ready` event performance. It shows how to disable member chunking at startup.

```python
import discord

intents = discord.Intents.default()
# Enable privileged intents if needed, e.g.:
# intents.members = True
# intents.presences = True

client = discord.Client(intents=intents, chunk_guilds_at_startup=False)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# client.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Discord.py: Get DM Channel Recipients

Source: https://discordpy.readthedocs.io/en/stable/

Access a list of recipients for a DM channel. For a 1-on-1 DM, this will contain a single recipient.

```Python
discord.DMChannel.recipients
```

--------------------------------

### Handling Button Styles and Premium Features

Source: https://discordpy.readthedocs.io/en/stable/

Explains different button styles available in discord.py, including 'primary' and 'premium' styles. It also covers message types related to premium guild subscriptions and entitlements.

```Python
discord.ButtonStyle.premium
```

```Python
discord.VoiceChannelEffectAnimationType.premium
```

```Python
discord.MessageType.premium_guild_subscription
```

```Python
discord.MessageType.premium_guild_tier_1
```

```Python
discord.MessageType.premium_guild_tier_2
```

```Python
discord.MessageType.premium_guild_tier_3
```

```Python
discord.AuditLogDiff.premium_progress_bar_enabled
```

```Python
discord.Guild.premium_progress_bar_enabled
```

```Python
discord.EntitlementType.premium_purchase
```

```Python
discord.Member.premium_since
```

```Python
discord.EntitlementType.premium_subscription
```

```Python
discord.ButtonStyle.primary
```

--------------------------------

### Get Discord Onyx Color

Source: https://discordpy.readthedocs.io/en/stable/

Represents Discord's onyx color, likely used for specific UI elements or themes.

```python
discord.Colour.onyx_embed()
```

```python
discord.Colour.onyx_theme()
```

--------------------------------

### Get Discord.py Version - discord

Source: https://discordpy.readthedocs.io/en/stable/

This documentation entry provides information on how to access the version number of the discord.py library. This is useful for checking compatibility or reporting issues.

```python
discord.__version__
```

--------------------------------

### Get Client Status with discord.Member.client_status

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the client status of a member, indicating their online status (e.g., online, idle, do not disturb).

```python
from discord import Member

# Example:
# async def get_member_status(member: Member):
#     status = member.client_status
#     print(f"{member.name}'s status: {status}")
```

--------------------------------

### Working with Discord Commands and Help Command Sorting in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to configure the sorting of commands within help command structures in discord.py, covering both default and minimal help command implementations.

```python
default_help_command.sort_commands
# Whether to sort commands in the default help command

minimal_help_command.sort_commands
# Whether to sort commands in the minimal help command
```

--------------------------------

### Discord.py: Get Cooldown Retry After

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the remaining time before a command's cooldown expires. This is applicable to commands.Command, commands.Group, and commands.HybridGroup.

```python
commands.Command.get_cooldown_retry_after()
commands.Group.get_cooldown_retry_after()
commands.HybridGroup.get_cooldown_retry_after()
```

--------------------------------

### Example: Creating a GroupCog with Guild Only Restriction

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Demonstrates how to create a GroupCog that is restricted to a specific guild using the @app_commands.guild_only() decorator. This decorator applies to the entire group of application commands within the cog.

```Python
from discord import app_commands
from discord.ext import commands

@app_commands.guild_only()
class MyCog(commands.GroupCog, group_name='my-cog'):
    pass

```

--------------------------------

### Get Clean Parameters of discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the parameter dictionary for a command, excluding the context or self parameters. This is useful for inspecting the command's signature.

```python
_property _clean_params
```

--------------------------------

### ext.commands: Add support for converting StoreChannel via StoreChannelConverter

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `StoreChannelConverter` to the `ext.commands` extension. This converter allows commands to accept `StoreChannel` objects as arguments, enabling easier interaction with store channels.

```Python
from discord.ext import commands

# Example usage within a command:
# @bot.command()
# async def get_store_channel_info(ctx, channel: commands.StoreChannelConverter):
#     await ctx.send(f'Store channel name: {channel.name}')
```

--------------------------------

### Discord Media Item Loading State

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates the different loading states for Discord Media Items, including 'loaded' and 'loading'.

```python
import discord

# Accessing media item loading states
loaded_state = discord.MediaItemLoadingState.loaded
loading_state = discord.MediaItemLoadingState.loading
```

--------------------------------

### HybridGroup @before_invoke Decorator

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Explains the @before_invoke decorator for HybridGroup, used to register a coroutine as a pre-invoke hook. This hook is executed before a command is called and can be used for setup tasks, receiving a Context object as its sole parameter.

```python
@before_invoke¶
    
A decorator that registers a coroutine as a pre-invoke hook.
A pre-invoke hook is called directly before the command is called. This makes it a useful function to set up database connections or any type of set up required.
This pre-invoke hook takes a sole parameter, a `Context`.
See `Bot.before_invoke()` for more info.
Changed in version 2.0: `coro` parameter is now positional-only.

Parameters
    
**coro** (coroutine) – The coroutine to register as the pre-invoke hook.

Raises
    
**TypeError** – The coroutine passed is not actually a coroutine.
```

--------------------------------

### Get Creator Information

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves information about the creator of an AutoMod rule, Scheduled Event, or a server Template. This can include the creator object or their ID.

```python
discord.AutoModRule.creator
discord.ScheduledEvent.creator
discord.Template.creator
discord.AutoModRule.creator_id
discord.ScheduledEvent.creator_id
```

--------------------------------

### Get Cog Listeners

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/cogs

Retrieves a list of listeners registered to a cog. Each listener is returned as a tuple containing its name and the function object.

```python
>>> for name, func in cog.get_listeners():
...     print(name, '->', func)
```

--------------------------------

### Discord.py: Handle Raw Typing Event

Source: https://discordpy.readthedocs.io/en/stable/

Process events when a user starts or stops typing in a channel. This can be used for real-time feedback or presence indicators.

```Python
discord.RawTypingEvent
```

--------------------------------

### Get All Application Commands

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Retrieves all application commands currently registered in the command tree. This function allows fetching global commands or commands within a specific guild, with optional filtering by command type.

```Python
get_commands(_*_ , _guild =None_, _type =None_)
```

--------------------------------

### Working with Discord Threads and Starter Messages in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to access the starter message associated with a Discord thread using discord.py.

```python
thread.starter_message
# Accessing the message that started a thread
```

--------------------------------

### Get Cooldown Retry After Time

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves the amount of time in seconds remaining before the command can be invoked again. Returns 0.0 if the command is not on cooldown. The context parameter is positional-only.

```python
get_cooldown_retry_after(_ctx_ , _/_)

Parameters
    ctx (Context) – The invocation context to retrieve the cooldown from.
```

--------------------------------

### Get Bot Prefix

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Asynchronous function to retrieve the bot's prefix based on the message context. The message parameter is positional-only since version 2.0.

```python
_await _get_prefix(_message_ , _/_)
```

--------------------------------

### Working with Discord Message Types in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to identify different types of Discord messages, including those related to stages and system messages, using discord.py.

```python
message_type.stage_end
# Identifying a stage end message

message_type.stage_raise_hand
# Identifying a stage raise hand message
```

--------------------------------

### Iterate Entitlements with discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves an asynchronous iterator of `Entitlements` for applications. This feature was added in version 2.4. Examples show iterating directly or flattening into a list.

```Python
async for entitlement in client.entitlements(limit=100):
    print(entitlement.user_id, entitlement.ends_at)
```

```Python
entitlements = [entitlement async for entitlement in client.entitlements(limit=100)]
```

--------------------------------

### Discord.py: Get Audit Log Reason

Source: https://discordpy.readthedocs.io/en/stable/

Retrieve the reason provided for an audit log entry. This helps in understanding the context of moderation actions.

```Python
discord.AuditLogEntry.reason
```

--------------------------------

### Discord.py: Get Raw Status

Source: https://discordpy.readthedocs.io/en/stable/

Retrieve the raw status information for a client or member. This provides the underlying status data without any processing.

```Python
discord.ClientStatus.raw_status
```

```Python
discord.Member.raw_status
```

--------------------------------

### discord.py: Guild Templates

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds support for guild templates, allowing creation of guilds based on templates. Includes `Template` for reading template info and `Client.fetch_template()` to get template details. Note that fetching templates is restricted for bots.

```Python
template = await client.fetch_template(template_code)
await client.create_guild(name="New Guild", template=template)
```

--------------------------------

### Probe Audio with discord.py FFmpeg

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates probing audio files using FFmpeg with discord.py. The `probe()` method is used to gather information about audio streams, essential for playback.

```Python
await discord.FFmpegOpusAudio.probe(source, *, executable='ffmpeg')
```

--------------------------------

### discord.py: Register Pre-Invoke Hook with @before_invoke

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The @before_invoke decorator registers a coroutine as a pre-invoke hook, executed before a command. It's useful for setup tasks and takes a Context object as a parameter.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.before_invoke
    async def my_command(self, ctx: commands.Context):
        await ctx.send("Command will be executed!")

    async def _before_invoke(self, ctx: commands.Context):
        # Setup logic here
        print(f"Before invoke: {ctx.command.name}")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

--------------------------------

### Discord.py Command Copying and Global Sync

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to copy command objects and sync application commands globally or to specific guilds using discord.py's CommandTree.

```Python
import discord
from discord.ext import commands
from discord import app_commands

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix='!', intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync commands globally
        await self.tree.sync()
        print("Global commands synced.")

        # Example: Syncing to a specific guild
        # guild_id = 123456789012345678  # Replace with your guild ID
        # guild = discord.Object(id=guild_id)
        # await self.tree.sync(guild=guild)
        # print(f"Commands synced to guild {guild_id}.")

    async def on_ready(self):
        print(f'Logged in as {self.user}')

# Example of copying a command
# async def my_command_callback(ctx):
#     await ctx.send('This is a command.')

# original_cmd = commands.Command(name='original', callback=my_command_callback)
# copied_cmd = original_cmd.copy()
# copied_cmd.name = 'copied'

# bot = MyBot()
# bot.add_command(original_cmd)
# bot.add_command(copied_cmd)

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Create a UserSelect Menu

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Instantiates a UserSelect menu for Discord interactions. Allows configuration of custom ID, placeholder text, minimum and maximum values, disabled state, default selections, and row positioning.

```Python
discord.ui.UserSelect(
    custom_id='select_users',
    placeholder='Select users',
    min_values=1,
    max_values=5,
    disabled=False,
    row=0
)
```

--------------------------------

### Accessing Proxy URLs and Audit Log Diffs

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to get proxy URLs for attachments and unfurled media, and access differences in audit logs, including prune delete days and preferred locale.

```Python
discord.Attachment.proxy_url
```

```Python
discord.AuditLogDiff.prune_delete_days
```

```Python
discord.AuditLogDiff.preferred_locale
```

--------------------------------

### Check for Guild Owner or Specific Permissions (Python)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Illustrates using `@commands.check_any` to combine multiple checks. This example checks if the invoker is either the bot owner or the server owner, demonstrating logical OR for command access.

```Python
def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

@bot.command()
@commands.check_any(commands.is_owner(), is_guild_owner())
async def only_for_owners(ctx):
    await ctx.send('Hello mister owner!')
```

--------------------------------

### Working with Discord Activity Types and States in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to represent and manage user activities and their states, including streaming status and custom states, using discord.py.

```python
activity.state
# Getting the state of a user's activity

activity_type.streaming
# Representing the streaming activity type
```

--------------------------------

### Getting Member's Permissions in a Channel

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds `Member.permissions_in()` as an alternative method to `Channel.permissions_for()` for checking a member's permissions in a specific channel.

```Python
member.permissions_in(channel)
```

--------------------------------

### Add AppInfo icon_url_as and cover_image_url_as

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces methods to retrieve application icon and cover image URLs in various formats. Requires discord.py library.

```python
Add support for `AppInfo.icon_url_as()` and `AppInfo.cover_image_url_as()` (GH-5888)
```

--------------------------------

### Add Command with Guild Restriction via Decorator

Source: https://discordpy.readthedocs.io/en/stable/faq

This example illustrates how to directly specify a guild for a command using the `guild` argument within the `@tree.command()` decorator.

```python
from discord.ext import commands
from discord import app_commands, Interaction

# Assuming 'tree' is your CommandTree instance
@tree.command(guild=discord.Object(123456789012345678))
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")
```

--------------------------------

### Get Cog Commands

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/cogs

Retrieves a list of commands associated with a specific cog object. This is useful for dynamically managing or displaying available commands.

```python
>>> cog = bot.get_cog('Greetings')
>>> commands = cog.get_commands()
>>> print([c.name for c in commands])
```

--------------------------------

### Consume All Arguments in discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/faq

Demonstrates how to configure a discord.py command to accept all subsequent arguments as a single string, even if they contain spaces. This is achieved by using the `*` syntax in the command signature.

```Python
@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)
```

--------------------------------

### Get Qualified Name for Commands and Groups

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to retrieve the fully qualified name for commands, groups, and cogs in discord.py. This is helpful for uniquely identifying command structures.

```Python
discord.app_commands.AppCommandGroup.qualified_name
```

```Python
discord.app_commands.Command.qualified_name
```

```Python
discord.app_commands.ContextMenu.qualified_name
```

```Python
discord.app_commands.Group.qualified_name
```

```Python
commands.Cog.qualified_name
```

```Python
commands.Command.qualified_name
```

```Python
commands.Group.qualified_name
```

```Python
commands.HybridGroup.qualified_name
```

--------------------------------

### Get Command Attributes for Help Command

Source: https://discordpy.readthedocs.io/en/stable/

Allows accessing command attributes, specifically for the help command. This can include command aliases, descriptions, and other metadata used for generating help messages.

```python
from discord.ext import commands

# Example (within a custom help command):
# async def send_command_help(ctx, command):
#     aliases = command.aliases
#     await ctx.send(f"Aliases: {aliases}")
```

--------------------------------

### Get HTTP Exception Code with discord.HTTPException

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the HTTP status code associated with an HTTPException. This is useful for understanding the nature of API errors.

```python
from discord import HTTPException

# Example of catching the exception:
# try:
#     # ... API call ...
# except HTTPException as e:
#     print(f"HTTP error occurred: {e.status} - {e.text}")
```

--------------------------------

### Configure Text Styles and Command Signatures in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details text styling options for modals and commands, including short text input styles and the display of command signatures. This helps in creating user-friendly and informative bot interfaces.

```python
discord.TextStyle.short
commands.Command.short_doc
commands.Group.short_doc
commands.HybridGroup.short_doc
commands.DefaultHelpCommand.shorten_text()
commands.Command.signature
commands.Group.signature
commands.HybridGroup.signature
```

--------------------------------

### Working with Discord Soundboard Functionality in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Provides information on Discord's soundboard features, including audit log actions for sound creation, deletion, and updates, as well as related classes.

```python
audit_log_action.soundboard_sound_create
# Audit log action for creating a soundboard sound

soundboard_sound
# Represents a soundboard sound object
```

--------------------------------

### Discord.py Command Brief Description

Source: https://discordpy.readthedocs.io/en/stable/

Allows setting a brief description for commands, which can be used in command help messages.

```python
commands.Command.brief
```

--------------------------------

### Discord.py: Get Raw Mentions

Source: https://discordpy.readthedocs.io/en/stable/

Retrieve the raw list of all mentions (users, roles, channels) within a message. This provides a comprehensive view of mentions in the message content.

```Python
discord.InteractionMessage.raw_mentions
```

```Python
discord.Message.raw_mentions
```

```Python
discord.MessageSnapshot.raw_mentions
```

```Python
discord.WebhookMessage.raw_mentions
```

--------------------------------

### Python: Combining Multiple Checks for a Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates how to apply multiple checks to a single command using decorators. All specified checks must pass for the command to execute. This example uses `@commands.is_owner()` and a custom `is_in_guild()` check.

```Python
def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == guild_id
    return commands.check(predicate)

@bot.command()
@commands.is_owner()
@is_in_guild(41771983423143937)
async def secretguilddata(ctx):
    """super secret stuff"""
    await ctx.send('secret stuff')
```

--------------------------------

### Get Partial Messageable

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns a partial messageable object using a channel ID. This is useful for sending messages without an API call. Introduced in version 2.0.

```python
get_partial_messageable(_id_ , _*_ , _guild_id =None_, _type =None_)
```

--------------------------------

### Attach ChannelSelect Menu with discord.ui.select

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This example demonstrates how to use the @discord.ui.select decorator to attach a ChannelSelect menu to a discord.py View. The decorated function handles the interaction, sending a message with the mention of the selected channel.

```python
class View(discord.ui.View):

    @discord.ui.select(cls=ChannelSelect, channel_types=[discord.ChannelType.text])
    async def select_channels(self, interaction: discord.Interaction, select: ChannelSelect):
        return await interaction.response.send_message(f'You selected {select.values[0].mention}')
```

--------------------------------

### Discord Application Description

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves descriptions for application-related objects like IntegrationApplication and MessageApplication.

```python
discord.IntegrationApplication.description
discord.MessageApplication.description
```

--------------------------------

### Handle TimeoutError with Client.wait_for

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Provides an example of using a timeout with `Client.wait_for()`. It demonstrates how to catch the `asyncio.TimeoutError` when the specified time limit is reached and how to process the event if it occurs within the timeout.

```Python
def pred(m):
    return m.author == message.author and m.channel == message.channel

try:

    msg = await client.wait_for('message', check=pred, timeout=60.0)
except asyncio.TimeoutError:
    await channel.send('You took too long...')
else:
    await channel.send('You said {0.content}, {0.author}.'.format(msg))
```

--------------------------------

### Find Discord Models with discord.utils.get

Source: https://discordpy.readthedocs.io/en/stable/faq

Demonstrates how to find specific Discord models like guilds and channels by their names using the `discord.utils.get` function. It includes checks to ensure the model was found before proceeding.

```Python
guild = discord.utils.get(client.guilds, name='My Server')

# make sure to check if it's found
if guild is not None:
    # find a channel by name
    channel = discord.utils.get(guild.text_channels, name='cool-channel')
```

--------------------------------

### Update Synchronous Webhook Usage in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Illustrates the updated way to initialize and use synchronous webhooks in discord.py. The `RequestsWebhookAdapter` is now used directly when creating a partial webhook.

```Python
# before
webhook = discord.Webhook.partial(123456, 'token-here', adapter=discord.RequestsWebhookAdapter())
webhook.send('Hello World', username='Foo')
```

--------------------------------

### Slap command with Greedy converter

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates using the Greedy converter to accept multiple members for a command. It attempts to convert as many arguments as possible until it can no longer convert.

```Python
import discord
from discord.ext import commands

@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')
```

--------------------------------

### Get Bot User from Context (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Provides access to the bot's user object within the context. Similar to `Guild.me`, but can return the `ClientUser` in private message contexts.

```python
context.me

```

--------------------------------

### Discord.py Connection and Content Handling

Source: https://discordpy.readthedocs.io/en/stable/

Covers various aspects of Discord client connection, including AutoShardedClient, Client, and handling message content. Also includes methods for creating application emojis and guilds.

```Python
import discord
from discord.ext import commands
import asyncio

# --- Client Connection Examples ---

# Using discord.Client
# client = discord.Client(intents=discord.Intents.default())
# @client.event
# async def on_ready():
#     print(f'Logged in as {client.user}')
#     # await client.connect() # connect is usually called by client.run()
# client.run('YOUR_BOT_TOKEN')

# Using discord.AutoShardedClient
# auto_sharded_client = discord.AutoShardedClient(intents=discord.Intents.default())
# @auto_sharded_client.event
# async def on_ready():
#     print(f'Auto-sharded client logged in as {auto_sharded_client.user}')
# auto_sharded_client.run('YOUR_BOT_TOKEN')

# --- Message Content Handling ---

# To access message content, ensure the message_content intent is enabled
# intents = discord.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     print(f'Message content: {message.content}')
#     await bot.process_commands(message)

# --- Guild and Emoji Creation ---

# bot = commands.Bot(command_prefix='!')

# @bot.command()
# async def create_stuff(ctx):
#     # Create application emoji
#     try:
#         with open('path/to/your/emoji.png', 'rb') as fp:
#             emoji_image = fp.read()
#         created_emoji = await ctx.guild.create_custom_emoji(name='myemoji', image=emoji_image)
#         await ctx.send(f'Created emoji: {created_emoji}')
#     except discord.HTTPException as e:
#         await ctx.send(f'Failed to create emoji: {e}')

#     # Create a category channel
#     try:
#         category = await ctx.guild.create_category('My New Category')
#         await ctx.send(f'Created category: {category.name}')
#     except discord.HTTPException as e:
#         await ctx.send(f'Failed to create category: {e}')

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Running Converters Manually

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Shows how to use the `run_converters` coroutine to manually execute the library's argument conversion process. This is useful for custom error handling or understanding how conversions work internally. It takes the context, converter, argument string, and parameter information.

```Python
import discord
from discord.ext import commands
from typing import Any

# Assuming ctx, converter, argument, and param are defined elsewhere
# Example usage:
# result = await commands.run_converters(ctx, converter, argument, param)
```

--------------------------------

### Get Reaction Author Member

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds `RawReactionActionEvent.member` to retrieve the member who performed a reaction. This provides direct access to the user who added or removed a reaction.

```Python
event.member
```

--------------------------------

### Set Default Permissions for Discord Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This example shows how to set default permissions for a discord.py application command using the `default_permissions` decorator. It specifies that the user must have the 'manage_messages' permission to use the command.

```Python
@app_commands.command()
@app_commands.default_permissions(manage_messages=True)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('You may or may not have manage messages.')
```

--------------------------------

### Handling Discord Application Command Parameters

Source: https://discordpy.readthedocs.io/en/stable/

Details attributes related to application command parameters, including requirements and resolution. This is key for defining how commands accept arguments.

```python
discord.app_commands.Argument.required
discord.app_commands.Parameter.required
```

--------------------------------

### Accessing Discord Guild Preview Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to access information from a guild preview, such as its splash image and available stickers, using discord.py.

```python
guild_preview.splash
# Getting the guild preview's splash image URL

guild_preview.stickers
# Accessing stickers available in a guild preview
```

--------------------------------

### Check if Client is Ready

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns a boolean indicating if the client's internal cache is ready for use.

```python
is_ready()
```

--------------------------------

### Get Context from Message or Interaction

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Asynchronously returns the invocation context from a message or interaction. This is a lower-level function for process_commands(). The returned context must have its 'valid' attribute checked before invocation.

```python
await client._get_context(origin, cls=cls)
```

--------------------------------

### Discord.py UI Components and Containers

Source: https://discordpy.readthedocs.io/en/stable/

Details the creation and usage of UI components like Buttons, Select Menus, and Labels within Discord messages using discord.py's UI framework. It also covers organizing components within Containers and ActionRows.

```Python
import discord
from discord.ext import commands
from discord import ui

class MyView(ui.View):
    def __init__(self):
        super().__init__()
        # Add a button
        self.add_item(ui.Button(label='Click Me!', style=discord.ButtonStyle.primary))
        # Add a select menu
        options = [
            discord.SelectOption(label='Option 1', description='The first option'),
            discord.SelectOption(label='Option 2', description='The second option')
        ]
        self.add_item(ui.Select(placeholder='Choose an option...', options=options))
        # Add a label component
        self.add_item(ui.Label(text='This is a label.'))

    @ui.button(label='Another Button', style=discord.ButtonStyle.secondary)
    async def another_button_callback(self, interaction: discord.Interaction, button: ui.Button):
        await interaction.response.send_message('You clicked the other button!', ephemeral=True)

    @ui.select(placeholder='Select something...')
    async def select_callback(self, interaction: discord.Interaction, select: ui.Select):
        await interaction.response.send_message(f'You selected: {select.values[0]}', ephemeral=True)

# Example of using a container (which holds components)
# class MyContainerView(ui.View):
#     def __init__(self):
#         super().__init__()
#         container = ui.Container()
#         container.add_item(ui.Button(label='Inside Container'))
#         self.add_item(container)

# Example of ActionRow containing components
# class ActionRowView(ui.View):
#     def __init__(self):
#         super().__init__()
#         action_row = ui.ActionRow()
#         action_row.add_item(ui.Button(label='Button in ActionRow'))
#         self.add_item(action_row)

# bot = commands.Bot(command_prefix='!')

# @bot.command()
# async def show_ui(ctx):
#     await ctx.send('Here is a UI:', view=MyView())

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Get Command Description Location for Translations

Source: https://discordpy.readthedocs.io/en/stable/

Specifies the location for command descriptions when dealing with translations in application commands. This helps in managing localized command information.

```python
from discord import app_commands

# Example usage within command definition:
# @app_commands.command()
# @app_commands.describe(user="The user to greet")
# async def greet(interaction: discord.Interaction, user: discord.Member):
#     # The description for 'user' is handled by the describe decorator
#     pass
```

--------------------------------

### Select Menu Placeholder

Source: https://discordpy.readthedocs.io/en/stable/

Sets the placeholder text for a select menu.

```Python
discord.SelectMenu.placeholder
discord.TextInput.placeholder
discord.ui.ChannelSelect.placeholder
discord.ui.MentionableSelect.placeholder
discord.ui.RoleSelect.placeholder
discord.ui.Select.placeholder
discord.ui.TextInput.placeholder
```

--------------------------------

### Asset Helper Methods in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Introduces new helper methods added to the Asset object for customizing asset retrieval, such as specifying size and format.

```python
Helper methods Asset.with_size(), Asset.with_format(), and Asset.with_static_format() have also been added.
```

--------------------------------

### Add support for premium app integrations

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces comprehensive support for premium app integrations, including SKU and entitlement management, new enums, client methods for fetching and creating entitlements, and buttons for purchasing SKUs.

```Python
import discord
from discord import ui

class SKU:
    pass

class Entitlement:
    pass

class SKUFlags:
    pass

class SKUType:
    pass

class EntitlementType:
    pass

class EntitlementOwnerType:
    pass

class Client:
    def fetch_skus(self):
        pass

    def fetch_entitlement(self, entitlement_id: int):
        pass

    def create_entitlement(self, sku_id: int, owner_id: int):
        pass

    entitlements: list[Entitlement]

class Interaction:
    entitlement_sku_ids: list[int]
    entitlements: list[Entitlement]

class ButtonStyle:
    premium: str

class Button:
    sku_id: int

# Example of a premium button (conceptual)
# premium_button = ui.Button(style=ButtonStyle.premium, sku_id=1234567890, label='Buy Now')

```

--------------------------------

### Discord.py: Get Group Channel Recipients

Source: https://discordpy.readthedocs.io/en/stable/

Access a list of all recipients (members) in a group DM channel. This includes all users participating in the group chat.

```Python
discord.GroupChannel.recipients
```

--------------------------------

### Discord.py Event Status and Member Flags

Source: https://discordpy.readthedocs.io/en/stable/

Details event statuses and member flags within discord.py, including 'completed' status and flags related to onboarding and home actions. Also touches upon message flags and component types.

```Python
import discord
from discord.ext import commands

# Example of checking event status (hypothetical)
# class EventStatus:
#     completed = 1 # Example value

# Example of checking member flags
# async def check_member_flags(member: discord.Member):
#     if member.flags.completed_onboarding:
#         print(f'{member.name} has completed onboarding.')
#     if member.flags.completed_home_actions:
#         print(f'{member.name} has completed home actions.')

# Example of checking message flags
# async def check_message_flags(message: discord.Message):
#     if message.flags.components_v2:
#         print('Message uses components v2.')

# Example of ComponentType
# component_type = discord.ComponentType.button
# print(f'Component type: {component_type}')

# bot = commands.Bot(command_prefix='!')

# @bot.command()
# async def check_flags(ctx, member: discord.Member):
#     await check_member_flags(member)

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Get Discord Blurple Color

Source: https://discordpy.readthedocs.io/en/stable/

Represents Discord's signature blurple color. This can be used for styling messages or embeds to match Discord's branding.

```python
discord.Colour.og_blurple()
```

--------------------------------

### Discord.py: Get DM Channel Recipient

Source: https://discordpy.readthedocs.io/en/stable/

Access the member object for the other recipient in a direct message channel. This is specific to DM channels with one other user.

```Python
discord.DMChannel.recipient
```

--------------------------------

### Execute Command - discord.ext.commands.Command

Source: https://discordpy.readthedocs.io/en/stable/

This documentation entry refers to the execution of a command within the discord.ext.commands extension. It details how commands are invoked and processed.

```python
commands.Command.__call__()
```

--------------------------------

### Create a Discord UI File Component

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Shows how to create a UI File component for attaching files to Discord messages. It explains the 'media' parameter, which can be a local file path or an already uploaded attachment, and covers spoiler and ID options.

```Python
import discord
from discord import ui

class MyView(ui.LayoutView):
    file = ui.File('attachment://file.txt')
    # attachment://file.txt points to an attachment uploaded alongside this view

# Parameters for ui.File:
# media (Union[`str`, `UnfurledMediaItem`, `discord.File`]) – This file’s media. If this is a string it must point to a local file uploaded within the parent view of this item, and must meet the `attachment://<filename>` format.
# spoiler (`bool`) – Whether to flag this file as a spoiler. Defaults to `False`.
# id (Optional[`int`]) – The ID of this component. This must be unique across the view.
```

--------------------------------

### Utilize Sleep and Logging Functions in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates the use of utility functions for pausing execution with `sleep_until` and setting up logging for the Discord client. These are fundamental for asynchronous operations and bot monitoring.

```python
discord.utils.sleep_until()
discord.utils.setup_logging()
```

--------------------------------

### Get Command Name Location for Translations

Source: https://discordpy.readthedocs.io/en/stable/

Specifies the location for command names when dealing with translations in application commands. This is crucial for providing localized command names.

```python
from discord import app_commands

# Example usage within command definition:
# @app_commands.command(name="mycommand")
# async def my_command(interaction: discord.Interaction):
#     # The name 'mycommand' can be localized using translation mechanisms
#     await interaction.response.send_message("Command executed!")
```

--------------------------------

### Get Bot Permissions from Context (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns the resolved permissions for the bot within the current channel. For interaction-based commands, this reflects effective permissions which may differ from other `abc.Messageable` endpoints.

```python
context.bot_permissions

```

--------------------------------

### MinimalHelpCommand: Add Subcommand Formatting

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Adds formatting information on a subcommand to the paginator. The default implementation displays the prefix and the command's qualified name, optionally followed by an en dash and the command's short documentation. The parameter is positional-only since version 2.0.

```Python
def add_subcommand_formatting(command, /):
    """Adds formatting information on a subcommand.

    The formatting should be added to the `paginator`.
    The default implementation is the prefix and the `Command.qualified_name`
    optionally followed by an En dash and the command’s `Command.short_doc`.
    Changed in version 2.0: `command` parameter is now positional-only.

    Parameters
    ----------
    command : Command
        The command to show information of.
    """
    pass
```

--------------------------------

### Purge Messages in Discord Channels

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of purging messages from various channel types in discord.py. The `purge()` method is used to delete multiple messages at once.

```Python
await discord.StageChannel.purge(limit=100, check=None, before=None, after=None, bulk=True)
```

```Python
await discord.TextChannel.purge(limit=100, check=None, before=None, after=None, bulk=True)
```

```Python
await discord.Thread.purge(limit=100, check=None, before=None, after=None, bulk=True)
```

```Python
await discord.VoiceChannel.purge(limit=100, check=None, before=None, after=None, bulk=True)
```

--------------------------------

### Copy Command Instance

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Creates and returns a new instance of the command, effectively duplicating the command object.

```python
copy()
```

--------------------------------

### Discord.py: Get Raw Role Mentions

Source: https://discordpy.readthedocs.io/en/stable/

Access the raw list of role mentions within a message. This allows for specific parsing of role mentions in the message content.

```Python
discord.InteractionMessage.raw_role_mentions
```

```Python
discord.Message.raw_role_mentions
```

```Python
discord.MessageSnapshot.raw_role_mentions
```

```Python
discord.WebhookMessage.raw_role_mentions
```

--------------------------------

### Create and Manage Discord UI Labels

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates how to create a Label component for Discord UI, including setting text and description. Labels are used to provide text above input fields in modals.

```Python
import discord

# Example of creating a Label
label = discord.ui.Label(text="Username:", description="Enter your Discord username")

# Accessing attributes
print(label.text)
print(label.description)
```

--------------------------------

### Thread Permissions in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Illustrates how thread permissions are inherited from their parent channel in discord.py. It shows examples of checking permissions for sending messages and reacting to messages within threads, emphasizing the need to check parent channel permissions.

```Python
# Example: Checking if a member can send messages in a public thread
# Requires 'send_messages_in_threads' permission in the parent channel and the thread not being locked.

# Example: Checking if a member can react to messages in a private thread
# Requires 'read_message_history' and 'add_reactions' in the parent channel, and being a member of the thread or having 'manage_threads' permission.
```

--------------------------------

### Sync Command Tree for a Specific Guild

Source: https://discordpy.readthedocs.io/en/stable/faq

This code demonstrates how to synchronize the command tree for a particular guild after defining commands, ensuring they are registered correctly.

```python
import discord

# Assuming 'tree' is your CommandTree instance
await tree.sync(guild=discord.Object(123456789012345678))
```

--------------------------------

### Get Next Iteration Time (ext.tasks)

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds the `Loop.next_iteration` property to retrieve the scheduled time of the next loop iteration. This is useful for monitoring and scheduling task execution.

```Python
loop.next_iteration
```

--------------------------------

### Command Usage and Permissions in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details the usage string for commands and permissions related to application commands, embedded activities, and external applications in discord.py.

```python
commands.Command.usage
discord.Permissions.use_application_commands
discord.Permissions.use_embedded_activities
discord.Permissions.use_external_apps
discord.Permissions.use_external_emojis
discord.Permissions.use_external_sounds
discord.Permissions.use_external_stickers
discord.Permissions.use_soundboard
discord.Permissions.use_voice_activation
```

--------------------------------

### Get Creation Timestamp

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the timestamp indicating when a Discord object was created. This attribute is available for a wide range of objects including channels, guilds, members, messages, and more.

```python
await discord.abc.GuildChannel.created_at
await discord.app_commands.AppCommandChannel.created_at
await discord.app_commands.AppCommandThread.created_at
await discord.AuditLogEntry.created_at
await discord.BaseActivity.created_at
await discord.CategoryChannel.created_at
await discord.ClientUser.created_at
await discord.DMChannel.created_at
await discord.Emoji.created_at
await discord.Entitlement.created_at
await discord.ForumChannel.created_at
await discord.GroupChannel.created_at
await discord.Guild.created_at
await discord.GuildPreview.created_at
await discord.Interaction.created_at
await discord.InteractionMessage.created_at
await discord.Invite.created_at
await discord.Member.created_at
await discord.Message.created_at
await discord.MessageInteraction.created_at
await discord.MessageInteractionMetadata.created_at
await discord.MessageSnapshot.created_at
await discord.Object.created_at
await discord.PartialEmoji.created_at
await discord.PartialInviteChannel.created_at
await discord.PartialInviteGuild.created_at
await discord.PartialMessage.created_at
await discord.PartialMessageable.created_at
await discord.Poll.created_at
await discord.PrimaryGuild.created_at
await discord.Role.created_at
await discord.SKU.created_at
await discord.SoundboardSound.created_at
await discord.Spotify.created_at
await discord.StageChannel.created_at
await discord.Sticker.created_at
await discord.Subscription.created_at
await discord.SyncWebhook.created_at
await discord.TeamMember.created_at
await discord.Template.created_at
await discord.TextChannel.created_at
await discord.Thread.created_at
await discord.User.created_at
await discord.VoiceChannel.created_at
await discord.VoiceChannelSoundEffect.created_at
await discord.Webhook.created_at
await discord.WebhookMessage.created_at
await discord.Widget.created_at
await discord.WidgetChannel.created_at
await discord.WidgetMember.created_at
```

--------------------------------

### Dynamic Cooldown with Factory (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Implements a dynamic cooldown where a factory function determines if a cooldown applies. This example bypasses cooldown for a specific user ID. If a cooldown is triggered, a `CommandOnCooldown` error is raised and handled.

```python
import discord
from discord import app_commands
from typing import Optional

def cooldown_for_everyone_but_me(interaction: discord.Interaction) -> Optional[app_commands.Cooldown]:
    if interaction.user.id == 80088516616269824: # Replace with actual owner ID
        return None
    return app_commands.Cooldown(1, 10.0)

# Assuming 'tree' is an instance of discord.app_commands.CommandTree

@tree.command()
@app_commands.checks.dynamic_cooldown(cooldown_for_everyone_but_me)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('Hello')

@test.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(str(error), ephemeral=True)
```

--------------------------------

### Discord Role Subscription Details

Source: https://discordpy.readthedocs.io/en/stable/

Contains information about role subscriptions.

```python
discord.RoleSubscriptionInfo
```

--------------------------------

### Use Custom Permissions Object for Discord Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This example demonstrates using a custom `discord.Permissions` object to define default permissions for a discord.py application command. It combines a predefined administrator permission with the 'manage_messages' permission.

```Python
ADMIN_PERMS = discord.Permissions(administrator=True)

@app_commands.command()
@app_commands.default_permissions(ADMIN_PERMS, manage_messages=True)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('You may or may not have manage messages.')
```

--------------------------------

### Discord Interaction Response Launch Activity

Source: https://discordpy.readthedocs.io/en/stable/

Shows the method to launch an activity via a Discord Interaction Response. This is typically used in slash commands.

```python
import discord

# Launching an activity through an interaction response
# Assuming 'interaction' is a discord.Interaction object
# interaction.response.launch_activity()
```

--------------------------------

### Register Pre-Invoke Hook - discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The @before_invoke decorator registers a coroutine as a pre-invoke hook, called before a command is invoked, provided all checks and argument parsing succeed. It takes a Context object and is useful for setup tasks.

--------------------------------

### Get content length of LayoutView

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Returns the total length of all text content within the view's items. This is useful for adhering to Discord's display character limits for views.

```python
layout_view.content_length()
```

--------------------------------

### Discord Command and Flag Requirements

Source: https://discordpy.readthedocs.io/en/stable/

Highlights attributes related to command and flag requirements, ensuring that commands have the necessary parameters or flags set.

```python
commands.Command.require_var_positional
commands.Flag.required
commands.Parameter.required
```

--------------------------------

### Get Guild Rules Channel

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds `Guild.rules_channel` to retrieve the rules channel of public guilds. This feature is restricted to guilds participating in or planning to participate in Server Discovery.

```Python
guild.rules_channel
```

--------------------------------

### Working with Discord UI Buttons and Styles in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to set and retrieve the style for UI buttons in discord.py.

```python
ui_button.style
# Getting the style of a UI button
```

--------------------------------

### Discord.py: Get Raw Channel Mentions

Source: https://discordpy.readthedocs.io/en/stable/

Access the raw list of channel mentions present in a message. This can be useful for parsing message content and identifying mentioned channels.

```Python
discord.InteractionMessage.raw_channel_mentions
```

```Python
discord.Message.raw_channel_mentions
```

```Python
discord.MessageSnapshot.raw_channel_mentions
```

```Python
discord.WebhookMessage.raw_channel_mentions
```

--------------------------------

### discord.py: Using AsyncIterator.map()

Source: https://discordpy.readthedocs.io/en/stable/migrating

Demonstrates the simplification of mapping a function over items from an asynchronous iterator, moving from AsyncIterator.map() to a direct list comprehension.

```Python
# before
content_of_messages = []
async for content in channel.history().map(lambda m: m.content):
    content_of_messages.append(content)

# after
content_of_messages = [message.content async for message in channel.history()]
```

--------------------------------

### Keyword-Only Argument (*)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Explains how to use a keyword-only argument with `*` to capture all remaining input as a single string, useful for arguments with spaces that shouldn't be split.

```Python
import discord
from discord.ext import commands

# Assuming 'bot' is an instance of commands.Bot
@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)
```

--------------------------------

### Discord.py: Permissions General

Source: https://discordpy.readthedocs.io/en/stable/

A method that

--------------------------------

### Get a command from the internal list of commands in discord.ext.commands

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This method retrieves a Command object from the internal list of commands managed by the GroupMixin. It can also be used to retrieve aliases. Returns the requested command, or None if not found.

```python
get_command(name , /)
```

--------------------------------

### Discord.py App Command and Locale Handling

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing application command types and handling locale-specific strings for messages.

```Python
import discord

# Example of accessing the message app command type
message_app_command_type = discord.AppCommandType.message
print(message_app_command_type)

# Example of locale-specific message handling
locale_message = discord.app_commands.locale_str.message
print(locale_message)
```

--------------------------------

### Discord.py: Text Channel and Text-Based Components

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing text channels within guilds and categories, as well as components related to text input and display.

```python
category_channel.text_channels
guild.text_channels
component_type.text_input
text_channel
text_display
text_input
```

--------------------------------

### Get the ID of a sent message

Source: https://discordpy.readthedocs.io/en/stable/faq

Retrieves the ID of a message after it has been sent. The `send` method returns the sent Message object, from which the ID can be accessed.

```Python
message = await channel.send('hmm…')
message_id = message.id
```

--------------------------------

### Discord.py: Get Guild Raid Detection Time

Source: https://discordpy.readthedocs.io/en/stable/

Access the timestamp when a raid was detected on a Discord guild. This attribute provides information about security-related events within the guild.

```Python
discord.Guild.raid_detected_at
```

--------------------------------

### Initialize AutoShardedClient

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Shows how to initialize `discord.AutoShardedClient` for managing multiple shards of a Discord bot within a single process. This is a simplified approach compared to manual sharding.

```Python
client = discord.AutoShardedClient()
```

--------------------------------

### Configure Help Commands in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to customize the behavior of help commands within a Discord bot, including sending bot, cog, command, and group help messages, as well as handling errors and displaying parameter descriptions.

```python
commands.HelpCommand.send_bot_help()
commands.HelpCommand.send_cog_help()
commands.HelpCommand.send_command_help()
commands.HelpCommand.send_error_message()
commands.HelpCommand.send_group_help()
commands.Context.send_help()
commands.DefaultHelpCommand.send_pages()
commands.MinimalHelpCommand.send_pages()
commands.HelpCommand.show_hidden
commands.DefaultHelpCommand.show_parameter_descriptions
```

--------------------------------

### Discord.py - Working with UI Views and Components

Source: https://discordpy.readthedocs.io/en/stable/

This snippet details how to interact with UI Views and their associated components in discord.py. It lists various components that can be part of a View, such as Buttons, Select Menus, and Text Inputs.

```Python
discord.ui.View
discord.ui.ActionRow.view
discord.ui.Button.view
discord.ui.ChannelSelect.view
discord.ui.Container.view
discord.ui.DynamicItem.view
discord.ui.File.view
discord.ui.Item.view
discord.ui.Label.view
discord.ui.MediaGallery.view
discord.ui.MentionableSelect.view
discord.ui.RoleSelect.view
discord.ui.Section.view
discord.ui.Select.view
discord.ui.Separator.view
discord.ui.TextDisplay.view
discord.ui.TextInput.view
discord.ui.Thumbnail.view
discord.ui.UserSelect.view
```

--------------------------------

### discord.py HelpCommand - Getting Command Signature

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The `get_command_signature` method is used to retrieve the formatted signature of a given command. This is useful for displaying how a command should be used, including its arguments and their types. The `command` parameter is positional-only.

```python
def get_command_signature(_command_, /):
    """Retrieves the signature portion of the help page."""
    return "str"
```

--------------------------------

### Create Discord Guild

Source: https://discordpy.readthedocs.io/en/stable/

Provides functionality to create a new Discord guild (server). This action is typically performed by a bot with specific permissions.

```python
await discord.Client.create_guild()
await commands.Bot.create_guild()
await discord.Template.create_guild()
```

--------------------------------

### Customizing Cog Behavior with Meta Options

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/cogs

Demonstrates how to customize a cog's behavior by passing options to its metaclass, `commands.CogMeta`. This example shows how to override the cog's default name using the `name` keyword argument during class definition.

```Python
class MyCog(commands.Cog, name='My Cog'):
    pass
```

--------------------------------

### Discord UI Section Creation and Management

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates how to create and manage a UI section in Discord bots using the discord.ui.Section class. This includes adding, removing, and finding items within the section, as well as handling interactions.

```Python
from discord.ui import Section, TextDisplay, Item
from discord import Interaction

# Example of creating a Section
section = Section(
    TextDisplay("Hello"),
    accessory=Item(), # Replace with an actual Item
    id=1
)

# Adding an item
section.add_item(TextDisplay("World"))

# Removing an item
section.remove_item(TextDisplay("Hello"))

# Finding an item
found_item = section.find_item(1)

# Clearing all items
section.clear_items()

# Interaction check (coroutine)
async def check_interaction(interaction: Interaction) -> bool:
    return True

# Accessing properties
section_id = section.id
section_children = section.children
section_accessory = section.accessory
section_parent = section.parent
section_view = section.view

# Iterating through children
for item in section.walk_children():
    pass

# Getting content length
content_length = section.content_length()
```

--------------------------------

### Python discord.py @before_invoke Decorator

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The @before_invoke decorator in discord.py registers a coroutine as a pre-invoke hook for a command group. This hook runs just before the command is executed, suitable for setup tasks like database connections. It accepts a Context object as its only argument.

```python
@before_invoke
    
A decorator that registers a coroutine as a pre-invoke hook.
A pre-invoke hook is called directly before the command is called. This makes it a useful function to set up database connections or any type of set up required.
This pre-invoke hook takes a sole parameter, a `Context`.
See `Bot.before_invoke()` for more info.
Changed in version 2.0: `coro` parameter is now positional-only. 

Parameters
    
**coro** (coroutine) – The coroutine to register as the pre-invoke hook. 

Raises
    
**TypeError** – The coroutine passed is not actually a coroutine.
```

--------------------------------

### Implementing Modals and Interaction Types in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section covers the implementation of modals and different interaction types within discord.py, including modal submission and related metadata.

```python
modal_ui = discord.ui.Modal
interaction_modal_response = discord.InteractionResponseType.modal
modal_interaction_metadata = discord.MessageInteractionMetadata.modal_interaction
interaction_modal_submit = discord.InteractionType.modal_submit
```

--------------------------------

### Discord.py: Get Session Remaining Limits

Source: https://discordpy.readthedocs.io/en/stable/

Retrieve the number of remaining requests allowed within the current session's rate limit. This helps in managing API usage.

```Python
discord.SessionStartLimits.remaining
```

--------------------------------

### Get Maximum Command Name Length (Python)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Calculates and returns the length of the longest command name within a given sequence of commands. The `commands` parameter is positional-only since version 2.0.

```python
def get_max_size(commands, /):
    """
    Returns the largest name length of the specified command list.
    Changed in version 2.0: `commands` parameter is now positional-only.

    Parameters
        commands (Sequence[Command]): A sequence of commands to check for the largest size.

    Returns
        The maximum width of the commands.

    Return type:
        int
    """
    pass
```

--------------------------------

### Get Cooldown Retry After in discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Calculates the remaining time in seconds before a command can be invoked again. This is useful for implementing rate limiting or informing users about cooldown periods. If the command is not on cooldown, it returns 0.0.

```python
get_cooldown_retry_after(_ctx_ , _/_)
    
    Retrieves the amount of seconds before this command can be tried again.
    New in version 1.4.
    Changed in version 2.0: `ctx` parameter is now positional-only.

    Parameters
        
        **ctx** (`Context`) – The invocation context to retrieve the cooldown from.

    Returns
        
        The amount of time left on this command’s cooldown in seconds. If this is `0.0` then the command isn’t on cooldown.

    Return type
        
        `float`
```

--------------------------------

### Create Context Menu Command - discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Creates an application command context menu from a regular function. The function must accept an Interaction as the first parameter and a Member, User, or Message as the second. Parameters like name, nsfw, auto_locale_strings, and extras can be configured.

```Python
@discord.app_commands.context_menu(_*_ , _name =..._, _nsfw =False_, _auto_locale_strings =True_, _extras =..._)
    
Creates an application command context menu from a regular function.
This function must have a signature of `Interaction` as its first parameter and taking either a `Member`, `User`, or `Message`, or a `typing.Union` of `Member` and `User` as its second parameter.
```

--------------------------------

### Handling Iterable Attributes in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_async

Demonstrates how to access attributes like `Client.servers` or `Server.members` which have changed from sequences (lists) to iterables. Direct indexing is no longer supported and requires explicit casting to a list.

```Python
# Before (direct indexing)
if client.servers[0].name == "test":
    # do something

# After (casting to list for indexing)
servers = list(client.servers)
if servers[0].name == "test":
    # do something

# Note: The order of elements in the iterated data is not guaranteed.
```

--------------------------------

### Python: Custom Converter with Parameter Metadata

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates using `commands.parameter` to specify a custom converter for a command parameter, resolving type checker warnings.

```Python
class SomeType:
    foo: int

class MyVeryCoolConverter(commands.Converter[SomeType]):
    ...  # implementation left as an exercise for the reader

@bot.command()
async def bar(ctx, cool_value: MyVeryCoolConverter):
    cool_value.foo  # type checker warns MyVeryCoolConverter has no value foo (uh-oh)
```

```Python
@bot.command()
async def bar(ctx, cool_value: SomeType = commands.parameter(converter=MyVeryCoolConverter)):
    cool_value.foo  # no error (hurray)
```

--------------------------------

### Discord.py: Command Prefix Handling

Source: https://discordpy.readthedocs.io/en/stable/

Includes functions for defining command prefixes, allowing commands to be invoked by mentioning the bot or using specific prefixes.

```python
commands.when_mentioned()
commands.when_mentioned_or()
```

--------------------------------

### Create a Discord.py Hybrid Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The `@discord.ext.commands.hybrid_command()` decorator creates a hybrid command that works as both a traditional command and an application command. Converters are automatically handled, and checks function as they would for regular commands, using `Context` instead of `Interaction`.

```python
import discord
from discord.ext import commands

@commands.hybrid_command(name='hybrid_hello')
async def hybrid_hello(ctx: commands.Context):
    """A hybrid command that says hello."""
    await ctx.send(f'Hello {ctx.author}!')
```

--------------------------------

### Get Color Attributes for Discord Objects

Source: https://discordpy.readthedocs.io/en/stable/

Accesses the color or colour attribute of various Discord objects, such as Embeds, Members, and Roles. This attribute represents the color associated with the object.

```python
import discord

# Example for Embed:
# embed = discord.Embed(color=discord.Color.blue())
# print(f"Embed color: {embed.color}")

# Example for Member:
# member: discord.Member = ... # Assume member object is obtained
# print(f"Member color: {member.color}")
```

--------------------------------

### Accessing Discord SKU and Subscription Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to access Stock Keeping Unit (SKU) information and subscription details within discord.py, including SKU types and subscription statuses.

```python
sku_type.subscription
# Representing a subscription SKU type

subscription_status
# Enum for different subscription statuses
```

--------------------------------

### Discord.py Help Commands and Range Errors

Source: https://discordpy.readthedocs.io/en/stable/

This snippet details attributes for using minimal help commands and handling range errors in discord.py, including minimum values and loop configurations.

```python
minimal_help_command = commands.MinimalHelpCommand
range_error_minimum = commands.RangeError.minimum
loop_minutes = tasks.Loop.minutes
```

--------------------------------

### Manage SKU and Subscription Data in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Covers the handling of Stock Keeping Units (SKUs) and subscription information, including associating SKUs with buttons, entitlements, and sticker packs, as well as managing SKU flags and types.

```python
discord.SKU
discord.Button.sku_id
discord.Entitlement.sku_id
discord.StickerPack.sku_id
discord.ui.Button.sku_id
discord.Subscription.sku_ids
discord.SKUFlags
discord.SKUType
```

--------------------------------

### Handling Command Prefixes and Flags

Source: https://discordpy.readthedocs.io/en/stable/

Details how to manage command prefixes and positional flags within the discord.py command framework. This includes accessing the prefix and defining positional arguments.

```Python
commands.Context.prefix
```

```Python
commands.Paginator.prefix
```

```Python
commands.Flag.positional
```

--------------------------------

### Discord Thread Auto Archive Duration

Source: https://discordpy.readthedocs.io/en/stable/

This property allows you to get or set the auto-archive duration for a Discord thread. This controls how long a thread remains active before being automatically archived.

```python
discord.app_commands.AppCommandThread.auto_archive_duration
discord.AuditLogDiff.auto_archive_duration
discord.Thread.auto_archive_duration
```

--------------------------------

### Create a command using the @command decorator in discord.ext.commands

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This decorator is a shortcut for creating a Command and adding it to the bot's command list. It converts a method into a Command object and registers it. It returns the created Command object.

```python
@command(*args, **kwargs)
```

--------------------------------

### Create Discord Integration

Source: https://discordpy.readthedocs.io/en/stable/

Enables the creation of an integration within a guild, which could be for bots, webhooks, or other services.

```python
await discord.Guild.create_integration()
```

--------------------------------

### Create Discord Webhook

Source: https://discordpy.readthedocs.io/en/stable/

Enables the creation of a webhook for a channel, allowing external applications to send messages to Discord.

```python
await discord.ForumChannel.create_webhook()
await discord.StageChannel.create_webhook()
await discord.TextChannel.create_webhook()
await discord.VoiceChannel.create_webhook()
```

--------------------------------

### Discord Bot Login

Source: https://discordpy.readthedocs.io/en/stable/

Shows the 'login' method for discord.py bots, used to establish a connection to Discord.

```python
from discord.ext import commands

# Logging in the bot
# Assuming 'bot' is a commands.Bot object
# await bot.login('YOUR_BOT_TOKEN')
```

--------------------------------

### Handle Sharding and Session Information in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to manage sharded clients and access shard-related information, including connection timeouts, shard IDs, and the total number of shards. This is crucial for large-scale bot deployments.

```python
discord.AutoShardedClient.shard_connect_timeout
discord.ShardInfo.shard_count
discord.ConnectionClosed.shard_id
discord.Guild.shard_id
discord.PrivilegedIntentsRequired.shard_id
discord.AutoShardedClient.shard_ids
discord.ShardInfo
discord.AutoShardedClient.shards
```

--------------------------------

### Define Choices for App Command Arguments

Source: https://discordpy.readthedocs.io/en/stable/

Allows defining a list of choices for an argument in an application command. This provides users with a predefined set of options to select from.

```python
from discord import app_commands

# Example:
# @app_commands.command()
# @app_commands.describe(option="Choose an option")
# @app_commands.choices(option=[
#     app_commands.Choice(name="Option 1", value=1),
#     app_commands.Choice(name="Option 2", value=2),
# ])
# async def my_command(interaction: discord.Interaction, option: int):
#     await interaction.response.send_message(f"You chose: {option}")
```

--------------------------------

### discord.py Tasks Loop Decorators

Source: https://discordpy.readthedocs.io/en/stable/ext/tasks/index

Decorators for handling events in discord.py Tasks Loop. `@after_loop` is called after the loop finishes, `@before_loop` is called before the loop starts, and `@error` is called when an unhandled exception occurs.

```python
import discord
from discord.ext import tasks

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_loop.start()

    def cog_unload(self):
        self.my_loop.cancel()

    @tasks.loop(seconds=5)
    async def my_loop(self):
        await self.some_function()

    @my_loop.after_loop
    async def after_my_loop(self):
        print('My loop finished.')

    @my_loop.before_loop
    async def before_my_loop(self):
        await self.bot.wait_until_ready()
        print('Waiting for bot to be ready...')

    @my_loop.error
    async def on_my_loop_error(self, error):
        print(f'An error occurred: {error}')
```

--------------------------------

### discord.py: Using AsyncIterator.find()

Source: https://discordpy.readthedocs.io/en/stable/migrating

Illustrates the transition from AsyncIterator.find() to discord.utils.find() for searching within an asynchronous iterator based on a predicate function.

```Python
def predicate(event):
    return event.reason is not None

# before
event = await guild.audit_logs().find(predicate)

# after
event = await discord.utils.find(predicate, guild.audit_logs())
```

--------------------------------

### Add support for casting Attachment to str to get the URL

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enables casting an `Attachment` object directly to a string to retrieve its URL. This provides a convenient shorthand for accessing the file's web address.

```Python
from discord import Attachment

# Example usage:
# attachment = ...
# url = str(attachment)
```

--------------------------------

### Discord.py: Get Partial Message

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves a partial message object by its ID. This can be called on various channel types like DMChannel, StageChannel, TextChannel, Thread, and VoiceChannel, as well as PartialMessageable.

```python
discord.DMChannel.get_partial_message()
discord.PartialMessageable.get_partial_message()
discord.StageChannel.get_partial_message()
discord.TextChannel.get_partial_message()
discord.Thread.get_partial_message()
discord.VoiceChannel.get_partial_message()
```

--------------------------------

### Python discord.py: Hybrid command with described flags

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to use the `description` keyword argument within `commands.flag()` to provide inline descriptions for parameters in a discord.py hybrid command's FlagConverter.

```Python
class BanFlags(commands.FlagConverter):
    member: discord.Member = commands.flag(description='The member to ban')
    reason: str = commands.flag(description='The reason for the ban')
    days: int = commands.flag(default=1, description='The number of days worth of messages to delete')


@commands.hybrid_command()
async def ban(ctx, *, flags: BanFlags):
    ...

```

--------------------------------

### Fetch Discord Template

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Asynchronously fetches a Discord template using its code or a discord.new URL. Raises NotFound if the template is invalid or HTTPException if the fetch fails. Returns the Template object.

```python
await client._fetch_template(code)
```

--------------------------------

### All Channels App Command Context in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This documentation covers 'AllChannels' for app commands, specifying that a command can be used in all channel types.

```Python
discord.app_commands.AllChannels
```

--------------------------------

### Discord.py Command Flags and Concurrency

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates accessing attributes and methods related to command flags, argument limits, and concurrency control in discord.py's command framework.

```Python
from discord.ext import commands

# Example of accessing a flag attribute
max_args_flag = commands.Flag.max_args
print(max_args_flag)

# Example of using a max concurrency method
# async def my_command(ctx):
#     await commands.max_concurrency(1, message=True, key=lambda m: m.author.id)(ctx)
#     ...

# Example of accessing a max concurrency setting
max_concurrency_setting = discord.SessionStartLimits.max_concurrency
print(max_concurrency_setting)
```

--------------------------------

### DefaultHelpCommand Attributes

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Details the configurable attributes of the DefaultHelpCommand class, which control the appearance and behavior of help messages, such as width, sorting, DM settings, and text formatting.

```python
width: int
sort_commands: bool
dm_help: Optional[bool]
dm_help_threshold: Optional[int]
indent: int
arguments_heading: str
show_parameter_descriptions: bool
commands_heading: str
default_argument_description: str
no_category: str
paginator: Paginator
```

--------------------------------

### Discord Bot Listener and Cog Listener

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to use the 'listen' decorator for bots and cogs in discord.py to handle events.

```python
from discord.ext import commands

# Using the listener decorator for a bot
# @commands.Bot.listen()
# async def on_message(message):
#     pass

# Using the listener decorator for a cog
# class MyCog(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     @commands.Cog.listener()
#     async def on_ready(self):
#         print('Bot is ready!')
#
# async def setup(bot):
#     await bot.add_cog(MyCog(bot))
```

--------------------------------

### Get Audit Log Difference Code with discord.AuditLogDiff.code

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the 'code' attribute from an AuditLogDiff object, which might represent a specific code related to the audit log entry, such as a status code or identifier.

```python
from discord import AuditLogDiff

# Example:
# diff: AuditLogDiff = ... # Assume diff is obtained from audit logs
# code = diff.code
# print(f"Audit log diff code: {code}")
```

--------------------------------

### Discord.py Context and Command Handling

Source: https://discordpy.readthedocs.io/en/stable/

Focuses on the `Context` object in discord.py's commands extension, which provides information about the command invocation. It also covers various command-related converters and error types.

```Python
import discord
from discord.ext import commands

# intents = discord.Intents.default()
# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def context_info(ctx: commands.Context):
#     """Displays information about the command context."""
#     await ctx.send(f"Author: {ctx.author}")
#     await ctx.send(f"Channel: {ctx.channel}")
#     await ctx.send(f"Guild: {ctx.guild}")
#     await ctx.send(f"Message: {ctx.message.content}")

# Example of accessing context within app commands (often implicit)
# @discord.app_commands.command(name='appcontext')
# async def app_context_command(interaction: discord.Interaction):
#     # The interaction object itself serves as the context
#     await interaction.response.send_message(f'App command context: {interaction.user}')

# Example of Command Registration Error
# class CustomCommand(commands.Command):
#     pass

# try:
#     # Attempting to register a command with the same name twice would raise an error
#     pass
# except commands.CommandRegistrationError as e:
#     print(f"Command registration error: {e}")

# Example of BadUnionArgument
# @bot.command()
# async def union_command(ctx, arg: commands.Union[int, str]):
#     await ctx.send(f"Received: {arg} (Type: {type(arg)})")

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.BadUnionArgument):
#         await ctx.send(f"Could not convert argument to either int or str: {error}")
#     else:
#         await ctx.send(f"An error occurred: {error}")

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Discord.

Source: https://discordpy.readthedocs.io/en/stable/

No description

--------------------------------

### Get Command by Name in discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a specific Command object from the internal list using its name. This method can also be used to access aliases and supports fully qualified names for subcommands. If the command is not found, it returns None.

```python
get_command(_name_ , _/_)
    
    Get a `Command` from the internal list of commands.
    This could also be used as a way to get aliases.
    The name could be fully qualified (e.g. `'foo bar'`) will get the subcommand `bar` of the group command `foo`. If a subcommand is not found then `None` is returned just as usual.
    Changed in version 2.0: `name` parameter is now positional-only.

    Parameters
        
        **name** (`str`) – The name of the command to get.

    Returns
        
        The command that was requested. If not found, returns `None`.

    Return type
        
        Optional[`Command`]
```

--------------------------------

### Discord.py Polls and Multiple Choice Prompts

Source: https://discordpy.readthedocs.io/en/stable/

This section covers attributes for handling polls and multiple choice options in discord.py, including poll multiplicity and onboarding prompt types.

```python
poll_multiple = discord.Poll.multiple
multiple_choice_prompt = discord.OnboardingPromptType.multiple_choice
```

--------------------------------

### Change VoiceClient AudioSource at Runtime

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Demonstrates how to change the audio source for a VoiceClient at runtime, including adding a PCMVolumeTransformer to control volume. This change enhances resilience towards reconnections.

```Python
vc.source = discord.PCMVolumeTransformer(vc.source)
vc.source.volume = 0.6
```

--------------------------------

### Get Fully Qualified Name of Command Group

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Returns the complete name of a command group, including its parent's name. This provides a unique identifier for commands within nested structures, like '/foo bar' having a qualified name of 'foo bar'.

```Python
qualified_name = group._qualified_name
```

--------------------------------

### Fix uninitialized CustomActivity.created_at

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Corrects an issue where `CustomActivity.created_at` might be uninitialized. Requires discord.py.

```python
Fix uninitialised `CustomActivity.created_at` (GH-6095)
```

--------------------------------

### discord.py Command Attributes Explained

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Details the various attributes of a discord.py Command, including its name, aliases, help text, callback function, and configuration options like enabled status and cooldowns.

```python
name: str
callback: coroutine
help: Optional[str]
brief: Optional[str]
usage: Optional[str]
alias: Union[List[str], Tuple[str]]
enabled: bool
parent: Optional[Group]
cog: Optional[Cog]
checks: List[Callable[[Context], bool]]
description: str
hidden: bool
rest_is_raw: bool
invoked_subcommand: Optional[Command]
require_var_positional: bool
ignore_extra: bool
cooldown_after_parsing: bool
extras: dict
```

--------------------------------

### Python: Add exception handling for reconnects in a task

Source: https://discordpy.readthedocs.io/en/stable/ext/tasks/index

This example shows how to add specific exception types to a task's error handling using `add_exception_type`. This is useful for handling reconnections or specific database errors, like `asyncpg.PostgresConnectionError`, during a recurring task like `batch_update`.

```Python
import asyncpg\nfrom discord.ext import tasks, commands\n\nclass MyCog(commands.Cog):\n    def __init__(self, bot):\n        self.bot = bot\n        self.data = []\n        self.batch_update.add_exception_type(asyncpg.PostgresConnectionError)\n        self.batch_update.start()\n\n    def cog_unload(self):\n        self.batch_update.cancel()\n\n    @tasks.loop(minutes=5.0)\n    async def batch_update(self):\n        async with self.bot.pool.acquire() as con:\n            # batch update here...\n            pass\n
```

--------------------------------

### Working with Discord UI Separators and Spacing in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to use UI separator components and manage their spacing in discord.py for creating visually organized interfaces.

```python
separator_component.spacing
# Getting the spacing of a UI separator component

ui_separator.spacing
# Getting the spacing of a UI separator
```

--------------------------------

### Discord App Command Names and Localizations

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing the 'name' and 'name_localizations' attributes for Discord application commands and their arguments.

```python
print(discord.app_commands.AppCommand.name)
print(discord.app_commands.AppCommand.name_localizations)
print(discord.app_commands.Argument.name_localizations)
```

--------------------------------

### MinimalHelpCommand: Send Pages

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

A coroutine helper utility to send the page output from the paginator to the destination. This method is used internally for paginating help messages.

```Python
async def send_pages():
    """A helper utility to send the page output from paginator to the destination."""
    pass
```

--------------------------------

### Getting Guild ID in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet shows how to retrieve the unique identifier (guild_id) for various Discord entities. The guild_id attribute is crucial for uniquely identifying a guild in API requests and internal logic.

```python
import discord

# Assuming 'interaction' is a discord.Interaction object
if interaction.guild_id:
    print(f"Interaction occurred in guild with ID: {interaction.guild_id}")

# Assuming 'app_command' is a discord.app_commands.AppCommand object
if app_command.guild_id:
    print(f"App command is associated with guild ID: {app_command.guild_id}")

# Assuming 'member' is a discord.Member object
if member.guild:
    print(f"Member's guild ID: {member.guild.id}")
```

--------------------------------

### Handling Missing Permissions and Roles in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet demonstrates how to handle scenarios where a bot or user is missing required permissions or roles in discord.py. It includes specific exceptions for missing permissions, roles, and any roles.

```python
bot_missing_permissions = commands.BotMissingPermissions.missing_permissions
missing_permissions = commands.MissingPermissions.missing_permissions
app_command_missing_permissions = discord.app_commands.BotMissingPermissions.missing_permissions
app_command_missing_permissions_alt = discord.app_commands.MissingPermissions.missing_permissions
bot_missing_role = commands.BotMissingRole.missing_role
missing_role = commands.MissingRole.missing_role
app_command_missing_role = discord.app_commands.MissingRole.missing_role
app_command_missing_any_role = discord.app_commands.MissingAnyRole.missing_roles
bot_missing_any_role = commands.BotMissingAnyRole.missing_roles
missing_any_role = commands.MissingAnyRole.missing_roles
missing_application_id = discord.MissingApplicationID
missing_flag_argument = commands.MissingFlagArgument
missing_required_argument = commands.MissingRequiredArgument
missing_required_attachment = commands.MissingRequiredAttachment
missing_required_flag = commands.MissingRequiredFlag
```

--------------------------------

### Discord Available Items

Source: https://discordpy.readthedocs.io/en/stable/

This section details various items that can be considered 'available' within Discord, such as emojis, stickers, SKUs, and soundboard sounds. It also includes information on whether audit log differences are available.

```python
discord.AuditLogDiff.available
discord.Emoji.available
discord.GuildSticker.available
discord.SKUFlags.available
discord.SoundboardSound.available
```

--------------------------------

### Discord Last Message Access

Source: https://discordpy.readthedocs.io/en/stable/

Provides examples of accessing the last message sent in various types of Discord channels, including Stage, Text, Thread, and Voice channels. This is useful for retrieving recent conversation history.

```python
import discord

# Accessing the last message in different channel types
last_message_stage = discord.StageChannel.last_message
last_message_text = discord.TextChannel.last_message
last_message_thread = discord.Thread.last_message
last_message_voice = discord.VoiceChannel.last_message
```

--------------------------------

### Playing Audio with discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates the `play()` method for playing audio in a voice channel using discord.py. This is a fundamental function for music bots or voice channel interactions.

```Python
discord.VoiceClient.play()
```

--------------------------------

### Discord Button Styles and Colors

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates the usage of different button styles and predefined color constants in Discord.py. These are fundamental for creating interactive elements and styling messages.

```python
import discord

# Button Style Example
button = discord.ui.Button(style=discord.ButtonStyle.danger, label="Click Me")

# Color Examples
color1 = discord.Colour.dark_blue()
color2 = discord.Colour.dark_gold()
color3 = discord.Colour.default()
```

--------------------------------

### Create a UI Text Input with discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This snippet demonstrates how to create a UI text input component in discord.py. It shows the initialization of the TextInput class with various parameters like label, custom_id, style, placeholder, default value, required status, min/max length, and row positioning.

```Python
import discord
from discord import ui

# Example of creating a TextInput
text_input = ui.TextInput(
    label="Your Feedback",
    custom_id="feedback_input",
    style=discord.TextStyle.paragraph,
    placeholder="Enter your feedback here...",
    default="",
    required=True,
    min_length=10,
    max_length=500,
    row=0
)
```

--------------------------------

### discord.py: Command Hooks (before_invoke, after_invoke)

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Implements `before_invoke()` and `after_invoke()` decorators for the `ext.commands` extension, allowing custom logic before and after command execution.

```Python
@bot.command()
@commands.before_invoke(before_hook)
@commands.after_invoke(after_hook)
async def my_command(ctx):
    pass
```

--------------------------------

### Discord Role Subscription Information

Source: https://discordpy.readthedocs.io/en/stable/

Covers attributes related to role subscriptions, including purchase notifications and associated listing IDs.

```python
discord.Message.role_subscription
discord.RoleSubscriptionInfo.role_subscription_listing_id
discord.MessageType.role_subscription_purchase
discord.SystemChannelFlags.role_subscription_purchase_notification_replies
discord.SystemChannelFlags.role_subscription_purchase_notifications
```

--------------------------------

### Initialize Discord Bot

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Asynchronously initializes the bot and automatically cleans up. This is a new feature introduced in version 2.0.

```python
async with bot:
    # Bot initialization logic here
```

--------------------------------

### Send Messages and Audio in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details the various methods for sending messages, alerts, and audio packets across different channel types and user contexts in Discord. This covers sending text, alerts, audio data, and managing message permissions.

```python
discord.abc.Messageable.send()
discord.DMChannel.send()
commands.Context.send()
discord.GroupChannel.send()
discord.Member.send()
discord.PartialMessageable.send()
discord.StageChannel.send()
discord.SyncWebhook.send()
discord.TextChannel.send()
discord.Thread.send()
discord.User.send()
discord.VoiceChannel.send()
discord.Webhook.send()
discord.AutoModRuleActionType.send_alert_message
discord.VoiceClient.send_audio_packet()
discord.Permissions.send_messages
discord.Permissions.send_messages_in_threads
discord.Permissions.send_polls
discord.VoiceChannel.send_sound()
discord.Permissions.send_tts_messages
discord.Permissions.send_voice_messages
```

--------------------------------

### Create Permissions with Keyword Arguments

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds support for passing keyword arguments when creating `Permissions` objects. This provides a more flexible and readable way to define permission sets.

```Python
Permissions(manage_messages=True, read_messages=False)
```

--------------------------------

### Discord.py Modals and Interaction Types

Source: https://discordpy.readthedocs.io/en/stable/

No description

--------------------------------

### MinimalHelpCommand: Add Bot Commands Formatting

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Adds the minified bot heading with commands to the output, formatting them for the paginator. The default implementation includes a bold underline heading followed by commands on the next line. Parameters are positional-only since version 2.0.

```Python
def add_bot_commands_formatting(commands, heading, /):
    """Adds the minified bot heading with commands to the output.

    The formatting should be added to the `paginator`.
    The default implementation is a bold underline heading followed by commands
    separated by an EN SPACE (U+2002) in the next line.
    Changed in version 2.0: `commands` and `heading` parameters are now positional-only.

    Parameters
    ----------
    commands : Sequence[Command]
        A list of commands that belong to the heading.
    heading : str
        The heading to add to the line.
    """
    pass
```

--------------------------------

### Add InteractionResponse.launch_activity() in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `InteractionResponse.launch_activity()` in discord.py, enabling responses that launch activities.

```python
Add support for `InteractionResponse.launch_activity()` responses (GH-10193)
```

--------------------------------

### Discord SystemChannelFlags RoleSubscriptionPurchaseNotificationReplies

Source: https://discordpy.readthedocs.io/en/stable/

Flag to enable role subscription purchase notification replies.

```python
discord.SystemChannelFlags.role_subscription_purchase_notification_replies
```

--------------------------------

### Get mutual guilds from client cache via User.mutual_guilds

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds the `mutual_guilds` attribute to the `User` class, allowing retrieval of guilds shared between the user and the client from the client's cache. This provides an efficient way to access common guild information.

```Python
from discord import User

# Example usage:
# user = User(state=..., data={...})
# mutual_guilds = user.mutual_guilds
```

--------------------------------

### Discord.py Mentioning and Message Mentions

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing attributes and methods related to mentioning users, roles, and channels, as well as handling message mentions.

```Python
import discord

# Example of accessing mention for a role
role_mention = discord.Role.mention
print(role_mention)

# Example of checking if a user is mentioned in a message
# async def check_mention(message):
#     if message.mentions:
#         print("Message contains mentions")

# Example of checking if everyone is mentioned
mention_everyone = discord.Message.mention_everyone
print(mention_everyone)
```

--------------------------------

### Discord.py Command and Range Errors

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates accessing exceptions related to maximum concurrency and range errors in discord.py's command framework.

```Python
from discord.ext import commands

# Example of accessing a max concurrency exception
max_concurrency_error = commands.MaxConcurrencyReached
print(max_concurrency_error)

# Example of accessing a range error maximum
range_error_maximum = commands.RangeError.maximum
print(range_error_maximum)
```

--------------------------------

### Perform HTTP Requests Asynchronously with aiohttp

Source: https://discordpy.readthedocs.io/en/stable/faq

Illustrates how to make non-blocking HTTP requests using the `aiohttp` library within an `async` function, contrasting it with the blocking `requests` library.

```python
# bad
r = requests.get('http://aws.random.cat/meow')
if r.status_code == 200:
    js = r.json()
    await channel.send(js['file'])

# good
async with aiohttp.ClientSession() as session:
    async with session.get('http://aws.random.cat/meow') as r:
        if r.status == 200:
            js = await r.json()
            await channel.send(js['file'])
```

--------------------------------

### discord.py Annotated Type Hint

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Explains typing.Annotated for providing type hints to type checkers while specifying a different converter for the library. Requires Python 3.9+ or typing_extensions.

```Python
from typing import Annotated

@bot.command()
async def fun(ctx, arg: Annotated[str, lambda s: s.upper()]):
    await ctx.send(arg)
```

--------------------------------

### discord.py Union Type Hint

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates using typing.Union to allow a command parameter to accept multiple types, with conversion attempts in a specified order. Raises BadUnionArgument if all conversions fail.

```Python
import typing
import discord

@bot.command()
async def union(ctx, what: typing.Union[discord.TextChannel, discord.Member]):
    await ctx.send(what)
```

--------------------------------

### Discord.py: AppCommand Transformers and Translators

Source: https://discordpy.readthedocs.io/en/stable/

Documents the 'Transform' and 'Transformer' classes for application commands, including the 'transform()' method and 'TransformerError'. Also covers the 'Translator' class and its 'translate()' method.

```python
app_commands.Transform
app_commands.Transformer.transform()
app_commands.TransformerError.transformer
app_commands.Translator.translate()
interaction.translate()
```

--------------------------------

### Ban command with Greedy and Optional converters

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to combine Greedy with Optional for flexible command arguments, allowing an optional integer parameter for delete days. This enables varied invocation syntaxes.

```Python
import typing
import discord
from discord.ext import commands

@bot.command()
async def ban(ctx, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *, 
                   reason: str):
    """Mass bans members with an optional delete_days parameter"""
    delete_seconds = delete_days * 86400 # one day
    for member in members:
        await member.ban(delete_message_seconds=delete_seconds, reason=reason)
```

--------------------------------

### Multiple Bot Owners and Team Support (ext.commands)

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Extends the commands extension to support multiple bot owners via `Bot.owner_ids` and team-based ownership. This allows for more flexible bot administration.

```Python
bot.owner_ids = {123456789012345678, 987654321098765432}
```

--------------------------------

### Define a Basic Hybrid Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

This snippet demonstrates how to define a simple hybrid command using the `Bot.hybrid_command()` decorator. The command `test` can be invoked via text or as a slash command, sending a confirmation message.

```Python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.hybrid_command()
async def test(ctx):
    await ctx.send("This is a hybrid command!")

# Remember to sync your CommandTree for slash commands to appear
# await bot.tree.sync()

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Define and Invoke App Commands with discord.app_commands.command

Source: https://discordpy.readthedocs.io/en/stable/

Decorator used to define application commands (slash commands, context menus) in discord.py. It allows for registering commands with Discord's API.

```python
from discord import app_commands

# Example for a slash command:
# @app_commands.command(name="hello", description="Says hello")
# async def hello_command(interaction: discord.Interaction):
#     await interaction.response.send_message("Hello!")

# Example for a context menu command:
# @app_commands.context_menu(name="Report Message")
# async def report_message(interaction: discord.Interaction, message: discord.Message):
#     await interaction.response.send_message("Message reported!")
```

--------------------------------

### Create Discord Soundboard Sound

Source: https://discordpy.readthedocs.io/en/stable/

Allows a guild to upload and create a custom sound for the soundboard feature.

```python
await discord.Guild.create_soundboard_sound()
```

--------------------------------

### Product Purchase Information

Source: https://discordpy.readthedocs.io/en/stable/

Details the `product_name` attribute for guild product purchases in discord.py, relevant for managing in-game or in-app purchases within Discord.

```Python
discord.GuildProductPurchase.product_name
```

--------------------------------

### Positional Arguments

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates how to define and use positional arguments in a command. The command takes multiple positional arguments, which are passed directly as function parameters.

```Python
import discord
from discord.ext import commands

# Assuming 'bot' is an instance of commands.Bot
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
```

```Python
import discord
from discord.ext import commands

# Assuming 'bot' is an instance of commands.Bot
@bot.command()
async def test(ctx, arg1, arg2):
    await ctx.send(f'You passed {arg1} and {arg2}')
```

--------------------------------

### Utilizing Source Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to retrieve source information from various Discord objects like Webhooks and Templates using discord.py. This includes accessing source channels and guilds.

```python
webhook.source_channel
# Accessing the source channel of a webhook

webhook.source_guild
# Accessing the source guild of a webhook

template.source_guild
# Accessing the source guild of a template
```

--------------------------------

### Upload many command with multiple attachments

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to handle multiple attachments, with the first being required and the second being optional using typing.Optional. It lists the URLs of the provided attachments.

```Python
import typing
import discord
from discord.ext import commands

@bot.command()
async def upload_many(
    ctx,
    first: discord.Attachment,
    second: typing.Optional[discord.Attachment],
):
    if second is None:
        files = [first.url]
    else:
        files = [first.url, second.url]

    await ctx.send(f'You uploaded: {" ".join(files)}')
```

--------------------------------

### Discord.py Paginator and Channel User Limits

Source: https://discordpy.readthedocs.io/en/stable/

Details accessing properties for paginator size limits and maximum users in video channels.

```Python
from discord.ext import commands
import discord

# Example of accessing max size for a paginator
max_paginator_size = commands.Paginator.max_size
print(max_paginator_size)

# Example of accessing max stage video users
max_stage_users = discord.Guild.max_stage_video_users
print(max_stage_users)
```

--------------------------------

### Discord SystemChannelFlags RoleSubscriptionPurchaseNotifications

Source: https://discordpy.readthedocs.io/en/stable/

Flag to enable role subscription purchase notifications.

```python
discord.SystemChannelFlags.role_subscription_purchase_notifications
```

--------------------------------

### Custom String to Point Transformation

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates how to create a custom Transformer to convert a comma-separated string into a Point NamedTuple for an application command parameter. It shows the Transformer class definition, the transform method, and how to apply it using app_commands.Transform.

```Python
import typing
import discord
from discord import app_commands

class Point(typing.NamedTuple):
    x: int
    y: int

class PointTransformer(app_commands.Transformer):
    async def transform(self, interaction: discord.Interaction, value: str) -> Point:
        (x, _, y) = value.partition(',')
        return Point(x=int(x.strip()), y=int(y.strip()))

@app_commands.command()
async def graph(interaction: discord.Interaction, point: app_commands.Transform[Point, PointTransformer]):
    await interaction.response.send_message(str(point))
```

--------------------------------

### Discord Role Connections Verification URL

Source: https://discordpy.readthedocs.io/en/stable/

Specifies the URL for verifying role connections for applications and partial applications.

```python
discord.AppInfo.role_connections_verification_url
discord.PartialAppInfo.role_connections_verification_url
```

--------------------------------

### Managing Presence and Intents

Source: https://discordpy.readthedocs.io/en/stable/

Details the `presences` intent required for tracking user presence and the `presets` attribute for auto-moderation triggers in discord.py.

```Python
discord.Intents.presences
```

```Python
discord.AutoModTrigger.presets
```

--------------------------------

### Discord.py Embeds and Copying Functionality

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to create and manipulate Discord Embeds, including copying existing embeds. Also covers related functionalities like sticker packs and audit log diffs.

```Python
import discord
from discord.ext import commands

# bot = commands.Bot(command_prefix='!')

# @bot.command()
# async def create_and_copy_embed(ctx):
#     # Create an embed
#     embed = discord.Embed(
#         title="Example Embed",
#         description="This is a sample embed.",
#         color=discord.Color.blue()
#     )
#     embed.add_field(name="Field 1", value="Value 1", inline=False)
#     embed.set_footer(text="Footer text")

#     # Copy the embed
#     copied_embed = embed.copy()
#     copied_embed.title = "Copied Embed"
#     copied_embed.color = discord.Color.green()

#     await ctx.send(embed=embed)
#     await ctx.send(embed=copied_embed)

# Example of accessing cover image from sticker pack
# sticker_pack = discord.StickerPack(...) # Assume this is a StickerPack object
# if sticker_pack.cover_sticker:
#     print(f"Cover sticker ID: {sticker_pack.cover_sticker_id}")

# Example of accessing cover image from guild scheduled event
# scheduled_event = discord.ScheduledEvent(...) # Assume this is a ScheduledEvent object
# if scheduled_event.cover_image:
#     print(f"Event cover image URL: {scheduled_event.cover_image}")

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Create a Discord UI View

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Inherit from discord.ui.View to create custom UI views for Discord bots. Configure timeout and manage child items.

```python
class MyView(discord.ui.View):
    def __init__(self, *, timeout=180.0):
        super().__init__(timeout=timeout)
```

--------------------------------

### Fetch SKUs with Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves all available SKUs (Stock Keeping Units) for the bot. This function requires the application ID to be set.

```Python
await bot.fetch_skus()
```

--------------------------------

### Update Asynchronous Webhook Usage in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Shows the updated method for initializing and using asynchronous webhooks in discord.py. The `AsyncWebhookAdapter` is no longer needed; the `session` can be passed directly to the `discord.Webhook.from_url` method.

```Python
# before
async with aiohttp.ClientSession() as session:
    webhook = discord.Webhook.from_url('url-here', adapter=discord.AsyncWebhookAdapter(session))
    await webhook.send('Hello World', username='Foo')

# after
async with aiohttp.ClientSession() as session:
    webhook = discord.Webhook.from_url('url-here', session=session)
    await webhook.send('Hello World', username='Foo')
```

--------------------------------

### Manage Permissions and Settings in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details methods for setting permissions on guild channels and configuring various settings like slowmode delay, author information, embed fields, and more. This is essential for bot administration and channel management.

```python
discord.abc.GuildChannel.set_permissions()
discord.CategoryChannel.set_permissions()
discord.ForumChannel.set_permissions()
discord.StageChannel.set_permissions()
discord.TextChannel.set_permissions()
discord.VoiceChannel.set_permissions()
discord.Embed.set_author()
discord.Embed.set_field_at()
discord.Embed.set_footer()
discord.Embed.set_image()
discord.Embed.set_thumbnail()
discord.app_commands.CommandTree.set_translator()
discord.app_commands.AppCommandChannel.slowmode_delay
discord.app_commands.AppCommandThread.slowmode_delay
discord.AuditLogDiff.slowmode_delay
discord.ForumChannel.slowmode_delay
discord.StageChannel.slowmode_delay
discord.TextChannel.slowmode_delay
discord.Thread.slowmode_delay
discord.VoiceChannel.slowmode_delay
```

--------------------------------

### Handling Stickers and Sticker Packs in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to work with stickers, sticker packs, and related attributes in discord.py. This includes accessing stickers on guilds, messages, and sticker packs.

```python
guild.stickers
# Accessing stickers available on a guild

message.stickers
# Accessing stickers attached to a message

sticker_pack.stickers
# Accessing stickers within a sticker pack
```

--------------------------------

### Add description to commands.Cog

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces a `description` keyword argument for `commands.Cog` to provide descriptions for cogs. Requires discord.py's ext.commands.

```python
[ext.commands] Add support for `description` keyword argument in `commands.Cog` (GH-6028)
```

--------------------------------

### Fetch Guild Preview in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds the `Client.fetch_guild_preview()` method, allowing clients to fetch preview information for guilds.

```Python
Add `Client.fetch_guild_preview()` (GH-9986)
```

--------------------------------

### Python: Create a simple background task in a Cog

Source: https://discordpy.readthedocs.io/en/stable/ext/tasks/index

This snippet demonstrates how to create a basic background task using `@tasks.loop` within a `commands.Cog`. The task runs every 5 seconds, printing an index that increments with each execution. It also includes `cog_unload` to cancel the task when the cog is unloaded.

```Python
from discord.ext import tasks, commands\n\nclass MyCog(commands.Cog):\n    def __init__(self):\n        self.index = 0\n        self.printer.start()\n\n    def cog_unload(self):\n        self.printer.cancel()\n\n    @tasks.loop(seconds=5.0)\n    async def printer(self):\n        print(self.index)\n        self.index += 1\n
```

--------------------------------

### Publish Messages in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to publish messages across different contexts in discord.py. The `publish()` method is typically used for announcement channels or webhook messages.

```Python
await discord.InteractionMessage.publish()
```

```Python
await discord.Message.publish()
```

```Python
await discord.PartialMessage.publish()
```

```Python
await discord.WebhookMessage.publish()
```

--------------------------------

### Support Components v2 in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds support for Discord's "Components v2" in discord.py, introducing `ui.LayoutView` for manual layouting and new components like `SectionComponent`, `TextDisplay`, `ThumbnailComponent`, `MediaGalleryComponent`, `FileComponent`, `SeparatorComponent`, `Container`, and `ActionRow`. Backwards compatibility is maintained.

```python
Add support for Discord’s “Components v2” (GH-10166)
    
    * A new `ui.LayoutView` is used to use these components which requires manual layouting.
    * Backwards compatibility is maintained with everything, including `ui.DynamicItem`.
    * 

Adds the following new components with their UI counterpart
    
      * `SectionComponent` corresponds to `ui.Section`
      * `TextDisplay` corresponds to `ui.TextDisplay`
      * `ThumbnailComponent` corresponds to `ui.Thumbnail`
      * `MediaGalleryComponent` corresponds to `ui.MediaGallery`
      * `FileComponent` corresponds to `ui.File`
      * `SeparatorComponent` corresponds to `ui.Separator`
      * `Container` corresponds to `ui.Container`
      * `ActionRow` corresponds to `ui.ActionRow`
```

--------------------------------

### discord.py: Send Command Help

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Handles the implementation of the single command page in the help command. This coroutine is called for individual commands. Message sending should be done within this method using get_destination(). Customization is possible via overriding. Access invocation context via HelpCommand.context.

```Python
async def _send_command_help(self, command, /):
    """Handles the implementation of the single command page in the help command."""
    # Implementation details for sending command help messages
```

--------------------------------

### Discord Bot Load Extension

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates the 'load_extension' method for discord.py bots, used to load command extensions (cogs).

```python
from discord.ext import commands

# Loading a bot extension
# Assuming 'bot' is a commands.Bot object
# await bot.load_extension('my_cog_extension')
```

--------------------------------

### Discord Available Tags

Source: https://discordpy.readthedocs.io/en/stable/

This documentation covers the retrieval of available tags for Forum Channels and Audit Log Differences. Tags can be used for categorizing and organizing content.

```python
discord.AuditLogDiff.available_tags
discord.ForumChannel.available_tags
```

--------------------------------

### Register a Discord.py Cog

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/cogs

Demonstrates how to add a defined cog, 'Greetings', to a discord.py bot instance. This is done by creating an instance of the cog class and passing it to the `bot.add_cog()` method.

```Python
await bot.add_cog(Greetings(bot))
```

--------------------------------

### Create Application Command with @command Decorator

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

The @command decorator is used to create an application command from a regular function directly under a CommandTree. It allows customization of the command's name, description, NSFW status, and guild targeting. Parameters include name, description, nsfw, guild, guilds, auto_locale_strings, and extras.

```Python
@command(_*_, _name =..._, _description =..._, _nsfw =False_, _guild =..._, _guilds =..._, _auto_locale_strings =True_, _extras =..._)
    
A decorator that creates an application command from a regular function directly under this tree. 

Parameters
    
  * **name** (Union[`str`, `locale_str`]) – The name of the application command. If not given, it defaults to a lower-case version of the callback name.
  * **description** (Union[`str`, `locale_str`]) – The description of the application command. This shows up in the UI to describe the application command. If not given, it defaults to the first line of the docstring of the callback shortened to 100 characters.
  * **nsfw** (`bool`) – 
Whether the command is NSFW and should only work in NSFW channels. Defaults to `False`.
Due to a Discord limitation, this does not work on subcommands.
  * **guild** (Optional[`Snowflake`]) – 
The guild to add the command to. If not given or `None` then it becomes a global command instead.
Note
Due to a Discord limitation, this keyword argument cannot be used in conjunction with contexts (e.g. `app_commands.allowed_contexts()`) or installation types (e.g. `app_commands.allowed_installs()`).
  * **guilds** (List[`Snowflake`]) – 
The list of guilds to add the command to. This cannot be mixed with the `guild` parameter. If no guilds are given at all then it becomes a global command instead.
Note
Due to a Discord limitation, this keyword argument cannot be used in conjunction with contexts (e.g. `app_commands.allowed_contexts()`) or installation types (e.g. `app_commands.allowed_installs()`).
  * **auto_locale_strings** (`bool`) – If this is set to `True`, then all translatable strings will implicitly be wrapped into `locale_str` rather than `str`. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to `True`.
  * **extras** (`dict`) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.
```

--------------------------------

### Create Subcommands with discord.py Group Decorator

Source: https://discordpy.readthedocs.io/en/stable/faq

Illustrates how to create nested commands in discord.py using the `group()` decorator. This allows for organizing commands into logical groups, similar to subcommands in other frameworks.

```Python
@bot.group()
async def git(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid git command passed...')

@git.command()
async def push(ctx, remote: str, branch: str):
    await ctx.send(f'Pushing to {remote} {branch}')
```

--------------------------------

### Discord Tasks Loop

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates the use of the 'tasks.loop' decorator for creating background tasks that run periodically in discord.py.

```python
from discord.ext import tasks

# Creating a background task
# @tasks.loop(seconds=60)
# async def my_background_task():
#     print('Task is running!')

# Starting the task
# my_background_task.start()
```

--------------------------------

### Create RoleSelect Menu

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Instantiates a RoleSelect UI component for Discord interactions. It allows users to select roles from a guild. Configuration includes custom ID, placeholder text, minimum and maximum values for selection, disabled state, default selections, and row positioning.

```Python
discord.ui.RoleSelect(
    custom_id='role_select',
    placeholder='Select roles...', 
    min_values=1,
    max_values=3,
    disabled=False,
    row=0
)
```

--------------------------------

### Upload many command with Greedy discord.Attachment

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates using Greedy with discord.Attachment to capture all remaining attachments after the first required one. It lists the URLs of all provided attachments.

```Python
import discord
from discord.ext import commands

@bot.command()
async def upload_many(
    ctx,
    first: discord.Attachment,
    remaining: commands.Greedy[discord.Attachment],
):
    files = [first.url]
    files.extend(a.url for a in remaining)
    await ctx.send(f'You uploaded: {" ".join(files)})'
```

--------------------------------

### Discord.py: Working with Teams and Team Members

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access information related to teams, including the 'Team' object itself, team members, and flags indicating team membership.

```python
app_info.team
member.team
user_flags.team_user
member_role
team_membership_state
```

--------------------------------

### Connect to Discord Gateway

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Establishes a WebSocket connection to Discord, initiating the event loop and message listening. This method is crucial for the bot's operation and handles reconnection logic. It can raise GatewayNotFound or ConnectionClosed exceptions.

```python
await client._connect(reconnect=True)
```

--------------------------------

### Fetching All Application Commands for a Guild or Globally

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

The `_fetch_commands` coroutine retrieves all application commands. It can fetch global commands if no guild is specified, or commands belonging to a specific guild. This includes context menu commands.

```python
global_commands = await bot._fetch_commands()

guild_commands = await bot._fetch_commands(guild=discord.Object(id=9876543210))
```

--------------------------------

### Formatting Help Commands in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet showcases methods for formatting help commands, including 'add_aliases_formatting', 'add_bot_commands_formatting', and 'add_command_formatting' for minimal help commands.

```Python
commands.MinimalHelpCommand.add_aliases_formatting()
commands.MinimalHelpCommand.add_bot_commands_formatting()
commands.DefaultHelpCommand.add_command_formatting()
commands.MinimalHelpCommand.add_command_formatting()
```

--------------------------------

### Handling Purchase Notifications

Source: https://discordpy.readthedocs.io/en/stable/

Covers message types and structures related to purchase notifications in discord.py, which are used to inform users about successful purchases.

```Python
discord.Message.purchase_notification
```

```Python
discord.MessageType.purchase_notification
```

```Python
discord.PurchaseNotification
```

--------------------------------

### Iterate and Flatten AsyncIterator in Python

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Demonstrates how to iterate over messages using an async for loop and how to convert an AsyncIterator to a list using the flatten() method in Python.

```Python
async for message in channel.history():
    print(message)
```

```Python
messages = await channel.history().flatten()
for message in messages:
    print(message)
```

--------------------------------

### Working with Discord Stage Channel Converters in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to use the `StageChannelConverter` for converting arguments to `discord.StageChannel` objects in discord.py commands.

```python
commands.StageChannelConverter
# Converter for StageChannel arguments in commands
```

--------------------------------

### Add support for on_audit_log_entry_create() event

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces support for the new `on_audit_log_entry_create()` event, allowing developers to react to audit log entries.

```python
Add support for new `on_audit_log_entry_create()` event
```

--------------------------------

### Add Platform and Assets to Activities

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enhances the Activity and Game classes by adding support for platform information and assets. This allows for richer representation of user activities.

```python
Add support for platform and assets to activities (GH-9677).
    
    * Add `Activity.platform`.
    * Add `Game.platform`.
    * Add `Game.assets`.
```

--------------------------------

### Handle Discord Button Styles

Source: https://discordpy.readthedocs.io/en/stable/

Details the available styles for Discord UI buttons, including the `secondary` style for custom buttons.

```python
discord.ButtonStyle.secondary
```

--------------------------------

### Register Command with Decorator or add_command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows two equivalent methods for registering a command: using the `@bot.command()` decorator directly or defining the command separately and then using `bot.add_command()`.

```Python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx):
    pass

# Alternative registration:
# @commands.command()
# async def test(ctx):
#     pass
# bot.add_command(test)
```

--------------------------------

### Execute Task - discord.ext.tasks.Loop

Source: https://discordpy.readthedocs.io/en/stable/

This documentation entry refers to the execution of a loop task within the discord.ext.tasks extension. It explains how scheduled or recurring tasks are initiated and managed.

```python
tasks.Loop.__call__()
```

--------------------------------

### Accessing Discord Guild and Guild Preview Stickers in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to retrieve stickers associated with a guild or its preview using discord.py.

```python
guild.stickers
# Accessing stickers available on a guild

guild_preview.stickers
# Accessing stickers available in a guild preview
```

--------------------------------

### Discord.py Verification Levels and Member Access

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates accessing verification levels and attributes related to members, including member counts and member-specific actions.

```Python
import discord

# Example of accessing a verification level
medium_verification = discord.VerificationLevel.medium
print(medium_verification)

# Example of accessing member count in a guild
guild_member_count = discord.Guild.member_count
print(guild_member_count)

# Example of accessing member-specific audit log actions
member_update_action = discord.AuditLogAction.member_update
print(member_update_action)
```

--------------------------------

### Discord.py Media and Component Types

Source: https://discordpy.readthedocs.io/en/stable/

Shows accessing attributes and classes related to media, including media components, galleries, and different channel types.

```Python
import discord

# Example of accessing media-related attributes
media_component_media = discord.FileComponent.media
print(media_component_media)

# Example of accessing a media gallery component
media_gallery = discord.MediaGalleryComponent
print(media_gallery)

# Example of accessing a channel type for media
media_channel_type = discord.ChannelType.media
print(media_channel_type)
```

--------------------------------

### SoundboardSoundConverter for ext.commands in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `SoundboardSoundConverter` for the `discord.ext.commands` extension, facilitating the conversion of soundboard sound arguments in commands.

```Python
[ext.commands] Add `SoundboardSoundConverter` (GH-9973)
```

--------------------------------

### Basic FlagConverter Usage

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates how to define and use a FlagConverter for a ban command, specifying member, reason, and optional days. The command is invoked with a flag-like syntax.

```Python
from discord.ext import commands
import discord

class BanFlags(commands.FlagConverter):
    member: discord.Member
    reason: str
    days: int = 1

@commands.command()
async def ban(ctx, *, flags: BanFlags):
    plural = f'{flags.days} days' if flags.days != 1 else f'{flags.days} day'
    await ctx.send(f'Banned {flags.member} for {flags.reason!r} (deleted {plural} worth of messages)')

```

--------------------------------

### Resolving Discord Invites and Templates

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to resolve Discord invites and templates using utility functions. This is helpful for processing invite links and template codes.

```python
discord.utils.resolve_invite()
discord.utils.resolve_template()
```

--------------------------------

### Retrieving Items with discord.utils.get()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

A new utility function, `discord.utils.get()`, simplifies the retrieval of items from collections based on their attributes.

```Python
discord.utils.get(iterable, **attributes)
```

--------------------------------

### Spotify Album Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This documentation covers accessing Spotify 'album' and 'album_cover_url' attributes for music activity.

```Python
discord.Spotify.album
discord.Spotify.album_cover_url
```

--------------------------------

### Python: Basic Discord Member Conversion in Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Illustrates a simple command `joined` that uses `discord.Member` as a type hint. The library automatically handles the conversion of the provided argument to a `discord.Member` object.

```Python
@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')

```

--------------------------------

### Discord Command and Interaction Permissions

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to define and manage default permissions for application commands, context menus, and groups in Discord.py. This ensures commands are accessible only to authorized users.

```python
import discord

# Default member permissions for an app command
default_member_perms = discord.app_commands.AppCommand.default_member_permissions

# Default permissions for a command
default_command_perms = discord.app_commands.Command.default_permissions

# Function to set default permissions
default_permissions_func = discord.app_commands.default_permissions()
```

--------------------------------

### Create a group using the @group decorator in discord.ext.commands

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This decorator is a shortcut for creating a Group and adding it to the bot's command list. It converts a method into a Group object and registers it. It returns the created Group object.

```python
@group(*args, **kwargs)
```

--------------------------------

### Discord.py: Thumbnail and Attachment Flags

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates accessing thumbnail-related attributes for embeds and attachment flags, as well as thumbnail components.

```python
embed.thumbnail
attachment_flags.thumbnail
thumbnail_component
```

--------------------------------

### Discord Role Converters and Not Found Errors

Source: https://discordpy.readthedocs.io/en/stable/

Includes converters and exception types for handling roles, such as `commands.RoleConverter` and `commands.RoleNotFound`.

```python
commands.RoleConverter
commands.RoleNotFound
```

--------------------------------

### UserSelect Attributes and Methods

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides an overview of the attributes and methods available for the UserSelect class, including properties for custom ID, selected values, disabled state, and methods for handling interactions.

```Python
# Attributes
user_select.custom_id
user_select.default_values
user_select.disabled
user_select.id
user_select.max_values
user_select.min_values
user_select.parent
user_select.placeholder
user_select.required
user_select.type
user_select.values
user_select.view

# Methods
await user_select.callback(interaction)
await user_select.interaction_check(interaction)
```

--------------------------------

### Discord.py Message Components and Containers

Source: https://discordpy.readthedocs.io/en/stable/

Explains the structure of message components in discord.py, including ActionRows, Labels, and general component types. It also covers how components are organized within messages.

```Python
import discord
from discord.ext import commands
from discord import ui

# Example of creating a message with components
# async def send_message_with_components(ctx):
#     view = ui.View()
#     # Add a button to the view
#     view.add_item(ui.Button(label='Click Me', style=discord.ButtonStyle.primary))
#     # Add a label component
#     view.add_item(ui.Label(text='This is a label.'))

#     # Components are typically sent within ActionRows
#     # The ui.View automatically handles creating ActionRows for items added directly
#     # You can also manually create ActionRows:
#     # action_row = ui.ActionRow()
#     # action_row.add_item(ui.Button(label='Button in ActionRow'))
#     # view.add_item(action_row)

#     await ctx.send("Here are some components:", view=view)

# Example of accessing components from a message
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     if message.components:
#         print(f'Message {message.id} has components:')
#         for component in message.components:
#             # component here is an ActionRow
#             for sub_component in component.children:
#                 print(f'  - {sub_component.label or sub_component.text} (Type: {sub_component.type})')
#     await bot.process_commands(message)

# Example of ComponentType enum
# print(discord.ComponentType.button)
# print(discord.ComponentType.label)
# print(discord.ComponentType.action_row)

# bot = commands.Bot(command_prefix='!')
# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Fetch Premium Sticker Packs with Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves all available premium sticker packs for the bot. This function does not require any parameters.

```Python
await bot.fetch_premium_sticker_packs()
```

--------------------------------

### Command Aliases and Flags in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This documentation covers 'aliases' for commands and flags, used to define alternative names for commands or arguments.

```Python
commands.Command.aliases
commands.Flag.aliases
```

--------------------------------

### discord.py Optional Type Hint

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to use typing.Optional for command parameters, allowing for default values or None if the conversion fails. This converter works with positional parameters.

```Python
import typing

@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send(f'{amount} bottles of {liquid} on the wall!')
```

--------------------------------

### Walk Cog Commands (with Subcommands)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/cogs

Generates all commands within a cog, including any subcommands. This provides a comprehensive view of a cog's command structure.

```python
>>> print([c.qualified_name for c in cog.walk_commands()])
```

--------------------------------

### Use Fallback audioop Package

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Integrates a fallback package for `audioop` to ensure compatibility with Python 3.13 and newer versions.

```Python
Use a fallback package for `audioop` to allow the library to work in Python 3.13 or newer.
```

--------------------------------

### NumPy Style Docstrings for Commands

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Allows the use of NumPy style docstrings for regular commands to set parameter descriptions. This improves the clarity and consistency of command documentation, aiding in understanding command usage and parameters.

```Python
[ext.commands] Add support for NumPy style docstrings for regular commands to set parameter descriptions.
```

--------------------------------

### Describe Command Parameters - discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Describes command parameters by their name using keyword arguments. Alternatively, parameter descriptions can be provided using Google, Sphinx, or Numpy style docstrings. Raises TypeError if the parameter name is not found.

```Python
@discord.app_commands.describe(_** parameters_)
    
Describes the given parameters by their name using the key of the keyword argument as the name.
```

--------------------------------

### Discord.py: Color Conversion to RGB

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates converting a Discord color object to its RGB tuple representation.

```python
color.to_rgb()
```

--------------------------------

### Help Command Aliases Heading in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This entry shows 'aliases_heading' from 'MinimalHelpCommand', used to customize the heading for aliases in help messages.

```Python
commands.MinimalHelpCommand.aliases_heading
```

--------------------------------

### All Permissions in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This entry highlights 'Permissions.all()' and 'Permissions.all_channel()', used to represent or check all available permissions.

```Python
discord.Permissions.all()
discord.Permissions.all_channel()
```

--------------------------------

### Allowing All Mentions and Intents in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet demonstrates 'AllowedMentions.all()' and 'Intents.all()', used to configure or enable all possible mentions and intents respectively.

```Python
discord.AllowedMentions.all()
discord.Intents.all()
```

--------------------------------

### discord.py HelpCommand Base Implementation

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The HelpCommand class serves as the foundation for creating custom help commands in discord.py bots. It manages the display of bot, cog, and command help, with options to control hidden command visibility and command check verification. Instances are deep-copied on invocation to prevent state-related issues.

```python
class discord.ext.commands.HelpCommand:
    # Attributes: cog, command_attrs, context, invoked_with, show_hidden, verify_checks
    # Methods: add_check, async_command_callback, command_not_found, async_filter_commands, get_bot_mapping, get_command_signature, get_destination, get_max_size, async_on_help_command_error, async_prepare_help_command, remove_check, remove_mentions, async_send_bot_help, async_send_cog_help, async_send_command_help, async_send_error_message, async_send_group_help, subcommand_not_found
    pass
```

--------------------------------

### Discord Colour Light Theme

Source: https://discordpy.readthedocs.io/en/stable/

Provides methods for creating light-themed colors in discord.py, including light embed colors and shades of gray.

```python
import discord

# Creating light embed color
light_embed_color = discord.Colour.light_embed()

# Creating light gray color
light_gray_color = discord.Colour.light_gray()
light_grey_color = discord.Colour.light_grey()

# Creating lighter gray colors
lighter_gray_color = discord.Colour.lighter_gray()
lighter_grey_color = discord.Colour.lighter_grey()
```

--------------------------------

### Discord Sticker Description

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves descriptions for various sticker types, including StandardSticker, Sticker, and StickerPack.

```python
discord.StandardSticker.description
discord.Sticker.description
discord.StickerPack.description
```

--------------------------------

### Accessing Discord Client and Bot Stickers in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to retrieve stickers available through the client or bot instance in discord.py.

```python
client.stickers
# Accessing all available stickers via the client

bot.stickers
# Accessing all available stickers via the bot
```

--------------------------------

### Command Parameters

Source: https://discordpy.readthedocs.io/en/stable/

Represents the parameters associated with an application command.

```Python
discord.app_commands.Command.parameters
```

--------------------------------

### ChannelSelect Initialization

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Initializes a ChannelSelect component for Discord UI. Allows customization of channel types, placeholder text, selection limits, and default values. Note that channel types are filtered to specific types, and placeholder text has a character limit.

```python
discord.ui.ChannelSelect(_*_, _custom_id =..., _channel_types =..., _placeholder =None_, _min_values =1_, _max_values =1_, _disabled =False_, _row =None_, _default_values =..._, _id =None_)
```

--------------------------------

### Discord.py Member and Role Management

Source: https://discordpy.readthedocs.io/en/stable/

Covers accessing member-related classes and attributes, including member converters, member flags, and role membership.

```Python
from discord.ext import commands
import discord

# Example of a member converter
member_converter = commands.MemberConverter
print(member_converter)

# Example of accessing member flags
member_flags = discord.MemberFlags
print(member_flags)

# Example of accessing membership state of a team member
membership_state = discord.TeamMember.membership_state
print(membership_state)
```

--------------------------------

### Python: Presence and Member Update Events

Source: https://discordpy.readthedocs.io/en/stable/migrating

Illustrates the separation of on_member_update and the introduction of on_presence_update events. This change aligns the library with API behavior and improves efficiency for listeners.

```Python
# before
@client.event
async def on_member_update(self, before, after):
    if before.nick != after.nick:
        await nick_changed(before, after)
    if before.status != after.status:
        await status_changed(before, after)

# after
@client.event
async def on_member_update(self, before, after):
    if before.nick != after.nick:
        await nick_changed(before, after)

@client.event
async def on_presence_update(self, before, after):
    if before.status != after.status:
        await status_changed(before, after)
```

--------------------------------

### Discord.py: Terms of Service URL Access

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to retrieve the 'terms_of_service_url' from application information objects.

```python
app_info.terms_of_service_url
partial_app_info.terms_of_service_url
```

--------------------------------

### Accessing Discord Sticker Packs and Items in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to work with sticker packs and individual sticker items in discord.py, including accessing the stickers within a pack.

```python
discord.StickerPack
# Represents a sticker pack

discord.StickerItem
# Represents an individual sticker item
```

--------------------------------

### Discord.py - Miscellaneous Attributes and Values

Source: https://discordpy.readthedocs.io/en/stable/

This snippet lists various attributes and values across different discord.py classes, including command context, transformer errors, flags, and version information.

```Python
commands.Context.valid
discord.app_commands.TransformerError.value
discord.ApplicationFlags.value
discord.AttachmentFlags.value
discord.AutoModPresets.value
discord.ChannelFlags.value
discord.Colour.value
discord.EmbedFlags.value
commands.RangeError.value
discord.Intents.value
discord.InviteFlags.value
discord.MemberCacheFlags.value
discord.MemberFlags.value
discord.MessageFlags.value
discord.Permissions.value
discord.PublicUserFlags.value
discord.RoleFlags.value
discord.SelectOption.value
discord.SKUFlags.value
discord.SystemChannelFlags.value
discord.TextInput.value
discord.ui.TextInput.value
commands.TooManyFlags.values
discord.ui.ChannelSelect.values
discord.ui.MentionableSelect.values
discord.ui.RoleSelect.values
discord.ui.Select.values
discord.ui.UserSelect.values
discord.version_info
```

--------------------------------

### Add Properties to PartialAppInfo and AppInfo

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enhances `PartialAppInfo` and `AppInfo` by adding several new properties, providing more detailed information about applications within the Discord API.

```Python
# Add various new properties to PartialAppInfo and AppInfo (GH-9298).
```

--------------------------------

### Create Discord Forum Tag

Source: https://discordpy.readthedocs.io/en/stable/

Allows for the creation of a tag within a forum channel, used to categorize and organize posts.

```python
await discord.ForumChannel.create_tag()
```

--------------------------------

### Manage Discord Events and Integrations with discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet covers functionalities related to managing scheduled events, integrations, and subscription statuses within Discord. It includes attributes for event times, statuses, and methods for interacting with integrations and entitlements.

```python
discord.Activity.end
discord.Game.end
discord.Spotify.end
discord.Poll.end()
discord.ScheduledEvent.end()
discord.InteractionMessage.end_poll()
discord.Message.end_poll()
discord.PartialMessage.end_poll()
discord.WebhookMessage.end_poll()
discord.ScheduledEvent.end_time
discord.EventStatus.ended
discord.CallMessage.ended_timestamp
discord.SubscriptionStatus.ending
discord.VoiceClient.endpoint
discord.Entitlement.ends_at
discord.Entitlement
discord.Subscription.entitlement_ids
discord.Interaction.entitlement_sku_ids
discord.EntitlementOwnerType
discord.Interaction.entitlements
discord.Client.entitlements()
commands.Bot.entitlements()
discord.EntitlementType
discord.ScheduledEvent.entity_id
discord.AuditLogDiff.entity_type
discord.ScheduledEvent.entity_type
discord.EntityType
discord.Attachment.ephemeral
discord.MessageFlags.ephemeral
discord.Client.event()
commands.Bot.event()
discord.AuditLogDiff.event_type
discord.AutoModRule.event_type
discord.RawReactionActionEvent.event_type
discord.Permissions.events()
discord.EventStatus
discord.AllowedMentions.everyone
```

--------------------------------

### Add SKU Subscriptions Support in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Implements support for SKU subscriptions, introducing new events such as `on_subscription_create()`, `on_subscription_update()`, and `on_subscription_delete()`. It also adds a `SubscriptionStatus` enum, a `Subscription` model, and methods like `SKU.fetch_subscription()` and `SKU.subscriptions()`.

```Python
Adds new events `on_subscription_create()`, `on_subscription_update()`, and `on_subscription_delete()`
Add `SubscriptionStatus` enum
Add `Subscription` model
Add `SKU.fetch_subscription()` and `SKU.subscriptions()`
```

--------------------------------

### Add support for guest invites in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces support for guest invites in discord.py, facilitating easier server access for new members.

```python
Add support for guest invites (GH-10220)
```

--------------------------------

### Accessing Discord Subscription Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to access subscription-related information, including the subscription status and SKU types, using discord.py.

```python
discord.Subscription
# Represents a user's subscription

discord.SubscriptionStatus
# Enum for different subscription statuses
```

--------------------------------

### Managing Discord Guild and Member Status in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to access and manage status information for members and guilds, including widget member status and client status.

```python
member.status
# Getting the current status of a member

widget_member.status
# Getting the status of a member in a widget

client.status
# Getting the client's current status
```

--------------------------------

### Discord Role Select Component

Source: https://discordpy.readthedocs.io/en/stable/

Represents a UI component that allows users to select roles.

```python
discord.ui.RoleSelect
```

--------------------------------

### Bot Check Registration

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Demonstrates implementing `bot_check` to register a check that runs for every command invocation within the cog.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def bot_check(self, ctx):
        # Example: Ensure bot is ready before commands execute
        if self.bot.is_ready():
            return True
        raise commands.CheckFailure('Bot is not ready yet.')
```

--------------------------------

### Discord.py Polls and Multiple Choice Prompts

Source: https://discordpy.readthedocs.io/en/stable/

This snippet covers attributes for handling polls and multiple choice options in discord.py, including poll multiplicity and onboarding prompt types.

```python
poll_multiple = discord.Poll.multiple
multiple_choice_prompt = discord.OnboardingPromptType.multiple_choice
```

--------------------------------

### Send Bot Help Page (Python)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Handles the implementation for the bot command page in the help command, called when no arguments are provided. This coroutine method should send the message internally using `get_destination()`. The `mapping` parameter is positional-only since version 2.0, and commands are not pre-filtered.

```python
async def _send_bot_help(mapping, /):
    """
    Handles the implementation of the bot command page in the help command. This function is called when the help command is called with no arguments.
    It should be noted that this method does not return anything – rather the actual message sending should be done inside this method. Well behaved subclasses should use `get_destination()` to know where to send, as this is a customisation point for other users.
    You can override this method to customise the behaviour.
    Note
        You can access the invocation context with `HelpCommand.context`.
    Also, the commands in the mapping are not filtered. To do the filtering you will have to call `filter_commands()` yourself.
    Changed in version 2.0: `mapping` parameter is now positional-only.

    Parameters
        mapping (Mapping[Optional[Cog], List[Command]]): A mapping of cogs to commands that have been requested by the user for help. The key of the mapping is the `Cog` that the command belongs to, or `None` if there isn’t one, and the value is a list of commands that belongs to that cog.
    """
    pass
```

--------------------------------

### Discord.py: Handling Temporary Attributes and Timeouts

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates accessing attributes related to temporary status and timeouts, such as 'temporary' flags, 'timed_out_until' timestamps, and timeout-related actions.

```python
audit_log_diff.temporary
invite.temporary
member.timed_out_until
auto_mod_action_type.timeout
view.timeout
```

--------------------------------

### App Command Permissions

Source: https://discordpy.readthedocs.io/en/stable/

Represents permissions for application commands, including specific permission settings.

```Python
discord.app_commands.AppCommandPermissions.permission
discord.app_commands.AppCommandChannel.permissions
discord.app_commands.AppCommandThread.permissions
discord.app_commands.GuildAppCommandPermissions.permissions
discord.AppInstallParams.permissions
discord.AuditLogDiff.permissions
commands.Context.permissions
discord.Interaction.permissions
discord.RawAppCommandPermissionsUpdateEvent.permissions
discord.Role.permissions
```

--------------------------------

### Pass client to Webhook.from_url() and Webhook.partial()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Allows passing a client instance to `Webhook.from_url()` and `Webhook.partial()`, enabling the use of views for bot-owned webhooks.

```python
Add support for passing a client to `Webhook.from_url()` and `Webhook.partial()`
    
    * This allows them to use views (assuming they are “bot owned” webhooks)
```

--------------------------------

### Discord.py - Accessing Verification and Vanity URL Information

Source: https://discordpy.readthedocs.io/en/stable/

This snippet covers accessing verification-related attributes and vanity URL information for guilds and applications. It includes properties like `verification_level`, `vanity_url`, and `vanity_url_code`.

```Python
guild.vanity_url
guild.vanity_url_code
partial_invite_guild.vanity_url
partial_invite_guild.vanity_url_code
app_info.verify_key
partial_app_info.verify_key
client_user.verified
public_user_flags.verified_bot
user_flags.verified_bot
public_user_flags.verified_bot_developer
user_flags.verified_bot_developer
commands.HelpCommand.verify_checks
```

--------------------------------

### User Select Component in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates the usage of the User Select component in discord.py for creating interactive UI elements where users can select other users.

```python
discord.ui.UserSelect
discord.ComponentType.user_select
```

--------------------------------

### Discord Hybrid Command Autocomplete

Source: https://discordpy.readthedocs.io/en/stable/

This covers implementing autocomplete for hybrid commands and groups in Discord.py. It allows for dynamic suggestions for command arguments, enhancing user experience.

```python
commands.HybridCommand.autocomplete()
commands.HybridGroup.autocomplete()
```

--------------------------------

### Discord.py: Working with Titles and Embeds

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates accessing and setting the 'title' attribute for various objects, including attachments, embeds, and prompts, as well as converting embeds to dictionaries.

```python
attachment.title
embed.title
embed.to_dict()
```

--------------------------------

### discord.py: Using AsyncIterator.get()

Source: https://discordpy.readthedocs.io/en/stable/migrating

Demonstrates the change from using AsyncIterator.get() to discord.utils.get() for finding an item within an asynchronous iterator, specifying criteria like author name.

```Python
# before
msg = await channel.history().get(author__name='Dave')

# after
msg = await discord.utils.get(channel.history(), author__name='Dave')
```

--------------------------------

### Discord Guild Product Purchase Listing ID

Source: https://discordpy.readthedocs.io/en/stable/

Shows the 'listing_id' attribute for Discord Guild Product Purchases, which uniquely identifies a product listing.

```python
import discord

# Accessing the listing ID for a guild product purchase
listing_id = discord.GuildProductPurchase.listing_id
```

--------------------------------

### Discord Command Description

Source: https://discordpy.readthedocs.io/en/stable/

Retrieves the description for commands, cogs, flags, and parameters within the discord.py command framework.

```python
commands.Bot.description
commands.Cog.description
commands.CogMeta.description
commands.Command.description
commands.Flag.description
commands.Parameter.description
```

--------------------------------

### Python: Inline Advanced Converter for Custom Data

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates creating an inline advanced converter for a custom class `JoinDistance`. The `convert` class method handles the conversion logic, allowing the custom class to be used directly as a type hint in commands.

```Python
class JoinDistance:
    def __init__(self, joined, created):
        self.joined = joined
        self.created = created

    @classmethod
    async def convert(cls, ctx, argument):
        member = await commands.MemberConverter().convert(ctx, argument)
        return cls(member.joined_at, member.created_at)

    @property
    def delta(self):
        return self.joined - self.created

@bot.command()
async def delta(ctx, *, member: JoinDistance):
    is_new = member.delta.days < 100
    if is_new:
        await ctx.send("Hey you're pretty new!")
    else:
        await ctx.send("Hm you're not so new.")

```

--------------------------------

### discord.py Application Command Types

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Specifies the different types of application commands available in Discord. These include chat input (slash commands), user context menu commands, and message context menu commands.

```Python
class _discord.AppCommandType:
    """The type of application command.
    New in version 2.0.
    """
    chat_input = ...
    user = ...
    message = ...
```

--------------------------------

### Create Discord Invite

Source: https://discordpy.readthedocs.io/en/stable/

Facilitates the creation of an invite link for a specific channel. This can be done for various channel types including guild channels, category channels, forum channels, stage channels, text channels, and voice channels.

```python
await discord.abc.GuildChannel.create_invite()
await discord.CategoryChannel.create_invite()
await discord.ForumChannel.create_invite()
await discord.StageChannel.create_invite()
await discord.TextChannel.create_invite()
await discord.VoiceChannel.create_invite()
```

--------------------------------

### MinimalHelpCommand: Add Aliases Formatting

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Formats a command's aliases for the paginator. The default implementation bolds the `aliases_heading` and lists aliases separated by commas. This method is not called if there are no aliases. The parameter is positional-only since version 2.0.

```Python
def add_aliases_formatting(aliases, /):
    """Adds the formatting information on a command’s aliases.

    The formatting should be added to the `paginator`.
    The default implementation is the `aliases_heading` bolded followed by a
    comma separated list of aliases.
    This is not called if there are no aliases to format.
    Changed in version 2.0: `aliases` parameter is now positional-only.

    Parameters
    ----------
    aliases : Sequence[str]
        A list of aliases to format.
    """
    pass
```

--------------------------------

### Discord.py: Handling Too Many Arguments and Flags

Source: https://discordpy.readthedocs.io/en/stable/

Documents exceptions related to command arguments and flags, specifically 'TooManyArguments' and 'TooManyFlags'.

```python
commands.TooManyArguments
commands.TooManyFlags
```

--------------------------------

### Discord.py Permissions Management

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates accessing various permission flags and management-related attributes within discord.py, such as managing channels, emojis, guilds, roles, and webhooks.

```Python
import discord

# Example of accessing a permission
manage_channels_permission = discord.Permissions.manage_channels
print(manage_channels_permission)

# Example of accessing a managed emoji attribute
managed_emoji = discord.Emoji.managed
print(managed_emoji)

# Example of accessing a managed role attribute
managed_role = discord.Role.managed
print(managed_role)
```

--------------------------------

### Discord.py Message and Interaction Handling

Source: https://discordpy.readthedocs.io/en/stable/

Covers accessing message-related attributes and handling interactions, including message objects and command context.

```Python
import discord
from discord.ext import commands

# Example of accessing the message object from context
# async def get_message_from_context(ctx: commands.Context):
#     return ctx.message

# Example of accessing the message from an interaction
# async def get_message_from_interaction(interaction: discord.Interaction):
#     return interaction.message

# Example of accessing a message object
message_obj = discord.Message
print(message_obj)
```

--------------------------------

### Edit Application Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Asynchronously edits an existing application command with new parameters like name, description, permissions, DM permission status, and options. It returns the updated AppCommand object and can raise exceptions for various issues including missing IDs or permissions.

```Python
await app_command.edit(
    name="new_name",
    description="new_description",
    default_member_permissions=Permissions.from_string("read"),
    dm_permission=False,
    options=[...]
)
# Returns: AppCommand
# Raises: NotFound, Forbidden, HTTPException, MissingApplicationID
```

--------------------------------

### Discord.py UI Element Length and Value Limits

Source: https://discordpy.readthedocs.io/en/stable/

Covers accessing properties for setting maximum lengths and values for UI elements like text inputs and arguments in discord.py.

```Python
import discord

# Example of accessing max length for an argument
argument_max_length = discord.app_commands.Argument.max_length
print(argument_max_length)

# Example of accessing max length for a text input
text_input_max_length = discord.TextInput.max_length
print(text_input_max_length)

# Example of accessing max value for an argument
argument_max_value = discord.app_commands.Argument.max_value
print(argument_max_value)
```

--------------------------------

### SoundboardSoundConverter: Convert to SoundboardSound

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Converts an argument to a SoundboardSound. Similar to other converters, it prioritizes local guild lookups and falls back to the global cache for DM contexts. Lookups are performed by ID, then by name. This feature was introduced in version 2.5.

```python
class SoundboardSoundConverter:
    async def convert(self, ctx, argument):
        # Conversion logic here
        pass
```

--------------------------------

### Discord.py: Interaction and Status Properties

Source: https://discordpy.readthedocs.io/en/stable/

This snippet covers various properties related to user status, command behavior, and interaction handling within discord.py. It includes attributes for checking if extra arguments are ignored, indentation in help commands, and the status of integrations.

```python
discord.PrimaryGuild.identity_enabled
discord.Status.idle
commands.Command.ignore_extra
discord.Embed.image
discord.AuditLogDiff.in_onboarding
discord.OnboardingPrompt.in_onboarding
discord.RoleFlags.in_prompt
discord.SubscriptionStatus.inactive
discord.WebhookType.incoming
commands.DefaultHelpCommand.indent
discord.Locale.indonesian
```

--------------------------------

### Bot Check Once Registration

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Shows how to implement `bot_check_once` to register a check that runs once per bot invocation for commands within the cog.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def bot_check_once(self, ctx):
        # Example: Log every command invocation
        print(f'Command invoked: {ctx.command}')
        return True
```

--------------------------------

### Configure Default Intents with Exclusions

Source: https://discordpy.readthedocs.io/en/stable/intents

This snippet demonstrates how to initialize default intents and then disable specific ones like 'typing' and 'presences'. It shows how to pass these configured intents to either `discord.Client` or `commands.Bot`.

```python
import discord

intents = discord.Intents.default()
typing = False
presences = False

# Somewhere else:
# client = discord.Client(intents=intents)
# or
# from discord.ext import commands
# bot = commands.Bot(command_prefix='!', intents=intents)
```

--------------------------------

### Discord App Command Description Localizations

Source: https://discordpy.readthedocs.io/en/stable/

Allows access to description localizations for Discord application commands, groups, and arguments.

```python
discord.app_commands.AppCommand.description_localizations
discord.app_commands.AppCommandGroup.description_localizations
discord.app_commands.Argument.description_localizations
```

--------------------------------

### Upload command with discord.Attachment converter

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Illustrates retrieving a single uploaded file using the discord.Attachment converter. The command sends back the URL of the uploaded file.

```Python
import discord
from discord.ext import commands

@bot.command()
async def upload(ctx, attachment: discord.Attachment):
    await ctx.send(f'You have uploaded <{attachment.url}>')
```

--------------------------------

### Fetch Premium Sticker Pack in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds `Client.fetch_premium_sticker_pack()` to retrieve information about premium sticker packs.

```Python
Add `Client.fetch_premium_sticker_pack()` (GH-9909)
```

--------------------------------

### Handle Private Channel Restrictions

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to handle commands or contexts that are restricted to private channels in discord.py. This includes checking for private channel context and applying restrictions.

```Python
discord.app_commands.AppCommandContext.private_channel
```

```Python
discord.app_commands.private_channel_only()
```

```Python
discord.Client.private_channels
```

```Python
commands.Bot.private_channels
```

```Python
commands.PrivateMessageOnly
```

--------------------------------

### Formatting Subcommands in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This entry highlights 'add_subcommand_formatting()' from 'MinimalHelpCommand' for formatting subcommands in help messages.

```Python
commands.MinimalHelpCommand.add_subcommand_formatting()
```

--------------------------------

### Working with Discord Commands and Context in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to access information about subcommand usage within a command context in discord.py.

```python
context.subcommand_passed
# Information about the subcommand that was passed
```

--------------------------------

### Using clean_content converter with default and custom options

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to use the built-in `clean_content` converter to sanitize message content. It can be used directly or with custom initialization parameters, such as `use_nicknames=False`.

```Python
import discord
from discord.ext import commands

# Assuming 'bot' is an instance of commands.Bot
# bot = commands.Bot(command_prefix='!')

@bot.command()
async def clean(ctx, *, content: commands.clean_content):
    await ctx.send(content)

# or for fine-tuning

@bot.command()
async def clean(ctx, *, content: commands.clean_content(use_nicknames=False)):
    await ctx.send(content)
```

--------------------------------

### discord.py: AutoShardedClient Redesign for Multi-Process

Source: https://discordpy.readthedocs.io/en/stable/whats_new

The `AutoShardedClient` has been redesigned for better multi-process cluster support. It includes `ShardInfo` for shard-specific operations, methods to access shard information, and a reworked connection flow to handle `IDENTIFY` rate limits. A `before_identify_hook` is also added for pre-identification control.

```Python
shard_info = await auto_sharded_client.get_shard(shard_id)
await auto_sharded_client.shards
await auto_sharded_client.before_identify_hook()
```

--------------------------------

### Manage Soundboards in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Provides methods for managing soundboards within guilds and clients. This includes accessing soundboard sounds via `Client.soundboard_sounds` and `Guild.soundboard_sounds`, fetching default sounds, and creating new soundboard entries.

```Python
`Client.soundboard_sounds`
`Guild.soundboard_sounds`
`Client.get_soundboard_sound()`
`Guild.get_soundboard_sound()`
`Client.fetch_soundboard_default_sounds()`
`Guild.fetch_soundboard_sound()`
`Guild.fetch_soundboard_sounds()`
`Guild.create_soundboard_sound()`
```

--------------------------------

### Reference Channels in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section lists various ways channels are referenced and identified within discord.py, including types, permissions, context, and interaction-related attributes.

```python
discord.AppCommandOptionType.channel
discord.AppCommandPermissionType.channel
discord.AuditLogDiff.channel
discord.AutoModAction.channel
commands.BucketType.channel
commands.Context.channel
commands.NSFWChannelRequired.channel
discord.Interaction.channel
discord.Invite.channel
discord.Message.channel
discord.PartialMessage.channel
discord.ScheduledEvent.channel
discord.SelectDefaultValueType.channel
discord.StageInstance.channel
discord.SyncWebhook.channel
discord.VoiceChannelEffect.channel
discord.VoiceClient.channel
discord.VoiceState.channel
discord.Webhook.channel
discord.WelcomeChannel.channel
```

--------------------------------

### Respect ext.commands Hybrid App Command Enabled

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Ensures that the `enabled` keyword argument is respected for hybrid application commands in the `ext.commands` extension.

```Python
[ext.commands] Respect `enabled` keyword argument for hybrid app commands (GH-10001)
```

--------------------------------

### Convert to Game

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Converts a string argument to a Game object. This converter is straightforward and does not involve complex lookup strategies.

```python
class GameConverter(Converter):
    async def convert(self, ctx, argument):
        # Converts to a Game object
        pass
```

--------------------------------

### ext.commands: Add linesep keyword argument to Paginator

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces the `linesep` keyword argument to the `Paginator` class in `ext.commands`. This allows customization of the line separator used when paginating messages, offering more control over message formatting.

```Python
from discord.ext.commands.view import Paginator

# Example usage:
# paginator = Paginator(pages=['Page 1', 'Page 2'], linesep='---\n')

```

--------------------------------

### Create MentionableSelect Menu

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Instantiates a MentionableSelect UI component for Discord interactions. This allows users to select members or roles from a guild. Customization options include placeholder text, minimum and maximum number of selections, disabled state, default selections, and row positioning.

```python
discord.ui.MentionableSelect(
    custom_id='unique-select-id',
    placeholder='Select members or roles...', 
    min_values=1,
    max_values=3,
    disabled=False,
    row=0
)
```

--------------------------------

### discord.py: Using AsyncIterator.flatten()

Source: https://discordpy.readthedocs.io/en/stable/migrating

Shows how to replace AsyncIterator.flatten() with a list comprehension over the asynchronous iterator to collect all items.

```Python
# before
users = await reaction.users().flatten()

# after
users = [user async for user in reaction.users()]
```

--------------------------------

### Accessing Discord Stage Instance Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to interact with Stage Instances, including creating, deleting, and updating them, as well as accessing related audit log actions.

```python
discord.StageInstance
# Represents a Stage Instance

entity_type.stage_instance
# Enum value for Stage Instance entity type
```

--------------------------------

### Validate Keyword Arguments in Client Start/Run

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Ensures keyword arguments passed to Client.start() and Client.run() are validated.

```Python
client.start()
client.run()
```

--------------------------------

### Partial Application Information

Source: https://discordpy.readthedocs.io/en/stable/

Represents partial application information, likely for reduced data retrieval.

```Python
discord.PartialAppInfo
```

--------------------------------

### Accessing Discord Guild and Invite Target Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access information related to guild invites and target types for streams using discord.py.

```python
invite_target.stream
# Representing a stream as an invite target
```

--------------------------------

### Define a Discord Bot Cog

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Demonstrates how to create a custom Cog by inheriting from discord.ext.commands.Cog. This allows grouping related commands and listeners for better organization in a Discord bot.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Add commands and listeners here

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

--------------------------------

### Run Bot - discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

A blocking call that abstracts away the event loop initialisation. This function also sets up the logging library. This function must be the last function to call due to the fact that it is blocking.

```Python
run(_token_ , _*_ , _reconnect =True_, _log_handler =..._, _log_formatter =..._, _log_level =..._, _root_logger =False_)
```

--------------------------------

### Iterate Through Cog Application Commands

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Details the `walk_app_commands()` method, an iterator that recursively yields all application commands and groups defined within the cog.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='greet')
    async def greet(self, interaction: discord.Interaction):
        await interaction.response.send_message('Greetings!')

    @discord.app_commands.command(name='farewell')
    async def farewell(self, interaction: discord.Interaction):
        await interaction.response.send_message('Goodbye!')

    def iterate_app_commands(self):
        for app_command in self.walk_app_commands():
            print(app_command.name)
```

--------------------------------

### Discord.py Command Argument Types

Source: https://discordpy.readthedocs.io/en/stable/

Lists various types of command arguments that can be used in discord.py, including arguments for bad values, colors, and unions.

```python
commands.BadArgument
commands.BadBoolArgument
commands.BadColourArgument
commands.BadFlagArgument
commands.BadInviteArgument
commands.BadLiteralArgument
commands.BadUnionArgument
```

--------------------------------

### Discord.py: Webhook Functionalities

Source: https://discordpy.readthedocs.io/en/stable/

Covers various aspects of webhook integration in discord.py, including creating, deleting, and updating webhooks, as well as handling webhook messages and intents.

```python
discord.Webhook
discord.AuditLogAction.webhook_create
discord.AuditLogAction.webhook_delete
discord.Message.webhook_id
discord.AuditLogAction.webhook_update
discord.WebhookMessage
discord.Intents.webhooks
discord.ForumChannel.webhooks()
discord.Guild.webhooks()
discord.StageChannel.webhooks()
discord.TextChannel.webhooks()
discord.VoiceChannel.webhooks()
```

--------------------------------

### discord.py: PartialInviteGuild Icon URL

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Updates `PartialInviteGuild.icon_url_as()` to support `static_format` for consistent icon URL generation.

```Python
icon_url = partial_invite_guild.icon_url_as(format='png')
```

--------------------------------

### Listen to Discord Messages with discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Demonstrates how to use the `@bot.listen('on_message')` decorator to create a listener for incoming messages in discord.py. This function will be called for every message the bot can see.

```Python
import discord

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.listen('on_message')
async def my_message(message):
    print('two')

# Example of another listener
@bot.event
async def on_message(message):
    print('one')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Manage Self-Role and Guild Settings in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Provides access to the self-role configured for a guild and methods for managing guild-specific settings.

```python
discord.Guild.self_role
```

--------------------------------

### Add default_reaction_emoji and default_forum_layout to Guild.create_forum()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Updates `Guild.create_forum()` to accept `default_reaction_emoji` and `default_forum_layout` parameters, allowing customization of default settings when creating forum channels.

```Python
# Add support for default_reaction_emoji and default_forum_layout in Guild.create_forum() (GH-9300).
```

--------------------------------

### Accessing Soundboard Sounds in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to access soundboard sound-related attributes and methods within discord.py. This includes properties on Guild, Bot, and specific Soundboard classes.

```python
guild.soundboard_sounds
# Accessing soundboard sounds on a Guild object

bot.soundboard_sounds
# Accessing soundboard sounds on a Bot object
```

--------------------------------

### Send Cog Help Page (Python)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Handles the implementation for the cog page in the help command, called when a cog is provided as an argument. This coroutine method should send the message internally using `get_destination()`. Subclasses can override this method for customization.

```python
async def _send_cog_help(cog, /):
    """
    Handles the implementation of the cog page in the help command. This function is called when the help command is called with a cog as the argument.
    It should be noted that this method does not return anything – rather the actual message sending should be done inside this method. Well behaved subclasses should use `get_destination()` to know where to send, as this is a customisation point for other users.
    You can override this method to customise the behaviour.
    Note
    """
    pass
```

--------------------------------

### Working with Discord Attachments and Files in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to handle Discord attachments and files, including accessing their properties like spoiler status and source message deleted flag.

```python
attachment_flags.spoiler
# Checking if an attachment is a spoiler

message_flags.source_message_deleted
# Checking if the source message for flags was deleted
```

--------------------------------

### Formatting Command Arguments in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This entry highlights 'add_command_arguments()' from 'DefaultHelpCommand' for formatting command arguments in help messages.

```Python
commands.DefaultHelpCommand.add_command_arguments()
```

--------------------------------

### Discord Allowed Mentions and Guild Roles

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to specify allowed roles for mentions and access the list of roles within a guild.

```python
discord.AllowedMentions.roles
discord.Guild.roles
```

--------------------------------

### discord.py: Command Callback

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The core implementation of the help command. It's recommended to customize behavior through other dispatched methods rather than overriding this coroutine directly. It handles dispatching to specific help sending methods.

```Python
async def _command_callback(self, ctx, /, *args, command=None):
    """The actual implementation of the help command."""
    # Core logic for the help command
```

--------------------------------

### Retrieving Account Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This documentation covers accessing the 'account' attribute for various integration types, including Bot, Integration, PartialIntegration, and StreamIntegration.

```Python
discord.BotIntegration.account
discord.Integration.account
discord.PartialIntegration.account
discord.StreamIntegration.account
```

--------------------------------

### Discord Command with Predefined Choices

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Defines a Discord slash command that accepts a 'fruits' parameter with predefined choices (apple, banana, cherry). The command responds with the user's selected favorite fruit.

```python
import discord
from discord import app_commands

# Assuming Choice is defined elsewhere or imported
# from discord.app_commands import Choice

# Placeholder for Choice if not imported
class Choice:
    def __init__(self, name, value):
        self.name = name
        self.value = value

@app_commands.describe(fruits='fruits to choose from')
@app_commands.choices(fruits=[
    Choice(name='apple', value=1),
    Choice(name='banana', value=2),
    Choice(name='cherry', value=3),
])
async def fruit(interaction: discord.Interaction, fruits: Choice[int]):
    await interaction.response.send_message(f'Your favourite fruit is {fruits.name}.')
```

--------------------------------

### Add Equality and Hash Support to Asset

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enables equality comparison and hash support for the Asset class.

```Python
# Asset equality and hash support.
```

--------------------------------

### Define Command Callbacks in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet illustrates how to define callback functions for commands and context menus in discord.py. It points to the `callback` attribute in `discord.app_commands.Command`, `discord.app_commands.ContextMenu`, and `commands.Command`.

```python
discord.app_commands.Command.callback
discord.app_commands.ContextMenu.callback
commands.Command.callback
```

--------------------------------

### Handle Channel Mentions and Types in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section covers attributes related to channel mentions, message types, and component types in discord.py. It includes `channel_mentions`, `channel_message`, `channel_select`, and channel type specifications for app commands.

```python
discord.Message.channel_mentions
discord.InteractionResponseType.channel_message
discord.MessageType.channel_name_change
discord.ComponentType.channel_select
discord.app_commands.Argument.channel_types
discord.app_commands.Parameter.channel_types
discord.app_commands.Transformer.channel_types
discord.SelectMenu.channel_types
discord.ui.ChannelSelect.channel_types
```

--------------------------------

### Discord UI Label Description

Source: https://discordpy.readthedocs.io/en/stable/

Provides access to the description attribute for discord.ui.Label, a UI element for displaying text.

```python
discord.ui.Label.description
```

--------------------------------

### Add Colour Preview for Colour Class

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds a color preview feature for colors predefined in the `Colour` class. This allows developers to easily visualize the colors available within the library.

```Python
Add colour preview for the colours predefined in `Colour`
```

--------------------------------

### Add role tag support

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces support for role tags, allowing access to premium subscriber roles, bot-managed roles, and integration roles. Requires discord.py.

```python
Add support for role tags.
    
    * `Guild.premium_subscriber_role` to get the “Nitro Booster” role (if available).
    * `Guild.self_role` to get the bot’s own role (if available).
    * `Role.tags` to get the role’s tags.
    * `Role.is_premium_subscriber()` to check if a role is the “Nitro Booster” role.
    * `Role.is_bot_managed()` to check if a role is a bot role (i.e. the automatically created role for bots).
    * `Role.is_integration()` to check if a role is role created by an integration.
```

--------------------------------

### Join Notification Settings

Source: https://discordpy.readthedocs.io/en/stable/

Flags related to join notifications in system channels, specifically for join notification replies and general join notifications.

```python
discord.SystemChannelFlags.join_notification_replies
```

```python
discord.SystemChannelFlags.join_notifications
```

--------------------------------

### Create Context Menu Command with @context_menu Decorator

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

The @context_menu decorator creates an application command context menu from a regular function. The function must accept an Interaction as the first parameter and a Member, User, or Message as the second. It allows customization of the command's name, NSFW status, and guild targeting.

```Python
@context_menu(_*_, _name =..._, _nsfw =False_, _guild =..._, _guilds =..._, _auto_locale_strings =True_, _extras =..._)
    
A decorator that creates an application command context menu from a regular function directly under this tree.
This function must have a signature of `Interaction` as its first parameter and taking either a `Member`, `User`, or `Message`, or a `typing.Union` of `Member` and `User` as its second parameter.
Examples
content_copy```
@app_commands.context_menu()
async def react(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message('Very cool message!', ephemeral=True)

@app_commands.context_menu()
async def ban(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f'Should I actually ban {user}...', ephemeral=True)

```


Parameters
    
  * **name** (Union[`str`, `locale_str`]) – The name of the context menu command. If not given, it defaults to a title-case version of the callback name. Note that unlike regular slash commands this can have spaces and upper case characters in the name.
  * **nsfw** (`bool`) – 
Whether the command is NSFW and should only work in NSFW channels. Defaults to `False`.
Due to a Discord limitation, this does not work on subcommands.
```

--------------------------------

### Autocomplete for Discord Command Parameter

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This Python code demonstrates how to use the `@autocomplete` decorator to provide suggestions for a command parameter. The `fruits_autocomplete` function takes the interaction and current user input, returning a list of `Choice` objects for the 'fruit' parameter.

```Python
import discord
from discord import app_commands
from typing import List

# Assume 'app_commands' is imported and a command is defined
# @app_commands.command()
# async def fruits(interaction: discord.Interaction, fruit: str):
#     await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')

@fruits.autocomplete('fruit')
async def fruits_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    # Example: Provide a list of fruits based on current input
    fruit_choices = [
        app_commands.Choice(name='Apple', value='apple'),
        app_commands.Choice(name='Banana', value='banana'),
        app_commands.Choice(name='Cherry', value='cherry'),
    ]
    return [choice for choice in fruit_choices if choice.name.lower().startswith(current.lower())]

```

--------------------------------

### Add Options to a Discord Select Menu

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Shows how to add options to an existing discord.ui.Select component using the `add_option` method. Each option can have a label, value, description, emoji, and a default selected state.

```Python
import discord

select_menu = discord.ui.Select()

select_menu.add_option(
    label="Option A",
    value="value_a",
    description="Description for option A",
    emoji="🅰️"
)
select_menu.add_option(
    label="Option B",
    value="value_b",
    description="Description for option B",
    default=True
)
```

--------------------------------

### Working with Discord Sticker Types in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to use the `StickerType` enum in discord.py to categorize different types of stickers.

```python
discord.StickerType
# Enum for different sticker types

discord.StickerType.standard
# Represents a standard sticker type
```

--------------------------------

### Python: Override Cog Loading in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Demonstrates how to override an already loaded cog in discord.py using the `override` parameter in `Bot.add_cog()`. This is a change from previous versions where a `ClientException` was raised.

```python
from discord.ext import commands

# Assuming 'bot' is an instance of commands.Bot
# cog_instance = MyCog()
# bot.add_cog(cog_instance, override=True) # Use override=True to replace an existing cog
```

--------------------------------

### Restarting and Resuming Discord Voice Clients

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to restart a loop task and resume a voice client connection in discord.py. These methods are essential for managing background tasks and audio playback.

```python
tasks.Loop.restart()
discord.VoiceClient.resume()
```

--------------------------------

### Create Discord Direct Message Channel

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Initiates a direct message channel with a specified user. This is typically handled transparently by the library but can be called explicitly. Introduced in version 2.0.

```python
await client._create_dm(user_snowflake)
```

--------------------------------

### Accessing Primary Guild Information

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access the primary guild associated with users, members, and client users in discord.py. Also includes information about primary SKU IDs and guilds.

```Python
discord.ClientUser.primary_guild
```

```Python
discord.Member.primary_guild
```

```Python
discord.TeamMember.primary_guild
```

```Python
discord.User.primary_guild
```

```Python
discord.WidgetMember.primary_guild
```

```Python
discord.AppInfo.primary_sku_id
```

```Python
discord.PrimaryGuild
```

--------------------------------

### Pack Sticker

Source: https://discordpy.readthedocs.io/en/stable/

Represents a standard sticker and provides a method to pack it.

```Python
discord.StandardSticker.pack()
discord.StandardSticker.pack_id
```

--------------------------------

### Create Discord Stage Channel

Source: https://discordpy.readthedocs.io/en/stable/

Facilitates the creation of a new stage channel within a guild or category, designed for live audio events.

```python
await discord.CategoryChannel.create_stage_channel()
await discord.Guild.create_stage_channel()
```

--------------------------------

### discord.py: Using AsyncIterator.chunk()

Source: https://discordpy.readthedocs.io/en/stable/migrating

Explains the change from AsyncIterator.chunk() to discord.utils.as_chunks() for iterating over an asynchronous iterator in chunks of a specified size.

```Python
# before
async for leader, *users in reaction.users().chunk(3):
    ...

# after
async for leader, *users in discord.utils.as_chunks(reaction.users(), 3):
    ...
```

--------------------------------

### Create Custom Activities

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `CustomActivity` for creating custom presence activities. Note that bots currently cannot send custom activities.

```Python
CustomActivity(name='Custom Status', state='Playing a game')
```

--------------------------------

### Define Command Prefix: Mention or Specific Prefix

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Provides a callable for the `Bot.command_prefix` attribute that allows commands to be invoked either by mentioning the bot or by using a specified prefix. It can also handle multiple prefixes.

```Python
discord.ext.commands.when_mentioned_or(* prefixes)
```

```Python
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
```

```Python
async def get_prefix(bot, message):
    extras = await prefixes_for(message.guild) # returns a list
    return commands.when_mentioned_or(*extras)(bot, message)
```

--------------------------------

### Python Enhancement Proposals (PEP)

Source: https://discordpy.readthedocs.io/en/stable/

Lists relevant Python Enhancement Proposals (PEPs) that are often referenced in Python development, including PEP 3107, PEP 440, and PEP 526.

```Python
PEP 3107
```

```Python
PEP 440
```

```Python
PEP 526
```

--------------------------------

### Discord.py Base Classes

Source: https://discordpy.readthedocs.io/en/stable/

Represents base classes for various Discord entities, providing a foundation for more specific implementations.

```python
discord.BaseActivity
discord.BaseSoundboardSound
```

--------------------------------

### Handle Invite Create and Delete Events

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds support for `on_invite_create()` and `on_invite_delete()` events. These events allow bots to track when invites are created or deleted within a guild.

```Python
async def on_invite_create(invite):
    pass
```

```Python
async def on_invite_delete(invite):
    pass
```

--------------------------------

### Command Parameter Name/Description

Source: https://discordpy.readthedocs.io/en/stable/

Specifies translation context locations for parameter names and descriptions in application commands.

```Python
discord.app_commands.TranslationContextLocation.parameter_description
discord.app_commands.TranslationContextLocation.parameter_name
```

--------------------------------

### Adding Options to Select Menus in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This entry shows the 'add_option()' method for the 'Select' UI component, used to add options to a select menu.

```Python
discord.ui.Select.add_option()
```

--------------------------------

### Working with Discord Role Tags and Subscription Listings in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to access subscription listing IDs associated with role tags in discord.py.

```python
role_tags.subscription_listing_id
# The ID of the subscription listing associated with the role
```

--------------------------------

### Append Items to UI Select Menus

Source: https://discordpy.readthedocs.io/en/stable/

Provides methods to add options or items to select components within Discord's UI framework. This is used for creating interactive menus for users to choose from.

```Python
discord.ui.Select.append_option()
discord.ui.MediaGallery.append_item()
```

--------------------------------

### Handling Rate Limits

Source: https://discordpy.readthedocs.io/en/stable/whats_new

The library now automatically handles rate limiting, ensuring smoother interactions with the Discord API.

```Python
# No specific code example, handled internally by the library.
```

--------------------------------

### Set Parameter Choices - discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Instructs command parameters to use specific choices for their options. This is done by providing choices keyed by the parameter name.

```Python
@discord.app_commands.choices(_** parameters_)
    
Instructs the given parameters by their name to use the given choices for their choices.
```

--------------------------------

### Working with Locale and Message Types

Source: https://discordpy.readthedocs.io/en/stable/

Covers locale settings, specific message types like 'poll_result' and premium guild tiers, and the `pong` interaction response type in discord.py.

```Python
discord.Locale.polish
```

```Python
discord.MessageType.poll_result
```

```Python
discord.MessageType.premium_guild_subscription
```

```Python
discord.MessageType.premium_guild_tier_1
```

```Python
discord.MessageType.premium_guild_tier_2
```

```Python
discord.MessageType.premium_guild_tier_3
```

```Python
discord.InteractionResponseType.pong
```

```Python
discord.InteractionResponse.pong()
```

--------------------------------

### Python: Creating a Reusable Check Decorator

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to create a custom decorator factory (`is_owner`) that returns a check function. This pattern allows for more organized and reusable check logic, especially when checks need parameters or have internal state.

```Python
def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 316026178463072268
    return commands.check(predicate)

@bot.command(name='eval')
@is_owner()
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))
```

--------------------------------

### Discord.py Content Length and UI Layouts

Source: https://discordpy.readthedocs.io/en/stable/

Covers methods related to calculating content length for UI elements like ActionRows, Containers, and Sections, which is relevant for UI layout management in discord.py.

```Python
import discord
from discord.ext import commands
from discord import ui

# Example of content_length for UI elements (conceptual)
# These methods are typically internal or used for layout calculations.

# class MyActionRow(ui.ActionRow):
#     def content_length(self):
#         # Calculates the length/size of the ActionRow based on its children
#         return len(self.children)

# class MyContainer(ui.Container):
#     def content_length(self):
#         # Calculates the length/size of the Container
#         return len(self.children)

# class MyLayoutView(ui.View):
#     def content_length(self):
#         # Calculates the length/size of the View
#         return len(self.children)

# class MySection(ui.View):
#     def content_length(self):
#         # Calculates the length/size of the Section
#         return len(self.children)

# Example of Attachment content_type
# async def check_attachment_type(ctx, attachment: discord.Attachment):
#     print(f'Attachment {attachment.filename} content type: {attachment.content_type}')

# Example of UnfurledMediaItem content_type
# class UnfurledMediaItem:
#     def __init__(self, content_type):
#         self.content_type = content_type

# media_item = UnfurledMediaItem('image/jpeg')
# print(f'Media item content type: {media_item.content_type}')

# bot = commands.Bot(command_prefix='!')
# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Custom converter using Converter class for random member slapping

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Defines a custom converter `Slapper` that inherits from `commands.Converter`. It randomly selects a guild member and formats a string indicating the author slapping the chosen member for a given reason.

```Python
import discord
import random
from discord.ext import commands

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f'{ctx.author} slapped {to_slap} because *{argument}*'

# Assuming 'bot' is an instance of commands.Bot
# bot = commands.Bot(command_prefix='!')

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)
```

--------------------------------

### Handle Discord Stage Instance Events

Source: https://discordpy.readthedocs.io/en/stable/

These events relate to stage instances within Discord, such as their creation, deletion, or updates. They are useful for managing live audio events.

```python
discord.on_stage_instance_create(instance: discord.StageInstance) -> None
```

```python
discord.on_stage_instance_update(instance: discord.StageInstance) -> None
```

```python
discord.on_stage_instance_delete(instance: discord.StageInstance) -> None
```

--------------------------------

### Add Proxy Support for CDN Fetching

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Implements proxy support for fetching resources from the Content Delivery Network (CDN), enhancing network flexibility.

```Python
Add proxy support fetching from the CDN (GH-9966)
```

--------------------------------

### Python discord.py: Hybrid command with flattened flags

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates how discord.py's FlagConverter flattens parameters for hybrid commands. A FlagConverter class with 'member', 'reason', and 'days' is shown to be equivalent to individual parameters in a hybrid command.

```Python
class BanFlags(commands.FlagConverter):
    member: discord.Member
    reason: str
    days: int = 1


@commands.hybrid_command()
async def ban(ctx, *, flags: BanFlags):
    ...

```

```Python
@commands.hybrid_command()
async def ban(ctx, member: discord.Member, reason: str, days: int = 1):
    ...

```

--------------------------------

### Embed constructor parameters now implicitly convert to str

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Updates the `Embed` constructor to implicitly convert its parameters to strings. This simplifies embedding creation by automatically handling type conversions for fields like title, description, and URL.

```Python
from discord import Embed

# Example usage:
# embed = Embed(title=123, description=45.67)
# # Title will be '123', description will be '45.67'
```

--------------------------------

### Discord Permissions and Member Deafening

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to manage member deafening status and the corresponding permission flags in Discord.py. This is essential for voice channel management.

```python
import discord

# Checking member deafened status
is_deafened = discord.WidgetMember.deafened

# Permission for deafening members
can_deafen = discord.Permissions.deafen_members

# Voice state deafened status
voice_deafened = discord.VoiceState.deaf
```

--------------------------------

### Manage Discord Invites

Source: https://discordpy.readthedocs.io/en/stable/

This snippet details functionalities for managing Discord invites, including creating, deleting, and updating invites, as well as retrieving invite-related information. It's useful for bots that manage server access or track invite statistics.

```python
discord.AuditLogDiff.inviter
discord.Invite.inviter
discord.Intents.invites
discord.abc.GuildChannel.invites()
discord.CategoryChannel.invites()
discord.ForumChannel.invites()
discord.Guild.invites()
discord.StageChannel.invites()
discord.TextChannel.invites()
discord.VoiceChannel.invites()
discord.Guild.invites_paused()
discord.Guild.invites_paused_until
discord.InviteTarget
discord.InviteType
discord.AuditLogAction.invite_create
discord.AuditLogAction.invite_delete
discord.AuditLogAction.invite_update
discord.Widget.invite_url
commands.InviteConverter
discord.TeamMembershipState.invited
discord.InviteFlags
discord.Invite
```

--------------------------------

### All Commands in GroupMixin in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This documentation covers 'all_commands' attribute in 'GroupMixin', which returns a dictionary of all commands within a group.

```Python
commands.GroupMixin.all_commands
```

--------------------------------

### Define Checks for App Commands and Context Menus

Source: https://discordpy.readthedocs.io/en/stable/

Allows defining custom checks for discord.app_commands.Command and discord.app_commands.ContextMenu. These checks are functions that determine if the command can be invoked.

```python
from discord import app_commands

# Example for Command:
# class MyCog(commands.Cog):
#     @app_commands.command()
#     @app_commands.check(my_custom_check)
#     async def my_app_command(self, interaction: discord.Interaction):
#         await interaction.response.send_message("Hello!")

# Example for ContextMenu:
# @app_commands.context_menu(name="My Context Menu")
# @app_commands.check(another_check)
# async def my_context_menu(interaction: discord.Interaction):
#     await interaction.response.send_message("Context menu action!")
```

--------------------------------

### Command Paginator

Source: https://discordpy.readthedocs.io/en/stable/

Defines classes and attributes related to command pagination, including the paginator itself and its pages.

```Python
commands.Paginator.pages
commands.Paginator
commands.DefaultHelpCommand.paginator
commands.MinimalHelpCommand.paginator
```

--------------------------------

### Launch Activity Interaction

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Responds to a Discord interaction by launching an associated application activity. This is only available for apps with activities enabled and is a coroutine. New in version 2.6.

```Python
async def _launch_activity():
    """This function is a _coroutine_.
    Responds to this interaction by launching the activity associated with the app. Only available for apps with activities enabled.
    New in version 2.6.
    """
    pass
```

--------------------------------

### Configure Discord App Information and Slugs

Source: https://discordpy.readthedocs.io/en/stable/

Provides access to application information, including the application's slug, which is a unique identifier used in URLs and API endpoints.

```python
discord.AppInfo.slug
```

--------------------------------

### Discord.py - Voice Channel and Client Management

Source: https://discordpy.readthedocs.io/en/stable/

This snippet focuses on functionalities related to voice channels and voice clients within discord.py. It includes accessing voice channels, managing voice states, and interacting with the voice client.

```Python
discord.CategoryChannel.voice_channels
discord.Guild.voice_channels
commands.Context.voice_client
discord.Guild.voice_client
discord.Client.voice_clients
commands.Bot.voice_clients
discord.Intents.voice_states
discord.StageChannel.voice_states
discord.VoiceChannel.voice_states
discord.VoiceChannel
commands.VoiceChannelConverter
discord.VoiceChannelEffect
discord.VoiceChannelEffectAnimation
discord.VoiceChannelEffectAnimationType
discord.VoiceChannelSoundEffect
discord.VoiceClient
discord.VoiceProtocol
discord.VoiceState
discord.Member.voice
discord.MemberCacheFlags.voice
discord.MessageFlags.voice
discord.EntityType.voice
```

--------------------------------

### Support Soundboard and VC Effects in discord.py

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces support for Soundboard and Voice Channel effects. This includes new models for soundboard sounds and voice channel effects, methods for sending sounds via `VoiceChannel.send_sound()`, and updates to audit log actions and intents related to expressions and emojis.

```Python
Add `BaseSoundboardSound`, `SoundboardDefaultSound`, and `SoundboardSound`
Add `VoiceChannelEffect`
Add `VoiceChannelEffectAnimation`
Add `VoiceChannelEffectAnimationType`
Add `VoiceChannelSoundEffect`
Add `VoiceChannel.send_sound()`
Add new audit log actions: `AuditLogAction.soundboard_sound_create`, `AuditLogAction.soundboard_sound_update`, and `AuditLogAction.soundboard_sound_delete`.
Add `Intents.expressions` and make `Intents.emojis` and `Intents.emojis_and_stickers` aliases of that intent.
Add new events: `on_soundboard_sound_create()`, `on_soundboard_sound_update()`, `on_soundboard_sound_delete()`, and `on_voice_channel_effect()`.
```

--------------------------------

### Discord.py Content Filtering and Context

Source: https://discordpy.readthedocs.io/en/stable/

Covers handling message content, including explicit media detection, and managing command context. Also includes methods for consuming entitlements and handling content-related errors.

```Python
import discord
from discord.ext import commands

# Intents needed to read message content
# intents = discord.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     # Check for explicit media in attachments
#     if message.attachments:
#         for attachment in message.attachments:
#             if attachment.flags.contains_explicit_media:
#                 await message.channel.send(f'Attachment {attachment.filename} might contain explicit media.')

#     # Check for explicit media in embeds
#     if message.embeds:
#         for embed in message.embeds:
#             if embed.flags.contains_explicit_media:
#                 await message.channel.send('An embed might contain explicit media.')

#     # Process commands after handling message content
#     await bot.process_commands(message)

# Example of context usage within a command
# @bot.command()
# async def show_context(ctx):
#     await ctx.send(f'Command invoked in channel: {ctx.channel.name}')
#     await ctx.send(f'Invoked by: {ctx.author.name}')

# Example of consuming entitlements (hypothetical)
# class Entitlement:
#     def consume(self):
#         # Logic to consume entitlement
#         pass
#     consumed = property(lambda self: True) # Example property

# Example of handling TranslationError context
# class TranslationError(Exception):
#     def __init__(self, message, context):
#         super().__init__(message)
#         self.context = context

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### discord.py AppCommandChannel Methods

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Describes the methods available for the AppCommandChannel class, including checking if the channel is NSFW or a news channel, resolving the channel from cache, and fetching the full channel object.

```Python
class AppCommandChannel:
    def is_nsfw(self) -> bool
    def is_news(self) -> bool
    def resolve(self) -> Optional[abc.GuildChannel]
    async def fetch(self) -> abc.GuildChannel
```

--------------------------------

### Fetch Specific Premium Sticker Pack with Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a specific premium sticker pack using its unique ID. Requires the `sticker_pack_id` as an integer argument.

```Python
await bot.fetch_premium_sticker_pack(1234567890)
```

--------------------------------

### Creating Abstract Cog Mixins with CogMeta

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Demonstrates how to create an abstract cog mixin by combining discord.py's CogMeta with Python's abc.ABCMeta. It shows the structure for defining a base abstract cog and a mixin class that inherits from both.

```Python
import abc

class CogABCMeta(commands.CogMeta, abc.ABCMeta):
    pass

class SomeMixin(metaclass=abc.ABCMeta):
    pass

class SomeCogMixin(SomeMixin, commands.Cog, metaclass=CogABCMeta):
    pass
```

--------------------------------

### Add parameters to Guild.create_stage_channel()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Expands support for numerous parameters within `Guild.create_stage_channel()`.

```python
Add support for many more parameters within `Guild.create_stage_channel()` (GH-9245)
```

--------------------------------

### Manage App Command Allowed Contexts

Source: https://discordpy.readthedocs.io/en/stable/

Allows specifying the contexts in which an application command can be used. This is useful for controlling command availability across different Discord environments (e.g., guilds, DMs).

```Python
discord.app_commands.Group.allowed_contexts
commands.Bot.allowed_contexts
discord.app_commands.allowed_contexts()
```

--------------------------------

### Create a Discord.py Command

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The `@discord.ext.commands.command()` decorator transforms a Python function into a Discord command. It automatically extracts help text from the function's docstring. Checks added via other decorators are included, and custom checks cannot be supplied directly through this decorator.

```python
import discord
from discord.ext import commands

@commands.command()
async def my_command(ctx):
    """This is my custom command."""
    await ctx.send('Hello!')
```

--------------------------------

### User Converter and Input Errors in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains the UserConverter class for converting input to User objects and the UserInputError for handling user-related input issues in discord.py commands.

```python
commands.UserConverter
commands.UserInputError
commands.UserNotFound
```

--------------------------------

### Discord Member Roles and Role Tags

Source: https://discordpy.readthedocs.io/en/stable/

Covers attributes for accessing a member's roles and information about role tags.

```python
discord.Member.roles
discord.RoleTags
```

--------------------------------

### Fetch Application Info with Team Support

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enhances `Client.application_info()` to include support for teams, allowing retrieval of team-related information when fetching application details. This is useful for applications managed by teams.

```Python
client.application_info()
```

--------------------------------

### Create Discord Permissions - Events

Source: https://discordpy.readthedocs.io/en/stable/

Represents the permission to create events within Discord.

```python
discord.Permissions.create_events
```

--------------------------------

### Register Commands with discord.app_commands.CommandTree

Source: https://discordpy.readthedocs.io/en/stable/

The central object for managing and syncing application commands with Discord. It allows adding commands, groups, and syncing them to specific guilds or globally.

```python
import discord
from discord.ext import commands

# Example:
# class MyBot(commands.Bot):
#     def __init__(self):
#         super().__init__(command_prefix='!', intents=discord.Intents.default())
#         self.tree = app_commands.CommandTree(self)
#
#     async def on_ready(self):
#         await self.tree.sync() # Sync commands globally
#         print(f'Logged in as {self.user}')
#
# bot = MyBot()
# bot.run('YOUR_TOKEN')
```

--------------------------------

### Create a UI Container with discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This snippet shows how to create a UI container in discord.py, which can hold other UI components like ActionRows. It demonstrates subclassing ui.Container and adding components, such as buttons, within it.

```Python
import discord
from discord import ui

class MyContainer(ui.Container):
    action_row = ui.ActionRow()

    @action_row.button(label='A button in a container!')
    async def a_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You clicked a button!')

```

--------------------------------

### Adding Commands to Command Trees and Bots in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet demonstrates adding commands to command trees and bots using 'add_command()', applicable to app commands, groups, and general command management.

```Python
discord.app_commands.CommandTree.add_command()
discord.app_commands.Group.add_command()
commands.Bot.add_command()
commands.Group.add_command()
commands.GroupMixin.add_command()
commands.HybridGroup.add_command()
```

--------------------------------

### Migrate from Client.send_message to Channel.send

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Demonstrates the migration from the older `client.send_message` method to the new `channel.send` method for sending simple text messages in discord.py. This change simplifies message sending.

```python
await client.send_message(channel, 'Hello')
```

```python
await channel.send('Hello')
```

--------------------------------

### Process Commands with discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates the process of handling and executing commands within a discord.py bot. The `process_commands()` method is crucial for the bot's command invocation system.

```Python
await discord.Bot.process_commands(message)
```

--------------------------------

### Add support for PartialEmoji.url_as()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces the `url_as()` method to the `PartialEmoji` class. This method allows developers to retrieve the URL for a partial emoji in different formats or sizes, enhancing emoji handling capabilities.

```Python
from discord import PartialEmoji

# Example usage:
# emoji = PartialEmoji(id=1234567890)
# url = emoji.url_as(size=128)
```

--------------------------------

### Send Discord Webhook Message (Sync)

Source: https://discordpy.readthedocs.io/en/stable/migrating

Demonstrates how to send a message to a Discord webhook using the synchronous `SyncWebhook` class. It requires the webhook ID and token, and allows customization of the username.

```python
webhook = discord.SyncWebhook.partial(123456, 'token-here')
webhook.send('Hello World', username='Foo')
```

--------------------------------

### Configure AutoShardedClient with Shard Count and IDs

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Illustrates how to configure `discord.AutoShardedClient` to manage a specific number of shards or a subset of shard IDs. This provides more granular control over the bot's sharding strategy.

```Python
# launch 10 shards regardless
client = discord.AutoShardedClient(shard_count=10)

# launch specific shard IDs in this process
client = discord.AutoShardedClient(shard_count=10, shard_ids=(1, 2, 5, 6))
```

--------------------------------

### Add an item to LayoutView

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Adds an item to the LayoutView, allowing for fluent-style chaining. This method raises exceptions if the item is invalid, the view is full, or the item cannot be added to the specified row.

```python
layout_view.add_item(item)
```

--------------------------------

### Accessing Discord Audit Log Actions in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Lists various audit log actions available in discord.py, covering events like sticker creation, deletion, updates, and stage instance modifications.

```python
audit_log_action.sticker_create
# Audit log action for sticker creation

audit_log_action.stage_instance_delete
# Audit log action for deleting a stage instance
```

--------------------------------

### ext.commands: Allow None for HelpCommand.verify_checks

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Modifies `HelpCommand.verify_checks` to accept `None`. When `None` is provided, checks are only verified in a guild context, simplifying the handling of checks in DMs versus guilds.

```Python
from discord.ext import commands

# Example usage:
# class CustomHelp(commands.HelpCommand):
#     def __init__(self):
#         super().__init__()
#         self.verify_checks = None # Verify checks only in guilds

# bot.help_command = CustomHelp()
```

--------------------------------

### Create Test Discord Entitlement

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Creates a test entitlement for an application's SKU, linking it to an owner and owner type. This feature was added in version 2.4 and requires the application ID. It can raise MissingApplicationID, NotFound exceptions.

```python
await client._create_entitlement(sku_snowflake, owner_snowflake, discord.EntitlementOwnerType.user)
```

--------------------------------

### Discord.py AutoMod Actions and Triggers

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing attributes related to Discord's AutoMod actions and triggers, including matched content, keywords, mention limits, and mention spam protection.

```Python
import discord

# Example of accessing an AutoMod action attribute
matched_content_action = discord.AutoModAction.matched_content
print(matched_content_action)

# Example of accessing an AutoMod trigger type
mention_spam_trigger = discord.AutoModRuleTriggerType.mention_spam
print(mention_spam_trigger)
```

--------------------------------

### Create Discord Hybrid Command (@hybrid_command)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The @hybrid_command decorator creates a hybrid command, which works both as a traditional command and an application command. It invokes hybrid_command() and adds it to the internal command list via add_command(). It returns a decorator that converts a method into a Command.

```Python
@hybrid_command(_name =..., _with_app_command =True_, _* args_, _** kwargs_)
def hybrid_command_func(self):
    pass
```

--------------------------------

### Discord.py: Walk Commands and Children

Source: https://discordpy.readthedocs.io/en/stable/

Enables iteration over commands and child elements within command structures and UI components. This is useful for introspection and managing command hierarchies or UI layouts.

```python
commands.Cog.walk_app_commands()
discord.ui.ActionRow.walk_children()
discord.ui.Container.walk_children()
discord.ui.LayoutView.walk_children()
discord.ui.Modal.walk_children()
discord.ui.Section.walk_children()
discord.ui.View.walk_children()
discord.app_commands.CommandTree.walk_commands()
discord.app_commands.Group.walk_commands()
commands.Bot.walk_commands()
commands.Cog.walk_commands()
commands.Group.walk_commands()
commands.GroupMixin.walk_commands()
commands.HybridGroup.walk_commands()
```

--------------------------------

### Fetch Default Soundboard Sounds with Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves all default soundboard sounds available to the bot. This function does not require any parameters.

```Python
await bot.fetch_soundboard_default_sounds()
```

--------------------------------

### Autocomplete Choices for Discord Commands

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Generates a list of autocomplete choices for a Discord command based on a provided list of fruits and a search query. It filters the fruits to match the query case-insensitively.

```Python
fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
return [
    app_commands.Choice(name=fruit, value=fruit)
    for fruit in fruits if current.lower() in fruit.lower()
]
```

--------------------------------

### Create Discord Role

Source: https://discordpy.readthedocs.io/en/stable/

Allows a guild to create a new role, which can then be assigned to members to manage permissions and hierarchy.

```python
await discord.Guild.create_role()
```

--------------------------------

### Managing Member Permissions and MFA in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet details attributes related to member permissions, Multi-Factor Authentication (MFA), and user flags in discord.py. It covers MFA status, MFA levels, and specific user flags like MFA SMS.

```python
mfa_enabled = discord.ClientUser.mfa_enabled
mfa_level_diff = discord.AuditLogDiff.mfa_level
mfa_level_guild = discord.Guild.mfa_level
mfa_sms_flag = discord.UserFlags.mfa_sms
mfa_level_enum = discord.MFALevel
```

--------------------------------

### Discord.py Button Components

Source: https://discordpy.readthedocs.io/en/stable/

Defines and utilizes button components for interactive messages. This includes creating buttons, handling button clicks, and styling them.

```python
discord.Button
discord.ui.Button
discord.ComponentType.button
discord.ui.ActionRow.button()
discord.ui.button()
discord.Activity.buttons
discord.ButtonStyle
discord.ButtonStyle.blurple
```

--------------------------------

### Python: Late Binding with Default Parameter

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to use `commands.parameter` with a lambda function for late binding of a default command parameter value.

```Python
@bot.command()
async def wave(ctx, to: discord.User = commands.parameter(default=lambda ctx: ctx.author)):
    await ctx.send(f'Hello {to.mention} :wave:')
```

--------------------------------

### Working with Discord Status Display Types in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to use the `StatusDisplayType` enum in discord.py to represent different ways user statuses can be displayed.

```python
status_display_type
# Enum for different status display types
```

--------------------------------

### discord.SelectOption

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Represents a single option within a select menu. It includes properties for label, value, description, emoji, and default selection status.

```python
class SelectOption:
    label: str
    value: str
    description: Optional[str]
    emoji: Optional[PartialEmoji]
    default: bool
```

--------------------------------

### Discord.py Colors

Source: https://discordpy.readthedocs.io/en/stable/

Provides functionalities for working with colors in discord.py, including predefined colors and methods to create custom colors.

```python
discord.Colour.b
discord.Colour.blue()
discord.Colour.blurple()
discord.Colour.brand_green()
discord.Colour.brand_red()
```

--------------------------------

### Discord.py: Spotify Track Information

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access the 'track_id' and 'track_url' from Spotify activity.

```python
spotify.track_id
spotify.track_url
```

--------------------------------

### ext.commands: Add PartialMessageConverter

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `PartialMessageConverter` to the `ext.commands` extension. This converter allows commands to accept `PartialMessage` objects, enabling easier referencing and interaction with specific messages.

```Python
from discord.ext import commands

# Example usage within a command:
# @bot.command()
# async def get_message_content(ctx, message: commands.PartialMessageConverter):
#     await ctx.send(f'Message content: {message.content}')
```

--------------------------------

### Fix Signature Display for None Parameters

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Addresses an issue in `ext.commands` where `=None` was incorrectly displayed in the command signature, improving the clarity of command documentation.

```Python
# [ext.commands] Fix =None being displayed in signature.
```

--------------------------------

### Adding an Application Command to the Tree

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

The `add_command` method adds an application command or group to the command tree. Commands are added locally and require a `sync()` call to be enabled in the client. It supports adding commands globally or to specific guilds, with an option to override existing commands.

```python
await bot.add_command(my_command, guild=discord.Object(id=9876543210))
await bot.add_command(another_command, guilds=[discord.Object(id=9876543210), discord.Object(id=1122334455)])
```

--------------------------------

### Execute Discord Commands and Checks

Source: https://discordpy.readthedocs.io/en/stable/

This snippet focuses on command execution and related checks within discord.py, including invoking commands, checking cooldowns, and determining ownership. It's essential for building command-based bots.

```python
commands.Bot.invoke()
commands.Context.invoke()
commands.Group.invoke_without_command
commands.Context.invoked_parents
commands.Command.invoked_subcommand
commands.Context.invoked_subcommand
commands.Context.invoked_with
commands.HelpCommand.invoked_with
commands.is_owner()
commands.Bot.is_owner()
commands.Command.is_on_cooldown()
commands.Group.is_on_cooldown()
commands.HybridGroup.is_on_cooldown()
```

--------------------------------

### Add ForumChannel.default_layout

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds support for `ForumChannel.default_layout`.

```python
Add support for `ForumChannel.default_layout`
```

--------------------------------

### Discord.py Message Attributes: Content, Type, Flags, and More

Source: https://discordpy.readthedocs.io/en/stable/

This section outlines attributes related to the content, type, and flags of messages in discord.py, along with message-related application and converter objects.

```python
message_snapshots = discord.Message.message_snapshots
message_type = discord.MessageType
message_flags = discord.MessageFlags
message_application = discord.MessageApplication
message_reference = discord.MessageReference
message_interaction = discord.MessageInteraction
message_interaction_metadata = discord.MessageInteractionMetadata
message_converter = commands.MessageConverter
message_not_found = commands.MessageNotFound
messageable = discord.abc.Messageable
```

--------------------------------

### Add scheduled_event parameter for StageChannel.create_instance()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds the `scheduled_event` parameter to `StageChannel.create_instance()`, allowing the creation of stage instances associated with a scheduled event.

```Python
import discord

class StageChannel:
    def create_instance(self, *, scheduled_event: discord.ScheduledEvent = None):
        pass

# Example usage:
# stage_channel = discord.utils.get(guild.channels, name='Stage')
# scheduled_event = discord.utils.get(guild.scheduled_events, name='My Event')
# if stage_channel and scheduled_event:
#     stage_channel.create_instance(scheduled_event=scheduled_event)

```

--------------------------------

### Discord.py: Accessing Interaction Tokens and Webhook Tokens

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access the 'token' attribute for interactions, sync webhooks, voice clients, and webhooks.

```python
interaction.token
sync_webhook.token
voice_client.token
webhook.token
```

--------------------------------

### Handle Silent Messages and Single Selects

Source: https://discordpy.readthedocs.io/en/stable/

Covers flags for sending silent messages and attributes related to single-select options in onboarding prompts or audit log differences.

```python
discord.MessageFlags.silent
discord.AuditLogDiff.single_select
discord.OnboardingPrompt.single_select
```

--------------------------------

### Fetch Discord Entitlements

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Retrieves a list of entitlements for a Discord application, with options to filter by limit, date, SKUs, user, guild, and exclusion criteria. It handles potential errors like missing application IDs or HTTP exceptions.

```Python
async def fetch_entitlements(self, *, limit: Optional[int] = 100, before: Optional[Union[Snowflake, datetime.datetime]] = None, after: Optional[Union[Snowflake, datetime.datetime]] = None, skus: Optional[Sequence[Snowflake]] = None, user: Optional[Snowflake] = None, guild: Optional[Snowflake] = None, exclude_ended: bool = False, exclude_deleted: bool = True):
    """Fetches entitlements for the application.

    All parameters are optional.

    Parameters
    ----------
    limit : Optional[int]
        The number of entitlements to retrieve. If None, it retrieves every entitlement for this application. Note, however, that this would make it a slow operation. Defaults to 100.
    before : Optional[Union[Snowflake, datetime.datetime]]
        Retrieve entitlements before this date or entitlement. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
    after : Optional[Union[Snowflake, datetime.datetime]]
        Retrieve entitlements after this date or entitlement. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
    skus : Optional[Sequence[Snowflake]]
        A list of SKUs to filter by.
    user : Optional[Snowflake]
        The user to filter by.
    guild : Optional[Snowflake]
        The guild to filter by.
    exclude_ended : bool
        Whether to exclude ended entitlements. Defaults to False.
    exclude_deleted : bool
        Whether to exclude deleted entitlements. Defaults to True.

    Raises
    ------
    MissingApplicationID
        The application ID could not be found.
    HTTPException
        Fetching the entitlements failed.
    TypeError
        Both `after` and `before` were provided, as Discord does not support this type of pagination.

    Yields
    ------
    Entitlement
        The entitlement with the application.
    """
    pass
```

--------------------------------

### Migrate from Client.send_file to Channel.send with single file

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Illustrates the transition from `client.send_file` to `channel.send` for uploading a single file in discord.py. The new method uses the `discord.File` object for file uploads.

```python
await client.send_file(channel, 'cool.png', filename='testing.png', content='Hello')
```

```python
await channel.send('Hello', file=discord.File('cool.png', 'testing.png'))
```

--------------------------------

### Channel Jump URLs

Source: https://discordpy.readthedocs.io/en/stable/

Provides jump URLs for various types of Discord channels, allowing direct linking to specific channels. This includes guild channels, app command channels, and threads.

```python
discord.abc.GuildChannel.jump_url
```

```python
discord.app_commands.AppCommandChannel.jump_url
```

```python
discord.app_commands.AppCommandThread.jump_url
```

```python
discord.CategoryChannel.jump_url
```

```python
discord.DMChannel.jump_url
```

```python
discord.ForumChannel.jump_url
```

```python
discord.GroupChannel.jump_url
```

```python
discord.InteractionMessage.jump_url
```

```python
discord.Message.jump_url
```

```python
discord.MessageReference.jump_url
```

```python
discord.PartialMessage.jump_url
```

```python
discord.PartialMessageable.jump_url
```

```python
discord.StageChannel.jump_url
```

```python
discord.TextChannel.jump_url
```

```python
discord.Thread.jump_url
```

```python
discord.VoiceChannel.jump_url
```

```python
discord.WebhookMessage.jump_url
```

--------------------------------

### Join Thread

Source: https://discordpy.readthedocs.io/en/stable/

Method to join a Discord thread. This allows a user or bot to become a participant in a thread.

```python
discord.Thread.join()
```

--------------------------------

### Python: Schedule a task for multiple specific times daily

Source: https://discordpy.readthedocs.io/en/stable/ext/tasks/index

This snippet demonstrates how to schedule a task to run at multiple specific times throughout the day. The `my_task` is configured to run at 8:00 AM, 12:30 PM, and 4:40:30 PM UTC daily by providing a list of `datetime.time` objects to the `time` parameter.

```Python
import datetime\nfrom discord.ext import commands, tasks\n\utc = datetime.timezone.utc\n\n# If no tzinfo is given then UTC is assumed.\ntimes = [\n    datetime.time(hour=8, tzinfo=utc),\n    datetime.time(hour=12, minute=30, tzinfo=utc),\n    datetime.time(hour=16, minute=40, second=30, tzinfo=utc)\n]\n\nclass MyCog(commands.Cog):\n    def __init__(self, bot):\n        self.bot = bot\n        self.my_task.start()\n\n    def cog_unload(self):\n        self.my_task.cancel()\n\n    @tasks.loop(time=times)\n    async def my_task(self):\n        print("My task is running!")\n
```

--------------------------------

### Implement UI Component Callbacks in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section details the callback mechanisms for various UI components in discord.py, such as buttons and select menus. It references the `callback()` method for these interactive elements.

```python
discord.ui.Button.callback()
discord.ui.ChannelSelect.callback()
discord.ui.DynamicItem.callback()
discord.ui.Item.callback()
discord.ui.MentionableSelect.callback()
discord.ui.RoleSelect.callback()
discord.ui.Select.callback()
discord.ui.UserSelect.callback()
```

--------------------------------

### Manage Cog Lifecycle with commands.Cog

Source: https://discordpy.readthedocs.io/en/stable/

Provides methods for managing the lifecycle of a Cog, including loading, unloading, and handling command errors. Cogs are used to organize bot commands and listeners.

```python
from discord.ext import commands

# Example Cog structure:
# class MyCog(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     async def cog_load(self):
#         print("MyCog loaded!")
#
#     async def cog_unload(self):
#         print("MyCog unloaded!")
#
#     @commands.command()
#     async def hello(self, ctx):
#         await ctx.send("Hello from MyCog!")
#
# async def setup(bot):
#     await bot.add_cog(MyCog(bot))
```

--------------------------------

### Working with Discord AutoMod Rules and Triggers in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to configure and use AutoMod rules in discord.py, focusing on trigger types like slurs and spam.

```python
auto_mod_presets.slurs
# Accessing the predefined slur trigger type

auto_mod_rule_trigger_type.spam
# Accessing the spam trigger type for AutoMod rules
```

--------------------------------

### Add AppInfo.role_connections_verification_url

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces the `AppInfo.role_connections_verification_url` attribute.

```python
Add `AppInfo.role_connections_verification_url`
```

--------------------------------

### Convert to Invite

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Converts a string argument to an Invite object via an HTTP request using Bot.fetch_invite(). Raises BadInviteArgument on failure.

```python
class InviteConverter(Converter):
    async def convert(self, ctx, argument):
        # Uses Bot.fetch_invite()
        pass
```

--------------------------------

### Discord AutoSharded Bot and Client

Source: https://discordpy.readthedocs.io/en/stable/

This covers the implementation of auto-sharded bots and clients in Discord.py, which are essential for managing large-scale Discord bots by distributing the workload across multiple processes.

```python
commands.AutoShardedBot
discord.AutoShardedClient
```

--------------------------------

### Waiting Until Client is Ready

Source: https://discordpy.readthedocs.io/en/stable/whats_new

The `Client.wait_until_ready()` coroutine facilitates the creation of tasks that depend on the client's cache being fully populated.

```Python
await client.wait_until_ready()
```

--------------------------------

### Support NewType and type Aliases in ext.commands

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds support for `typing.NewType` and `type` keyword type aliases in `ext.commands`, including for application commands. This enhances type hinting and command parameter handling.

```python
[ext.commands] Add support for `typing.NewType` and `type` keyword type aliases (GH-9815).
    
    * Also supports application commands.
```

--------------------------------

### Discord.py - Permissions for Viewing and Voice Operations

Source: https://discordpy.readthedocs.io/en/stable/

This snippet outlines permissions related to viewing different types of guild information and managing voice channels. It includes permissions like `view_channel`, `view_guild_insights`, and `voice`.

```Python
discord.Permissions.view_audit_log
discord.Permissions.view_channel
discord.Permissions.view_creator_monetization_analytics
discord.Permissions.view_guild_insights
discord.Permissions.voice()
discord.ui.Separator.visible
discord.SeparatorComponent.visible
```

--------------------------------

### Discord.py Command Errors and Exceptions

Source: https://discordpy.readthedocs.io/en/stable/

Details common exceptions raised during command processing in discord.py, such as CommandAlreadyRegistered, CommandError, CommandNotFound, CommandOnCooldown, CommandRegistrationError, and CommandSignatureMismatch.

```Python
from discord.ext import commands

# Example of catching a CommandNotFound error
@commands.command()
async def my_command(ctx):
    await ctx.send('Hello!')

@my_command.error
async def my_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That command does not exist.')
    else:
        await ctx.send(f'An error occurred: {error}')

# Example of CommandOnCooldown
@commands.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def limited_command(ctx):
    await ctx.send('This command can only be used once per minute.')

@limited_command.error
async def limited_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Try again in {error.retry_after:.2f} seconds.')
    else:
        await ctx.send(f'An error occurred: {error}')
```

--------------------------------

### ext.commands: strip_after_prefix parameter for Bot constructor

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds the `strip_after_prefix` parameter to the `Bot` constructor in the `ext.commands` extension. When enabled, this option automatically strips whitespace that appears after the command prefix, improving command parsing robustness.

```Python
from discord.ext import commands

# Example usage:
# bot = commands.Bot(command_prefix='!', strip_after_prefix=True)
```

--------------------------------

### Post-Invoke Hooks in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet demonstrates 'after_invoke()' methods for various command types, used to execute code after a command has been invoked.

```Python
commands.Bot.after_invoke()
commands.Command.after_invoke()
commands.Group.after_invoke()
commands.HybridCommand.after_invoke()
commands.HybridGroup.after_invoke()
commands.after_invoke()
```

--------------------------------

### Fix FFmpegAudio and Subclasses

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Addresses various fixes and improvements for `FFmpegAudio` and its related subclasses.

```python
Fixes and improvements for `FFmpegAudio` and all related subclasses (GH-9528).
```

--------------------------------

### Discord.py: Accessing Topic Attributes for Channels and Stages

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing the 'topic' attribute for various channel types, including text channels, forum channels, stage channels, and stage instances.

```python
app_command_channel.topic
forum_channel.topic
stage_channel.topic
stage_instance.topic
text_channel.topic
```

--------------------------------

### Handle Extension Already Loaded Error in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This exception is raised when attempting to load an extension that is already loaded in discord.py. It inherits from ExtensionError and indicates the name of the extension.

```Python
class ExtensionAlreadyLoaded(ExtensionError):
    """An exception raised when an extension has already been loaded.

    This inherits from `ExtensionError`
    """
    pass

```

--------------------------------

### discord.py: Handle Gateway Rate Limits

Source: https://discordpy.readthedocs.io/en/stable/whats_new

discord.py now handles gateway rate limits, ensuring more robust communication with the Discord gateway.

```python
# This is an internal library feature. Users do not need to implement specific code for this.

```

--------------------------------

### PartialInviteGuild Banner Changes in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Details the updates to PartialInviteGuild.banner due to the asset redesign. The banner attribute is now an Asset object, potentially being None, and URL access has been simplified.

```python
PartialInviteGuild.banner (replaced by PartialInviteGuild.banner.key)
PartialInviteGuild.banner_url (replaced by PartialInviteGuild.banner)
  * The new attribute may now be None.
PartialInviteGuild.banner_url_as (replaced by PartialInviteGuild.banner.replace)
```

--------------------------------

### ext.commands: Allow callable types as bucket keys for cooldowns

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Enhances the cooldown system in `ext.commands` by allowing callable types to be used as bucket keys. This provides more dynamic and flexible ways to define cooldown scopes for commands.

```Python
from discord.ext import commands

# Example usage:
# def custom_cooldown_key(ctx):
#     return ctx.author.id
#
# @bot.command()
# @commands.cooldown(1, 60, key=custom_cooldown_key)
# async def limited_command(ctx):
#     await ctx.send('This command has a custom cooldown.')
```

--------------------------------

### Create a Discord.py Hybrid Group

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The `@discord.ext.commands.hybrid_group()` decorator creates a hybrid command group, combining the functionality of a standard command group with application command compatibility. It defaults to creating a `HybridGroup`.

```python
import discord
from discord.ext import commands

@commands.hybrid_group(name='hybrid_admin')
async def hybrid_admin(ctx: commands.Context):
    """A hybrid command group for admin tasks."""
    pass

@hybrid_admin.command()
async def reload(ctx: commands.Context, extension: str):
    await ctx.send(f'Reloading {extension}...')
```

--------------------------------

### Access Discord Application Command Options

Source: https://discordpy.readthedocs.io/en/stable/

Allows access to the options provided by users when they invoke application commands. This is crucial for parsing user input and executing commands correctly.

```python
discord.app_commands.AppCommand.options
```

```python
discord.app_commands.AppCommandGroup.options
```

--------------------------------

### Discord.py: Target Attributes for Various Objects

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing 'target' related attributes across different discord.py objects. These include target applications for invites, target IDs for permission updates, and target messages/users for interaction metadata.

```python
invite.target_application
permissions.target_id
metadata.target_message
metadata.target_user
```

--------------------------------

### Fetch Application Command Permissions

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Asynchronously fetches the permissions of an application command within a specific guild. This operation requires the client to have an application ID and can fail if permissions are insufficient, the command is not found, or the HTTP request encounters an error.

```Python
await app_command.fetch_permissions(guild)
# Parameters: guild (Snowflake)
# Raises: Forbidden, HTTPException, MissingApplicationID, NotFound
```

--------------------------------

### Register a View for Persistent Listening in discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Explains how to register a `discord.ui.View` or `discord.ui.LayoutView` for persistent listening. This is crucial for components that need to maintain state across program restarts or message updates.

```Python
import discord
from discord.ext import commands

# Assume MyPersistentView is a subclass of discord.ui.View
# with persistent=True and components having custom_id
# class MyPersistentView(discord.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)
#
#     @discord.ui.button(label='Click Me', custom_id='persistent_button')
#     async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
#         await interaction.response.send_message('Button clicked!')

# Assuming 'bot' is an instance of commands.Bot
# persistent_view = MyPersistentView()
# bot.add_view(persistent_view)

```

--------------------------------

### discord.py: Handling Embed Empty Attributes

Source: https://discordpy.readthedocs.io/en/stable/migrating

Shows the migration from using discord.Embed.Empty as a sentinel value to using None for representing empty or removed embed attributes, and the impact on embed equality checks.

```Python
# before
embed = discord.Embed(title='foo')
embed.title = discord.Embed.Empty
embed == embed.copy() # False

# after
embed = discord.Embed(title='foo')
embed.title = None
embed == embed.copy() # True
{embed, embed} # Raises TypeError
```

--------------------------------

### Discord Select Menu Required Fields

Source: https://discordpy.readthedocs.io/en/stable/

Attributes indicating if certain select menu types are required.

```python
discord.Select.required
```

--------------------------------

### Discord Command with Enum Choices

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates defining a Discord slash command where the 'fruits' parameter uses an `enum.Enum` for choices. The command responds with the user's selected favorite fruit.

```python
import discord
from discord import app_commands
import enum

class Fruits(enum.Enum):
    apple = 1
    banana = 2
    cherry = 3

@app_commands.command()
@app_commands.describe(fruits='fruits to choose from')
async def fruit(interaction: discord.Interaction, fruits: Fruits):
    await interaction.response.send_message(f'Your favourite fruit is {fruits}.')
```

--------------------------------

### Reply to a Message (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

A shortcut method to send a reply to a message. For interaction contexts, it functions similarly to sending a message. It handles various exceptions related to sending messages and permissions.

```python
async def reply(content: Optional[str] = None, **kwargs) -> Message:
    """A shortcut method to send() to reply to the Message referenced by this context.

    For interaction based contexts, this is the same as send().

    Parameters
    ----------
    content : Optional[str]
        The content of the message to send.

    Raises
    ------
    HTTPException
        Sending the message failed.
    Forbidden
        You do not have the proper permissions to send the message.
    ValueError
        The `files` list is not of the appropriate size.
    TypeError
        You specified both `file` and `files`.

    Returns
    ------
    Message
        The message that was sent.
    """
    # Implementation details would go here
```

--------------------------------

### Working with Discord.py Message References and IDs

Source: https://discordpy.readthedocs.io/en/stable/

This section focuses on attributes related to message references and various message IDs within discord.py, including those used in interactions and raw events.

```python
message_ref_id = discord.MessageReference.message_id
interaction_message_id = discord.InteractionCallbackResponse.message_id
raw_message_id = discord.RawMessageDeleteEvent.message_id
raw_update_message_id = discord.RawMessageUpdateEvent.message_id
poll_vote_message_id = discord.RawPollVoteActionEvent.message_id
reaction_message_id = discord.RawReactionActionEvent.message_id
clear_emoji_message_id = discord.RawReactionClearEmojiEvent.message_id
clear_message_id = discord.RawReactionClearEvent.message_id
bulk_delete_message_ids = discord.RawBulkMessageDeleteEvent.message_ids
```

--------------------------------

### Discord.py Locale and Language Settings

Source: https://discordpy.readthedocs.io/en/stable/

Details locale settings for different languages supported by discord.py, including specific regional variations.

```python
discord.Locale.brazil_portuguese
discord.Locale.british_english
discord.Locale.bulgarian
```

--------------------------------

### Discord.py Command and Group Commands Access

Source: https://discordpy.readthedocs.io/en/stable/

Demonstrates how to access the list of commands associated with a Bot, a Group, or a HybridGroup in discord.py. This is useful for introspection and dynamic command handling.

```Python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def show_commands(ctx):
    # Accessing commands from the bot itself
    bot_commands = [cmd.name for cmd in bot.commands]
    await ctx.send(f"Bot commands: {', '.join(bot_commands)}")

    # If you have groups, you can access their commands too
    # Example: Assuming a group named 'mygroup'
    # if 'mygroup' in bot.all_commands:
    #     group_commands = [cmd.name for cmd in bot.all_commands['mygroup'].commands]
    #     await ctx.send(f"Mygroup commands: {', '.join(group_commands)}")

# Example of a group
group = commands.Group(name='mygroup', invoke_without_command=True)

@group.command()
async def subgroup_command(ctx):
    await ctx.send('This is a subgroup command.')

# Add the group to the bot
# bot.add_command(group)

# Accessing commands from a group (if added to bot)
# if 'mygroup' in bot.all_commands:
#     group_commands = [cmd.name for cmd in bot.all_commands['mygroup'].commands]
#     print(f"Group commands: {group_commands}")

# Accessing commands from a HybridGroup (similar to Group)
# hybrid_group = commands.HybridGroup(name='hybridgroup')
# bot.add_command(hybrid_group)
# if 'hybridgroup' in bot.all_commands:
#     hybrid_group_commands = [cmd.name for cmd in bot.all_commands['hybridgroup'].commands]
#     print(f"HybridGroup commands: {hybrid_group_commands}")
```

--------------------------------

### Discord Activity Details URL

Source: https://discordpy.readthedocs.io/en/stable/

Provides access to the details_url attribute for discord.Activity, used for linking custom activities.

```python
discord.Activity.details_url
```

--------------------------------

### Discord.py Guild By Category Method

Source: https://discordpy.readthedocs.io/en/stable/

Provides a method to retrieve guild information organized by category.

```python
discord.Guild.by_category()
```

--------------------------------

### Discord AppCommandThread Fetching

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Describes the _fetch() coroutine for AppCommandThread, which fetches the full thread object from the API and handles potential exceptions like NotFound or Forbidden.

```python
_fetch()

This function is a _coroutine_.
Fetches the partial channel to a full `Thread`. 

Raises
    
  * **NotFound** – The thread was not found.
  * **Forbidden** – You do not have the permissions required to get a thread.
  * **HTTPException** – Retrieving the thread failed.


Returns
    
The full thread. 

Return type
    
`Thread`
```

--------------------------------

### Discord.py Cooldowns for Commands

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to implement rate limiting for commands using the @commands.cooldown decorator in discord.py. It covers setting the rate, period, and bucket type for cooldowns.

```Python
import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def slow_command(ctx):
    """This command can only be used once every 30 seconds per user."""
    await ctx.send('You can use this command again soon!')

@slow_command.error
async def slow_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Please wait {error.retry_after:.2f} seconds.')
    else:
        await ctx.send(f'An error occurred: {error}')

# Example of accessing cooldown information
# command = bot.get_command('slow_command')
# if command and command.cooldown:
#     print(f"Cooldown rate: {command.cooldown.rate}")
#     print(f"Cooldown per: {command.cooldown.per}")
#     print(f"Cooldown bucket: {command.cooldown.type}")

# Example of copying cooldowns (e.g., for command groups)
# original_command = bot.get_command('slow_command')
# new_command = commands.Command(name='copy_slow', callback=slow_command.callback)
# if original_command and original_command.cooldown:
#     new_command.cooldown = original_command.cooldown.copy()

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### Adding Tags and Users to Threads in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet demonstrates 'add_tags()' and 'add_user()' for the 'Thread' class, used for managing thread metadata and participants.

```Python
discord.Thread.add_tags()
discord.Thread.add_user()
```

--------------------------------

### Handle Discord Interaction Events

Source: https://discordpy.readthedocs.io/en/stable/

These events are triggered by user interactions with the bot, such as slash commands, context menus, and button clicks. They are fundamental for building interactive Discord bots.

```python
discord.on_interaction(interaction: discord.Interaction) -> None
```

--------------------------------

### Partial Integration

Source: https://discordpy.readthedocs.io/en/stable/

Represents a partial integration, likely for reduced data retrieval.

```Python
discord.PartialIntegration
```

--------------------------------

### HybridGroup can_run Method

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Describes the asynchronous 'can_run' method of HybridGroup, which checks if a command can be executed by verifying all predicates in the 'checks' attribute and ensuring the command is not disabled.

```python
_await _can_run(_ctx_ , _/_)
    
This function is a _coroutine_.
Checks if the command can be executed by checking all the predicates inside the `checks` attribute. This also checks whether the command is disabled.
Changed in version 1.3: Checks whether the command is disabled or not
Changed in version 2.0: `ctx` parameter is now positional-only.

Parameters
    

```

--------------------------------

### Command Parameter Kind and Context Kwargs

Source: https://discordpy.readthedocs.io/en/stable/

Defines the 'kind' of a command parameter and accesses keyword arguments ('kwargs') from a command context. These are used for command parsing and execution.

```python
commands.Parameter.kind
```

```python
commands.Context.kwargs
```

--------------------------------

### Audio Source Handling

Source: https://discordpy.readthedocs.io/en/stable/

Represents an audio source that can be played in Discord voice channels. This is fundamental for bots that provide music or audio playback features.

```Python
discord.AudioSource
```

--------------------------------

### Fix ext.commands Context Defer

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Ensures that `Context.defer` in the `ext.commands` extension does not unconditionally defer.

```Python
[ext.commands] Fix `Context.defer` unconditionally deferring
```

--------------------------------

### Use importlib.metadata in __main__ Script

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Updates the `__main__` script to utilize `importlib.metadata` instead of the deprecated `pkg_resources` library. This modernizes the script and ensures compatibility with future Python versions.

```Python
# Conceptual change in a __main__.py script
# Replaces calls like pkg_resources.get_distribution('my_package').version
# with importlib.metadata.version('my_package')

import importlib.metadata
import sys

# Example (conceptual):
# try:
#     version = importlib.metadata.version('discord.py')
# except importlib.metadata.PackageNotFoundError:
#     version = 'unknown'
# print(f"discord.py version: {version}")

# This change affects how the library's version is determined in standalone scripts.
```

--------------------------------

### Upload an image file

Source: https://discordpy.readthedocs.io/en/stable/faq

Uploads a file to Discord using the `discord.File` object. Supports uploading from a file path, a file-like object, or a URL. For URLs, `aiohttp` is used for downloading.

```Python
await channel.send(file=discord.File('my_file.png'))
```

```Python
with open('my_file.png', 'rb') as fp:
    await channel.send(file=discord.File(fp, 'new_filename.png'))
```

```Python
my_files = [
    discord.File('result.zip'),
    discord.File('teaser_graph.png'),
]
await channel.send(files=my_files)
```

```Python
import io
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get(my_url) as resp:
        if resp.status != 200:
            return await channel.send('Could not download file...')
        data = io.BytesIO(await resp.read())
        await channel.send(file=discord.File(data, 'cool_image.png'))
```

--------------------------------

### Discord ComponentType Role Select

Source: https://discordpy.readthedocs.io/en/stable/

The component type for a role select menu.

```python
discord.ComponentType.role_select
```

--------------------------------

### Send multiple files using Channel.send

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Demonstrates how to send multiple file attachments simultaneously using the `channel.send` method in discord.py. This is achieved by passing a list of `discord.File` objects to the `files` parameter.

```python
my_files = [
    discord.File('cool.png', 'testing.png'),
    discord.File(some_fp, 'cool_filename.png'),
]

await channel.send('Your images:', files=my_files)
```

--------------------------------

### Add Signal Handling to Client.run()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Reintroduces signal handling to Client.run() to address issues with proper cleanup for some users.

```Python
client.run()
```

--------------------------------

### Working with Discord Permissions for Stage Moderator in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to check for stage moderator permissions using discord.py.

```python
permissions.stage_moderator()
# Checking if the user has stage moderator permissions
```

--------------------------------

### Create Discord Sticker

Source: https://discordpy.readthedocs.io/en/stable/

Enables the creation of a new sticker within a guild, which can be used in chat messages.

```python
await discord.Guild.create_sticker()
```

--------------------------------

### Fix Paginator Prefix Handling

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Resolves an issue where a `None` prefix in the paginator could result in empty pages.

```python
# [ext.commands] Fix issue with paginator prefix being `None` causing empty pages. (GH-2471)
```

--------------------------------

### Handle Discord Subscription Events

Source: https://discordpy.readthedocs.io/en/stable/

These events are related to user subscriptions, which might be used for premium features or content access within Discord.

```python
discord.on_subscription_create(subscription: discord.Subscription) -> None
```

```python
discord.on_subscription_update(subscription: discord.Subscription) -> None
```

```python
discord.on_subscription_delete(subscription: discord.Subscription) -> None
```

--------------------------------

### Fix cog descriptions in MinimalHelpCommand

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Corrects an issue where cog descriptions were not displayed in the `MinimalHelpCommand`. This ensures that cog descriptions are properly rendered in the minimal help output.

```python
Fix cog descriptions not showing in `MinimalHelpCommand` (GH-2139)
```

--------------------------------

### Upload command with Optional discord.Attachment

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates making the discord.Attachment converter optional using typing.Optional. If no attachment is provided, a specific message is sent.

```Python
import typing
import discord
from discord.ext import commands

@bot.command()
async def upload(ctx, attachment: typing.Optional[discord.Attachment]):
    if attachment is None:
        await ctx.send('You did not upload anything!')
    else:
        await ctx.send(f'You have uploaded <{attachment.url}>')
```

--------------------------------

### Fix Guild.create_forum available_tags

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Corrects an issue where `available_tags` and `default_thread_slowmode_delay` were not respected when creating a forum channel using `Guild.create_forum()`. This ensures forum creation parameters are applied correctly.

```Python
Fix `available_tags` and `default_thread_slowmode_delay` not being respected in `Guild.create_forum()`
```

--------------------------------

### Thread Convenience Properties in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Shows how the Thread object in discord.py provides convenience properties and methods to access information about its parent channel, such as category, NSFW status, and permissions.

```Python
thread.category
thread.category_id
thread.is_news()
thread.is_nsfw()
thread.permissions_for(member)
```

--------------------------------

### Sync Application Commands in discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

This function is used to sync application commands to Discord. It's necessary for commands to appear in the Discord client. It handles various exceptions that might occur during the syncing process, such as network issues, invalid command data, or missing permissions.

```python
async def sync_commands(guild: Optional[Snowflake] = None) -> List[AppCommand]:
    """Syncs application commands to Discord.

    Parameters:
        guild (Optional[Snowflake]): The guild to sync commands to. If None, syncs global commands.

    Returns:
        List[AppCommand]: The application's synced commands.

    Raises:
        HTTPException: If syncing fails.
        CommandSyncFailure: If syncing fails due to user error (e.g., invalid data).
        Forbidden: If the client lacks the 'applications.commands' scope.
        MissingApplicationID: If the client does not have an application ID.
        TranslationError: If an error occurs during command translation.
    """
    # Implementation details for syncing commands would go here
```

--------------------------------

### Discord File Handling and Attributes

Source: https://discordpy.readthedocs.io/en/stable/

This snippet covers classes and attributes related to file handling in discord.py. It includes classes for representing audio files, general file uploads, and accessing file-specific attributes like filename and size limits.

```python
discord.FFmpegAudio
discord.FFmpegOpusAudio
discord.FFmpegPCMAudio
discord.Embed.fields
discord.File
discord.ui.File
discord.ComponentType.file
discord.FileComponent
discord.Attachment.filename
discord.File.filename
commands.Context.filesize_limit
discord.Guild.filesize_limit
discord.Interaction.filesize_limit
```

--------------------------------

### Discord Component Description

Source: https://discordpy.readthedocs.io/en/stable/

Accesses the description attribute for UI components such as LabelComponent and ThumbnailComponent.

```python
discord.LabelComponent.description
discord.ThumbnailComponent.description
```

--------------------------------

### Fix Client.create_server() functionality

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Corrects an issue with the `Client.create_server()` method that caused it to stop working. This restores the functionality for creating new servers.

```python
Fix issue with `Client.create_server()` that made it stop working.
```

--------------------------------

### discord.py: Using AsyncIterator.filter()

Source: https://discordpy.readthedocs.io/en/stable/migrating

Illustrates the change from AsyncIterator.filter() to incorporating the filter condition directly into the asynchronous list comprehension.

```Python
def predicate(message):
    return not message.author.bot

# before
user_messages = []
async for message in channel.history().filter(lambda m: not m.author.bot):
    user_messages.append(message)

# after
user_messages = [message async for message in channel.history() if not m.author.bot]
```

--------------------------------

### Discord Exceptions

Source: https://discordpy.readthedocs.io/en/stable/

Represents base exceptions for Discord-related errors, including DiscordException and DiscordServerError.

```python
discord.DiscordException
discord.DiscordServerError
```

--------------------------------

### Create and Use ActionRow with Buttons in discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Demonstrates how to create a custom view inheriting from LayoutView and add a button to an ActionRow. The button is configured with a label and an asynchronous callback function that responds to the interaction.

```Python
class MyView(ui.LayoutView):
    row = ui.ActionRow()
    # or you can use your subclass:
    # row = MyActionRow()

    # you can add items with row.button and row.select
    @row.button(label='A button!')
    async def row_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You clicked a button!')
```

--------------------------------

### discord.py: Removed Parameters and Attributes

Source: https://discordpy.readthedocs.io/en/stable/migrating

This snippet details parameters that have been removed from discord.py functions and methods, such as 'self_bot' from Bot. It also lists removed attributes like 'original' from ExtensionNotFound and 'clean_prefix' from HelpCommand.

```python
# Removed parameter: 'self_bot' from Bot
# class Bot:
#     def __init__(self, command_prefix, ...):
#         # 'self_bot' parameter removed
#         pass

# Removed attribute: 'original' from ExtensionNotFound
# class ExtensionNotFound(Exception):
#     def __init__(self, name):
#         self.name = name
#         # 'original' attribute removed

# Removed attribute: 'type' from Cooldown class (use Cooldown.type instead)
# class Cooldown:
#     def __init__(self, rate, per, type=BucketType.default):
#         # 'type' parameter in __init__ might be removed or changed
#         # Accessing cooldown type should now be via an attribute like 'type'
#         pass

# Removed attribute: 'clean_prefix' from HelpCommand
# class HelpCommand:
#     def __init__(self):
#         # 'clean_prefix' attribute removed
#         # Use ctx.clean_prefix instead
#         pass

```

--------------------------------

### Discord.py: Wait for Events

Source: https://discordpy.readthedocs.io/en/stable/

Provides methods to wait for specific events or conditions within the discord.py library. This includes waiting for modal submissions, view interactions, or bot readiness.

```python
discord.ui.LayoutView.wait()
discord.ui.Modal.wait()
discord.ui.View.wait()
discord.Client.wait_for()
commands.Bot.wait_for()
discord.Client.wait_until_ready()
commands.Bot.wait_until_ready()
```

--------------------------------

### Discord Message Nonce

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing the 'nonce' attribute for Discord messages.

```python
print(discord.Message.nonce)
```

--------------------------------

### Detailed __repr__ for Public Types

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Provides proper and more detailed __repr__ methods for all public facing types.

```Python
# Custom __repr__ for public types.
```

--------------------------------

### Discord.py Guild Member and Presence Limits

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access properties related to guild member and presence limits, including maximum members and presences.

```Python
import discord

# Example of accessing max members in a guild
max_members = discord.Guild.max_members
print(max_members)

# Example of accessing max presences in a guild
max_presences = discord.Guild.max_presences
print(max_presences)
```

--------------------------------

### Discord Role Creation and Update Logging

Source: https://discordpy.readthedocs.io/en/stable/

Shows audit log actions for role creation and role updates, indicating when roles are added or modified in a guild.

```python
discord.AuditLogAction.role_create
discord.AuditLogAction.role_update
```

--------------------------------

### Discord.py: Role Subscription and Poll Vote Counts

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates accessing the total months subscribed for role subscriptions and the total votes for polls.

```python
role_subscription_info.total_months_subscribed
poll.total_votes
```

--------------------------------

### Update discord.py Event Signatures

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Shows the changes in event signatures for command handling in discord.py. The 'command' parameter has been removed from on_command and on_command_completion, and reordered in on_command_error for consistency.

```python
on_command(ctx)
on_command_completion(ctx)
on_command_error(ctx, error)
```

--------------------------------

### Discord UI Separator Configuration

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Illustrates how to configure and use the discord.ui.Separator class for creating visual dividers in Discord UI layouts. It covers properties like visibility, spacing, and ID.

```Python
from discord.ui import Separator
from discord.ui.enums import SeparatorSpacing

# Example of creating a Separator
separator = Separator(visible=True, spacing=SeparatorSpacing.small, id=2)

# Accessing properties
separator_id = separator.id
separator_visible = separator.visible
separator_spacing = separator.spacing
separator_parent = separator.parent
separator_view = separator.view
```

--------------------------------

### Emoji Creation and Management in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section covers various aspects of emoji handling, including creating custom emojis, managing emoji limits within a guild, and converting emoji inputs for commands.

```python
discord.AuditLogAction.emoji_create
discord.AuditLogAction.emoji_delete
discord.Guild.emoji_limit
discord.AuditLogAction.emoji_update
commands.EmojiConverter
discord.Client.emojis
commands.Bot.emojis
discord.Guild.emojis
discord.GuildPreview.emojis
discord.Intents.emojis
discord.Intents.emojis_and_stickers
```

--------------------------------

### Walk Application Commands

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides an iterator to recursively traverse all application commands and their sub-commands within the command tree. It supports iterating over global commands or commands within a specific guild, and filtering by command type.

```Python
_for ... in _walk_commands(_*_ , _guild=None_ , _type= <AppCommandType.chat_input: 1>_)
```

--------------------------------

### discord.py: Gateway Intents with Client

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Support for gateway intents has been added to discord.py. Intents are passed via the 'intents' parameter in the Client constructor using the Intents class.

```python
import discord

# Example of enabling specific intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

```

--------------------------------

### Check if Client or Bot is Ready

Source: https://discordpy.readthedocs.io/en/stable/

Determines if the Discord client or bot has successfully connected and is ready to process events. This is a fundamental check for bot operation.

```python
discord.Client.is_ready()
```

```python
commands.Bot.is_ready()
```

--------------------------------

### Handling Permissions and Priority Speaker

Source: https://discordpy.readthedocs.io/en/stable/

Covers the `priority_speaker` permission and attributes related to audit log differences and guild privacy levels in discord.py.

```Python
discord.Permissions.priority_speaker
```

```Python
discord.AuditLogDiff.privacy_level
```

```Python
discord.ScheduledEvent.privacy_level
```

```Python
discord.StageInstance.privacy_level
```

--------------------------------

### Fetch Discord Entities

Source: https://discordpy.readthedocs.io/en/stable/

This snippet demonstrates various methods for fetching different entities within the Discord API using discord.py. These include fetching messages, users, guilds, channels, members, and more. These methods are crucial for interacting with and retrieving data from Discord.

```python
discord.app_commands.AppCommandChannel.fetch()
discord.app_commands.AppCommandThread.fetch()
discord.InteractionMessage.fetch()
discord.Message.fetch()
discord.PartialMessage.fetch()
discord.StickerItem.fetch()
discord.SyncWebhook.fetch()
discord.Webhook.fetch()
discord.WebhookMessage.fetch()
discord.Client.fetch_application_emoji()
commands.Bot.fetch_application_emoji()
discord.Client.fetch_application_emojis()
commands.Bot.fetch_application_emojis()
discord.Guild.fetch_automod_rule()
discord.Guild.fetch_automod_rules()
discord.Guild.fetch_ban()
discord.Client.fetch_channel()
commands.Bot.fetch_channel()
discord.Guild.fetch_channel()
discord.Guild.fetch_channels()
discord.app_commands.CommandTree.fetch_command()
discord.app_commands.CommandTree.fetch_commands()
discord.Guild.fetch_emoji()
discord.Guild.fetch_emojis()
discord.Client.fetch_entitlement()
commands.Bot.fetch_entitlement()
discord.Client.fetch_guild()
commands.Bot.fetch_guild()
discord.Client.fetch_guild_preview()
commands.Bot.fetch_guild_preview()
discord.Client.fetch_guilds()
commands.Bot.fetch_guilds()
discord.StageChannel.fetch_instance()
discord.Client.fetch_invite()
commands.Bot.fetch_invite()
discord.Widget.fetch_invite()
discord.Guild.fetch_member()
discord.Thread.fetch_member()
discord.Guild.fetch_members()
discord.Thread.fetch_members()
discord.abc.Messageable.fetch_message()
discord.DMChannel.fetch_message()
commands.Context.fetch_message()
discord.GroupChannel.fetch_message()
discord.Member.fetch_message()
discord.PartialMessageable.fetch_message()
discord.StageChannel.fetch_message()
discord.SyncWebhook.fetch_message()
discord.TextChannel.fetch_message()
discord.Thread.fetch_message()
discord.User.fetch_message()
discord.VoiceChannel.fetch_message()
discord.Webhook.fetch_message()
discord.app_commands.AppCommand.fetch_permissions()
discord.Client.fetch_premium_sticker_pack()
commands.Bot.fetch_premium_sticker_pack()
discord.Client.fetch_premium_sticker_packs()
commands.Bot.fetch_premium_sticker_packs()
discord.Guild.fetch_role()
discord.Guild.fetch_roles()
discord.AutoModAction.fetch_rule()
discord.Guild.fetch_scheduled_event()
discord.Guild.fetch_scheduled_events()
discord.AutoShardedClient.fetch_session_start_limits()
discord.Client.fetch_skus()
commands.Bot.fetch_skus()
discord.Client.fetch_soundboard_default_sounds()
commands.Bot.fetch_soundboard_default_sounds()
discord.Guild.fetch_soundboard_sound()
discord.Guild.fetch_soundboard_sounds()
discord.Client.fetch_stage_instance()
commands.Bot.fetch_stage_instance()
discord.Client.fetch_sticker()
commands.Bot.fetch_sticker()
discord.Guild.fetch_sticker()
discord.Guild.fetch_stickers()
discord.SKU.fetch_subscription()
discord.Client.fetch_template()
commands.Bot.fetch_template()
discord.InteractionMessage.fetch_thread()
discord.Message.fetch_thread()
discord.PartialMessage.fetch_thread()
discord.WebhookMessage.fetch_thread()
discord.Client.fetch_user()
commands.Bot.fetch_user()
discord.Member.fetch_voice()
discord.Client.fetch_webhook()
commands.Bot.fetch_webhook()
discord.Client.fetch_widget()
commands.Bot.fetch_widget()
```

--------------------------------

### Manage Assets and Attachments

Source: https://discordpy.readthedocs.io/en/stable/

Handles the management of various assets and attachments within Discord, including file attachments to messages and general asset handling. This is crucial for bots that send files or interact with media.

```Python
discord.Asset
discord.Activity.assets
discord.Game.assets
discord.Streaming.assets
discord.Permissions.attach_files
discord.Attachment
discord.AppCommandOptionType.attachment
discord.UnfurledMediaItem.attachment_id
discord.AttachmentFlags
discord.Message.attachments
discord.MessageSnapshot.attachments
```

--------------------------------

### Check if Command Can Run

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Asynchronously checks if the command can be run in the given context, considering all applicable checks and conditions.

```python
_await _can_run(_ctx_ , _/_)
```

--------------------------------

### Add two integers using type annotation

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Demonstrates how to use Python's function annotations to specify that command arguments `a` and `b` should be converted to integers. The sum is then sent back to the channel.

```Python
import discord
from discord.ext import commands

# Assuming 'bot' is an instance of commands.Bot
# bot = commands.Bot(command_prefix='!')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)
```

--------------------------------

### PCM Audio and Volume Transformer

Source: https://discordpy.readthedocs.io/en/stable/

Represents PCM audio data and a transformer for adjusting its volume.

```Python
discord.PCMAudio
discord.PCMVolumeTransformer
```

--------------------------------

### Partner User Flags

Source: https://discordpy.readthedocs.io/en/stable/

Represents user flags indicating partner status.

```Python
discord.PublicUserFlags.partner
discord.UserFlags.partner
```

--------------------------------

### Python discord.py: Tuple flag for coordinate parsing

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to use typing.Tuple with specific types (int, int) to parse pairs of values, such as coordinates, for a discord.py command flag. Requires quoting for arguments with spaces.

```Python
# point: 10 11 point: 12 13
class Coordinates(commands.FlagConverter):
    point: Tuple[int, int]

```

--------------------------------

### Add Guild Premium Subscribers

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces Guild.premium_subscribers to retrieve all members currently boosting the guild.

```Python
guild.premium_subscribers
```

--------------------------------

### Python: Execute code before a command with @before_invoke

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The `@discord.ext.commands.before_invoke` decorator registers a coroutine to be executed before a command. This is useful for setting up context or logging command invocations. The `coro` parameter is now positional-only.

```Python
async def record_usage(ctx):
    print(ctx.author, 'used', ctx.command, 'at', ctx.message.created_at)

@bot.command()
@commands.before_invoke(record_usage)
async def who(ctx): # Output: <User> used who at <Time>
    await ctx.send('i am a bot')

class What(commands.Cog):

    @commands.before_invoke(record_usage)
    @commands.command()
    async def when(self, ctx): # Output: <User> used when at <Time>
        await ctx.send(f'and i have existed since {ctx.bot.user.created_at}')
```

--------------------------------

### Discord Guild Roles

Source: https://discordpy.readthedocs.io/en/stable/

A list of all roles within a guild.

```python
discord.Guild.roles
```

--------------------------------

### Discord App Command Option Type Number

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates the 'number' constant for Discord App Command Option Types.

```python
discord.AppCommandOptionType.number
```

--------------------------------

### Discord.py Bucket Type for Rate Limiting

Source: https://discordpy.readthedocs.io/en/stable/

Defines different bucket types for rate limiting commands, allowing for granular control over command usage frequency.

```python
commands.BucketType
```

--------------------------------

### Schedule Background Tasks with @loop Decorator

Source: https://discordpy.readthedocs.io/en/stable/ext/tasks/index

The `@discord.ext.tasks.loop` decorator simplifies scheduling background tasks. It allows configuration of intervals (seconds, minutes, hours, specific times), loop count, reconnection behavior, and task naming. The decorated function must be a coroutine.

```Python
@discord.ext.tasks.loop(seconds=5, reconnect=True)
async def my_task():
    await discord.Client.send_message('Hello!')

@discord.ext.tasks.loop(time=[datetime.time(9, 0), datetime.time(17, 0)])
async def scheduled_task():
    print('Scheduled task running')
```

--------------------------------

### MinimalHelpCommand: Add Command Formatting

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

A utility function to format commands and groups for display. This method is positional-only since version 2.0.

```Python
def add_command_formatting(command, /):
    """A utility function to format commands and groups.

    Changed in version 2.0: `command` parameter is now positional-only.

    Parameters
    ----------
    command : Command
        The command to format.
    """
    pass
```

--------------------------------

### Wait for Reaction Event with Client.wait_for

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Shows how to use `Client.wait_for()` to wait for a 'reaction_add' event, returning both the reaction and the user who added it. This demonstrates the function's ability to return multiple arguments.

```Python
reaction, user = await client.wait_for('reaction_add', check=lambda r, u: u.id == 176995180300206080)

# use user and reaction
```

--------------------------------

### Create Discord Direct Message (DM)

Source: https://discordpy.readthedocs.io/en/stable/

Allows creating a direct message channel with a member or user. This is typically used to initiate a private conversation.

```python
await discord.Member.create_dm()
await discord.User.create_dm()
```

--------------------------------

### Convert to ForumChannel

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Converts a string argument to a ForumChannel. Supports lookup by ID, mention, channel URL, or name within the guild or global cache.

```python
class ForumChannelConverter(Converter):
    async def convert(self, ctx, argument):
        # Lookup strategy: ID, mention, channel URL, name
        pass
```

--------------------------------

### Discord RoleSubscriptionInfo RoleSubscriptionListingID

Source: https://discordpy.readthedocs.io/en/stable/

The listing ID for a role subscription.

```python
discord.RoleSubscriptionInfo.role_subscription_listing_id
```

--------------------------------

### CommandNotFound Exception

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Raised when a command is attempted to be invoked but no command with that name is found. This exception inherits from CommandError.

```python
class discord.ext.commands.CommandNotFound(message=None, *args):
    """Exception raised when a command is attempted to be invoked but no command under that name is found.

    This is not raised for invalid subcommands, rather just the initial main command that is attempted to be invoked.
    This inherits from `CommandError`.
    """
    pass
```

--------------------------------

### Argument Class in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Represents an application command argument, including its type, name, description, choices, and constraints. New in version 2.0.

```python
class Argument:
    autocomplete: bool
    channel_types: List[ChannelType]
    choices: List[Choice]
    description: str
    description_localizations: Dict[Locale, str]
    max_length: Optional[int]
    max_value: Optional[Union[int, float]]
    min_length: Optional[int]
    min_value: Optional[Union[int, float]]
    name: str
    name_localizations: Dict[Locale, str]
    parent: Union[AppCommand, AppCommandGroup]
    required: bool
    type: AppCommandOptionType
```

--------------------------------

### Retrieve Command or Group by Name

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Fetches a command or subgroup from the group's internal list using its name. Returns the found command or None if no command matches the provided name.

```Python
found_command = group.get_command('command_name')
```

--------------------------------

### Handle UI Separators and Styles in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains the usage of separator components in Discord UI, including their types and spacing. This is used for visually organizing elements within message components.

```python
discord.ui.Separator
discord.ComponentType.separator
discord.SeparatorComponent
discord.SeparatorSpacing
```

--------------------------------

### Accessing Discord Guild and Category Channel Stage Instances in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to retrieve stage instances associated with a guild or category channels using discord.py.

```python
guild.stage_instances
# Accessing all stage instances within a guild
```

--------------------------------

### Handle Discord Safety Alerts and Levels

Source: https://discordpy.readthedocs.io/en/stable/

Provides information on Discord's safety features, including NSFW levels and safety alerts channels within guilds. This is important for bots that moderate content or manage server settings.

```python
discord.NSFWLevel.safe
discord.Guild.safety_alerts_channel
```

--------------------------------

### Discord.py: Thread Management and Related Attributes

Source: https://discordpy.readthedocs.io/en/stable/

Covers accessing and managing threads, including thread objects, thread members, and attributes related to thread creation, deletion, and updates.

```python
interaction_message.thread
message.thread
raw_thread_delete_event.thread
thread_member
forum_channel.threads
text_channel.threads
```

--------------------------------

### Add Permissions Stream

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces the Permissions.stream permission.

```Python
Permissions.stream
```

--------------------------------

### Iterate Through Cog Commands

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Explains the `walk_commands()` method, an iterator that recursively yields all commands and subcommands defined within the cog.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def music(self, ctx):
        await ctx.send('Music commands')

    @music.command()
    async def play(self, ctx, song: str):
        await ctx.send(f'Playing: {song}')

    def iterate_commands(self):
        for command in self.walk_commands():
            print(command.name)
```

--------------------------------

### Send a Direct Message (DM)

Source: https://discordpy.readthedocs.io/en/stable/faq

Sends a direct message to a user. This can be done by fetching the user object first or by using the message author from an event. Requires a discord.Client instance and a User or Member object.

```Python
user = client.get_user(381870129706958858)
await user.send('👀')
```

```Python
await message.author.send('👋')
```

--------------------------------

### Handle Calls in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section covers attributes and types related to voice calls within discord.py. It includes `discord.Message.call` and `discord.MessageType.call` for message-related call information.

```python
discord.Message.call
discord.MessageType.call
```

--------------------------------

### Checking Library Version Info

Source: https://discordpy.readthedocs.io/en/stable/whats_new

A new `version_info` named tuple is available to check the version information of the library.

```Python
from discord import version_info

print(version_info)
```

--------------------------------

### Audit Log Creator Monetization Actions

Source: https://discordpy.readthedocs.io/en/stable/

Represents actions in the audit log related to monetization requests and terms acceptance by a creator.

```python
discord.AuditLogAction.creator_monetization_request_created
discord.AuditLogAction.creator_monetization_terms_accepted
```

--------------------------------

### discord.py: Concrete BadArgument Exceptions

Source: https://discordpy.readthedocs.io/en/stable/whats_new

In discord.py's ext.commands, all BadArgument exceptions from built-in converters now raise concrete exceptions for better differentiation.

```python
from discord.ext import commands

# Example of catching specific argument errors:
# @commands.Cog.listener()
# async def on_command_error(self, ctx, error):
#     if isinstance(error, commands.BadArgument):
#         if isinstance(error, commands.MemberNotFound):
#             await ctx.send("Member not found.")
#         elif isinstance(error, commands.BadInt):
#             await ctx.send("Please provide a valid integer.")
#         else:
#             await ctx.send(f"Invalid argument: {error}")

```

--------------------------------

### Discord Client Latency

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access latency information for Discord clients and shards. This is important for monitoring connection quality and bot responsiveness.

```python
import discord
from discord.ext import commands

# Accessing latency for AutoShardedClientauto_sharded_client_latency = discord.AutoShardedClient.latency

# Accessing latency for Client
client_latency = discord.Client.latency

# Accessing latency for Bot
bot_latency = commands.Bot.latency

# Accessing latency for ShardInfo
shard_info_latency = discord.ShardInfo.latency

# Accessing latency for VoiceClient
voice_client_latency = discord.VoiceClient.latency
```

--------------------------------

### Apply Checks to Commands in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet demonstrates how to apply checks to commands in discord.py using decorators. It includes `commands.Bot.check()`, `discord.app_commands.check()`, `commands.check()`, and `commands.check_any()`.

```python
commands.Bot.check()
discord.app_commands.check()
commands.check()
commands.check_any()
commands.Bot.check_once()
```

--------------------------------

### Create Command Shortcut - discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The @command decorator serves as a shortcut to invoke command() and add the command to the bot's internal list using add_command(). It returns a decorator that converts a method into a Command.

--------------------------------

### Working with Action Rows in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet highlights the 'action_row' component type and the 'ActionRow' and 'ui.ActionRow' classes, fundamental for organizing interactive elements in Discord messages.

```Python
discord.ComponentType.action_row
discord.ActionRow
discord.ui.ActionRow
```

--------------------------------

### Create Discord Entitlement

Source: https://discordpy.readthedocs.io/en/stable/

Enables the creation of entitlements, likely related to game or application access management within Discord. This function is available on both Bot and Client objects.

```python
await discord.Client.create_entitlement()
await commands.Bot.create_entitlement()
```

--------------------------------

### Adding Items to UI Components in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet demonstrates 'add_item()' for various UI components like ActionRow, Container, LayoutView, MediaGallery, Modal, Section, and View, used to add interactive elements.

```Python
discord.ui.ActionRow.add_item()
discord.ui.Container.add_item()
discord.ui.LayoutView.add_item()
discord.ui.MediaGallery.add_item()
discord.ui.Modal.add_item()
discord.ui.Section.add_item()
discord.ui.View.add_item()
```

--------------------------------

### Partial Sync Webhook

Source: https://discordpy.readthedocs.io/en/stable/

Represents a partial sync webhook, allowing interaction with webhook data.

```Python
discord.SyncWebhook.partial()
```

--------------------------------

### Discord.py Audit Log and Invite Properties

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access properties related to the audit log and invite system, such as max age, max uses, and differences in audit log entries.

```Python
import discord

# Example of accessing an audit log diff property
max_age_diff = discord.AuditLogDiff.max_age
print(max_age_diff)

# Example of accessing an invite property
invite_max_age = discord.Invite.max_age
print(invite_max_age)
```

--------------------------------

### discord.py: Guild Integrations Management

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Provides functionality to manage guild integrations. Includes `Integration` and `IntegrationAccount` for reading data, methods to fetch, create, edit, delete, and sync integrations within a guild. Audit log support for integrations is not yet available.

```Python
integrations = await guild.integrations()
new_integration = await guild.create_integration(...)
await integration.edit(...)
await integration.delete()
await integration.sync()
```

--------------------------------

### Add Colour.dark_embed() and Colour.light_embed()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `Colour.dark_embed()` and `Colour.light_embed()` for convenient color definitions.

```python
Add `Colour.dark_embed()` and `Colour.light_embed()` (GH-9219)
```

--------------------------------

### Handle Discord Connection and Resumption Events

Source: https://discordpy.readthedocs.io/en/stable/

These events are triggered when the Discord client connects, disconnects, or resumes its session. They are fundamental for managing the bot's online status and connection state.

```python
discord.on_connect() -> None
```

```python
discord.on_disconnect() -> None
```

```python
discord.on_resumed() -> None
```

```python
discord.on_shard_connect(shard_id: int) -> None
```

```python
discord.on_shard_disconnect(shard_id: int, status: int, reason: str) -> None
```

```python
discord.on_shard_ready(shard_id: int) -> None
```

```python
discord.on_shard_resumed(shard_id: int) -> None
```

--------------------------------

### User Flags and Bot Developer Status in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section lists attributes related to user flags, specifically identifying early supporters and verified bot developers. These flags provide information about a user's status within the Discord ecosystem.

```python
discord.PublicUserFlags.early_supporter
discord.UserFlags.early_supporter
discord.PublicUserFlags.early_verified_bot_developer
```

--------------------------------

### Update Permissions and Cooldowns in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Illustrates how to update permissions for overwrites and roles, as well as how to update rate limits for command cooldowns in discord.py.

```python
discord.PermissionOverwrite.update(permissions)
discord.Permissions.update(permissions)
discord.app_commands.Cooldown.update_rate_limit(cooldown)
```

--------------------------------

### Color Manipulation and Theming

Source: https://discordpy.readthedocs.io/en/stable/

Offers methods for manipulating Discord embed colors and applying theme-specific color values. This allows for consistent and visually appealing bot messages.

```Python
discord.Colour.ash_embed()
discord.Colour.ash_theme()
```

--------------------------------

### Use CDN URL for assets

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Switches to using the Content Delivery Network (CDN) URL for assets instead of the API URL. This can lead to faster asset loading.

```python
The CDN URL is now used instead of the API URL for assets.
```

--------------------------------

### RoleSelect Methods

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Details the asynchronous methods available for the RoleSelect component, specifically `asynccallback` for handling user selections and `asyncinteraction_check` for validating interactions before processing.

```Python
# Handling interactions
await role_select.asynccallback(interaction)
await role_select.asyncinteraction_check(interaction)
```

--------------------------------

### Working with Discord Voice State and Suppression in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to manage voice state suppression for members in discord.py.

```python
voice_state.suppress
# Whether the voice state is suppressed
```

--------------------------------

### discord.py Interaction - Response Property

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides an object responsible for handling the initial response to the interaction. Note that an interaction can only be responded to once; use `followup` for subsequent messages.

```python
response: InteractionResponse
```

--------------------------------

### Default Avatars and Channel Configurations

Source: https://discordpy.readthedocs.io/en/stable/

Details how default avatars are handled for different user types and how default configurations are set for channels, such as auto-archive duration and sort order. This impacts channel behavior and appearance.

```python
import discord

# Default avatar for a user
default_user_avatar = discord.User.default_avatar

# Default auto-archive duration for a forum channel
default_forum_archive = discord.ForumChannel.default_auto_archive_duration

# Default sort order for a forum channel
default_forum_sort = discord.ForumChannel.default_sort_order
```

--------------------------------

### ext.commands: Remove duplicates from HelpCommand.get_bot_mapping

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Ensures that `HelpCommand.get_bot_mapping` in `ext.commands` removes duplicate entries. This provides a cleaner and more accurate mapping of commands to their respective cogs.

```Python
from discord.ext import commands

# Example usage:
# help_command = commands.DefaultHelpCommand()
# bot_mapping = help_command.get_bot_mapping()
# # bot_mapping should now contain unique entries
```

--------------------------------

### Handle Discord Integration Events

Source: https://discordpy.readthedocs.io/en/stable/

These events relate to guild integrations, such as connecting Twitch or YouTube accounts. They allow bots to react to changes in these integrations.

```python
discord.on_integration_create(integration: discord.Integration) -> None
```

```python
discord.on_integration_update(integration: discord.Integration) -> None
```

--------------------------------

### Add role subscription attributes

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces support for role subscription related attributes, including `RoleSubscriptionInfo`, `MessageType.role_subscription_purchase`, system channel flags, and role tag properties.

```python
Add support for role subscription related attributes
    
    * `RoleSubscriptionInfo` within `Message.role_subscription`
    * `MessageType.role_subscription_purchase`
    * `SystemChannelFlags.role_subscription_purchase_notifications`
    * `SystemChannelFlags.role_subscription_purchase_notification_replies`
    * `RoleTags.subscription_listing_id`
    * `RoleTags.is_available_for_purchase()`
```

--------------------------------

### ActionRow Properties and Methods in discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Details the properties and methods available for the discord.ui.ActionRow class. This includes properties like _id, _children, _parent, and _view, as well as methods for managing items and walking through children.

```Python
# you can add items with row.button and row.select
    @row.button(label='A button!')
    async def row_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You clicked a button!')

_property _id
    
The ID of this component. 

Type
    
Optional[int] 

_property _children
    
The list of children attached to this action row. 

Type
    
List[Item] 

_for ... in _walk_children()
    
An iterator that recursively walks through all the children of this action row and its children, if applicable. 

Yields
    
Item – An item in the action row. 

content_length()
    
`int`: Returns the total length of all text content in this action row. 

add_item(_item_)
    
Adds an item to this action row.
This function returns the class instance to allow for fluent-style chaining. 

Parameters
    
**item** (Item) – The item to add to the action row. 

Raises
    
  * **TypeError** – An Item was not passed.
  * **ValueError** – Maximum number of children has been exceeded (5) or (40) for the entire view.


remove_item(_item_)
    
Removes an item from the action row.
This function returns the class instance to allow for fluent-style chaining. 

Parameters
    
**item** (Item) – The item to remove from the action row. 

find_item(_id_ , _/_)
    
Gets an item with Item.id set as id, or None if not found.
Warning
This is **not the same** as custom_id. 

Parameters
    
**id** (int) – The ID of the component. 

Returns
    
The item found, or None.

Return type
    
Optional[Item] 

clear_items()
    
Removes all items from the action row.
This function returns the class instance to allow for fluent-style chaining. 

_property _parent
    
This item’s parent, if applicable. Only available on items with children.
New in version 2.6.

Type
    
Optional[Item] 

_property _view
    
The underlying view for this item. 

Type
    
Optional[Union[View, LayoutView]] 

```

--------------------------------

### Utilizing Discord.py for Moderation and Channel Management

Source: https://discordpy.readthedocs.io/en/stable/

This snippet highlights discord.py features for moderation, including moving members and channels, and managing mute status. It covers permissions related to moderation and specific audit log actions.

```python
moderate_members_permission = discord.Permissions.moderate_members
moderated_tag = discord.ForumTag.moderated
moderation_intent = discord.Intents.moderation
moderators = discord.StageChannel.moderators
move_members_permission = discord.Permissions.move_members
move_channel_category = discord.abc.GuildChannel.move()
move_channel_forum = discord.ForumChannel.move()
move_channel_role = discord.Role.move()
move_channel_stage = discord.StageChannel.move()
move_channel_text = discord.TextChannel.move()
move_channel_voice = discord.VoiceChannel.move()
move_to_member = discord.Member.move_to()
move_to_voice_client = discord.VoiceClient.move_to()
mute_diff = discord.AuditLogDiff.mute
mute_voice_state = discord.VoiceState.mute
mute_members_permission = discord.Permissions.mute_members
muted_widget_member = discord.WidgetMember.muted
```

--------------------------------

### Discord Translator Load

Source: https://discordpy.readthedocs.io/en/stable/

Shows the 'load' method for Discord Translators, used to load translation data.

```python
import discord

# Loading translation data
# Assuming 'translator' is a discord.app_commands.Translator object
# translator.load()
```

--------------------------------

### Send Typing Indicator with Context

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Returns an asynchronous context manager that allows you to send a typing indicator to the destination for an indefinite period of time, or 10 seconds if the context manager is called using await. In an interaction based context, this is equivalent to a defer() call and does not do any typing calls.

```Python
async with channel.typing():
    # simulate something heavy
    await asyncio.sleep(20)

await channel.send('Done!')
```

```Python
await channel.typing()
```

--------------------------------

### Enabling All Member Cache Flags in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This documentation covers 'MemberCacheFlags.all()', used to enable caching for all member-related data.

```Python
discord.MemberCacheFlags.all()
```

--------------------------------

### Accessing Discord Guild and Channel Information in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to access various attributes related to Discord guilds and channels, such as splash images, sticker limits, and category channel information.

```python
guild.splash
# Getting the guild's splash image URL

category_channel.stage_channels
# Accessing stage channels within a category
```

--------------------------------

### Add DefaultAvatar.pink and Colour.pink()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `DefaultAvatar.pink` and a corresponding `Colour.pink()` method to represent the new pink default avatars available on Discord.

```Python
# Add DefaultAvatar.pink for new pink default avatars.
# Add Colour.pink() to get the pink default avatar colour.
```

--------------------------------

### Configure Discord AutoMod Presets

Source: https://discordpy.readthedocs.io/en/stable/

Details the `sexual_content` preset for Discord's AutoMod feature, allowing bots to automatically detect and flag or block sexually explicit content.

```python
discord.AutoModPresets.sexual_content
```

--------------------------------

### Discord.py - Video and Locale Information

Source: https://discordpy.readthedocs.io/en/stable/

This snippet covers attributes related to video playback quality modes in voice channels and stage channels, as well as locale settings, specifically Vietnamese.

```Python
discord.Embed.video
discord.AuditLogDiff.video_quality_mode
discord.StageChannel.video_quality_mode
discord.VoiceChannel.video_quality_mode
discord.VideoQualityMode
discord.Locale.vietnamese
```

--------------------------------

### Create Discord Application Emoji

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Creates a new emoji for the bot's application. Requires the emoji's name (2-32 characters) and image data (JPG, PNG, GIF). This function was introduced in version 2.5 and may raise MissingApplicationID or HTTPException.

```python
await client._create_application_emoji(name="my_emoji", image=emoji_bytes)
```

--------------------------------

### Improve Help Command Prefix Handling

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Ensures `HelpCommand.clean_prefix` correctly accounts for nickname mentions, improving help command prefix resolution.

```python
# [ext.commands] `HelpCommand.clean_prefix` now takes into consideration nickname mentions. (GH-2489)
```

--------------------------------

### Adding Files to Messages in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This documentation covers 'add_files()' for various message types, used to attach files to outgoing messages.

```Python
discord.InteractionMessage.add_files()
discord.Message.add_files()
discord.SyncWebhookMessage.add_files()
discord.WebhookMessage.add_files()
```

--------------------------------

### Discord Command Event Handlers

Source: https://discordpy.readthedocs.io/en/stable/

Defines event handlers for command execution, completion, and error handling within discord.py.

```python
discord.discord.ext.commands.on_command()
discord.discord.ext.commands.on_command_completion()
discord.discord.ext.commands.on_command_error()
```

--------------------------------

### Wait for a Message Event using Client.wait_for

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Illustrates the updated method for waiting for specific events, like a message, using `Client.wait_for()`. It shows the 'before' and 'after' code structure, highlighting the use of a predicate function for filtering.

```Python
# before
msg = await client.wait_for_message(author=message.author, channel=message.channel)

# after
def pred(m):
    return m.author == message.author and m.channel == message.channel

msg = await client.wait_for('message', check=pred)
```

--------------------------------

### Create Context from Interaction (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Creates a context object from a discord.Interaction, primarily for application command-based interactions like slash commands. It handles synthetic message creation for ephemeral responses and provides access to the invoking user and target message.

```python
await discord.ext.commands.Context._from_interaction(_interaction_)

```

--------------------------------

### Discord UI Select Required

Source: https://discordpy.readthedocs.io/en/stable/

Indicates if a generic UI select component is required.

```python
discord.ui.Select.required
```

--------------------------------

### Fetch Invite with Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Fetches an invite from a Discord invite URL or ID. It can include approximate member and presence counts, and optionally the expiration date. The `with_expiration` parameter is deprecated.

```Python
await bot.fetch_invite("https://discord.gg/example")
await bot.fetch_invite("example_id", with_counts=False)
```

--------------------------------

### ext.commands: Properly handle positional-only parameters in bot command signatures

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Improves the handling of positional-only parameters in command signatures within `ext.commands`. This ensures that commands with such parameters are parsed and displayed correctly.

```Python
from discord.ext import commands

# Example usage:
# @bot.command()
# async def positional_only( /, arg1: str):
#     await ctx.send(f'Received: {arg1}')
# # This command should now function correctly
```

--------------------------------

### Fetching a Specific Application Command

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

The `_fetch_command` coroutine retrieves a specific application command by its ID. It can fetch global commands or commands within a particular guild. It requires the command ID and optionally accepts a guild object.

```python
command = await bot._fetch_command(command_id=1234567890, guild=discord.Object(id=9876543210))
```

--------------------------------

### Subclassing discord.py Context

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Illustrates how to create a custom Context subclass in discord.py to add specific functionality. It shows defining a new context class with custom properties and then using it within the bot's on_message event.

```Python
class MyContext(commands.Context):
    @property
    def secret(self):
        return 'my secret here'

```

```Python
class MyBot(commands.Bot):
    async def on_message(self, message):
        ctx = await self.get_context(message, cls=MyContext)
        await self.invoke(ctx)

```

```Python
@bot.command()
async def secret(ctx):
    await ctx.send(ctx.secret)

```

--------------------------------

### ext.commands: Add GuildConverter

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces `GuildConverter` to the `ext.commands` extension. This converter simplifies the process of accepting `Guild` objects as command arguments, allowing users to refer to guilds by ID or name.

```Python
from discord.ext import commands

# Example usage within a command:
# @bot.command()
# async def get_guild_info(ctx, guild: commands.GuildConverter):
#     await ctx.send(f'Guild name: {guild.name}')
```

--------------------------------

### Define Chat Input Commands in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This section covers the definition of chat input commands in discord.py, referencing `discord.AppCommandType.chat_input` and `discord.MessageType.chat_input_command`.

```python
discord.AppCommandType.chat_input
discord.MessageType.chat_input_command
```

--------------------------------

### Update Context Handling in discord.py Commands

Source: https://discordpy.readthedocs.io/en/stable/migrating_to_v1

Demonstrates the change in how the Context object is passed to commands in discord.py, moving from an optional parameter to a mandatory one. This change aligns the Context object with the abc.Messageable interface.

```Python
# before
@bot.command()
async def foo():
    await bot.say('Hello')

# after
@bot.command()
async def foo(ctx):
    await ctx.send('Hello')

```

--------------------------------

### Discord.py Message Attributes: Content, Type, Flags, and More

Source: https://discordpy.readthedocs.io/en/stable/

This snippet outlines attributes related to the content, type, and flags of messages in discord.py, along with message-related application and converter objects.

```python
message_snapshots = discord.Message.message_snapshots
message_type = discord.MessageType
message_flags = discord.MessageFlags
message_application = discord.MessageApplication
message_reference = discord.MessageReference
message_interaction = discord.MessageInteraction
message_interaction_metadata = discord.MessageInteractionMetadata
message_converter = commands.MessageConverter
message_not_found = commands.MessageNotFound
messageable = discord.abc.Messageable
```

--------------------------------

### Working with Discord Message Snapshot Stickers in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Explains how to access stickers associated with a message snapshot in discord.py.

```python
message_snapshot.stickers
# Accessing stickers from a message snapshot
```

--------------------------------

### Add various new permissions

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces several new permission flags, including those for events, creator monetization analytics, and polls, as well as permissions for using external apps.

```Python
import discord

class Permissions:
    def events(self) -> 'Permissions':
        pass
    create_events: bool
    view_creator_monetization_analytics: bool
    send_polls: bool
    create_polls: bool
    use_external_apps: bool

# Example usage:
# new_permissions = discord.Permissions()
# new_permissions.send_polls = True
# new_permissions.create_events = True

```

--------------------------------

### Add support for AuditLogAction monetization fields

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Extends audit log capabilities to include monetization-related actions, specifically `creator_monetization_request_created` and `creator_monetization_terms_accepted`.

```Python
import discord

class AuditLogAction:
    creator_monetization_request_created: discord.AuditLogAction
    creator_monetization_terms_accepted: discord.AuditLogAction

# Example usage:
# async for entry in guild.audit_logs(action=discord.AuditLogAction.creator_monetization_request_created):
#     print(entry.user)

```

--------------------------------

### Check Subset/Superset Permissions

Source: https://discordpy.readthedocs.io/en/stable/

Compares permission sets to determine if one is a subset or superset of another. This helps in understanding permission hierarchies.

```python
discord.Permissions.is_subset()
```

```python
discord.Permissions.is_superset()
```

--------------------------------

### Send Message (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Sends a message to the destination with the given content. For interactions, it either sends an initial response or a followup message. It supports various message formatting options like embeds, files, and mentions, and handles related exceptions.

```python
async def send(content: Optional[str] = None, *, tts: bool = False, embed: Optional[Embed] = None, embeds: Optional[List[Embed]] = None, file: Optional[File] = None, files: Optional[List[File]] = None, stickers: Optional[List[discord.Asset]] = None, delete_after: Optional[float] = None, nonce: Optional[int] = None, allowed_mentions: Optional[AllowedMentions] = None, reference: Optional[Union[Message, MessageReference, PartialMessage]] = None, mention_author: Optional[bool] = None, view: Optional[Union[discord.ui.View, discord.ui.LayoutView]] = None, suppress_embeds: bool = False, ephemeral: bool = False, silent: bool = False, poll: Optional[discord.ui.types.Poll] = None) -> Message:
    """Sends a message to the destination with the content given.

    This works similarly to `send()` for non-interaction contexts.
    For interaction based contexts this does one of the following:
      * `discord.InteractionResponse.send_message()` if no response has been given.
      * A followup message if a response has been given.
      * Regular send if the interaction has expired

    Parameters
    ----------
    content : Optional[str]
        The content of the message to send.
    tts : bool
        Indicates if the message should be sent using text-to-speech.
    embed : Embed
        The rich embed for the content.
    embeds : List[Embed]
        A list of embeds for the content.
    file : File
        The file to upload.
    files : List[File]
        A list of files to upload. Must be a maximum of 10.
    stickers : List[discord.Asset]
        A list of stickers to send.
    nonce : int
        The nonce to use for sending this message.
    delete_after : Optional[float]
        If provided, the number of seconds to wait before deleting the message.
    allowed_mentions : AllowedMentions
        Controls the mentions being processed in this message.
    reference : Union[Message, MessageReference, PartialMessage]
        A reference to the Message to which you are replying.
    mention_author : Optional[bool]
        If set, overrides the `replied_user` attribute of `allowed_mentions`.
    view : Union[discord.ui.View, discord.ui.LayoutView]
        A Discord UI View to add to the message.
    suppress_embeds : bool
        Whether to suppress embeds for the message.
    ephemeral : bool
        Whether the message should be ephemeral (only visible to the user).
    silent : bool
        Whether the message should be sent silently (without notifications).
    poll : discord.ui.types.Poll
        A poll to send with the message.

    Returns
    ------
    Message
        The message that was sent.

    Raises
    ------
    HTTPException
        Sending the message failed.
    Forbidden
        You do not have the proper permissions to send the message.
    ValueError
        The `files` list is not of the appropriate size.
    TypeError
        You specified both `file` and `files`.
    """
    # Implementation details would go here
```

--------------------------------

### Discord Member Roles List

Source: https://discordpy.readthedocs.io/en/stable/

A list of roles assigned to a member.

```python
discord.Member.roles
```

--------------------------------

### Handle Command Registration Error in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Raised when a command cannot be added to discord.py because its name is already in use by a different command. It inherits from discord.ClientException and indicates if the conflict is with an alias.

```Python
class CommandRegistrationError(discord.ClientException):
    """An exception raised when the command can’t be added because the name is already taken by a different command.

    This inherits from `discord.ClientException`
    New in version 1.4.
    """
    def __init__(self, name: str, *, alias_conflict: bool = False):
        self.name = name
        self.alias_conflict = alias_conflict
        message = f"Command {name} is already registered."
        if alias_conflict:
            message += " It conflicts with an alias."
        super().__init__(message)

    name: str
        """The command name that had the error."""
    alias_conflict: bool
        """Whether the name that conflicts is an alias of the command we try to add."""

```

--------------------------------

### Discord Stream Integration Role Information

Source: https://discordpy.readthedocs.io/en/stable/

Provides information about the role associated with a stream integration.

```python
discord.StreamIntegration.role
```

--------------------------------

### Add Parameter.displayed_name Support in ext.commands

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Implements support for `Parameter.displayed_name` in `ext.commands`, enabling custom display names for command parameters.

```Python
# [ext.commands] Add support for Parameter.displayed_name (GH-9427).
```

--------------------------------

### Adding Views to Bots in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This entry shows the 'add_view()' method for 'Client' and 'Bot', used for adding persistent views to the bot.

```Python
discord.Client.add_view()
commands.Bot.add_view()
```

--------------------------------

### Handle Extension ImportErrors Gracefully

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Prevents `ExtensionNotFound` from being raised when extensions fail internally due to `ImportError`, improving extension loading robustness.

```python
# [ext.commands] Extensions that fail internally due to ImportError will no longer raise `ExtensionNotFound`. (GH-2244, GH-2275, GH-2291)
```

--------------------------------

### RoleSelect Attributes and Properties

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides an overview of the accessible attributes and properties of the RoleSelect component, including its unique identifier, default selections, disabled status, component type, selected values, and parent view.

```Python
# Accessing attributes
role_select.custom_id
role_select.default_values
role_select.disabled
role_select.type
role_select.values
role_select.parent
role_select.placeholder
role_select.required
role_select.view
```

--------------------------------

### Fix Client Entitlements Pagination

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Corrects an issue with `Client.entitlements()` where it was limited to returning only 100 entries, improving data retrieval.

```Python
Fix bug in `Client.entitlements()` only returning 100 entries (GH-10051)
```

--------------------------------

### Create Discord Permissions - Expressions

Source: https://discordpy.readthedocs.io/en/stable/

Represents the permission to create expressions, possibly related to custom emojis or stickers.

```python
discord.Permissions.create_expressions
```

--------------------------------

### HybridGroup @command Decorator

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Details the @command decorator for HybridGroup, which serves as a shortcut to invoke hybrid_command() and add the command to the internal list. It returns a decorator that converts a method into a Command and adds it to the bot.

```python
@command(_* args_, _** kwargs_)¶
    
A shortcut decorator that invokes `hybrid_command()` and adds it to the internal command list via `add_command()`.

Returns
    
A decorator that converts the provided method into a Command, adds it to the bot, then returns it.

Return type
    
Callable[…, `HybridCommand`]
```

--------------------------------

### Fallback Behaviour for CurrentGuild in ext.commands

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds fallback behavior to `CurrentGuild` in `ext.commands`, improving its robustness when guild information is not readily available.

```python
[ext.commands] Add fallback behaviour to `CurrentGuild`.
```

--------------------------------

### Discord.py Converters for Command Arguments

Source: https://discordpy.readthedocs.io/en/stable/

Showcases the various built-in converters in discord.py's commands extension, used to automatically convert user input into specific Python types or Discord objects for command arguments.

```Python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def convert_examples(ctx,
                           member: discord.Member,
                           channel: discord.TextChannel,
                           role: discord.Role,
                           emoji: discord.Emoji,
                           user: discord.User,
                           message: discord.Message,
                           invite: discord.Invite,
                           colour: discord.Colour):
    """Demonstrates various converters."""
    await ctx.send(f"Member: {member.name}")
    await ctx.send(f"Channel: {channel.name}")
    await ctx.send(f"Role: {role.name}")
    await ctx.send(f"Emoji: {emoji}")
    await ctx.send(f"User: {user.name}")
    await ctx.send(f"Message ID: {message.id}")
    await ctx.send(f"Invite URL: {invite.url}")
    await ctx.send(f"Colour: {colour}")

# Example of custom converter usage
# class MyCustomConverter(commands.Converter):
#     async def convert(self, ctx, argument):
#         # Custom conversion logic here
#         return argument.upper() # Example: convert to uppercase

# @bot.command()
# async def custom_convert(ctx, value: MyCustomConverter):
#     await ctx.send(f"Converted value: {value}")

# Example of handling ConversionError
# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.ConversionError):
#         await ctx.send(f"Could not convert argument: {error}")
#     else:
#         await ctx.send(f"An unexpected error occurred: {error}")

# bot.run('YOUR_BOT_TOKEN')
```

--------------------------------

### ext.commands: Add support for rgb CSS function in ColourConverter

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Extends the `ColourConverter` in the `ext.commands` extension to support the `rgb()` CSS function. This allows users to specify colors using the `rgb(r, g, b)` format in commands.

```Python
from discord.ext import commands

# Example usage within a command:
# @bot.command()
# async def set_color(ctx, color: commands.ColourConverter):
#     await ctx.send(f'Color set to RGB: {color.r}, {color.g}, {color.b}')
```

--------------------------------

### Python: Async Iterator Usage

Source: https://discordpy.readthedocs.io/en/stable/migrating

Shows the transition from a custom AsyncIterator class with a .next() method to standard asynchronous iterators using 'async for' or 'anext()'. This change simplifies iterator handling.

```Python
# before
it = channel.history()
while True:
    try:
        message = await self.next()
    except discord.NoMoreItems:
        break
    print(f'Found message with ID {message.id}')

# after
async for message in channel.history():
    print(f'Found message with ID {message.id}')
```

```Python
# before
it = channel.history()
first = await it.next()
if first.content == 'do not iterate':
    return
async for message in it:
    ...
```

--------------------------------

### Discord AppCommandChannel and AppCommandThread Resolution

Source: https://discordpy.readthedocs.io/en/stable/

Attributes for resolving channel and thread types within application commands.

```python
discord.app_commands.AppCommandChannel.resolve()
discord.app_commands.AppCommandThread.resolve()
```

--------------------------------

### Positional-Only Flag Parameters in ext.commands

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces support for positional-only flag parameters in `ext.commands`, allowing for more precise control over command argument parsing.

```python
[ext.commands] Add support for positional-only flag parameters (GH-9805).
```

--------------------------------

### Working with Discord Polls

Source: https://discordpy.readthedocs.io/en/stable/

Details the structures and attributes related to polls in Discord, including poll questions, answers, and message types for poll results. Also covers intents required for poll functionality.

```Python
discord.Poll
```

```Python
discord.Message.poll
```

```Python
discord.PollAnswer.poll
```

```Python
discord.MessageType.poll_result
```

```Python
discord.PollAnswer
```

```Python
discord.PollLayoutType
```

```Python
discord.PollMedia
```

```Python
discord.Intents.polls
```

```Python
discord.Poll.question
```

--------------------------------

### Copy discord.py Group

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Creates a copy of the current `Group`, returning a new instance of the group.

```python
copy()
```

--------------------------------

### Send a message to a specific channel

Source: https://discordpy.readthedocs.io/en/stable/faq

Fetches a specific channel using its ID and sends a message to it. Requires a discord.Client instance and the channel ID.

```Python
channel = client.get_channel(12324234183172)
await channel.send('hello')
```

--------------------------------

### Create Discord Hybrid Command Group (@hybrid_group)

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

The @hybrid_group decorator creates a hybrid command group, combining traditional and application command functionalities. It invokes hybrid_group() and adds it to the internal command list via add_command(). It returns a decorator that converts a method into a Group.

```Python
@hybrid_group(_name =..., _with_app_command =True_, _* args_, _** kwargs_)
def hybrid_group_func(self):
    pass
```

--------------------------------

### Partial Webhook

Source: https://discordpy.readthedocs.io/en/stable/

Represents a partial webhook, allowing interaction with webhook data.

```Python
discord.Webhook.partial()
```

--------------------------------

### Cog App Command Error Handling

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Shows how to implement `has_app_command_error_handler` and `cog_app_command_error` for handling errors specifically from application commands (slash commands) within a cog.

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def has_app_command_error_handler(self) -> bool:
        return True

    async def cog_app_command_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(f'App command error: {error}')
```

--------------------------------

### Discord User and Member Avatars

Source: https://discordpy.readthedocs.io/en/stable/

This documentation explains how to access and display user and member avatars in Discord.py. It includes details on retrieving default avatars, custom avatars, and avatar decorations, along with their associated SKU IDs.

```python
discord.Embed.author.avatar
commands.Context.author.avatar
discord.Message.author.avatar
discord.abc.User.avatar
discord.AuditLogDiff.avatar
discord.ClientUser.avatar
discord.Member.avatar
discord.SyncWebhook.avatar
discord.TeamMember.avatar
discord.User.avatar
discord.Webhook.avatar
discord.WidgetMember.avatar
discord.abc.User.avatar_decoration
discord.ClientUser.avatar_decoration
discord.Member.avatar_decoration
discord.TeamMember.avatar_decoration
discord.User.avatar_decoration
discord.WidgetMember.avatar_decoration
discord.abc.User.avatar_decoration_sku_id
discord.ClientUser.avatar_decoration_sku_id
discord.Member.avatar_decoration_sku_id
discord.TeamMember.avatar_decoration_sku_id
discord.User.avatar_decoration_sku_id
discord.WidgetMember.avatar_decoration_sku_id
```

--------------------------------

### Handle Soundboard Sound Not Found Errors in discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This exception is raised when the bot cannot find a soundboard sound. It inherits from BadArgument and is relevant for commands involving soundboard functionalities.

```Python
class SoundboardSoundNotFound(_argument_):
    """Exception raised when the bot can not find the soundboard sound.
    This inherits from `BadArgument`
    New in version 2.5.

    argument :: `str`
        The sound supplied by the caller that was not found
    """
    pass
```

--------------------------------

### Set Traceback for Hybrid Command Invocations

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Explicitly sets a traceback for hybrid command invocations within the `ext.commands` extension. This improves error reporting and debugging for hybrid commands.

```Python
[ext.commands] Explicit set a traceback for hybrid command invocations (GH-9205)
```

--------------------------------

### Discord Paginator Linesep

Source: https://discordpy.readthedocs.io/en/stable/

Shows the 'linesep' attribute for the commands.Paginator, which defines the line separator used in paginated messages.

```python
from discord.ext import commands

# Accessing the line separator for paginator
line_separator = commands.Paginator.linesep
```

--------------------------------

### PartialInviteGuild Icon Changes in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Explains the modifications to PartialInviteGuild.icon following the asset redesign. The icon attribute is now an Asset object, and its key can be accessed directly.

```python
PartialInviteGuild.icon (replaced by PartialInviteGuild.icon.key)
```

--------------------------------

### Add GIF Stickers Support

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces support for GIF stickers, enabling the use and display of animated stickers in Discord.

```python
Add support for GIF stickers (GH-9737).
```

--------------------------------

### Handle Discord Client Errors

Source: https://discordpy.readthedocs.io/en/stable/

Provides a general error handling method for the Discord client. This is a fallback for unhandled exceptions that may occur within the library.

```python
discord.Client.on_error(event: str, *args, **kwargs) -> None
```

```python
commands.Bot.on_error(event: str, *args, **kwargs) -> None
```

```python
discord.on_error(event: str, *args, **kwargs) -> None
```

--------------------------------

### CommandNotFound Exception in discord.py

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Handles exceptions raised when an application command cannot be found. It includes the command's name, parent command names, and the type of command that was not found.

```Python
class CommandNotFound(AppCommandError):
    """An exception raised when an application command could not be found.

    This inherits from `AppCommandError`.

    New in version 2.0.
    """
    def __init__(self, name: str, parents: List[str], type: AppCommandType = AppCommandType.chat_input) -> None:
        self.name: str = name
        self.parents: List[str] = parents
        self.type: AppCommandType = type
```

--------------------------------

### Discord ThumbnailComponent Attributes

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Details the attributes of the ThumbnailComponent in Discord.py, including description, id, media, spoiler, and type. It inherits from Component and represents thumbnails in the Discord Bot UI Kit.

```python
class ThumbnailComponent:
    description
    id
    media
    spoiler
    type
```

--------------------------------

### Python: Member Edit Method Return Value

Source: https://discordpy.readthedocs.io/en/stable/migrating

Demonstrates the change in the Member.edit() method from in-place editing to returning a new instance. This change helps prevent race conditions between edits and gateway events.

```Python
# before
await member.edit(nick='new nick')
await member.send(f'Your new nick is {member.nick}')

# after
updated_member = await member.edit(nick='new nick')
await member.send(f'Your new nick is {updated_member.nick}')
```

--------------------------------

### Handling Discord HTTP Exceptions in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Details how to access the HTTP status code from a `discord.HTTPException` in discord.py.

```python
http_exception.status
# Getting the HTTP status code from an exception
```

--------------------------------

### Manage App Command Permissions

Source: https://discordpy.readthedocs.io/en/stable/

Enables the management of permissions for application commands, allowing developers to control which roles or users can use specific commands within a guild. This includes updating and retrieving permission data.

```Python
discord.app_commands.AppCommandPermissions
discord.app_commands.AppCommandPermissionType
discord.AuditLogAction.app_command_permission_update
discord.AuditLogDiff.app_command_permissions
discord.ApplicationFlags.app_commands_badge
discord.Interaction.app_permissions
discord.app_commands.AppCommandGroup
discord.app_commands.AppCommand
discord.app_commands.AppCommandChannel
discord.app_commands.AppCommandContext
discord.app_commands.AppCommandError
discord.AppCommandOptionType
discord.app_commands.AppCommandThread
discord.AppCommandType
discord.app_commands.AppInstallationType
discord.AppInstallParams
discord.RawAppCommandPermissionsUpdateEvent.application_id
```

--------------------------------

### Add easier way to move channels using abc.GuildChannel.move()

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Provides a simplified method `move()` for `abc.GuildChannel` subclasses, making it easier to reorder channels within a guild. This function abstracts the underlying API calls required for channel position updates.

```Python
from discord.abc import GuildChannel

# Example usage:
# await channel.move(position=0)
```

--------------------------------

### URL Attributes in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Lists various attributes across different discord.py classes that store URLs, including assets, embeds, attachments, and UI components.

```python
discord.File.uri
discord.Asset.url
discord.Attachment.url
discord.Embed.url
discord.ui.Button.url
discord.ui.File.url
discord.Invite.url
discord.Message.url
discord.WebhookMessage.url
discord.User.avatar.url
```

--------------------------------

### Convert to ForumChannel using discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

This converter class is used to convert arguments to a discord.py ForumChannel. It supports lookups by ID, mention, channel URL, and name within the local guild or global cache for DMs. It can raise CommandError or BadArgument exceptions.

```Python
class ForumChannelConverter(Converter):
    async def convert(self, ctx, argument):
        # Lookup logic here
        pass
```

--------------------------------

### Copy Global Commands to a Specific Guild

Source: https://discordpy.readthedocs.io/en/stable/faq

This method is used for development purposes to copy all globally registered commands to a specific guild, allowing for easier testing.

```python
import discord

# Assuming 'tree' is your CommandTree instance
tree.copy_global_to(guild=discord.Object(123456789012345678))
```

--------------------------------

### Python: Handling Check Failures with Error Handlers

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/commands

Shows how to define an error handler for a specific command to catch `commands.CheckFailure` exceptions. This allows for custom responses when checks fail, such as informing the user that they don't have permission.

```Python
@bot.command()
@commands.is_owner()
@is_in_guild(41771983423143937)
async def secretguilddata(ctx):
    """super secret stuff"""
    await ctx.send('secret stuff')

@secretguilddata.error
async def secretguilddata_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('nothing to see here comrade.')
```

--------------------------------

### Managing Guild Pruning and Updates

Source: https://discordpy.readthedocs.io/en/stable/

Details methods for pruning members from a guild and attributes related to public updates channels and guild settings in discord.py.

```Python
discord.Guild.prune_members()
```

```Python
discord.AuditLogDiff.public_updates_channel
```

```Python
discord.Guild.public_updates_channel
```

--------------------------------

### Accessing Discord Guild Sticker Limits in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Shows how to retrieve the sticker limit for a Discord guild using discord.py.

```python
guild.sticker_limit
# Getting the maximum number of stickers a guild can have
```

--------------------------------

### Register Dynamic Items for Persistent Listening in discord.py

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Details the process of registering `DynamicItem` classes for persistent listening in discord.py. This method accepts class types and is used for components that need to persist beyond the program's lifecycle.

```Python
import discord
from discord.ext import commands

# Assume DynamicItem is defined elsewhere or imported
# class MyDynamicItem(discord.ui.DynamicItem):
#     async def interaction(self, interaction: discord.Interaction):
#         await interaction.response.send_message('Dynamic item clicked!')

# Assuming 'bot' is an instance of commands.Bot
# bot.add_dynamic_items(MyDynamicItem)

```

--------------------------------

### Update dependencies for Python 3.9+

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Updates library dependencies to support Python 3.9+ without requiring build tools. Requires discord.py.

```python
Update dependencies to allow the library to work on Python 3.9+ without requiring build tools. (GH-5984, GH-5970)
```

--------------------------------

### Publish Message to Followers (discord.py)

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Publishes a message to the channel's followers. Requires 'send_messages' permission and potentially 'manage_messages' if the message is not the user's own. Raises HTTPException on failure.

```Python
await message._publish()

```

--------------------------------

### Add Context.filesize_limit Property in ext.commands

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Adds the `Context.filesize_limit` property to the `ext.commands` context, allowing access to the current file size limit for uploads within commands.

```Python
# [ext.commands] Add Context.filesize_limit property (GH-9416).
```

--------------------------------

### Discord Forum Layout Type List View

Source: https://discordpy.readthedocs.io/en/stable/

Represents the 'list_view' layout type for Discord Forums, used for displaying forum posts in a list format.

```python
import discord

# Using the list view layout for forums
forum_list_view = discord.ForumLayoutType.list_view
```

--------------------------------

### discord.py Interaction - Followup Property

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Provides access to the webhook for sending follow-up messages after the initial interaction response has been sent.

```python
followup: Webhook
```

--------------------------------

### Discord Login Failure Exception

Source: https://discordpy.readthedocs.io/en/stable/

Represents the exception raised when a login attempt to Discord fails.

```python
import discord

# Handling login failures
# try:
#     await client.login('invalid_token')
# except discord.LoginFailure:
#     print('Login failed!')
```

--------------------------------

### Discord Member Flags DM Settings Upsell

Source: https://discordpy.readthedocs.io/en/stable/

Checks the dm_settings_upsell_acknowledged flag for discord.Member.

```python
discord.MemberFlags.dm_settings_upsell_acknowledged
```

--------------------------------

### Add support for allowed contexts in app commands

Source: https://discordpy.readthedocs.io/en/stable/whats_new

Introduces support for specifying the allowed contexts (e.g., guild, DM) where an application command can be used. This involves changes to decorators and the addition of new context-related classes and attributes.

```Python
from discord.app_commands import app_commands

# Example of using guild_only and dm_only decorators
@app_commands.command(name='mycommand')
@app_commands.guild_only()
def my_guild_command(interaction: discord.Interaction):
    pass

@app_commands.command(name='dmcommand')
@app_commands.dm_only()
def my_dm_command(interaction: discord.Interaction):
    pass

# Example of using allowed_contexts
@app_commands.command(name='contextcommand')
@app_commands.allowed_contexts(app_commands.AppCommandContext.guild, app_commands.AppCommandContext.bot_ கொள்ளலாம்)
def my_context_command(interaction: discord.Interaction):
    pass

# New class for context
class AppCommandContext:
    guild: str
    dm: str
    bot_ கொள்ளலாம்: str

# New attribute for commands
app_commands.Command.allowed_contexts: list[AppCommandContext]
app_commands.AppCommand.allowed_contexts: list[AppCommandContext]
app_commands.ContextMenu.allowed_contexts: list[AppCommandContext]

# New decorator
app_commands.private_channel_only()
app_commands.allowed_contexts()

```

--------------------------------

### discord.py Tasks Extension

Source: https://discordpy.readthedocs.io/en/stable/index

The discord.ext.tasks extension offers helpers for managing asyncio Tasks, useful for scheduling recurring operations within a Discord bot.

```Python
import discord
from discord.ext import tasks, commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(seconds=10)
    async def my_task(self):
        print('Task is running!')

    @my_task.before_loop
    async def before_my_task(self):
        await self.bot.wait_until_ready()

# To add this cog to your bot:
# await bot.add_cog(MyCog(bot))
```

--------------------------------

### Emoji and PartialEmoji Interface Changes in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Details the updated interface for Emoji and PartialEmoji objects, aligning them with the Asset object. This includes changes to URL attributes and the introduction of new methods for reading and saving.

```python
Emoji.url is now of str type.
Emoji.url_as has been removed.
Emoji.url.read has been replaced with Emoji.read().
Emoji.url.save has been replaced with Emoji.save().
```

--------------------------------

### Discord AllowedMentions Roles

Source: https://discordpy.readthedocs.io/en/stable/

Specifies which roles to mention in a message.

```python
discord.AllowedMentions.roles
```

--------------------------------

### Convert to Role

Source: https://discordpy.readthedocs.io/en/stable/ext/commands/api

Converts a string argument to a Role object within the local guild. Raises NoPrivateMessage in DM contexts. Supports lookup by ID, mention, or name.

```python
class RoleConverter(Converter):
    async def convert(self, ctx, argument):
        # Lookup strategy: ID, mention, name
        # Raises NoPrivateMessage in DMs
        pass
```

--------------------------------

### All User Flags in discord.py

Source: https://discordpy.readthedocs.io/en/stable/

This snippet shows 'PublicUserFlags.all()' and 'UserFlags.all()', used to represent or check all available user flags.

```Python
discord.PublicUserFlags.all()
discord.UserFlags.all()
```

--------------------------------

### AppInfo Cover Image Changes in discord.py

Source: https://discordpy.readthedocs.io/en/stable/migrating

Explains the modifications to AppInfo.cover_image following the asset redesign. The cover image attribute is now an Asset object, potentially being None, and URL access has been updated.

```python
AppInfo.cover_image (replaced by AppInfo.cover_image.key)
AppInfo.cover_image_url (replaced by AppInfo.cover_image)
  * The new attribute may now be None.
AppInfo.cover_image_url_as (replaced by AppInfo.cover_image.replace)
```

--------------------------------

### Discord.py Interaction Response Types and Modals

Source: https://discordpy.readthedocs.io/en/stable/

This section outlines attributes for handling modal interactions and response types in discord.py, including modal submission and related metadata.

```python
modal_ui = discord.ui.Modal
interaction_modal_response = discord.InteractionResponseType.modal
modal_interaction_metadata = discord.MessageInteractionMetadata.modal_interaction
interaction_modal_submit = discord.InteractionType.modal_submit
```

--------------------------------

### Discord AppCommandThread Properties

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Details various properties of the AppCommandThread class, including ID, type, name, parent information, owner details, message counts, permissions, and timestamps.

```python
id

The ID of the thread.
Type
`int` 

type

The type of thread.
Type
`ChannelType` 

name

The name of the thread.
Type
`str` 

parent_id

The parent text channel ID this thread belongs to.
Type
`int` 

owner_id

The user’s ID that created this thread.
New in version 2.6.
Type
`int` 

last_message_id

The last message ID of the message sent to this thread. It may _not_ point to an existing or valid message.
New in version 2.6.
Type
Optional[`int`] 

slowmode_delay

The number of seconds a member must wait between sending messages in this thread. A value of `0` denotes that it is disabled. Bots and users with `manage_channels` or `manage_messages` bypass slowmode.
New in version 2.6.
Type
`int` 

message_count

An approximate number of messages in this thread.
New in version 2.6.
Type
`int` 

member_count

An approximate number of members in this thread. This caps at 50.
New in version 2.6.
Type
`int` 

total_message_sent

The total number of messages sent, including deleted messages.
New in version 2.6.
Type
`int` 

permissions

The resolved permissions of the user who invoked the application command in that thread. 
Type
`Permissions` 

guild_id

The guild ID this thread belongs to.
Type
`int` 

archived

Whether the thread is archived. 
Type
`bool` 

locked

Whether the thread is locked. 
Type
`bool` 

invitable

Whether non-moderators can add other non-moderators to this thread. This is always `True` for public threads. 
Type
`bool` 

archiver_id

The user’s ID that archived this thread. 
Type
Optional[`int`] 

auto_archive_duration

The duration in minutes until the thread is automatically hidden from the channel list. Usually a value of 60, 1440, 4320 and 10080. 
Type
`int` 

archive_timestamp

An aware timestamp of when the thread’s archived status was last updated in UTC. 
Type
`datetime.datetime` 

guild

The channel’s guild, from cache, if found. 
Type
Optional[`Guild`] 

applied_tags

A list of tags applied to this thread.
New in version 2.6.
Type
List[`ForumTag`] 

parent

The parent channel this thread belongs to. 
Type
Optional[Union[`ForumChannel`, `TextChannel`]] 

flags

The flags associated with this thread.
New in version 2.6.
Type
`ChannelFlags` 

owner

The member this thread belongs to.
New in version 2.6.
Type
Optional[`Member`] 

mention

The string that allows you to mention the thread. 
Type
`str` 

jump_url

Returns a URL that allows the client to jump to the thread.
New in version 2.6.
Type
`str` 

created_at

An aware timestamp of when the thread was created in UTC.
Note
This timestamp only exists for threads created after 9 January 2022, otherwise returns `None`. 
```

--------------------------------

### Discord Bucket Type for Rate Limiting

Source: https://discordpy.readthedocs.io/en/stable/

Specifies the role bucket type for rate limiting, allowing different rate limits based on roles.

```python
commands.BucketType.role
```

--------------------------------

### Discord SelectMenu Component

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Represents a select menu, similar to a dropdown, for choosing options in the Discord UI Kit. It can be configured with placeholder text, minimum and maximum selection values, and a list of selectable options. Introduced in version 2.0.

```python
class discord.SelectMenu:
    """Represents a select menu from the Discord Bot UI Kit.

    A select menu is functionally the same as a dropdown, however on mobile it renders a bit differently.
    Note
    The user constructible and usable type to create a select menu is `discord.ui.Select` not this one.
    New in version 2.0.
    """
    type: `ComponentType`
    custom_id: Optional[`str`]
    placeholder: Optional[`str`]
    min_values: `int`
    max_values: `int`
    options: List[`SelectOption`]
    disabled: `bool`
    channel_types: List[`ChannelType`]
    id: Optional[`int`]
    required: `bool`
```

--------------------------------

### User and Guild Unavailability in Discord.py

Source: https://discordpy.readthedocs.io/en/stable/

Covers attributes related to user and guild unavailability in discord.py, such as discord.Guild.unavailable and discord.User.

```python
discord.Guild.unavailable
discord.User
```

--------------------------------

### Discord MediaGalleryComponent Attributes

Source: https://discordpy.readthedocs.io/en/stable/interactions/api

Details the attributes of the MediaGalleryComponent in Discord.py, including id, items, and type. It inherits from Component and represents media gallery components.

```python
class MediaGalleryComponent:
    id
    items
    type
```