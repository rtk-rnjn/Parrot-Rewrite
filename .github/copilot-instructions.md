### Create a Discord.py Extension

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/extensions.html

An extension is a Python file with an entry point called `setup`, which must be a Python coroutine. This example defines a simple command and adds it to the bot upon loading.

```python
from discord.ext import commands

@commands.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.display_name}.')

async def setup(bot):
    bot.add_command(hello)
```

--------------------------------

### Bot Setup and Configuration

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Details on setting up the root logger and asynchronous setup hooks for the bot.

```APIDOC
## Setup Root Logger

### Description
Whether to set up the root logger rather than the library logger. By default, only the library logger (`'discord'`) is set up. If this is set to `True` then the root logger is set up as well.

Defaults to `False`.

New in version 2.0.

### Parameters
* **`setup_hook`** (bool) - Optional - Whether to set up the root logger.

### Request Example
```python
# Example usage not directly provided, but conceptually:
# bot = commands.Bot(command_prefix='!', setup_hook=True)
```

### Response
No direct response, modifies logger behavior.
```

```APIDOC
## _setup_hook() Coroutine

### Description
A coroutine to be called to setup the bot, by default this is blank. To perform asynchronous setup after the bot is logged in but before it has connected to the Websocket, overwrite this coroutine. This is only called once, in `login()`, and will be called before any events are dispatched, making it a better solution than doing such setup in the `on_ready()` event.

**Warning**: Since this is called _before_ the websocket connection is made therefore anything that waits for the websocket will deadlock, this includes things like `wait_for()` and `wait_until_ready()`.

New in version 2.0.

### Method
`async def _setup_hook()`

### Endpoint
N/A (Internal method)

### Request Example
```python
# Example of overriding in a bot subclass:
# class MyBot(commands.Bot):
#     async def _setup_hook(self):
#         await super()._setup_hook()
#         # ... your setup code here ...
```

### Response
No direct response, performs asynchronous setup.
```

--------------------------------

### Update Extension Setup Function

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the transition from a synchronous setup function to an asynchronous one using await.

```python
# before
def setup(bot):
    bot.add_cog(MyCog(bot))

# after
async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

--------------------------------

### Bot Setup and Hooks

Source: https://discordpy.readthedocs.io/en/latest/api.html

Hooks and setup methods for configuring the bot before connection.

```APIDOC
## _setup_hook()

### Description
A coroutine to be called to setup the bot. Called once in login() before websocket connection.

### Method
Coroutine

## _before_identify_hook(shard_id, *, initial=False)

### Description
A hook that is called before IDENTIFYing a session.

### Parameters
#### Request Body
- **shard_id** (int) - Required - The shard ID that requested being IDENTIFY’d.
- **initial** (bool) - Optional - Whether this IDENTIFY is the first initial IDENTIFY.
```

--------------------------------

### Install discord.py on Windows

Source: https://discordpy.readthedocs.io/en/latest/intro.html

Installation command specifically for Windows environments.

```bash
py -3 -m pip install -U discord.py
```

--------------------------------

### Install library in virtual environment

Source: https://discordpy.readthedocs.io/en/latest/intro.html

Standard pip installation command to be run after activating the virtual environment.

```bash
$ pip install -U discord.py
```

--------------------------------

### Install discord.py with voice support

Source: https://discordpy.readthedocs.io/en/latest/intro.html

Installs the library with additional dependencies required for voice functionality.

```bash
python3 -m pip install -U discord.py[voice]
```

--------------------------------

### User Install Command

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

The `user_install()` decorator indicates that a command should be installed for users.

```APIDOC
## @discord.app_commands.user_install()

### Description
A decorator that indicates this command should be installed for users. This is not implemented as a `check()`, and is instead verified by Discord server side. Due to a Discord limitation, this decorator does nothing in subcommands and is ignored. New in version 2.4.

### Method
APPLY DECORATOR

### Endpoint
N/A (Decorator)

### Request Example
```python
@app_commands.command()
@app_commands.user_install()
async def my_user_install_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in users by default!')
```

### Response
N/A (Decorator)
```

--------------------------------

### Install discord.py via pip

Source: https://discordpy.readthedocs.io/en/latest/intro.html

Standard installation command for the discord.py library.

```bash
python3 -m pip install -U discord.py
```

--------------------------------

### Allowed Installs Command

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

The `allowed_installs()` decorator specifies the contexts (guilds, users) in which a command should be installed.

```APIDOC
## @discord.app_commands.allowed_installs()

### Description
A decorator that indicates this command should be installed in certain contexts. Valid contexts are guilds and users. This is not implemented as a `check()`, and is instead verified by Discord server side. Due to a Discord limitation, this decorator does nothing in subcommands and is ignored. New in version 2.4.

### Method
APPLY DECORATOR

### Endpoint
N/A (Decorator)

### Parameters
#### Query Parameters
- **guilds** (boolean) - Whether the command can be installed in guilds.
- **users** (boolean) - Whether the command can be installed for users.

### Request Example
```python
@app_commands.command()
@app_commands.allowed_installs(guilds=False, users=True)
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in users by default!')
```

### Response
N/A (Decorator)
```

--------------------------------

### Guild Install Command

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

The `guild_install()` decorator indicates that a command should be installed in guilds.

```APIDOC
## @discord.app_commands.guild_install()

### Description
A decorator that indicates this command should be installed in guilds. This is not implemented as a `check()`, and is instead verified by Discord server side. Due to a Discord limitation, this decorator does nothing in subcommands and is ignored. New in version 2.4.

### Method
APPLY DECORATOR

### Endpoint
N/A (Decorator)

### Request Example
```python
@app_commands.command()
@app_commands.guild_install()
async def my_guild_install_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in guilds by default!')
```

### Response
N/A (Decorator)
```

--------------------------------

### Extension Setup and Teardown

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/extensions.html

Extensions can define a `teardown` coroutine function, similar to `setup`, which is called when the extension is unloaded. Exceptions raised in `teardown` are ignored.

```python
async def setup(bot):
    print('I am being loaded!')

async def teardown(bot):
    print('I am being unloaded!')
```

--------------------------------

### Configure allowed installation types

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Use this decorator to specify whether the command is installed in guilds, for users, or both.

```python
@app_commands.command()
@app_commands.allowed_installs(guilds=False, users=True)
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in users by default!')
```

--------------------------------

### Simple Background Task in a Cog

Source: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

A basic example of a background task that runs every 5 seconds. Ensure the task is started in `__init__` and cancelled in `cog_unload`.

```python
from discord.ext import tasks, commands

class MyCog(commands.Cog):
    def __init__(self):
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1

```

--------------------------------

### Install Linux voice dependencies

Source: https://discordpy.readthedocs.io/en/latest/intro.html

Command to install required system-level dependencies for voice support on Debian-based systems.

```bash
$ apt install libffi-dev libnacl-dev python3-dev
```

--------------------------------

### Setup Logging Without Client.run

Source: https://discordpy.readthedocs.io/en/latest/logging.html

Initializes the library's default logging configuration manually using the utility function.

```python
import discord

discord.utils.setup_logging()

# or, for example
discord.utils.setup_logging(level=logging.INFO, root=False)
```

--------------------------------

### GET /welcome_screen

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the guild's welcome screen configuration.

```APIDOC
## GET /welcome_screen

### Description
Returns the guild's welcome screen. Requires 'COMMUNITY' feature and 'manage_guild' permission.

### Response
#### Success Response (200)
- **welcome_screen** (WelcomeScreen) - The welcome screen object.
```

--------------------------------

### Colour Creation Examples

Source: https://discordpy.readthedocs.io/en/latest/api.html

Demonstrates various ways to create Colour objects using classmethods.

```APIDOC
## Colour Creation

### From RGB
```python
colour = discord.Colour.from_rgb(255, 0, 0) # Red
```

### From HSV
```python
colour = discord.Colour.from_hsv(0.5, 1.0, 1.0) # Cyan
```

### From String
```python
colour = discord.Colour.from_str("#FF0000") # Red
colour = discord.Colour.from_str("rgb(255, 0, 0)") # Red
```

### Predefined Colours
```python
colour = discord.Colour.red()
colour = discord.Colour.blue()
colour = discord.Colour.default()
colour = discord.Colour.random()
```
```

--------------------------------

### AppInstallationType

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents the installation location of an application command.

```APIDOC
## AppInstallationType

### Description
Represents the installation location of an application command.
New in version 2.4.

### Parameters
- **guild** (`Optional[bool]`) – Whether the integration is a guild install.
- **user** (`Optional[bool]`) – Whether the integration is a user install.

### Properties
- **guild** (`bool`) - Whether the integration is a guild install.
- **user** (`bool`) - Whether the integration is a user install.
```

--------------------------------

### connect Method

Source: https://discordpy.readthedocs.io/en/latest/api.html

Establishes a WebSocket connection to Discord and starts the event loop.

```APIDOC
## connect Method

### Description
This function is a _coroutine_.
Creates a websocket connection and lets the websocket listen to messages from Discord. This is a loop that runs the entire event system and miscellaneous aspects of the library. Control is not resumed until the WebSocket connection is terminated.

### Parameters
- **reconnect** (`bool`) – If we should attempt reconnecting, either due to internet failure or a specific failure on Discord’s part. Certain disconnects that lead to bad state will not be handled (such as invalid sharding payloads or bad tokens).

### Raises
- **GatewayNotFound** – If the gateway to connect to Discord is not found. Usually if this is thrown then there is a Discord API outage.
- **ConnectionClosed** – The websocket connection has been terminated.
```

--------------------------------

### Voice Connection and Playback (Before)

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Example of the older method for joining a voice channel and playing audio using `create_ffmpeg_player`. This approach is now deprecated.

```python
vc = await client.join_voice_channel(channel)
player = vc.create_ffmpeg_player('testing.mp3', after=lambda: print('done'))
player.start()

player.is_playing()
player.pause()
player.resume()
player.stop()
# ...
```

--------------------------------

### Cog Inter-Command Communication Example

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html

This example demonstrates how one cog can interact with another by retrieving it using `bot.get_cog()`. This is useful for sharing state or functionality between cogs.

```Python
class Economy(commands.Cog):
    ...

    async def withdraw_money(self, member, money):
        # implementation here
        ...

    async def deposit_money(self, member, money):
        # implementation here
        ...

class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def coinflip(self):
        return random.randint(0, 1)

    @commands.command()
    async def gamble(self, ctx, money: int):
        """Gambles some money."""
        economy = self.bot.get_cog('Economy')
        if economy is not None:
            await economy.withdraw_money(ctx.author, money)
            if self.coinflip() == 1:
                await economy.deposit_money(ctx.author, money * 1.5)
```

--------------------------------

### Start a Scheduled Event

Source: https://discordpy.readthedocs.io/en/latest/api.html

Starts a scheduled event. This is a shorthand for editing the event's status to active. Ensure you have the necessary permissions.

```python
await event.start()
```

--------------------------------

### Channel Typing Indicator (Manual Start)

Source: https://discordpy.readthedocs.io/en/latest/api.html

This endpoint allows you to manually start sending a typing indicator to a channel. The indicator will remain active until explicitly stopped or a timeout occurs.

```APIDOC
## POST /channels/{channel.id}/typing (Manual Start)

### Description
Manually starts sending a typing indicator to the specified channel. The indicator will persist until stopped or a timeout is reached.

### Method
POST

### Endpoint
`/channels/{channel.id}/typing`

### Parameters
#### Path Parameters
- **channel.id** (string) - Required - The ID of the channel where the typing indicator should be displayed.

#### Query Parameters
None

#### Request Body
None

### Request Example
```python
await channel.typing()
# The typing indicator is now active.
# It will automatically stop after a default period or when the operation completes.
```

### Response
#### Success Response (200)
Indicates that the typing indicator has been successfully started.

#### Response Example
(No specific response body is detailed, success is indicated by the absence of an error.)
```

--------------------------------

### Shorthand for Starting a Scheduled Event

Source: https://discordpy.readthedocs.io/en/latest/api.html

This code snippet demonstrates the underlying mechanism for starting a scheduled event, which involves editing its status to 'active'.

```python
await event.edit(status=EventStatus.active)
```

--------------------------------

### AppInstallParams and IntegrationTypeConfig Models

Source: https://discordpy.readthedocs.io/en/latest/api.html

Models for configuring custom authorization URLs and installation contexts.

```APIDOC
## AppInstallParams

### Description
Represents the settings for a custom authorization URL of an application.

### Attributes
- **scopes** (List[str]) - The list of OAuth2 scopes.
- **permissions** (Permissions) - The permissions to give to the application.

## IntegrationTypeConfig

### Description
Represents the default settings for the application’s installation context.

### Attributes
- **oauth2_install_params** (Optional[AppInstallParams]) - The install params for the default in-app authorization link.
```

--------------------------------

### Implement setup_hook in Client

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows how to subclass Client and define an asynchronous setup_hook for initializing bot features.

```python
class MyClient(discord.Client):
    async def setup_hook(self):
        print('This is asynchronous!')

client = MyClient()
client.run(TOKEN)
```

--------------------------------

### Setup logging

Source: https://discordpy.readthedocs.io/en/latest/api.html

A helper function to set up logging with custom handlers, formatters, and levels. It provides defaults similar to logging.basicConfig but with discord.py specific configurations.

```python
# Example usage is not provided in the source, but the function signature is:
def setup_logging(*, handler=None, formatter=None, level=None, root=True): ...
```

--------------------------------

### Create a basic discord.py bot

Source: https://discordpy.readthedocs.io/en/latest/intro.html

A minimal example demonstrating how to subclass discord.Client and handle events. Requires the 'message_content' intent to be enabled.

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

### Set command as user-installed

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Use this decorator to indicate that the command should be installed for users.

```python
@app_commands.command()
@app_commands.user_install()
async def my_user_install_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in users by default!')
```

--------------------------------

### Load Extensions Asynchronously

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows how to load extensions using setup_hook or an async context manager.

```python
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

### Create a virtual environment

Source: https://discordpy.readthedocs.io/en/latest/intro.html

Commands to navigate to the project directory and initialize a new virtual environment.

```bash
$ cd your-bot-source
$ python3 -m venv bot-env
```

--------------------------------

### discord.__version__

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Retrieves the currently installed version of the discord.py library.

```APIDOC
## discord.__version__

### Description
Access the `__version__` attribute to get the installed version of the discord.py library.

### Method
N/A (Attribute access)

### Endpoint
N/A

### Parameters
N/A

### Request Example
```python
import discord

print(discord.__version__)
```

### Response
- **version** (string) - The version string of the discord.py library.
```

--------------------------------

### Start Scheduled Event

Source: https://discordpy.readthedocs.io/en/latest/api.html

Starts an active scheduled event. This is a shorthand for editing the event's status to `EventStatus.active`.

```APIDOC
## POST /channels/{channel.id}/events/{event.id}/start (Conceptual)

### Description
Starts the scheduled event, making it active.

### Method
`async`

### Endpoint
This action is performed on a `ScheduledEvent` object, typically via `await event.start()`.

### Parameters
#### Path Parameters
None directly for the method call, but the `event` object implies a context.

#### Query Parameters
None

#### Request Body
None

### Request Example
```python
# Assuming 'event' is a ScheduledEvent object
await event.start()
```

### Response
#### Success Response (200)
- **ScheduledEvent** (ScheduledEvent) - The scheduled event that was started.

#### Response Example
```json
{
  "id": 1234567890,
  "name": "My Awesome Event",
  "description": "Join us for some fun!",
  "start_time": "2023-10-27T10:00:00+00:00",
  "end_time": "2023-10-27T12:00:00+00:00",
  "privacy_level": "guild_only",
  "status": "active",
  "entity_type": "external",
  "user_count": 5
}
```

### Raises
- **ValueError**: If the scheduled event has already started or has ended.
- **Forbidden**: If the bot lacks the necessary permissions to start the event.
- **HTTPException**: If the event fails to start due to an API error.
```

--------------------------------

### discord.utils.setup_logging

Source: https://discordpy.readthedocs.io/en/latest/api.html

Helper function to configure logging for the library.

```APIDOC
## discord.utils.setup_logging

### Description
A helper function to setup logging, similar to logging.basicConfig but with different defaults and colour support.

### Parameters
- **handler** (logging.Handler) - Optional - The log handler to use.
- **formatter** (logging.Formatter) - Optional - The formatter to use.
- **level** (int) - Optional - The default log level.
- **root** (bool) - Optional - Whether to set up the root logger.
```

--------------------------------

### Configure command prefixes

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Examples of using when_mentioned_or to define command prefixes for a bot.

```python
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
```

```python
async def get_prefix(bot, message):
    extras = await prefixes_for(message.guild) # returns a list
    return commands.when_mentioned_or(*extras)(bot, message)
```

--------------------------------

### SessionStartLimits API

Source: https://discordpy.readthedocs.io/en/latest/api.html

Holds information about Discord session start limits.

```APIDOC
## SessionStartLimits

A class that holds info about session start limits.

### Attributes
- **max_concurrency** (int): The number of identify requests allowed per 5 seconds.
- **remaining** (int): The remaining number of session starts allowed for the current user.
- **reset_after** (int): The number of milliseconds until the limit resets.
- **total** (int): The total number of session starts the current user is allowed.
```

--------------------------------

### Create a text channel in a guild

Source: https://discordpy.readthedocs.io/en/latest/api.html

Demonstrates how to create a new text channel, including an example of setting up permission overwrites for private channels.

```python
channel = await guild.create_text_channel('cool-channel')
```

```python
overwrites = {
    guild.default_role: discord.PermissionOverwrite(read_messages=False),
    guild.me: discord.PermissionOverwrite(read_messages=True)
}

channel = await guild.create_text_channel('secret', overwrites=overwrites)
```

--------------------------------

### fetch_widget

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Gets a Widget from a guild ID.

```APIDOC
## fetch_widget

### Description
Gets a Widget from a guild ID. The guild must have the widget enabled.

### Parameters
#### Path Parameters
- **guild_id** (int) - Required - The ID of the guild.

### Response
#### Success Response (200)
- **Widget** (Object) - The guild’s widget.
```

--------------------------------

### GET /guild/widget

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the widget information for the guild.

```APIDOC
## GET /guild/widget

### Description
Returns the widget of the guild. The guild must have the widget enabled.

### Response
#### Success Response (200)
- **Widget** (Object) - The guild's widget.

### Errors
- **Forbidden** - The widget for this guild is disabled.
- **HTTPException** - Retrieving the widget failed.
```

--------------------------------

### Ban command invocation examples

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Shows valid ways to invoke the ban command with different argument combinations.

```text
$ban @Member @Member2 spam bot
$ban @Member @Member2 7 spam bot
$ban @Member spam
```

--------------------------------

### Example Cog with Special Methods and Custom Name

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Demonstrates a Cog with custom name and all special methods like cog_unload, bot_check, cog_check, cog_command_error, cog_before_invoke, cog_after_invoke, and a listener.

```python
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

### Get Partial Emoji Creation Time

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Access PartialEmoji.created_at to get the timestamp when the custom emoji was created.

```python
creation_time = partial_emoji.created_at
```

--------------------------------

### async connect()

Source: https://discordpy.readthedocs.io/en/latest/api.html

Establishes a connection to a voice server and returns a VoiceClient instance.

```APIDOC
## async connect()

### Description
Connects to voice and creates a VoiceClient to establish your connection to the voice server. This requires voice_states.

### Parameters
#### Query Parameters
- **timeout** (float) - Optional - The timeout in seconds to wait the connection to complete.
- **reconnect** (bool) - Optional - Whether the bot should automatically attempt a reconnect if a part of the handshake fails or the gateway goes down.
- **cls** (Type[VoiceProtocol]) - Optional - A type that subclasses VoiceProtocol to connect with. Defaults to VoiceClient.
- **self_mute** (bool) - Optional - Indicates if the client should be self-muted. New in version 2.0.
- **self_deaf** (bool) - Optional - Indicates if the client should be self-deafened. New in version 2.0.

### Response
#### Success Response
- **VoiceProtocol** - A voice client that is fully connected to the voice server.

### Errors
- **asyncio.TimeoutError** - Could not connect to the voice channel in time.
- **ClientException** - You are already connected to a voice channel.
- **OpusNotLoaded** - The opus library has not been loaded.
```

--------------------------------

### get_cog

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Gets the cog instance requested.

```APIDOC
## get_cog

### Description
Gets the cog instance requested by name.

### Parameters
#### Path Parameters
- **name** (str) - Required - The name of the cog.

### Response
#### Success Response (200)
- **cog** (Optional[Cog]) - The cog that was requested or None.
```

--------------------------------

### GET /channels/webhooks

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of webhooks for the channel.

```APIDOC
## GET /channels/webhooks

### Description
Gets the list of webhooks from this channel. Requires `manage_webhooks` permission.

### Response
#### Success Response (200)
- **webhooks** (List[Webhook]) - The webhooks for this channel.
```

--------------------------------

### GET /commands

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Fetches all current application commands, either globally or for a specific guild.

```APIDOC
## GET /commands

### Description
Fetches the application’s current commands. If no guild is passed, global commands are fetched; otherwise, the guild’s commands are fetched.

### Method
GET

### Endpoint
/commands

### Parameters
#### Query Parameters
- **guild** (Snowflake) - Optional - The guild to fetch the commands from.

### Response
#### Success Response (200)
- **commands** (List[AppCommand]) - The application’s commands.

#### Errors
- **HTTPException**: Fetching the commands failed.
- **MissingApplicationID**: The application ID could not be found.
```

--------------------------------

### Home Settings Actions

Source: https://discordpy.readthedocs.io/en/latest/api.html

Audit log entries for the creation and update of a guild's server guide (home settings).

```APIDOC
## home_settings_create

### Description
The guild’s server guide was created.

### Method
N/A (Event-based)

### Endpoint
N/A

### Response
#### Success Response (N/A)
N/A

## home_settings_update

### Description
The guild’s server guide was updated.

### Method
N/A (Event-based)

### Endpoint
N/A

### Response
#### Success Response (N/A)
N/A
```

--------------------------------

### Define a Cog with Commands and Listeners

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html

This example shows how to create a cog class that includes both a command and an event listener. Ensure the bot instance is passed during initialization to access its attributes and methods.

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

### Creating a SyncWebhook

Source: https://discordpy.readthedocs.io/en/latest/api.html

Demonstrates how to create a SyncWebhook instance using either a URL or by providing the webhook ID and token.

```APIDOC
## Creating a SyncWebhook

### `clsSyncWebhook.from_url(url, *, session=None, bot_token=None)`

Creates a partial `SyncWebhook` from a webhook URL.

**Parameters**
- `url` (str) - The URL of the webhook.
- `session` (requests.Session, optional) - The session to use for requests.
- `bot_token` (Optional[str], optional) - The bot authentication token for authenticated requests.

**Raises**
- `ValueError` - The URL is invalid.

### `clsSyncWebhook.partial(id, token, *, session=None, bot_token=None)`

Creates a partial `SyncWebhook`.

**Parameters**
- `id` (int) - The ID of the webhook.
- `token` (str) - The authentication token of the webhook.
- `session` (requests.Session, optional) - The session to use for requests.
- `bot_token` (Optional[str], optional) - The bot authentication token for authenticated requests.

**Returns**
A partial `SyncWebhook` object.
```

--------------------------------

### Get Resolved Message from Reference

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Access MessageReference.resolved to get the fully resolved message object that the reference points to.

```python
resolved_message = message_reference.resolved
```

--------------------------------

### Help Command Preparation and Callback

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Methods related to preparing the help command before execution and the main callback.

```APIDOC
## _await _prepare_help_command(_ctx_ , _command =None_, _/_)

### Description
A low level method that can be used to prepare the help command before it does anything. For example, if you need to prepare some state in your subclass before the command does its processing then this would be the place to do it. The default implementation does nothing.

Note
This is called _inside_ the help command callback body. So all the usual rules that happen inside apply here as well.
Changed in version 2.0: `ctx` and `command` parameters are now positional-only.

### Parameters
#### Path Parameters
- **ctx** (`Context`) – The invocation context.
- **command** (Optional[`str`]) – The argument passed to the help command.
```

```APIDOC
## _await _command_callback(_ctx_ , _/_ , _*_ , _command =None_)

### Description
The actual implementation of the help command. It is not recommended to override this method and instead change the behaviour through the methods that actually get dispatched.
  * `send_bot_help()`
  * `send_cog_help()`
  * `send_group_help()`
  * `send_command_help()`
  * `get_destination()`
  * `command_not_found()`
  * `subcommand_not_found()`
  * `send_error_message()`
  * `on_help_command_error()`
  * `prepare_help_command()`

Changed in version 2.0: `ctx` parameter is now positional-only.
```

--------------------------------

### Retrieve Entitlements

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Examples for iterating over or collecting entitlements using the client.entitlements method.

```python
async for entitlement in client.entitlements(limit=100):
    print(entitlement.user_id, entitlement.ends_at)
```

```python
entitlements = [entitlement async for entitlement in client.entitlements(limit=100)]
```

--------------------------------

### fetch_session_start_limits Method

Source: https://discordpy.readthedocs.io/en/latest/api.html

Fetches the session start limits for the gateway. Useful for advanced sharding configurations.

```APIDOC
## fetch_session_start_limits Method

### Description
This function is a _coroutine_.
Get the session start limits.
This is not typically needed, and will be handled for you by default. At the point where you are launching multiple instances with manual shard ranges and are considered required to use large bot sharding by Discord, this function when used along IPC and a before_identity_hook can speed up session start.
New in version 2.5.

### Returns
A class containing the session start limits

### Return Type
`SessionStartLimits`

### Raises
- **GatewayNotFound** – The gateway was unreachable
```

--------------------------------

### OnboardingPromptOption

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents an option for an onboarding prompt in a Discord guild. This can be manually created for Guild.edit_onboarding().

```APIDOC
## OnboardingPromptOption

### Description
Represents a onboarding prompt option.
This can be manually created for `Guild.edit_onboarding()`.
New in version 2.6.

### Attributes
- **channel_ids** (Set[`int`]) - The IDs of the channels the user will be added to if this option is selected.
- **channels** (List[Union[`abc.GuildChannel`, `Thread`]]) - The list of channels which will be made visible if this option is selected. Raises `ValueError` if the prompt option is manually created.
- **description** (Optional[`str`]) - The description of this prompt option.
- **emoji** (Optional[Union[`Emoji`, `PartialEmoji`]]) - The emoji tied to this option. May be a custom emoji, or a unicode emoji.
- **guild** (`Guild`) - The guild this prompt option is related to. Raises `ValueError` if the prompt option was created manually.
- **id** (`int`) - The ID of this prompt option. If this was manually created then the ID will be `0`.
- **role_ids** (Set[`int`]) - The IDs of the roles the user will be given if this option is selected.
- **roles** (List[`Role`]) - The list of roles given to the user if this option is selected. Raises `ValueError` if the prompt option is manually created.
- **title** (`str`) - The title of this prompt option.

### Parameters
- **title** (`str`) - The title of this prompt option.
- **emoji** (Union[`Emoji`, `PartialEmoji`, `str`]) - The emoji tied to this option. May be a custom emoji, or a unicode emoji. I f this is a string, it will be converted to a `PartialEmoji`.
- **description** (Optional[`str`]) - The description of this prompt option.
- **channels** (Iterable[Union[`abc.Snowflake`, `int`]]) - The channels the user will be added to if this option is selected.
- **roles** (Iterable[Union[`abc.Snowflake`, `int`]]) - The roles the user will be given if this option is selected.
```

--------------------------------

### GET /application_info

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves the bot's application information.

```APIDOC
## GET /application_info

### Description
Retrieves the bot’s application information.

### Method
GET

### Response
#### Success Response (200)
- **AppInfo** (object) - The bot’s application information.

### Errors
- **HTTPException**: Retrieving the information failed.
```

--------------------------------

### Get Bot's Self Role

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Use Guild.self_role to get the role that the bot automatically manages for itself on the server, if it exists.

```python
bot_role = guild.self_role
```

--------------------------------

### OnboardingPrompt

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents an onboarding prompt within a Discord guild. This can be manually created for Guild.edit_onboarding().

```APIDOC
## OnboardingPrompt

### Description
Represents a onboarding prompt.
This can be manually created for `Guild.edit_onboarding()`.
New in version 2.6.

### Attributes
- **guild** (`Guild`) - The guild this prompt is related to. Raises `ValueError` if the prompt was created manually.
- **id** (`int`) - The ID of this prompt. If this was manually created then the ID will be `0`.
- **in_onboarding** (`bool`) - Whether this prompt is in the onboarding flow. Defaults to `True`.
- **options** (List[`OnboardingPromptOption`]) - The options of this prompt.
- **required** (`bool`) - Whether this prompt is required. Defaults to `True`.
- **single_select** (`bool`) - Whether this prompt is single select. Defaults to `True`.
- **title** (`str`) - The title of this prompt.
- **type** (`OnboardingPromptType`) - The type of this prompt.

### Methods
- **get_option**(_option_id_ , _/_) - Optional[`OnboardingPromptOption`]: The option with the given ID, if found.
```

--------------------------------

### GET /guild/stickers

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of all stickers for the guild.

```APIDOC
## GET /guild/stickers

### Description
Retrieves a list of all stickers for the guild.

### Response
- **List[GuildSticker]** - The retrieved stickers.
```

--------------------------------

### Bot UI Kit Introduction

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Introduction to the discord.ui package for creating component-based UIs.

```APIDOC
## Bot UI Kit

The library has helpers to aid in creating component-based UIs. These are all in the `discord.ui` package.
```

--------------------------------

### Implement Custom HelpCommand in a Cog

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Example of subclassing MinimalHelpCommand and binding it to a Cog to dynamically manage help command behavior.

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

### GET /roles

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves all roles associated with the guild.

```APIDOC
## GET /roles

### Description
Retrieves all roles that the guild has.

### Method
GET

### Endpoint
/roles

### Response
#### Success Response (200)
- **roles** (List[Role]) - All roles in the guild.

#### Errors
- **HTTPException** - Retrieving the roles failed.
```

--------------------------------

### GET /skus

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the bot's available SKUs.

```APIDOC
## GET /skus

### Description
Returns the bot’s available SKUs.

### Method
GET

### Response
#### Success Response (200)
- **List[SKU]** (array) - A list of available SKU objects.
```

--------------------------------

### Iterate over Discord Intents

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Example showing how to map intent names to their values using the discord.Intents.all() method.

```python
friendly_names = {
    ...,
    'emojis_and_stickers': 'Emojis Intent',
    ...,
}
for name, value in discord.Intents.all():
    print(f'{friendly_names[name]}: {value}')
```

--------------------------------

### Run Client with asyncio.run

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates using asyncio.run to manage the event loop instead of the traditional Client.run method.

```python
client = discord.Client()

async def main():
    # do other async things
    await my_async_function()

    # start the client
    async with client:
        await client.start(TOKEN)

asyncio.run(main())
```

--------------------------------

### get_command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Get a Command from the internal list of commands.

```APIDOC
## get_command

### Description
Get a Command from the internal list of commands, including aliases.

### Parameters
#### Path Parameters
- **name** (str) - Required - The name of the command to get.

### Response
#### Success Response (200)
- **command** (Optional[Command]) - The command requested or None.
```

--------------------------------

### Define Command Choices with discord.py

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Use `app_commands.describe` and `app_commands.choices` to provide predefined options for command parameters. This example shows how to define choices for a 'fruits' parameter.

```python
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

### GET /guild/integrations

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns a list of all integrations attached to the guild.

```APIDOC
## GET /guild/integrations

### Description
Returns a list of all integrations attached to the guild. Requires manage_guild permission.

### Response
- **List[Integration]** - The list of integrations that are attached to the guild.
```

--------------------------------

### MinimalHelpCommand Methods

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Key methods for customizing the output and behavior of the help command.

```APIDOC
## MinimalHelpCommand Methods

### send_pages()
- **Description**: A coroutine that sends the page output from the paginator to the destination.

### get_command_signature(command)
- **Description**: Retrieves the signature portion of the help page.
- **Parameters**:
  - **command** (Command) - Required - The command to get the signature of.

### add_bot_commands_formatting(commands, heading)
- **Description**: Adds the minified bot heading with commands to the output.
- **Parameters**:
  - **commands** (Sequence[Command]) - Required - A list of commands that belong to the heading.
  - **heading** (str) - Required - The heading to add to the line.

### add_subcommand_formatting(command)
- **Description**: Adds formatting information on a subcommand.
- **Parameters**:
  - **command** (Command) - Required - The command to show information of.

### add_aliases_formatting(aliases)
- **Description**: Adds the formatting information on a command’s aliases.
- **Parameters**:
  - **aliases** (Sequence[str]) - Required - A list of aliases to format.
```

--------------------------------

### Fetch guilds with limit

Source: https://discordpy.readthedocs.io/en/latest/api.html

This example shows how to iterate over guilds the bot is in using `client.fetch_guilds`. Note that this method only retrieves partial guild information and is an API call.

```python
import discord

client = discord.Client()

async for guild in client.fetch_guilds(limit=150):
    print(guild.name)

```

--------------------------------

### Iterate Intents Configuration

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Example showing how to iterate through discord.Intents instances, noting that changes to attribute aliases may affect existing iteration logic.

```python
# before
friendly_names = {
    ...,
    'emojis': 'Emojis Intent',
    ...,
}
for name, value in discord.Intents.all():
    print(f'{friendly_names[name]}: {value}')
```

--------------------------------

### GET /guild/members/query

Source: https://discordpy.readthedocs.io/en/latest/api.html

Queries members by username or nickname.

```APIDOC
## GET /guild/members/query

### Description
Request members of this guild whose username or nickname starts with the given query.

### Parameters
#### Query Parameters
- **query** (str) - Optional - The string to search for.
- **limit** (int) - Optional - Max members to return (5-100).
- **presences** (bool) - Optional - Whether to request presences.
- **cache** (bool) - Optional - Whether to cache members internally.
- **user_ids** (List[int]) - Optional - List of user IDs to search for.

### Response
#### Success Response (200)
- **List[Member]** (Array) - The list of members that matched the query.

### Errors
- **asyncio.TimeoutError** - The query timed out.
- **ValueError** - Invalid parameters.
- **ClientException** - Presences intent not enabled.
```

--------------------------------

### Client Initialization

Source: https://discordpy.readthedocs.io/en/latest/api.html

Initializes a new discord.Client instance with specific configuration options.

```APIDOC
## Client Initialization

### Description
Initializes the client connection to Discord. This class is used to interact with the Discord WebSocket and API.

### Parameters
- **intents** (Intents) - Required - The intents that you want to enable for the session.
- **max_messages** (Optional[int]) - Optional - The maximum number of messages to store in the internal message cache. Defaults to 1000.
- **proxy** (Optional[str]) - Optional - Proxy URL.
- **shard_id** (Optional[int]) - Optional - Integer starting at 0 and less than shard_count.
- **shard_count** (Optional[int]) - Optional - The total number of shards.
- **application_id** (int) - Optional - The client’s application ID.
- **status** (Optional[Status]) - Optional - A status to start your presence with.
- **activity** (Optional[BaseActivity]) - Optional - An activity to start your presence with.
- **heartbeat_timeout** (float) - Optional - The maximum number of seconds before timing out and restarting the WebSocket. Defaults to 60 seconds.
```

--------------------------------

### Define a LayoutView with an ActionRow

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Example of subclassing LayoutView and adding a button to an ActionRow using a decorator.

```python
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

### GET /webhooks

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of webhooks associated with the channel.

```APIDOC
## GET /webhooks

### Description
Gets the list of webhooks from this channel. Requires `manage_webhooks` permission.

### Response
#### Success Response (200)
- **webhooks** (List[Webhook]) - The webhooks for this channel.
```

--------------------------------

### Using a constructed custom converter

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Demonstrates how to use a custom converter by constructing its instance, which is equivalent to using it directly.

```python
@bot.command()
async def slap(ctx, *, reason: Slapper()): # Equivalent to Slapper
    await ctx.send(reason)

```

--------------------------------

### GET /emojis

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves all custom emojis from the guild.

```APIDOC
## GET /emojis

### Description
Retrieves all custom Emoji objects from the guild.

### Method
GET

### Endpoint
/emojis

### Response
#### Success Response (200)
- **emojis** (List[Emoji]) - The retrieved emojis.

#### Errors
- **HTTPException** - An error occurred fetching the emojis.
```

--------------------------------

### Select Menus Introduction

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Introduction to the select menu classes provided by the library.

```APIDOC
## Select Menus

### Description
The library provides classes to help create the different types of select menus.
```

--------------------------------

### GET /guild/stickers/{sticker_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a custom sticker from the guild.

```APIDOC
## GET /guild/stickers/{sticker_id}

### Description
Retrieves a custom sticker from the guild.

### Parameters
#### Path Parameters
- **sticker_id** (int) - Required - The sticker’s ID.

### Response
- **GuildSticker** - The retrieved sticker.
```

--------------------------------

### GET /soundboard_sound/{sound_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a soundboard sound by its ID.

```APIDOC
## GET /soundboard_sound/{sound_id}

### Description
Returns a soundboard sound with the given ID.

### Method
GET

### Endpoint
/soundboard_sound/{sound_id}

### Parameters
#### Path Parameters
- **sound_id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **SoundboardSound** (Optional[SoundboardSound]) - The soundboard sound or None if not found.
```

--------------------------------

### WelcomeScreen Class

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents a Guild welcome screen with attributes for description, enabled status, and welcome channels. Includes a method to edit the welcome screen.

```APIDOC
## WelcomeScreen Class

### Description
Represents a `Guild` welcome screen.
New in version 2.0.

### Attributes
- **description** (str) - The description shown on the welcome screen.
- **welcome_channels** (List[WelcomeChannel]) - The channels shown on the welcome screen.
- **enabled** (bool) - Whether the welcome screen is displayed. This is equivalent to checking if `WELCOME_SCREEN_ENABLED` is present in `Guild.features`.

### Methods
#### async edit(_description: Optional[str], welcome_channels: Optional[List[WelcomeChannel]], enabled: Optional[bool], reason: Optional[str] = None_)

This is a coroutine.
Edit the welcome screen.
Welcome channels can only accept custom emojis if `Guild.premium_tier` is level 2 or above.
You must have `manage_guild` in the guild to do this.

**Parameters**
- **description** (Optional[str]) - The welcome screen’s description.
- **welcome_channels** (Optional[List[WelcomeChannel]]) - The welcome channels, in their respective order.
- **enabled** (Optional[bool]) - Whether the welcome screen should be displayed.
- **reason** (Optional[str]) - The reason for editing the welcome screen. Shows up on the audit log.

**Raises**
- HTTPException: Editing the welcome screen failed.
- Forbidden: You don’t have permissions to edit the welcome screen.
- NotFound: This welcome screen does not exist.

### Request Example
```python
rules_channel = guild.get_channel(12345678)
announcements_channel = guild.get_channel(87654321)

custom_emoji = utils.get(guild.emojis, name='loudspeaker')

await welcome_screen.edit(
    description='This is a very cool community server!',
    welcome_channels=[
        WelcomeChannel(channel=rules_channel, description='Read the rules!', emoji='👨‍🏫'),
        WelcomeChannel(channel=announcements_channel, description='Watch out for announcements!', emoji=custom_emoji),
    ]
)
```
```

--------------------------------

### GET /get_user

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a user from the cache by their ID.

```APIDOC
## GET get_user(id)

### Description
Returns a user with the given ID from the internal cache.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID to search for.

### Response
- **Returns** (Optional[User]) - The user or None if not found.
```

--------------------------------

### Voice Connection and Playback (After)

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Demonstrates the current method for connecting to a voice channel and playing audio using `VoiceClient.play()` with `discord.FFmpegPCMAudio`. This is the recommended approach.

```python
vc = await channel.connect()
vc.play(discord.FFmpegPCMAudio('testing.mp3'), after=lambda e: print('done', e))
vc.is_playing()
vc.pause()
vc.resume()
vc.stop()
```

--------------------------------

### Custom Flag Syntax: Windows-like

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Configure the flag syntax with custom delimiters and prefixes. This example uses no delimiter and '/' as a prefix.

```python
# /make food
class WindowsLikeFlags(commands.FlagConverter, prefix='/', delimiter=''):
    make: str

```

--------------------------------

### GET /stage_instance/{stage_instance_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a stage instance by its ID.

```APIDOC
## GET /stage_instance/{stage_instance_id}

### Description
Returns a stage instance with the given ID.

### Method
GET

### Endpoint
/stage_instance/{stage_instance_id}

### Parameters
#### Path Parameters
- **stage_instance_id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **StageInstance** (Optional[StageInstance]) - The stage instance or None if not found.
```

--------------------------------

### GET /get_command

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Retrieves a specific application command from the tree.

```APIDOC
## GET /get_command

### Description
Gets an application command from the tree.

### Method
GET

### Parameters
#### Query Parameters
- **command** (str) - Required - The name of the root command to get.
- **guild** (Snowflake) - Optional - The guild to get the command from. If None, gets a global command.
- **type** (AppCommandType) - Optional - The type of command to get. Defaults to chat_input.

### Response
#### Success Response (200)
- **command** (Optional[Union[Command, ContextMenu, Group]]) - The found command, or None if not found.
```

--------------------------------

### Get Channel Mention

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns the string that allows you to mention the channel.

```APIDOC
## GET /channels/{channel.id}/mention

### Description
Returns the string that allows you to mention the channel.

### Method
GET

### Endpoint
`/channels/{channel.id}/mention`

### Response
#### Success Response (200)
- **str** - The mention string for the channel.
```

--------------------------------

### Set command as guild-installed

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Use this decorator to indicate that the command should be installed in guilds.

```python
@app_commands.command()
@app_commands.guild_install()
async def my_guild_install_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in guilds by default!')
```

--------------------------------

### GET /get_guild

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a guild from the cache by its ID.

```APIDOC
## GET get_guild(id)

### Description
Returns a guild with the given ID from the internal cache.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID to search for.

### Response
- **Returns** (Optional[Guild]) - The guild or None if not found.
```

--------------------------------

### Onboarding API

Source: https://discordpy.readthedocs.io/en/latest/api.html

Functions for fetching and editing onboarding configurations.

```APIDOC
## GET /api/guilds/{guild.id}/onboarding

### Description
Fetches the onboarding configuration for this guild.

### Method
GET

### Endpoint
/api/guilds/{guild.id}/onboarding

### Parameters
#### Path Parameters
- **guild.id** (snowflake) - Required - The ID of the guild to fetch the onboarding configuration for.

### Response
#### Success Response (200)
- **Onboarding** - The onboarding configuration that was fetched.
```

```APIDOC
## PATCH /api/guilds/{guild.id}/onboarding

### Description
Edits the onboarding configuration for this guild.

### Method
PATCH

### Endpoint
/api/guilds/{guild.id}/onboarding

### Parameters
#### Path Parameters
- **guild.id** (snowflake) - Required - The ID of the guild to edit the onboarding configuration for.

#### Request Body
- **prompts** (List[OnboardingPrompt]) - Optional - The prompts for the onboarding configuration.
- **default_channels** (List[Snowflake]) - Optional - The default channels for the onboarding configuration.
- **enabled** (bool) - Optional - Whether the onboarding configuration is enabled.
- **mode** (OnboardingMode) - Optional - The mode of the onboarding configuration.
- **reason** (str) - Optional - The reason for editing the onboarding configuration. Shows up on the audit log.
```

--------------------------------

### GET /message-reference

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a message reference from the current message.

```APIDOC
## GET /message-reference

### Description
Creates a `MessageReference` from the current message.

### Method
GET

### Parameters
#### Query Parameters
- **fail_if_not_exists** (bool) - Optional - Whether the referenced message should raise `HTTPException` if the message no longer exists.
- **type** (MessageReferenceType) - Optional - The type of message reference.

### Response
#### Success Response (200)
- **reference** (MessageReference) - The reference to this message.
```

--------------------------------

### GET /guilds/{guild_id}

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a guild by its ID.

```APIDOC
## GET /guilds/{guild_id}

### Description
Retrieves a Guild from an ID.

### Parameters
#### Path Parameters
- **guild_id** (int) - Required - The guild's ID to fetch.

#### Query Parameters
- **with_counts** (bool) - Optional - Whether to include count information. Defaults to True.

### Response
#### Success Response (200)
- **Guild** (Object) - The guild from the ID.
```

--------------------------------

### GET /entitlements

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a list of entitlements for the current application.

```APIDOC
## GET /entitlements

### Description
Retrieves a list of entitlements for the current application. All parameters are optional.

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of entitlements to retrieve. Defaults to 100.
- **before** (Snowflake/datetime) - Optional - Retrieve entitlements before this date or entitlement.
- **after** (Snowflake/datetime) - Optional - Retrieve entitlements after this date or entitlement.
- **skus** (Sequence[Snowflake]) - Optional - A list of SKUs to filter by.
- **user** (Snowflake) - Optional - The user to filter by.
- **guild** (Snowflake) - Optional - The guild to filter by.
- **exclude_ended** (bool) - Optional - Whether to exclude ended entitlements. Defaults to False.
- **exclude_deleted** (bool) - Optional - Whether to exclude deleted entitlements. Defaults to True.

### Response
#### Success Response (200)
- **Entitlement** (Object) - The entitlement with the application.
```

--------------------------------

### Create and use a Webhook from a URL

Source: https://discordpy.readthedocs.io/en/latest/api.html

Initializes a webhook using a URL and an aiohttp session to send a message.

```python
from discord import Webhook
import aiohttp

async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('url-here', session=session)
        await webhook.send('Hello World', username='Foo')
```

--------------------------------

### GET /channels/{channel_id}

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a channel by its ID.

```APIDOC
## GET /channels/{channel_id}

### Description
Retrieves a GuildChannel, PrivateChannel, or Thread with the specified ID.

### Parameters
#### Path Parameters
- **channel_id** (int) - Required - The channel ID to fetch.

### Response
#### Success Response (200)
- **Channel** (Union[abc.GuildChannel, abc.PrivateChannel, Thread]) - The channel from the ID.
```

--------------------------------

### GET /application/emojis

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves all emojis associated with the current application.

```APIDOC
## GET /application/emojis

### Description
Retrieves all emojis for the current application.

### Method
GET

### Response
#### Success Response (200)
- **List[Emoji]** (array) - The list of emojis for the current application.
```

--------------------------------

### Greedy Argument Conversion Example

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Demonstrates how to use the Greedy converter to consume multiple arguments until a specific condition is met. This is useful for capturing a variable number of inputs before a final, distinct argument.

```Python
content_copy```
@commands.command()
async def test(ctx, numbers: Greedy[int], reason: str):
    await ctx.send("numbers: {}, reason: {}".format(numbers, reason))

```
```

--------------------------------

### GET /fetch_rule

Source: https://discordpy.readthedocs.io/en/latest/api.html

Fetches the rule associated with the executed action.

```APIDOC
## GET /fetch_rule

### Description
Fetches the rule whose action was taken. Requires `Permissions.manage_guild`.

### Returns
- **AutoModRule** - The rule that was executed.

### Errors
- **Forbidden**: You do not have permissions to view the rule.
- **HTTPException**: Fetching the rule failed.
```

--------------------------------

### GET /entitlements

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an asynchronous iterator of entitlements for the application.

```APIDOC
## GET /entitlements

### Description
Retrieves an asynchronous iterator of the `Entitlement` objects that the application has.

### Method
GET

### Parameters
#### Query Parameters
- **limit** (int) - Optional - Default 100
- **before** (int) - Optional
- **after** (int) - Optional
- **skus** (list) - Optional
- **user** (int) - Optional
- **guild** (int) - Optional
- **exclude_ended** (bool) - Optional - Default False
- **exclude_deleted** (bool) - Optional - Default True

### Request Example
```python
async for entitlement in client.entitlements(limit=100):
    print(entitlement.user_id, entitlement.ends_at)
```
```

--------------------------------

### GET /fetch_thread

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the public thread attached to a message.

```APIDOC
## GET /fetch_thread

### Description
Retrieves the public thread attached to this message.

### Response
#### Success Response (200)
- **Thread** (object) - The public thread attached to this message.
```

--------------------------------

### TextChannel Typing Indicator

Source: https://discordpy.readthedocs.io/en/latest/api.html

Example of using the typing indicator context manager.

```APIDOC
## TextChannel Typing Indicator

### Description
Allows sending a typing indicator to the channel.

### Example Usage
```python
async with channel.typing():
    # simulate something heavy
    await asyncio.sleep(20)

await channel.send('Done!')
```

### Alternative Usage
```python
await channel.typing()
```
```

--------------------------------

### Client Properties and Methods

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Information on accessing client-related data such as sounds, status, stickers, user information, and voice clients, along with methods for starting the client and unloading extensions.

```APIDOC
## _soundboard_sounds Property

### Description
The soundboard sounds that the connected client has.

New in version 2.5.

### Type
`List[SoundboardSound]`

### Endpoint
N/A (Property access)

### Response Example
```python
# Assuming 'bot' is your Bot instance:
# sounds = bot.soundboard_sounds
```
```

```APIDOC
## _start(_token_, **kwargs, reconnect=True) Coroutine

### Description
A shorthand coroutine for `login()` + `connect()`.

### Parameters
* **`token`** (`str`) - The authentication token. Do not prefix this token with anything as the library will do it for you.
* **`reconnect`** (`bool`) - If we should attempt reconnecting, either due to internet failure or a specific failure on Discord’s part. Certain disconnects that lead to bad state will not be handled (such as invalid sharding payloads or bad tokens).

### Raises
* **`TypeError`** - An unexpected keyword argument was received.

### Method
`async def _start(token, **kwargs, reconnect=True)`

### Endpoint
N/A (Internal method)

### Request Example
```python
# Example usage:
# await bot._start('YOUR_BOT_TOKEN')
```

### Response
Initiates bot login and connection.
```

```APIDOC
## _status Property

### Description
The status being used upon logging on to Discord.

### Type
`Status`

### Endpoint
N/A (Property access)

### Response Example
```python
# Assuming 'bot' is your Bot instance:
# current_status = bot.status
```
```

```APIDOC
## _stickers Property

### Description
The stickers that the connected client has.

New in version 2.0.

### Type
`Sequence[GuildSticker]`

### Endpoint
N/A (Property access)

### Response Example
```python
# Assuming 'bot' is your Bot instance:
# stickers = bot.stickers
```
```

```APIDOC
## _tree Property

### Description
The command tree responsible for handling the application commands in this bot.

New in version 2.0.

### Type
`CommandTree`

### Endpoint
N/A (Property access)

### Response Example
```python
# Assuming 'bot' is your Bot instance:
# command_tree = bot.tree
```
```

```APIDOC
## _unload_extension(_name_, **kwargs, package=None) Coroutine

### Description
Unloads an extension. When the extension is unloaded, all commands, listeners, and cogs are removed from the bot and the module is un-imported. The extension can provide an optional global function, `teardown`, to do miscellaneous clean-up if necessary. This function takes a single parameter, the `bot`, similar to `setup` from `load_extension()`.

Changed in version 2.0: This method is now a coroutine.

### Parameters
* **`name`** (`str`) - The extension name to unload. It must be dot separated like regular Python imports if accessing a sub-module. e.g. `foo.test` if you want to import `foo/test.py`.
* **`package`** (Optional[`str`]) - The package name to resolve relative imports with. This is required when unloading an extension using a relative path, e.g `.foo.test`. Defaults to `None`.

### Raises
* **`ExtensionNotFound`** - The name of the extension could not be resolved using the provided `package` parameter.
* **`ExtensionNotLoaded`** - The extension was not loaded.

### Method
`async def _unload_extension(name, **kwargs, package=None)`

### Endpoint
N/A (Internal method)

### Request Example
```python
# Example usage:
# await bot._unload_extension('my_extension')
```

### Response
Unloads the specified extension.
```

```APIDOC
## _user Property

### Description
Represents the connected client. `None` if not logged in.

### Type
Optional[`ClientUser`]

### Endpoint
N/A (Property access)

### Response Example
```python
# Assuming 'bot' is your Bot instance:
# current_user = bot.user
```
```

```APIDOC
## _users Property

### Description
Returns a list of all the users the bot can see.

### Type
`List[User]`

### Endpoint
N/A (Property access)

### Response Example
```python
# Assuming 'bot' is your Bot instance:
# all_users = bot.users
```
```

```APIDOC
## _voice_clients Property

### Description
Represents a list of voice connections. These are usually `VoiceClient` instances.

### Type
`List[VoiceProtocol]`

### Endpoint
N/A (Property access)

### Response Example
```python
# Assuming 'bot' is your Bot instance:
# voice_connections = bot.voice_clients
```
```

--------------------------------

### GET /pins

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of pinned messages from a channel.

```APIDOC
## GET /pins

### Description
Retrieves pinned messages from the channel. Returns a list of Message objects.

### Method
GET

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of pinned messages to retrieve. Defaults to 50.
- **before** (datetime.datetime or abc.Snowflake) - Optional - Retrieve pinned messages before this time or snowflake.
- **oldest_first** (bool) - Optional - If True, return messages in oldest to newest order. Defaults to False.

### Response
#### Success Response (200)
- **Message** (Object) - The pinned message with pinned_at set.
```

--------------------------------

### Onboarding Actions

Source: https://discordpy.readthedocs.io/en/latest/api.html

Audit log entries for the creation, update, and deletion of guild onboarding prompts and configurations.

```APIDOC
## onboarding_prompt_create

### Description
A guild onboarding prompt was created.

### Method
N/A (Event-based)

### Endpoint
N/A

### Parameters
#### Target
- **ID** (`Object`) - The ID of the prompt that the options belong to.
#### AuditLogDiff Attributes
- **type** (string) - The type of the onboarding prompt.
- **title** (string) - The title of the onboarding prompt.
- **options** (array) - The options for the onboarding prompt.
- **single_select** (boolean) - Whether the prompt is single select.
- **required** (boolean) - Whether the prompt is required.
- **in_onboarding** (boolean) - Whether the prompt is in the onboarding flow.

### Response
#### Success Response (N/A)
N/A

## onboarding_prompt_update

### Description
A guild onboarding prompt was updated.

### Method
N/A (Event-based)

### Endpoint
N/A

### Parameters
#### Target
- **ID** (`Object`) - The ID of the prompt that the options belong to.
#### AuditLogDiff Attributes
- **type** (string) - The type of the onboarding prompt.
- **title** (string) - The title of the onboarding prompt.
- **options** (array) - The options for the onboarding prompt.
- **single_select** (boolean) - Whether the prompt is single select.
- **required** (boolean) - Whether the prompt is required.
- **in_onboarding** (boolean) - Whether the prompt is in the onboarding flow.

### Response
#### Success Response (N/A)
N/A

## onboarding_prompt_delete

### Description
A guild onboarding prompt was deleted.

### Method
N/A (Event-based)

### Endpoint
N/A

### Parameters
#### Target
- **ID** (`Object`) - The ID of the prompt that the options belong to.
#### AuditLogDiff Attributes
- **type** (string) - The type of the onboarding prompt.
- **title** (string) - The title of the onboarding prompt.
- **options** (array) - The options for the onboarding prompt.
- **single_select** (boolean) - Whether the prompt is single select.
- **required** (boolean) - Whether the prompt is required.
- **in_onboarding** (boolean) - Whether the prompt is in the onboarding flow.

### Response
#### Success Response (N/A)
N/A

## onboarding_create

### Description
The guild’s onboarding configuration was created.

### Method
N/A (Event-based)

### Endpoint
N/A

### Parameters
#### Target
- **None** (`None`) - Target is always None.
#### Guild Access
- **guild** (`Guild`) - Access the guild object.
#### AuditLogDiff Attributes
- **enabled** (boolean) - Whether onboarding is enabled.
- **default_channels** (array) - The default channels for onboarding.
- **prompts** (array) - The prompts for onboarding.
- **mode** (string) - The mode of onboarding.

### Response
#### Success Response (N/A)
N/A

## onboarding_update

### Description
The guild’s onboarding configuration was updated.

### Method
N/A (Event-based)

### Endpoint
N/A

### Parameters
#### Target
- **None** (`None`) - Target is always None.
#### Guild Access
- **guild** (`Guild`) - Access the guild object.
#### AuditLogDiff Attributes
- **enabled** (boolean) - Whether onboarding is enabled.
- **default_channels** (array) - The default channels for onboarding.
- **prompts** (array) - The prompts for onboarding.
- **mode** (string) - The mode of onboarding.

### Response
#### Success Response (N/A)
N/A
```

--------------------------------

### Wait for reaction event

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Example of using client.wait_for to handle a specific reaction from a user with a timeout.

```python
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')
```

--------------------------------

### GET /role_member_counts

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a mapping of roles to the number of members that have them.

```APIDOC
## GET /role_member_counts

### Description
Retrieves a mapping of roles to the number of members that have it. Requires 'manage_roles' permission.

### Response
#### Success Response (200)
- **mapping** (Dict[Union[Object, Role], int]) - Mapping of roles to member counts.
```

--------------------------------

### GET /stickers/{sticker_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves sticker information by ID.

```APIDOC
## GET /stickers/{sticker_id}

### Description
Retrieves a Sticker with the specified ID.

### Method
GET

### Endpoint
/stickers/{sticker_id}

### Parameters
#### Path Parameters
- **sticker_id** (int) - Required - The ID of the sticker.

### Response
#### Success Response (200)
- **Sticker** (Union[StandardSticker, GuildSticker]) - The sticker you requested.
```

--------------------------------

### Define a LayoutView with a Container

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Demonstrates how to subclass ui.LayoutView and define a container with text content.

```python
class MyView(ui.LayoutView):
    container = ui.Container(ui.TextDisplay('I am a text display on a container!'))
    # or you can use your subclass:
    # container = MyContainer()
```

--------------------------------

### GET /guild/scheduled-events/{scheduled_event_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a scheduled event from the guild.

```APIDOC
## GET /guild/scheduled-events/{scheduled_event_id}

### Description
Retrieves a scheduled event from the guild.

### Parameters
#### Path Parameters
- **scheduled_event_id** (int) - Required - The scheduled event ID.
#### Query Parameters
- **with_counts** (bool) - Optional - Whether to include the number of users that are subscribed to the event. Defaults to True.

### Response
- **ScheduledEvent** - The scheduled event.
```

--------------------------------

### Compare Async Webhook Usage

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the change in how asynchronous webhooks are initialized, moving from an explicit adapter to a direct session parameter.

```python
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

### GET /guild/scheduled-events

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of all scheduled events for the guild.

```APIDOC
## GET /guild/scheduled-events

### Description
Retrieves a list of all scheduled events for the guild.

### Parameters
#### Query Parameters
- **with_counts** (bool) - Optional - Whether to include the number of users that are subscribed to the event. Defaults to True.

### Response
- **List[ScheduledEvent]** - The scheduled events.
```

--------------------------------

### GET /fetch_guilds

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of guilds the client has access to.

```APIDOC
## GET /fetch_guilds

### Description
Retrieves a list of guilds the client has access to.

### Query Parameters
- **limit** (int) - Optional - The number of guilds to retrieve. Defaults to 200.
- **before** (Union[abc.Snowflake, datetime.datetime]) - Optional - Retrieves guilds before this date or object.
- **after** (Union[abc.Snowflake, datetime.datetime]) - Optional - Retrieves guilds after this date or object.
- **with_counts** (bool) - Optional - Whether to include count information. Defaults to True.

### Response
- **Guild** - The guild with the guild data parsed.
```

--------------------------------

### Create Instant Invite API

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates an instant invite from a text or voice channel. Requires `create_instant_invite` permission.

```APIDOC
## POST /channels/{channel.id}/invites

### Description
Creates an instant invite for a given channel. Requires the `create_instant_invite` permission.

### Method
POST

### Endpoint
`/channels/{channel.id}/invites`

### Parameters
#### Path Parameters
- **channel.id** (snowflake) - Required - The ID of the channel to create an invite for.

#### Query Parameters
None

#### Request Body
- **max_age** (int) - Optional - The duration (in seconds) the invite should last. Defaults to 0 (never expires).
- **max_uses** (int) - Optional - The maximum number of times the invite can be used. Defaults to 0 (unlimited).
- **temporary** (bool) - Optional - Whether the invite grants temporary membership. Defaults to `False`.
- **unique** (bool) - Optional - Whether to ensure the invite is unique. Defaults to `True`.
- **target_type** (str) - Optional - The type of target for the invite (e.g., `stream`).
- **target_user** (User) - Optional - The user to invite (requires `target_type` to be `user`).
- **target_application_id** (snowflake) - Optional - The ID of the application to invite.
- **guest** (bool) - Optional - Whether to create a guest invite. Defaults to `False`.
- **reason** (str) - Optional - The reason for creating the invite, shown in the audit log.

### Request Example
```json
{
  "max_age": 86400,
  "max_uses": 5,
  "temporary": true,
  "reason": "Invite for a temporary event"
}
```

### Response
#### Success Response (200)
- **invite** (Invite) - The created invite object.

#### Response Example
```json
{
  "code": "EXAMPLECODE",
  "guild": {
    "id": "GUILD_ID",
    "name": "Example Guild"
  },
  "channel": {
    "id": "CHANNEL_ID",
    "name": "example-channel"
  },
  "inviter": {
    "username": "ExampleUser",
    "discriminator": "1234",
    "id": "USER_ID"
  },
  "target_type": null,
  "target_user": null,
  "uses": 0,
  "max_uses": 5,
  "max_age": 86400,
  "temporary": true,
  "created_at": "2023-10-27T10:00:00.000000+00:00"
}
```

### Errors
- **Forbidden**: You do not have permission to create an invite.
- **HTTPException**: Creating the invite failed.
```

--------------------------------

### discord.ui.Select Configuration

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Documentation for configuring various types of select menus and handling their callback values.

```APIDOC
## discord.ui.Select Configuration

### Description
Configures a select menu component. The `values` attribute in the callback returns different types based on the `cls` used.

### Parameters
- **cls** (Union[Type[Select], ...]) - Optional - The class to use for the select menu (e.g., Select, UserSelect, RoleSelect, MentionableSelect, ChannelSelect).
- **placeholder** (str) - Optional - Placeholder text (max 150 chars).
- **custom_id** (str) - Optional - ID received during interaction (max 100 chars).
- **min_values** (int) - Optional - Minimum items to choose (0-25, default 1).
- **max_values** (int) - Optional - Maximum items to choose (1-25, default 1).
- **options** (List[SelectOption]) - Optional - List of options (only for Select).
- **channel_types** (List[ChannelType]) - Optional - Types of channels to show (only for ChannelSelect).
- **disabled** (bool) - Optional - Whether the select is disabled (default False).
- **default_values** (Sequence[Snowflake]) - Optional - Default values for the menu.
- **id** (int) - Optional - Unique ID across the view (New in 2.6).

### Resolved Values
| Select Type | Resolved Values |
|---|---|
| discord.ui.Select | List[str] |
| discord.ui.UserSelect | List[Union[discord.Member, discord.User]] |
| discord.ui.RoleSelect | List[discord.Role] |
| discord.ui.MentionableSelect | List[Union[discord.Role, discord.Member, discord.User]] |
| discord.ui.ChannelSelect | List[Union[AppCommandChannel, AppCommandThread]] |
```

--------------------------------

### Fetch Stage Instance

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Gets a StageInstance for a stage channel ID.

```APIDOC
## GET /stage-instances/{channel_id}

### Description
Gets a StageInstance for a stage channel ID.

### Method
GET

### Endpoint
/stage-instances/{channel_id}

### Parameters
#### Path Parameters
- **channel_id** (int) - The stage channel ID.

### Raises
- **NotFound** - The stage instance or channel could not be found.
- **HTTPException** - Getting the stage instance failed.

### Returns
- **StageInstance** - The stage instance from the stage channel ID.
```

--------------------------------

### Get Channel Invites

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns a list of all active instant invites from this channel. Requires `manage_channels` permission.

```APIDOC
## GET /channels/{channel.id}/invites

### Description
Returns a list of all active instant invites from this channel. You must have `manage_channels` to get this information.

### Method
GET

### Endpoint
/channels/{channel.id}/invites

### Raises
- **Forbidden** - You do not have proper permissions to get the information.
- **HTTPException** - An error occurred while fetching the information.

### Returns
- The list of invites that are currently active.

### Return type
List[Invite]
```

--------------------------------

### GET /channels/{channel_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a channel or thread by its ID.

```APIDOC
## GET /channels/{channel_id}

### Description
Retrieves a `abc.GuildChannel` or `Thread` with the specified ID.

### Method
GET

### Endpoint
/channels/{channel_id}

### Parameters
#### Path Parameters
- **channel_id** (int) - Required - The ID of the channel or thread to retrieve.
```

--------------------------------

### Iterate and Flatten Channel History

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Examples for iterating through channel history using an async loop or list comprehension.

```python
counter = 0
async for message in channel.history(limit=200):
    if message.author == client.user:
        counter += 1
```

```python
messages = [message async for message in channel.history(limit=123)]
# messages is now a list of Message...
```

--------------------------------

### GET /scheduled_event/{scheduled_event_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a scheduled event by its ID.

```APIDOC
## GET /scheduled_event/{scheduled_event_id}

### Description
Returns a scheduled event with the given ID.

### Method
GET

### Endpoint
/scheduled_event/{scheduled_event_id}

### Parameters
#### Path Parameters
- **scheduled_event_id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **ScheduledEvent** (Optional[ScheduledEvent]) - The scheduled event or None if not found.
```

--------------------------------

### AppInfo Icon Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the replacement of AppInfo.icon with AppInfo.icon.key.

```python
AppInfo.icon.key
```

--------------------------------

### Scheduled Task at a Specific Time

Source: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

This example sets up a background task to run once daily at a specified time (8:30 AM UTC). The `time` parameter accepts a `datetime.time` object, assuming UTC if no timezone is provided.

```python
import datetime
from discord.ext import commands, tasks

utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=8, minute=30, tzinfo=utc)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=time)
    async def my_task(self):
        print("My task is running!")

```

--------------------------------

### TextChannel String Representation

Source: https://discordpy.readthedocs.io/en/latest/api.html

Shows how to get the string representation of a TextChannel object.

```APIDOC
## TextChannel String Representation

### Description
Returns the string representation of a `TextChannel` object.

### Function
- **str(x)**: Returns the channel's name.
```

--------------------------------

### Message Sending

Source: https://discordpy.readthedocs.io/en/latest/api.html

Example of sending a message to a channel after a computational task.

```APIDOC
## Message Sending

### Description
Example of sending a message to a channel after a computational task.

### Code Example
```python
# Do some computational magic for about 10 seconds
await channel.send('Done!')
```

### Version Notes
- **Changed in version 2.0**: This no longer works with the `with` syntax, `async with` must be used instead.
- **Changed in version 2.0**: Added functionality to `await` the context manager to send a typing indicator for 10 seconds.
```

--------------------------------

### GET /emoji/{emoji_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an emoji by its unique ID.

```APIDOC
## GET /emoji/{emoji_id}

### Description
Returns an emoji with the given ID.

### Method
GET

### Endpoint
/emoji/{emoji_id}

### Parameters
#### Path Parameters
- **emoji_id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **Emoji** (Optional[Emoji]) - The returned Emoji or None if not found.
```

--------------------------------

### PartialInviteGuild Banner Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the replacement of PartialInviteGuild.banner with PartialInviteGuild.banner.key.

```python
PartialInviteGuild.banner.key
```

--------------------------------

### Task Waiting for Bot Ready

Source: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

This configuration ensures that a background task only starts after the bot has successfully connected and is ready. The `before_loop` decorator is used to implement this waiting logic.

```python
from discord.ext import tasks, commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1

    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()

```

--------------------------------

### Application Commands and Bot Configuration

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Overview of application command structures and bot configuration settings available in the library.

```APIDOC
## Application Commands and Bot Configuration

### Description
This section covers the core components for defining application commands, managing bot permissions, and configuring allowed contexts and installation types for Discord bots.

### Key Components
- **discord.app_commands.AppCommand**: Represents a slash command.
- **discord.app_commands.ContextMenu**: Represents a context menu command.
- **commands.Bot.allowed_contexts**: Configures the contexts in which the bot can be used.
- **commands.Bot.allowed_installs**: Configures the installation types for the bot.
- **discord.AllowedMentions**: Controls how the bot handles mentions in messages.
```

--------------------------------

### GET /commands/{command_id}

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Fetches a specific application command by its ID.

```APIDOC
## GET /commands/{command_id}

### Description
Fetches an application command from the application.

### Method
GET

### Endpoint
/commands/{command_id}

### Parameters
#### Path Parameters
- **command_id** (int) - Required - The ID of the command to fetch.

#### Query Parameters
- **guild** (Snowflake) - Optional - The guild to fetch the command from. If not passed, the global command is fetched.

### Response
#### Success Response (200)
- **AppCommand** (object) - The application command object.

#### Errors
- **HTTPException**: Fetching the command failed.
- **MissingApplicationID**: The application ID could not be found.
- **NotFound**: The application command was not found.
```

--------------------------------

### Create FFmpegOpusAudio from Probe

Source: https://discordpy.readthedocs.io/en/latest/api.html

Use this factory method to create an FFmpegOpusAudio instance after probing the input source for audio codec and bitrate information. This is the recommended way to instantiate the class.

```python
source = await discord.FFmpegOpusAudio.from_probe("song.webm")
voice_client.play(source)
```

```python
source = await discord.FFmpegOpusAudio.from_probe("song.webm", method='fallback')
voice_client.play(source)
```

```python
def custom_probe(source, executable):
    # some analysis code here
    return codec, bitrate

source = await discord.FFmpegOpusAudio.from_probe("song.webm", method=custom_probe)
voice_client.play(source)
```

--------------------------------

### Get Channel Overwrites

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns all of the channel's permission overwrites.

```APIDOC
## GET /channels/{channel.id}/overwrites

### Description
Returns all of the channel's permission overwrites. This is returned as a dictionary where the key contains the target which can be either a `Role` or a `Member` and the value is the overwrite as a `PermissionOverwrite`.

### Method
GET

### Endpoint
/channels/{channel.id}/overwrites

### Returns
- The channel's permission overwrites.

### Return type
Dict[Union[Role, Member, Object], PermissionOverwrite]
```

--------------------------------

### Describe Command Parameters with app_commands.describe

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Provides descriptions for command parameters, either via decorator arguments or by parsing function docstrings.

```python
@app_commands.command(description='Bans a member')
@app_commands.describe(member='the member to ban')
async def ban(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f'Banned {member}')
```

```python
@app_commands.command()
async def ban(interaction: discord.Interaction, member: discord.Member):
    """Bans a member

    Parameters
    -----------
    member: discord.Member
        the member to ban
    """
    await interaction.response.send_message(f'Banned {member}')
```

--------------------------------

### PATCH /applications/@me

Source: https://discordpy.readthedocs.io/en/latest/api.html

Updates the current application's configuration, including installation parameters, flags, and metadata.

```APIDOC
## PATCH /applications/@me

### Description
Updates the current application's settings. Note that editing limited intent flags will result in the termination of the bot.

### Method
PATCH

### Endpoint
/applications/@me

### Parameters
#### Request Body
- **custom_install_url** (str) - Optional - The new custom authorization URL.
- **description** (str) - Optional - The new application description.
- **role_connections_verification_url** (str) - Optional - The new connection verification URL.
- **install_params_scopes** (List[str]) - Optional - The new list of OAuth2 scopes.
- **install_params_permissions** (Permissions) - Optional - The new permissions for install_params.
- **flags** (ApplicationFlags) - Optional - The new application flags (limited to specific intent flags).
- **icon** (bytes) - Optional - The new application icon.
- **cover_image** (bytes) - Optional - The new application cover image.
- **interactions_endpoint_url** (str) - Optional - The new interactions endpoint URL.
- **tags** (List[str]) - Optional - The new list of tags.
- **guild_install_scopes** (List[str]) - Optional - The new list of OAuth2 scopes for guild installation.
- **guild_install_permissions** (Permissions) - Optional - The new permissions for guild installation.
- **user_install_scopes** (List[str]) - Optional - The new list of OAuth2 scopes for user installation.
- **user_install_permissions** (Permissions) - Optional - The new permissions for user installation.
- **reason** (str) - Optional - The reason for the audit log.

### Response
#### Success Response (200)
- **AppInfo** (object) - The updated application information.
```

--------------------------------

### GET /channels/{channel_id}/invites

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of all active instant invites for a channel.

```APIDOC
## GET /channels/{channel_id}/invites

### Description
Returns a list of all active instant invites from this channel. Requires `manage_channels` permission.

### Response
#### Success Response (200)
- **invites** (List[Invite]) - The list of invites that are currently active.

### Errors
- **Forbidden**: You do not have proper permissions.
- **HTTPException**: An error occurred while fetching the information.
```

--------------------------------

### Initialize Client with Intents

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

The intents parameter is now mandatory for all Client subclasses. Explicitly define intents using discord.Intents.default() or specific configurations.

```python
# before
client = discord.Client()

# after
intents = discord.Intents.default()
client = discord.Client(intents=intents)
```

--------------------------------

### Hybrid Command with App Commands Describe

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Shows how to use `@app_commands.describe` with a hybrid command that utilizes a `FlagConverter`. This allows for inline descriptions of the flattened parameters.

```python
from discord import app_commands

class BanFlags(commands.FlagConverter):
    member: discord.Member
    reason: str
    days: int = 1


@commands.hybrid_command()
@app_commands.describe(
    member='The member to ban',
    reason='The reason for the ban',
    days='The number of days worth of messages to delete',
)
async def ban(ctx, *, flags: BanFlags):
    ...

```

--------------------------------

### GET /entitlements/{entitlement_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a specific entitlement by its ID.

```APIDOC
## GET /entitlements/{entitlement_id}

### Description
Retrieves an `Entitlement` object with the specified ID. This is a coroutine.

### Method
GET

### Endpoint
/entitlements/{entitlement_id}

### Parameters
#### Path Parameters
- **entitlement_id** (int) - Required - The entitlement’s ID to fetch from.

### Response
#### Success Response (200)
- **Entitlement** (object) - The entitlement requested.

#### Errors
- **NotFound**: An entitlement with this ID does not exist.
- **MissingApplicationID**: The application ID could not be found.
- **HTTPException**: Fetching the entitlement failed.
```

--------------------------------

### Global Before and After Invocation Hooks

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Sets up global hooks that execute before any command is invoked and after any command finishes, regardless of success or failure.

```python
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

### GET /channel/permissions_for

Source: https://discordpy.readthedocs.io/en/latest/api.html

Handles permission resolution for a User within the context of the channel.

```APIDOC
## GET /channel/permissions_for

### Description
Handles permission resolution for a User. Since partial messageables cannot reasonably have the concept of permissions, this will always return Permissions.none().

### Method
GET

### Endpoint
channel.permissions_for(obj)

### Parameters
#### Path Parameters
- **obj** (User) - Required - The user to check permissions for (ignored for partial messageables).

### Response
#### Success Response (200)
- **Permissions** - The resolved permissions object.
```

--------------------------------

### GET /webhooks/{webhook_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves webhook information by ID.

```APIDOC
## GET /webhooks/{webhook_id}

### Description
Retrieves a Webhook with the specified ID.

### Method
GET

### Endpoint
/webhooks/{webhook_id}

### Parameters
#### Path Parameters
- **webhook_id** (int) - Required - The ID of the webhook.

### Response
#### Success Response (200)
- **Webhook** (Object) - The webhook you requested.
```

--------------------------------

### PartialInviteGuild Icon Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the replacement of PartialInviteGuild.icon with PartialInviteGuild.icon.key.

```python
PartialInviteGuild.icon.key
```

--------------------------------

### Configure File Logging via Client.run

Source: https://discordpy.readthedocs.io/en/latest/logging.html

Redirects library logs to a file instead of stderr by passing a logging handler to the run method.

```python
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Assume client refers to a discord.Client subclass...
client.run(token, log_handler=handler)
```

--------------------------------

### GET /fetch_guild

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a specific Guild object by its ID.

```APIDOC
## GET /fetch_guild

### Description
Retrieves a Guild from an ID. Note that this does not receive full channel or member details.

### Parameters
#### Path Parameters
- **guild_id** (int) - Required - The guild’s ID to fetch from.

#### Query Parameters
- **with_counts** (bool) - Optional - Whether to include count information. Defaults to True.

### Response
- **Guild** - The guild from the ID.
```

--------------------------------

### Before Invoke Decorator for Commands

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Execute a function before a command is invoked. This can be used for setup, validation, or logging.

```Python
@bot.before_invoke
async def before_command_invoke(ctx):
    print(f'Invoking command: {ctx.command}')
```

--------------------------------

### GET /get_emoji

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a custom emoji from the cache by its ID.

```APIDOC
## GET get_emoji(id)

### Description
Returns a custom emoji with the given ID from the internal cache.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID to search for.

### Response
- **Returns** (Optional[Emoji]) - The custom emoji or None if not found.
```

--------------------------------

### GET /get_channel

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a channel or thread from the cache by its ID.

```APIDOC
## GET get_channel(id)

### Description
Returns a channel or thread with the given ID from the internal cache.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID to search for.

### Response
- **Returns** (Optional[Union[abc.GuildChannel, Thread, abc.PrivateChannel]]) - The returned channel or None if not found.
```

--------------------------------

### Compare Sync Webhook Usage

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the transition from using `discord.Webhook.partial` with an adapter to the new `discord.SyncWebhook.partial` for synchronous webhook operations.

```python
# before
webhook = discord.Webhook.partial(123456, 'token-here', adapter=discord.RequestsWebhookAdapter())
webhook.send('Hello World', username='Foo')

# after
webhook = discord.SyncWebhook.partial(123456, 'token-here')
webhook.send('Hello World', username='Foo')
```

--------------------------------

### Listen to Bot Messages

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Use the `bot.listen()` decorator to register a function that will be called when a specific event occurs. This example shows how to print 'two' when any message is received.

```python
@bot.listen('on_message')
async def my_message(message):
    print('two')
```

--------------------------------

### GET /user/{id}

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a user from the cache by their ID.

```APIDOC
## GET /user/{id}

### Description
Returns a user with the given ID from the internal cache.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **user** (Optional[User]) - The user or None if not found.
```

--------------------------------

### GET /guild/{id}

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a guild from the cache by its ID.

```APIDOC
## GET /guild/{id}

### Description
Returns a guild with the given ID from the internal cache.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **guild** (Optional[Guild]) - The guild or None if not found.
```

--------------------------------

### Guild Splash Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the replacement of Guild.splash with Guild.splash.key.

```python
Guild.splash.key
```

--------------------------------

### Fetch Invite

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Gets an Invite from a discord.gg URL or ID. Can include count and expiration information.

```APIDOC
## GET /invites/{code}

### Description
Gets an Invite from a discord.gg URL or ID. Can include count and expiration information.

### Method
GET

### Endpoint
/invites/{code}

### Parameters
#### Path Parameters
- **code** (str) - The invite code or URL.

#### Query Parameters
- **with_counts** (bool) - Whether to include count information in the invite. Defaults to True.
- **with_expiration** (bool) - Whether to include the expiration date of the invite. Defaults to True. Deprecated since version 2.6.
- **scheduled_event_id** (Optional[int]) - The ID of the scheduled event this invite is for.

### Raises
- **ValueError** - The url contains an event_id, but scheduled_event_id has also been provided.
- **NotFound** - The invite has expired or is invalid.
- **HTTPException** - Getting the invite failed.

### Returns
- **Invite** - The invite from the URL/ID.
```

--------------------------------

### MinimalHelpCommand Class Overview

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

The MinimalHelpCommand class is an implementation of a help command with minimal output, inheriting from HelpCommand.

```APIDOC
## MinimalHelpCommand

### Description
An implementation of a help command with minimal output. This class inherits from `HelpCommand` and provides hooks for customizing the formatting of help messages.

### Attributes
- **sort_commands** (bool) - Whether to sort the commands in the output alphabetically. Defaults to `True`.
- **commands_heading** (str) - The command list’s heading string. Defaults to "Commands".
- **aliases_heading** (str) - The alias list’s heading string. Defaults to "Aliases:".
- **dm_help** (Optional[bool]) - Indicates if the help command should DM the user. Defaults to `False`.
- **dm_help_threshold** (Optional[int]) - Character threshold for DMing if `dm_help` is `None`. Defaults to 1000.
- **no_category** (str) - String used for commands without a category. Defaults to "No Category".
- **paginator** (Paginator) - The paginator used to paginate the help command output.
```

--------------------------------

### Custom Flag Syntax: Posix-like

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Configure the flag syntax with custom delimiters and prefixes. This example uses space as a delimiter and '--' as a prefix.

```python
# --hello world syntax
class PosixLikeFlags(commands.FlagConverter, delimiter=' ', prefix='--'):
    hello: str

```

--------------------------------

### GET /channel/pins

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an asynchronous iterator of the pinned messages in the channel.

```APIDOC
## GET /channel/pins

### Description
Retrieves an asynchronous iterator of the pinned messages in the channel. Requires view_channel and read_message_history permissions.

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The maximum number of messages to retrieve (default 50).
- **before** (Message) - Optional - Retrieve messages before this message.
- **oldest_first** (bool) - Optional - Whether to return messages in oldest first order.

### Response
#### Success Response (200)
- **messages** (AsyncIterator[Message]) - An asynchronous iterator of pinned messages.
```

--------------------------------

### Define a LayoutView with a File component

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Shows how to include a ui.File component in a LayoutView, referencing a local attachment.

```python
import discord
from discord import ui

class MyView(ui.LayoutView):
    file = ui.File('attachment://file.txt')
    # attachment://file.txt points to an attachment uploaded alongside this view
```

--------------------------------

### GET /archived_threads

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an iterator of archived threads in a forum channel.

```APIDOC
## GET /archived_threads

### Description
Returns an asynchronous iterator over archived threads in a forum, ordered by decreasing archive timestamp. Requires `read_message_history`.

### Parameters
#### Query Parameters
- **limit** (bool) - Optional - Number of threads to retrieve.
- **before** (datetime) - Optional - Retrieve threads before this timestamp.
```

--------------------------------

### Get Channel Jump URL

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns a URL that allows the client to jump to the channel.

```APIDOC
## GET /channels/{channel.id}/jump

### Description
Returns a URL that allows the client to jump to the channel.

### Method
GET

### Endpoint
`/channels/{channel.id}/jump`

### Response
#### Success Response (200)
- **str** - The jump URL for the channel.
```

--------------------------------

### WelcomeChannel Class

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents a single welcome channel within a Guild welcome screen.

```APIDOC
## WelcomeChannel Class

### Description
Represents a `WelcomeScreen` welcome channel.
New in version 2.0.

### Attributes
- **channel** (abc.Snowflake) - The guild channel that is being referenced.
- **description** (str) - The description shown of the channel.
- **emoji** (Optional[PartialEmoji, Emoji, str]) - The emoji used beside the channel description.
```

--------------------------------

### ForumChannel Get Thread

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a specific thread from the ForumChannel by its ID.

```APIDOC
## ForumChannel Get Thread

### Description
Retrieves a specific thread from the ForumChannel by its ID.

### Method
`get_thread(thread_id: int) -> Optional[Thread]`

### Parameters
- **thread_id** (`int`): The ID of the thread to retrieve.

### Returns
- **Optional[Thread]**: The thread object if found, otherwise `None`.

### Note
This method does not always retrieve archived threads as they are not retained in the internal cache. For archived threads, use `Guild.fetch_channel()` instead.
```

--------------------------------

### Get Overwrites for Object

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns the channel-specific overwrites for a member or a role.

```APIDOC
## GET /channels/{channel.id}/overwrites/{obj.id}

### Description
Returns the channel-specific overwrites for a member or a role.

### Method
GET

### Endpoint
/channels/{channel.id}/overwrites/{obj.id}

### Parameters
#### Path Parameters
- **obj** (Union[Role, User, Object]) - The role or user denoting whose overwrite to get.

### Returns
- The channel-specific overwrites for the given object.
```

--------------------------------

### GET Emoji Asset

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the raw content of the emoji asset.

```APIDOC
## GET /emoji/asset

### Description
Retrieves the content of this asset as a bytes object.

### Method
GET

### Response
#### Success Response (200)
- **content** (bytes) - The raw content of the asset.
```

--------------------------------

### GET /channels/{channel_id}/stage-instance

Source: https://discordpy.readthedocs.io/en/latest/api.html

Fetches the currently running stage instance for the stage channel.

```APIDOC
## GET /channels/{channel_id}/stage-instance

### Description
Gets the running `StageInstance` associated with this channel.

### Method
GET

### Endpoint
/channels/{channel_id}/stage-instance

### Response
#### Success Response (200)
- **instance** (StageInstance) - The running stage instance.

### Errors
- **NotFound**: The stage instance or channel could not be found.
- **HTTPException**: Getting the stage instance failed.
```

--------------------------------

### GET /guild/automod/rules/{automod_rule_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Fetches a specific automod rule by ID.

```APIDOC
## GET /guild/automod/rules/{automod_rule_id}

### Description
Fetches an active automod rule from the guild. Requires manage_guild permission.

### Parameters
#### Path Parameters
- **automod_rule_id** (int) - Required - The ID of the automod rule.

### Response
#### Success Response (200)
- **AutoModRule** (Object) - The automod rule.

### Errors
- **Forbidden** - Permission denied.
- **NotFound** - Rule does not exist.
```

--------------------------------

### GET /channel/typing

Source: https://discordpy.readthedocs.io/en/latest/api.html

Sends a typing indicator to the destination. Can be used as an asynchronous context manager.

```APIDOC
## GET /channel/typing

### Description
Returns an asynchronous context manager that allows you to send a typing indicator to the destination for an indefinite period of time, or 10 seconds if the context manager is called using await.

### Method
GET

### Endpoint
channel.typing()

### Request Example
```python
async with channel.typing():
    await asyncio.sleep(20)
```

### Response
- **Success** - Sends typing indicator to the channel.
```

--------------------------------

### GET /guilds/{guild_id}/widget

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the widget information for a specific guild.

```APIDOC
## GET /guilds/{guild_id}/widget

### Description
Gets a Widget from a guild ID. The guild must have the widget enabled to get this information.

### Method
GET

### Endpoint
/guilds/{guild_id}/widget

### Parameters
#### Path Parameters
- **guild_id** (int) - Required - The ID of the guild.

### Response
#### Success Response (200)
- **Widget** (Object) - The guild's widget.
```

--------------------------------

### v1.0+ Converter Implementation

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Demonstrates the updated converter system introduced in v1.0, which requires an asynchronous `convert` method. This version accepts `ctx` and `argument` as parameters, enabling more complex and asynchronous conversions.

```python
class MyConverter(commands.Converter):
    async def convert(self, ctx, argument):
        return ctx.me
```

--------------------------------

### GET /guilds/{guild_id}/channels

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves all channels associated with the guild.

```APIDOC
## GET /guilds/{guild_id}/channels

### Description
Retrieves all `abc.GuildChannel` that the guild has.

### Method
GET

### Endpoint
/guilds/{guild_id}/channels

### Response
#### Success Response (200)
- **channels** (Sequence[`abc.GuildChannel`]) - All channels in the guild.
```

--------------------------------

### Connect to Voice

Source: https://discordpy.readthedocs.io/en/latest/api.html

Connects to a voice channel and establishes a `VoiceClient`. Requires 'voice_states' permission.

```APIDOC
## _await _connect(_*_ , _timeout=30.0_ , _reconnect=True_ , _cls= <class 'discord.voice_client.VoiceClient'>_, _self_deaf=False_ , _self_mute=False_) 

### Description
Connects to voice and creates a `VoiceClient` to establish your connection to the voice server. This requires `voice_states`.

### Parameters
- **timeout** (`float`) – The timeout in seconds to wait the connection to complete.
- **reconnect** (`bool`) – Whether the bot should automatically attempt a reconnect if a part of the handshake fails or the gateway goes down.
- **cls** (Type[`VoiceProtocol`]) – A type that subclasses `VoiceProtocol` to connect with. Defaults to `VoiceClient`.
- **self_mute** (`bool`) – Indicates if the client should be self-muted.
- **self_deaf** (`bool`) – Indicates if the client should be self-deafened.

### Raises
- **asyncio.TimeoutError** – Could not connect to the voice channel in time.
- **ClientException** – You are already connected to a voice channel.
- **OpusNotLoaded** – The opus library has not been loaded.

### Returns
- A voice client that is fully connected to the voice server.

### Return type
`VoiceProtocol`
```

--------------------------------

### GET /role/{role_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a specific role from the guild by its ID.

```APIDOC
## GET /role/{role_id}

### Description
Returns a role with the given ID.

### Method
GET

### Endpoint
/role/{role_id}

### Parameters
#### Path Parameters
- **role_id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **Role** (Optional[Role]) - The role or None if not found.
```

--------------------------------

### Create Guild from Template

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Create a new guild based on a provided guild template. The template can define initial settings for the new guild.

```Python
guild = await client.create_guild('New Guild Name', template='template_code')
```

--------------------------------

### GET /member/{user_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a member from the guild by their user ID.

```APIDOC
## GET /member/{user_id}

### Description
Returns a member with the given ID.

### Method
GET

### Endpoint
/member/{user_id}

### Parameters
#### Path Parameters
- **user_id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **Member** (Optional[Member]) - The member or None if not found.
```

--------------------------------

### GET /users/{user_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves user information by their unique ID.

```APIDOC
## GET /users/{user_id}

### Description
Retrieves a User based on their ID. You do not have to share any guilds with the user to get this information.

### Method
GET

### Endpoint
/users/{user_id}

### Parameters
#### Path Parameters
- **user_id** (int) - Required - The user's ID to fetch from.

### Response
#### Success Response (200)
- **User** (Object) - The user you requested.
```

--------------------------------

### TextChannel Equality and Hashing

Source: https://discordpy.readthedocs.io/en/latest/api.html

Demonstrates how to check for equality and hash TextChannel objects.

```APIDOC
## TextChannel Equality and Hashing

### Description
Checks for equality and hashing of `TextChannel` objects.

### Operators
- **x == y**: Checks if two channels are equal.
- **x != y**: Checks if two channels are not equal.
- **hash(x)**: Returns the channel's hash.
```

--------------------------------

### Default Opening Note Format

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

The default string format used by get_opening_note to instruct users on how to use the help command.

```text
Use {prefix}{command_name} [command] for more info on a command.
You can also use {prefix}{command_name} [category] for more info on a category.
```

--------------------------------

### GET /sticker/{id}

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a guild sticker from the cache by its ID.

```APIDOC
## GET /sticker/{id}

### Description
Returns a guild sticker with the given ID from the internal cache.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **sticker** (Optional[GuildSticker]) - The sticker or None if not found.
```

--------------------------------

### Load a Discord.py Extension

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/extensions.html

Use `Bot.load_extension()` to load an extension. The extension path is dot-qualified, similar to Python's import mechanism. For example, an extension in `plugins/hello.py` is loaded as `'plugins.hello'`.

```python
await bot.load_extension('hello')
```

--------------------------------

### GET /emoji/{id}

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a custom emoji from the cache by its ID.

```APIDOC
## GET /emoji/{id}

### Description
Returns a custom emoji with the given ID from the internal cache.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **emoji** (Optional[Emoji]) - The custom emoji or None if not found.
```

--------------------------------

### Create Discord Invite

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates an instant invite for a text or voice channel. Requires the 'create_instant_invite' permission. You can configure expiration, max uses, and temporary membership.

```python
await channel._create_invite(reason=None, max_age=0, max_uses=0, temporary=False, unique=True, target_type=None, target_user=None, target_application_id=None, guest=False)
```

--------------------------------

### Guild Discovery Splash Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the replacement of Guild.discovery_splash with Guild.discovery_splash.key.

```python
Guild.discovery_splash.key
```

--------------------------------

### GET /emojis/{emoji_id}

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a specific emoji for the current application.

```APIDOC
## GET /emojis/{emoji_id}

### Description
Retrieves an emoji for the current application.

### Parameters
#### Path Parameters
- **emoji_id** (int) - Required - The emoji ID to retrieve.

### Response
#### Success Response (200)
- **Emoji** (Object) - The emoji requested.
```

--------------------------------

### login

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Logs in the client with the specified credentials.

```APIDOC
## login(token)

### Description
Logs in the client with the specified credentials and calls the setup_hook(). This function is a coroutine.

### Parameters
#### Arguments
- **token** (str) - Required - The authentication token.

### Errors
- **LoginFailure**: Wrong credentials passed.
- **HTTPException**: Unknown HTTP related error.
```

--------------------------------

### Invite Creation

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates an instant invite from a text or voice channel.

```APIDOC
## POST /channels/{channel.id}/invites

### Description
Creates an instant invite from a text or voice channel. Requires `create_instant_invite` permission.

### Method
POST

### Endpoint
`/channels/{channel.id}/invites`

### Parameters
#### Query Parameters
- **max_age** (int) - Optional - How long the invite should last in seconds. If 0, the invite doesn't expire. Defaults to 0.
- **max_uses** (int) - Optional - How many uses the invite could be used for. If 0, there are unlimited uses. Defaults to 0.
- **temporary** (bool) - Optional - Denotes that the invite grants temporary membership. Defaults to False.
- **unique** (bool) - Optional - Indicates if a unique invite URL should be created. Defaults to True. If False, returns a previously created invite.
- **reason** (str) - Optional - The reason for creating this invite. Shows up on the audit log.
- **target_type** (InviteTarget) - Optional - The type of target for the voice channel invite, if any.
- **target_user** (User) - Optional - The user whose stream to display for this invite, required if `target_type` is `InviteTarget.stream`. The user must be streaming in the channel.
- **target_application_id** (int) - Optional - The id of the embedded application for the invite, required if `target_type` is `InviteTarget.embedded_application`.
- **guest** (bool) - Optional - Whether the invite is a guest invite. Defaults to False.

### Raises
- **HTTPException** - Invite creation failed.
- **NotFound** - The channel that was passed is a category or an invalid channel.

### Returns
- **Invite** - The invite that was created.
```

--------------------------------

### Edit a WelcomeScreen

Source: https://discordpy.readthedocs.io/en/latest/api.html

Updates the description, channels, and enabled status of a guild's welcome screen. Requires the manage_guild permission.

```python
rules_channel = guild.get_channel(12345678)
announcements_channel = guild.get_channel(87654321)

custom_emoji = utils.get(guild.emojis, name='loudspeaker')

await welcome_screen.edit(
    description='This is a very cool community server!',
    welcome_channels=[
        WelcomeChannel(channel=rules_channel, description='Read the rules!', emoji='👨‍🏫'),
        WelcomeChannel(channel=announcements_channel, description='Watch out for announcements!', emoji=custom_emoji),
    ]
)
```

--------------------------------

### Wait for Events with Client.wait_for

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Demonstrates the transition from legacy event-specific methods to the generalized wait_for pattern.

```python
# before
msg = await client.wait_for_message(author=message.author, channel=message.channel)

# after
def pred(m):
    return m.author == message.author and m.channel == message.channel

msg = await client.wait_for('message', check=pred)
```

--------------------------------

### Guild Banner Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the replacement of Guild.banner with Guild.banner.key.

```python
Guild.banner.key
```

--------------------------------

### GET /channel/history

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of messages from a channel with optional filtering parameters.

```APIDOC
## GET /channel/history

### Description
Retrieves message history from a channel. Returns an asynchronous iterator of Message objects.

### Method
GET

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of messages to retrieve.
- **before** (Snowflake/datetime) - Optional - Retrieve messages before this date or message.
- **after** (Snowflake/datetime) - Optional - Retrieve messages after this date or message.
- **around** (Snowflake/datetime) - Optional - Retrieve messages around this date or message.
- **oldest_first** (bool) - Optional - If True, return messages in oldest to newest order.

### Response
#### Success Response (200)
- **Message** (Object) - The message data parsed.

### Errors
- **Forbidden**: You do not have permissions to get channel message history.
- **HTTPException**: The request to get message history failed.
```

--------------------------------

### Initialize AutoShardedClient

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Basic initialization of the AutoShardedClient for bots requiring automatic sharding.

```python
client = discord.AutoShardedClient()
```

--------------------------------

### Iterate and Flatten Channel Pins

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Examples for iterating through pinned messages using an async loop or list comprehension.

```python
counter = 0
async for message in channel.pins(limit=250):
    counter += 1
```

```python
messages = [message async for message in channel.pins(limit=50)]
```

--------------------------------

### Make a Web Request with aiohttp

Source: https://discordpy.readthedocs.io/en/latest/faq.html

Performs a GET request to a specified URL using aiohttp and parses the JSON response. Ensure the response status is 200 before processing.

```python
async with aiohttp.ClientSession() as session:
    async with session.get('http://aws.random.cat/meow') as r:
        if r.status == 200:
            js = await r.json()
```

--------------------------------

### FFmpegOpusAudio.from_probe Class Method

Source: https://discordpy.readthedocs.io/en/latest/api.html

A factory method that creates an FFmpegOpusAudio instance after probing the input source for audio codec and bitrate information. This is recommended for performance.

```APIDOC
## FFmpegOpusAudio.from_probe Class Method

### Description
A factory method that creates a `FFmpegOpusAudio` after probing the input source for audio codec and bitrate information.

### Parameters
#### Path Parameters
- **source** - Required - Identical to the `source` parameter for the constructor.
- **method** (Optional[Union[`str`, Callable[`str`, `str`]]]) - Optional - The probing method used to determine bitrate and codec information. As a string, valid values are `native` to use ffprobe (or avprobe) and `fallback` to use ffmpeg (or avconv). As a callable, it must take two string arguments, `source` and `executable`. Both parameters are the same values passed to this factory function. `executable` will default to `ffmpeg` if not provided as a keyword argument.
- **kwargs** - Optional - The remaining parameters to be passed to the `FFmpegOpusAudio` constructor, excluding `bitrate` and `codec`.

### Request Example
```python
source = await discord.FFmpegOpusAudio.from_probe("song.webm")
voice_client.play(source)

# Using fallback method on Windows
source = await discord.FFmpegOpusAudio.from_probe("song.webm", method='fallback')
voice_client.play(source)

# Using a custom probe method
def custom_probe(source, executable):
    # some analysis code here
    return codec, bitrate
source = await discord.FFmpegOpusAudio.from_probe("song.webm", method=custom_probe)
voice_client.play(source)
```

### Raises
- **AttributeError** - Invalid probe method, must be `'native'` or `'fallback'`.
- **TypeError** - Invalid value for `probe` parameter, must be `str` or a callable.

### Returns
- **FFmpegOpusAudio** - An instance of this class.
```

--------------------------------

### GET /channels/{channel.id}/permissions_synced

Source: https://discordpy.readthedocs.io/en/latest/api.html

Checks if the permissions for this channel are synced with its category.

```APIDOC
## GET /channels/{channel.id}/permissions_synced

### Description
Whether or not the permissions for this channel are synced with the category it belongs to. If there is no category then this is `False`.

New in version 1.3.

### Method
GET

### Endpoint
`/channels/{channel.id}/permissions_synced`

### Response
#### Success Response (200)
- **bool** - `True` if permissions are synced with the category, `False` otherwise.

#### Response Example
```json
{
  "permissions_synced": true
}
```
```

--------------------------------

### Flatten SKU Subscriptions into a List

Source: https://discordpy.readthedocs.io/en/latest/api.html

Collect all subscriptions for an SKU into a list using an asynchronous list comprehension. This is a concise way to get all subscriptions if memory is not a concern.

```python
subscriptions = [subscription async for subscription in sku.subscriptions(limit=100, user=user)]
# subscriptions is now a list of Subscription...
```

--------------------------------

### Get Channel Messages

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of messages from a channel. All parameters are optional.

```APIDOC
## GET /channels/{channel.id}/messages

### Description
Retrieves a list of messages from a channel.

### Method
GET

### Endpoint
/channels/{channel.id}/messages

### Parameters
#### Query Parameters
- **limit** (Optional[int]) - The number of messages to retrieve. If `None`, retrieves every message in the channel. Note, however, that this would make it a slow operation.
- **before** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages before this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **after** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages after this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the naive datetime is naive, it is assumed to be local time.
- **around** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages around this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time. When using this argument, the maximum limit is 101. Note that if the limit is an even number then this will return at most limit + 1 messages.
- **oldest_first** (Optional[bool]) - If set to `True`, return messages in oldest->newest order. Defaults to `True` if `after` is specified, otherwise `False`.

### Raises
- **Forbidden** - You do not have permissions to get channel message history.
- **HTTPException** - The request to get message history failed.

### Yields
`Message` - The message with the message data parsed.
```

--------------------------------

### Set Default Permissions with a Permissions Object

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

You can also pass a `discord.Permissions` object to `@app_commands.default_permissions`. This allows for setting multiple permissions or more complex permission configurations. This example uses a pre-defined `ADMIN_PERMS` object and also sets `manage_messages`.

```python
ADMIN_PERMS = discord.Permissions(administrator=True)

@app_commands.command()
@app_commands.default_permissions(ADMIN_PERMS, manage_messages=True)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('You may or may not have manage messages.')
```

--------------------------------

### ChannelSelect in a discord.ui.LayoutView

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Example of using a ChannelSelect menu within a discord.ui.LayoutView. The callback receives the interaction and the select menu, allowing access to selected values via `select.values`.

```python
class MyView(discord.ui.LayoutView):
    action_row = discord.ui.ActionRow()

    @action_row.select(cls=ChannelSelect, channel_types=[discord.ChannelType.text])
    async def select_channels(self, interaction: discord.Interaction, select: ChannelSelect):
        return await interaction.response.send_message(f'You selected {select.values[0].mention}')
```

--------------------------------

### @discord.app_commands.context_menu

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Creates an application command context menu from a regular function.

```APIDOC
## @discord.app_commands.context_menu

### Description
Creates an application command context menu from a regular function. Requires a specific signature: Interaction as the first parameter and Member, User, or Message as the second.

### Parameters
- **name** (Union[str, locale_str]) - Optional - The name of the context menu command.
- **nsfw** (bool) - Optional - Whether the command is NSFW. Defaults to False.
- **auto_locale_strings** (bool) - Optional - If True, translatable strings are wrapped into locale_str. Defaults to True.
- **extras** (dict) - Optional - A dictionary to store extraneous data.
```

--------------------------------

### Get Pinned Messages

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an asynchronous iterator of pinned messages in a channel.

```APIDOC
## GET /channels/{channel.id}/pins

### Description
Retrieves an asynchronous iterator of the pinned messages in the channel. You must have `view_channel` and `read_message_history` to use this.

### Method
GET

### Endpoint
`/channels/{channel.id}/pins`

### Parameters
#### Query Parameters
- **limit** (Optional[int]) - The maximum number of pinned messages to retrieve. Defaults to 50.
- **before** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve pinned messages before this date or message.
- **oldest_first** (Optional[bool]) - If set to `True`, return messages in oldest->newest order. Defaults to `False`.

### Note
Due to a limitation with the Discord API, the `Message` object returned by this method does not contain complete `Message.reactions` data.

### Request Example
```python
counter = 0
async for message in channel.pins(limit=250):
    counter += 1
```

### Response Example
```python
messages = [message async for message in channel.pins(limit=50)]
```
```

--------------------------------

### Other Attributes and Methods

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

This section covers miscellaneous attributes and methods, including those related to onboarding, intents, and specific object properties.

```APIDOC
## Other Attributes and Methods

This section covers miscellaneous attributes and methods, including those related to onboarding, intents, and specific object properties.

### Attributes
- **discord.PrimaryGuild.identity_enabled**
- **discord.Status.idle**
- **commands.Command.ignore_extra**
- **discord.Embed.image**
- **discord.AuditLogDiff.in_onboarding**
- **discord.OnboardingPrompt.in_onboarding**
- **discord.RoleFlags.in_prompt**
- **discord.SubscriptionStatus.inactive**
- **discord.WebhookType.incoming**
- **commands.DefaultHelpCommand.indent**
- **discord.Locale.indonesian**
- **discord.AppInfo.install_params**
- **discord.StageChannel.instance**
- **discord.AppCommandOptionType.integer**
- **discord.Intents.integrations**
- **discord.Client.intents**
- **commands.Bot.intents**

### Methods
- **discord.Embed.insert_field_at()**
- **discord.ui.MediaGallery.insert_item_at()**

### Events
- **discord.AuditLogAction.integration_create**
- **discord.AuditLogAction.integration_delete**
- **discord.RawIntegrationDeleteEvent.integration_id**
- **discord.RoleTags.integration_id**
- **discord.AuditLogAction.integration_update

### Objects
- **discord.Integration**
- **discord.IntegrationAccount**
- **discord.IntegrationApplication**
- **discord.IntegrationTypeConfig**
- **discord.Intents
```

--------------------------------

### Get Member Role

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a role from the member's roles by its ID.

```APIDOC
## GET /users/@me/guilds/{guild.id}/member

### Description
Returns a role with the given ID from roles which the member has.

### Method
GET

### Endpoint
`/users/@me/guilds/{guild.id}/member`

### Parameters
#### Query Parameters
- **role_id** (int) - Required - The ID to search for.

### Response
#### Success Response (200)
- **Role** (Optional[Role]) - The role or `None` if not found in the member’s roles.

#### Response Example
{
  "example": "Role object or null"
}
```

--------------------------------

### Bot Lifecycle and Connection Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods for managing the bot's connection to Discord, including login, startup, and shutdown procedures.

```APIDOC
## _login(token)

### Description
Logs in the client with the specified credentials and calls the setup_hook().

### Method
Coroutine

### Parameters
#### Request Body
- **token** (str) - Required - The authentication token. Do not prefix this token with anything.

### Response
#### Errors
- **LoginFailure** - The wrong credentials are passed.
- **HTTPException** - An unknown HTTP related error occurred.
```

```APIDOC
## _connect(*, reconnect=True)

### Description
Creates a websocket connection and lets the websocket listen to messages from Discord.

### Method
Coroutine

### Parameters
#### Request Body
- **reconnect** (bool) - Optional - If we should attempt reconnecting.

### Response
#### Errors
- **GatewayNotFound** - If the gateway to connect to Discord is not found.
- **ConnectionClosed** - The websocket connection has been terminated.
```

```APIDOC
## _start(token, *, reconnect=True)

### Description
A shorthand coroutine for login() + connect().

### Method
Coroutine

### Parameters
#### Request Body
- **token** (str) - Required - The authentication token.
- **reconnect** (bool) - Optional - If we should attempt reconnecting.
```

--------------------------------

### Get Message

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a specific message by its ID. Requires appropriate permissions.

```APIDOC
## GET /channels/{channel.id}/messages/{message.id}

### Description
Retrieves a specific message by its ID.

### Method
GET

### Endpoint
`/channels/{channel.id}/messages/{message.id}`

### Parameters
#### Path Parameters
- **id** (int) - Required - The message ID to look for.

### Raises
- **NotFound** - The specified message was not found.
- **Forbidden** - You do not have the permissions required to get a message.
- **HTTPException** - Retrieving the message failed.

### Response
#### Success Response (200)
- **Message** (Message) - The message object.

#### Response Example
{
  "example": "Message object"
}
```

--------------------------------

### HelpCommand Class Overview

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Provides an overview of the HelpCommand class, its purpose, and key attributes.

```APIDOC
## Class discord.ext.commands.HelpCommand

### Description
The base implementation for help command formatting.

Note: Internally instances of this class are deep copied every time the command itself is invoked to prevent a race condition mentioned in GH-2123. This means that relying on the state of this class to be the same between command invocations would not work as expected.

### Attributes
- **cog** (Optional[Cog]) - A property for retrieving or setting the cog for the help command.
- **command_attrs** (dict) - A dictionary of options to pass in for the construction of the help command.
- **context** (Optional[Context]) - The context that invoked this help formatter.
- **invoked_with** (Optional[str]) - Similar to `Context.invoked_with` except properly handles the case where `Context.send_help()` is used.
- **show_hidden** (bool) - Specifies if hidden commands should be shown in the output. Defaults to `False`.
- **verify_checks** (Optional[bool]) - Specifies if commands should have their `Command.checks` called and verified. Defaults to `True`.
```

--------------------------------

### GET /emojis/{emoji_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a specific custom emoji from the guild by its ID.

```APIDOC
## GET /emojis/{emoji_id}

### Description
Retrieves a custom Emoji from the guild.

### Method
GET

### Endpoint
/emojis/{emoji_id}

### Parameters
#### Path Parameters
- **emoji_id** (int) - Required - The emoji’s ID.

### Response
#### Success Response (200)
- **emoji** (Emoji) - The retrieved emoji.

#### Errors
- **NotFound** - The emoji requested could not be found.
- **HTTPException** - An error occurred fetching the emoji.
```

--------------------------------

### GET /guilds/{guild_id}/members

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an asynchronous iterator for guild members.

```APIDOC
## GET /guilds/{guild_id}/members

### Description
Retrieves an asynchronous iterator that enables receiving the guild’s members. Requires `Intents.members` to be enabled.

### Method
GET

### Endpoint
/guilds/{guild_id}/members

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of members to retrieve. Defaults to 1000.
- **after** (Union[`abc.Snowflake`, `datetime.datetime`]) - Optional - Retrieve members after this date or object.

### Response
#### Success Response (200)
- **member** (`Member`) - The member with the member data parsed.
```

--------------------------------

### DefaultHelpCommand Class

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

The DefaultHelpCommand class manages the display of help information for bot commands, supporting customization of headings, indentation, and pagination behavior.

```APIDOC
## DefaultHelpCommand

### Description
The implementation of the default help command for discord.py bots. It provides various attributes to control the appearance and behavior of help output.

### Attributes
- **width** (int) - The maximum number of characters that fit in a line. Defaults to 80.
- **sort_commands** (bool) - Whether to sort the commands in the output alphabetically. Defaults to True.
- **dm_help** (Optional[bool]) - Indicates if the help command should DM the user. Defaults to False.
- **dm_help_threshold** (Optional[int]) - Character threshold for DMing if dm_help is None. Defaults to 1000.
- **indent** (int) - Indentation level for commands. Defaults to 2.
- **arguments_heading** (str) - Heading for arguments list. Defaults to "Arguments:".
- **show_parameter_descriptions** (bool) - Whether to show parameter descriptions. Defaults to True.
- **commands_heading** (str) - Heading for command list. Defaults to "Commands:".
- **default_argument_description** (str) - Default string for missing argument descriptions. Defaults to "No description given.".
- **no_category** (str) - String used for commands without a category. Defaults to "No Category".
- **paginator** (Paginator) - The paginator used for output.
```

```APIDOC
## Methods

### get_command_signature
Retrieves the signature portion of the help page.

#### Parameters
- **command** (Command) - Required - The command to get the signature of.

### add_indented_commands
Indents a list of commands after the specified heading.

#### Parameters
- **commands** (Sequence[Command]) - Required - A list of commands to indent.
- **heading** (str) - Required - The heading to add to the output.
- **max_size** (Optional[int]) - Optional - The max size for the gap between indents.

### add_command_arguments
Indents a list of command arguments after the arguments_heading.

#### Parameters
- **command** (Command) - Required - The command to list the arguments for.

### send_pages
A coroutine to send the page output from the paginator to the destination.
```

--------------------------------

### Sync Application Commands

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

This function synchronizes application commands with Discord. It must be called for the commands to be visible on Discord. It also runs a translator to get translated strings for feedback.

```APIDOC
## POST /sync/commands

### Description
Synchronizes application commands with Discord. This is necessary for application commands to appear on Discord. It also runs a translator to get translated strings for feedback.

### Method
POST

### Endpoint
/sync/commands

### Parameters
#### Query Parameters
- **guild** (Optional[Snowflake]) - Optional - The guild to sync the commands to. If None, then it syncs all global commands instead.

### Raises
- **HTTPException** – Syncing the commands failed.
- **CommandSyncFailure** – Syncing the commands failed due to a user related error, typically because the command has invalid data. This is equivalent to an HTTP status code of 400.
- **Forbidden** – The client does not have the `applications.commands` scope in the guild.
- **MissingApplicationID** – The client does not have an application ID.
- **TranslationError** – An error occurred while translating the commands.

### Returns
- **List[AppCommand]** - The application’s commands that got synced.
```

--------------------------------

### FlagConverter with Inline Descriptions

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Illustrates using the `description` keyword argument within `commands.flag()` to provide inline descriptions for flags in a `FlagConverter`. This is a convenient way to document flags directly.

```python
class BanFlags(commands.FlagConverter):
    member: discord.Member = commands.flag(description='The member to ban')
    reason: str = commands.flag(description='The reason for the ban')
    days: int = commands.flag(default=1, description='The number of days worth of messages to delete')


@commands.hybrid_command()
async def ban(ctx, *, flags: BanFlags):
    ...

```

--------------------------------

### GET get_member_named

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a member from the guild by their name, nickname, or global name.

```APIDOC
## GET get_member_named

### Description
Returns the first member found that matches the name provided. The lookup order includes username, nickname, and global name.

### Parameters
#### Path Parameters
- **name** (str) - Required - The name of the member to lookup.

### Response
#### Success Response (200)
- **member** (Optional[Member]) - The member object if found, otherwise None.
```

--------------------------------

### Flatten Pinned Messages into a List

Source: https://discordpy.readthedocs.io/en/latest/api.html

This example shows how to collect all pinned messages into a list using an asynchronous list comprehension. The `limit` parameter controls the maximum number of messages to retrieve.

```python
messages = [message async for message in channel.pins(limit=50)]
```

--------------------------------

### GET /channels/{channel_id}/pins

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of pinned messages from a channel.

```APIDOC
## GET /channels/{channel_id}/pins

### Description
Retrieves pinned messages from the specified channel. Returns a list of Message objects.

### Method
GET

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of pinned messages to retrieve. Defaults to 50.
- **before** (datetime.datetime or abc.Snowflake) - Optional - Retrieve pinned messages before this time or snowflake.
- **oldest_first** (bool) - Optional - If True, return messages in oldest to newest order. Defaults to False.

### Response
#### Success Response (200)
- **Message** (Object) - The pinned message with Message.pinned_at set.
```

--------------------------------

### Get Role Tags

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Access Role.tags to retrieve any associated tags for a role, such as those indicating premium subscription or integration.

```python
role_tags = role.tags
```

--------------------------------

### GET /messages/{message_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Fetches the full message object from a partial message.

```APIDOC
## GET /messages/{message_id}

### Description
Fetches the partial message to a full Message object.

### Method
GET

### Response
#### Success Response (200)
- **Message** - The full message object.

#### Error Handling
- **NotFound** - The message was not found.
- **Forbidden** - You do not have the permissions required to get a message.
- **HTTPException** - Retrieving the message failed.
```

--------------------------------

### Register a Command using Decorator and add_command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Demonstrates two equivalent ways to register a command: using the @bot.command() decorator directly or using the @commands.command() decorator with bot.add_command(). Requires enabling message_content intent.

```python
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx):
    pass

# or:

@commands.command()
async def test(ctx):
    pass

bot.add_command(test)
```

--------------------------------

### TeamMember String Representation

Source: https://discordpy.readthedocs.io/en/latest/api.html

Method for getting the string representation of a TeamMember object.

```APIDOC
## TeamMember String Representation

### `str(x)`

Returns the team member’s handle (e.g. `name` or `name#discriminator`).
New in version 1.3.
```

--------------------------------

### Help Command Core Methods

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

These methods handle the core logic of sending help messages for different command structures.

```APIDOC
## _await _send_group_help(_group_ , _/_)

### Description
Handles the implementation of the group page in the help command. This function is called when the help command is called with a group as the argument. It should be noted that this method does not return anything – rather the actual message sending should be done inside this method. Well behaved subclasses should use `get_destination()` to know where to send, as this is a customisation point for other users. You can override this method to customise the behaviour.

Note
You can access the invocation context with `HelpCommand.context`.
To get the commands that belong to this group without aliases see `Group.commands`. The commands returned not filtered. To do the filtering you will have to call `filter_commands()` yourself.
Changed in version 2.0: `group` parameter is now positional-only.

### Parameters
#### Path Parameters
- **group** (`Group`) – The group that was requested for help.
```

```APIDOC
## _await _send_command_help(_command_ , _/_)

### Description
Handles the implementation of the single command page in the help command. It should be noted that this method does not return anything – rather the actual message sending should be done inside this method. Well behaved subclasses should use `get_destination()` to know where to send, as this is a customisation point for other users. You can override this method to customise the behaviour.

Note
You can access the invocation context with `HelpCommand.context`.
Showing Help
There are certain attributes and methods that are helpful for a help command to show such as the following:
  * `Command.help`
  * `Command.brief`
  * `Command.short_doc`
  * `Command.description`
  * `get_command_signature()`

There are more than just these attributes but feel free to play around with these to help you get started to get the output that you want.
Changed in version 2.0: `command` parameter is now positional-only.

### Parameters
#### Path Parameters
- **command** (`Command`) – The command that was requested for help.
```

--------------------------------

### GET /channels/{channel.id}/webhooks

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of webhooks associated with a specific channel. Requires 'manage_webhooks' permission.

```APIDOC
## GET /channels/{channel.id}/webhooks

### Description
Gets the list of webhooks from this channel. You must have `manage_webhooks` permission to do this.

### Method
GET

### Endpoint
`/channels/{channel.id}/webhooks`

### Parameters
#### Path Parameters
- **channel.id** (int) - Required - The ID of the channel to retrieve webhooks from.

### Response
#### Success Response (200)
- **webhooks** (List[Webhook]) - A list of webhook objects.

#### Response Example
```json
{
  "webhooks": [
    {
      "id": 123456789012345678,
      "name": "My Webhook",
      "avatar": "a_abcdef1234567890",
      "token": "abcdef1234567890abcdef1234567890abcdef1234567890"
    }
  ]
}
```

### Errors
- **Forbidden** – You don’t have permissions to get the webhooks.
```

--------------------------------

### GET /application/emojis/{emoji_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a specific emoji by its ID for the current application.

```APIDOC
## GET /application/emojis/{emoji_id}

### Description
Retrieves an emoji for the current application.

### Method
GET

### Parameters
#### Path Parameters
- **emoji_id** (int) - Required - The emoji ID to retrieve.

### Response
#### Success Response (200)
- **Emoji** (object) - The emoji requested.
```

--------------------------------

### Attach a Channel Select Menu to a View

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Demonstrates using the select decorator with ChannelSelect to filter and retrieve specific channel types.

```python
class View(discord.ui.View):

    @discord.ui.select(cls=ChannelSelect, channel_types=[discord.ChannelType.text])
    async def select_channels(self, interaction: discord.Interaction, select: ChannelSelect):
        return await interaction.response.send_message(f'You selected {select.values[0].mention}')
```

--------------------------------

### Activate virtual environment

Source: https://discordpy.readthedocs.io/en/latest/intro.html

Commands to activate the virtual environment on Unix-like systems and Windows.

```bash
$ source bot-env/bin/activate
```

```bash
$ bot-env\Scripts\activate.bat
```

--------------------------------

### async with AutoShardedClient

Source: https://discordpy.readthedocs.io/en/latest/api.html

Asynchronously initialises the client and automatically cleans up. This is a context manager pattern for client initialization and cleanup.

```APIDOC
## async with AutoShardedClient

### Description
Asynchronously initialises the client and automatically cleans up.
New in version 2.0.

### Usage
```python
async with discord.AutoShardedClient(...) as client:
    # Bot logic here
```
```

--------------------------------

### Get Pinned Messages

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves pinned messages from a channel with optional filtering.

```APIDOC
## GET /channels/{channel.id}/pins

### Description
Retrieves a list of pinned messages in a channel.

### Method
GET

### Endpoint
/channels/{channel.id}/pins

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of pinned messages to retrieve. Defaults to 50.
- **before** (datetime or Snowflake) - Optional - Retrieve pinned messages before this time or snowflake.
- **oldest_first** (bool) - Optional - If True, return messages in oldest pin->newest pin order. Defaults to False.

### Raises
- **Forbidden** - You do not have the permission to retrieve pinned messages.
- **HTTPException** - Retrieving the pinned messages failed.

### Yields
- `Message` - The pinned message with `Message.pinned_at` set.
```

--------------------------------

### Get Invite Guild Icon URL with Static Format

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Retrieve the icon URL for a guild associated with an invite, specifying a static format for consistency. Supports various image formats.

```Python
icon_url = invite.guild.icon_url_as(static_format='png')
```

--------------------------------

### ContextMenu Class Definition

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Details for the ContextMenu class constructor and its configuration parameters.

```APIDOC
## class discord.app_commands.ContextMenu

### Description
A class that implements a context menu application command. These are usually created using decorators like `context_menu()`.

### Parameters
- **name** (Union[str, locale_str]) - Required - The name of the context menu.
- **callback** (coroutine) - Required - The coroutine executed when the command is called.
- **type** (AppCommandType) - Optional - The type of context menu command.
- **auto_locale_strings** (bool) - Optional - Whether to wrap translatable strings in locale_str. Defaults to True.
- **nsfw** (bool) - Optional - Whether the command is NSFW. Defaults to False.
- **extras** (dict) - Optional - Dictionary to store extraneous data.
```

--------------------------------

### Configure default intents with exclusions

Source: https://discordpy.readthedocs.io/en/latest/intents.html

Demonstrates using default intents while disabling specific ones like typing and presences to reduce event volume.

```python
 import discord
 intents = discord.Intents.default()
 intents.typing = False
 intents.presences = False

 # Somewhere else:
 # client = discord.Client(intents=intents)
 # or
 # from discord.ext import commands
 # bot = commands.Bot(command_prefix='!', intents=intents)

```

--------------------------------

### Run the bot script

Source: https://discordpy.readthedocs.io/en/latest/quickstart.html

Commands to execute the bot script on different operating systems.

```bash
$ py -3 example_bot.py
```

```bash
$ python3 example_bot.py
```

--------------------------------

### Command Prefix Helpers

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Provides utility functions for defining command prefixes, including options for mentioning the bot or using custom prefixes.

```APIDOC
## Prefix Helpers

### `when_mentioned(bot, msg, /)`

A callable that implements a command prefix equivalent to being mentioned.

**Parameters**
- **bot** (`Bot`) – The bot instance.
- **msg** (`Message`) – The message object.

**Note:** `bot` and `msg` parameters are positional-only since version 2.0.

### `when_mentioned_or(*prefixes)`

A callable that implements when mentioned or other prefixes provided.

**Parameters**
- **prefixes** (`*str`) – A variable number of prefix strings.

**Returns**
A callable that takes `bot` and `message` and returns a list of prefixes.

**Example**
```python
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
```

**Usage Note:** If used inside another callable, the returned callable must be invoked, e.g., `commands.when_mentioned_or(*extras)(bot, message)`.
```

--------------------------------

### Get Command by Name

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a `Command` object by its name, including aliases or fully qualified subcommand names. Returns `None` if not found.

```python
get_command(_name_)
```

--------------------------------

### Get Pinned Messages

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves pinned messages from a channel with optional filtering and ordering.

```APIDOC
## GET /channels/{channel.id}/pins

### Description
Retrieves a list of pinned messages in a specific channel.

### Method
GET

### Endpoint
`/channels/{channel.id}/pins`

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of pinned messages to retrieve. Defaults to 50. If None, retrieves all pinned messages.
- **before** (datetime.datetime or abc.Snowflake) - Optional - Retrieve pinned messages before this time or snowflake. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **oldest_first** (bool) - Optional - If set to True, return messages in oldest pin->newest pin order. Defaults to False.

### Raises
- **Forbidden** - You do not have the permission to retrieve pinned messages.
- **HTTPException** - Retrieving the pinned messages failed.

### Yields
- `Message` - The pinned message with `Message.pinned_at` set.
```

--------------------------------

### Utility and Data Structures

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Reference for various utility classes, event data, and media handling structures.

```APIDOC
## Utility and Data Structures

### Description
Provides access to various data structures used throughout the library, including thread management, asset handling, and interaction event data.

### Key Components
- **discord.Thread**: Represents a Discord thread, including archive status and tags.
- **discord.Attachment**: Represents a file attachment in a message.
- **discord.Asset**: Represents a CDN asset (e.g., avatars, icons).
- **discord.utils.as_chunks()**: Utility function to split iterables into chunks.
```

--------------------------------

### discord.on_ready()

Source: https://discordpy.readthedocs.io/en/latest/api.html

Called when the client is done preparing the data received from Discord. This event signifies that the client has successfully logged in and is ready to interact with guilds and other data.

```APIDOC
## discord.on_ready()

### Description
Called when the client is done preparing the data received from Discord. Usually after login is successful and the `Client.guilds` and co. are filled up.

**Warning**: This function is not guaranteed to be the first event called. Likewise, this function is **not** guaranteed to only be called once. This library implements reconnection logic and thus will end up calling this event whenever a RESUME request fails.

### Method
Event

### Endpoint
N/A (Internal Event)

### Parameters
None

### Request Example
N/A

### Response
N/A

#### Success Response (N/A)
N/A

#### Response Example
N/A
```

--------------------------------

### Create Webhook

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a webhook for a channel. Requires appropriate permissions.

```APIDOC
## _await _create_webhook(_*_ , _name_ , _avatar =None_, _reason =None_) 

### Description
Creates a webhook for a channel. You must have `manage_webhooks` to do this.

### Parameters
- **name** (`str`) – The name of the webhook.
- **avatar** (Optional[`bytes`]) – The avatar of the webhook as raw image bytes. Defaults to `None`.
- **reason** (Optional[`str`]) – The reason for creating this webhook. Shows up on the audit log.

### Raises
- **Forbidden** – You do not have permissions to create a webhook for this channel.
- **HTTPException** – Creating the webhook failed.
```

--------------------------------

### GET /channel/overwrites/{obj}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the channel-specific permission overwrites for a specific member or role.

```APIDOC
## GET /channel/overwrites/{obj}

### Description
Returns the channel-specific overwrites for a member or a role.

### Parameters
#### Path Parameters
- **obj** (Union[Role, User, Object]) - Required - The role or user denoting whose overwrite to get.

### Response
#### Success Response (200)
- **permissions** (PermissionOverwrite) - The permission overwrites for this object.
```

--------------------------------

### POST /sync

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Syncs the local application commands to Discord.

```APIDOC
## POST /sync

### Description
Syncs the application commands to Discord.

### Method
POST

### Parameters
#### Query Parameters
- **guild** (Snowflake) - Optional - The guild to sync commands for.
```

--------------------------------

### GET permissions_for

Source: https://discordpy.readthedocs.io/en/latest/api.html

Handles permission resolution for a specific Member or Role within the channel.

```APIDOC
## GET permissions_for

### Description
Handles permission resolution for the Member or Role, considering guild owner status, roles, channel overrides, and member timeouts.

### Parameters
#### Path Parameters
- **obj** (Union[Member, Role]) - Required - The object to resolve permissions for.
```

--------------------------------

### GET /channel/get_partial_message

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a PartialMessage object from a message ID without an API call.

```APIDOC
## GET /channel/get_partial_message

### Description
Creates a PartialMessage from the message ID. This is useful if you want to work with a message and only have its ID without doing an unnecessary API call.

### Method
GET

### Endpoint
channel.get_partial_message(message_id)

### Parameters
#### Path Parameters
- **message_id** (int) - Required - The message ID to create a partial message for.

### Response
#### Success Response (200)
- **PartialMessage** - The partial message object.
```

--------------------------------

### Configure specific intents manually

Source: https://discordpy.readthedocs.io/en/latest/intents.html

Demonstrates initializing an Intents object with only specific required intents enabled.

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

### Context Prefix and Resource Cleanup

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Information on accessing the clean prefix from a command context and cleaning up resources for audio and voice protocols.

```APIDOC
## Context Prefix and Resource Cleanup

### Description
This section covers accessing the cleaned command prefix from the context and methods for cleaning up resources used by audio sources and voice protocols.

### Context Clean Prefix
- `commands.Context.clean_prefix`

### Resource Cleanup
- `discord.AudioSource.cleanup()`
- `discord.FFmpegAudio.cleanup()`
- `discord.PCMVolumeTransformer.cleanup()`
- `discord.VoiceProtocol.cleanup()`
```

--------------------------------

### Get Message History

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns an asynchronous iterator for retrieving message history in a channel.

```APIDOC
## GET /channels/{channel.id}/messages

### Description
Returns an asynchronous iterator that enables receiving the destination’s message history. You must have `read_message_history` to do this.

### Method
GET

### Endpoint
`/channels/{channel.id}/messages`

### Parameters
#### Query Parameters
- **limit** (Optional[int]) - The number of messages to retrieve. If `None`, retrieves every message in the channel.
- **before** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages before this date or message.
- **after** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages after this date or message.
- **around** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages around this date or message. Maximum limit is 101.
- **oldest_first** (Optional[bool]) - If set to `True`, return messages in oldest->newest order.

### Raises
- **Forbidden** - You do not have the permissions to get channel message history.
- **HTTPException** - The request to get message history failed.

### Yields
- **Message** (Message) - The message with the message data parsed.

### Request Example
```python
counter = 0
async for message in channel.history(limit=200):
    if message.author == client.user:
        counter += 1
```

### Response Example
```python
messages = [message async for message in channel.history(limit=123)]
# messages is now a list of Message...
```
```

--------------------------------

### Command Signature

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Returns a POSIX-like signature string useful for help command output.

```APIDOC
## GET /signature

### Description
Returns a POSIX-like signature useful for help command output.

### Method
GET

### Endpoint
/signature

### Parameters
None

### Response
#### Success Response (200)
- **signature** (str) - The POSIX-like signature string.

#### Response Example
```json
{
  "signature": "[command]"
}
```
```

--------------------------------

### GET /guild/audit_logs

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves audit log entries for the guild based on specified filters.

```APIDOC
## GET /guild/audit_logs

### Description
Retrieves audit log entries for the guild. Allows filtering by date, user, and action type.

### Parameters
#### Query Parameters
- **after** (Union[Snowflake, datetime]) - Optional - Retrieve entries after this date or entry.
- **oldest_first** (bool) - Optional - If True, return entries in oldest to newest order.
- **user** (Snowflake) - Optional - The moderator to filter entries from.
- **action** (AuditLogAction) - Optional - The action to filter with.

### Response
#### Success Response (200)
- **AuditLogEntry** (Object) - The audit log entry.

### Errors
- **Forbidden** - You are not allowed to fetch audit logs.
- **HTTPException** - An error occurred while fetching the audit logs.
```

--------------------------------

### @discord.app_commands.describe

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Describes the given parameters by their name.

```APIDOC
## @discord.app_commands.describe

### Description
Describes the given parameters by their name using the key of the keyword argument as the name.

### Parameters
- **parameters** (Union[str, locale_str]) - Required - The description of the parameters.

### Errors
- **TypeError** - Raised if the parameter name is not found.
```

--------------------------------

### GET /guilds/{guild_id}/members/{member_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a specific member from a guild by their ID.

```APIDOC
## GET /guilds/{guild_id}/members/{member_id}

### Description
Retrieves a `Member` from a guild ID and a member ID.

### Method
GET

### Endpoint
/guilds/{guild_id}/members/{member_id}

### Parameters
#### Path Parameters
- **member_id** (int) - Required - The member’s ID to fetch from.

### Response
#### Success Response (200)
- **member** (`Member`) - The member from the member ID.
```

--------------------------------

### SyncWebhook Class Overview

Source: https://discordpy.readthedocs.io/en/latest/api.html

Provides an overview of the SyncWebhook class, its attributes, and available methods for synchronous webhook interactions.

```APIDOC
## SyncWebhook Class

Represents a synchronous Discord webhook. For an asynchronous counterpart, see `Webhook`.

### Attributes
- `avatar`: The avatar hash of the webhook.
- `channel`: The channel the webhook belongs to.
- `channel_id`: The ID of the channel the webhook belongs to.
- `created_at`: The creation timestamp of the webhook.
- `default_avatar`: The default avatar URL of the webhook.
- `display_avatar`: The display avatar of the webhook.
- `guild`: The guild the webhook belongs to.
- `guild_id`: The ID of the guild the webhook belongs to.
- `id`: The webhook's ID.
- `name`: The default name of the webhook.
- `source_channel`: The channel that this webhook is following (for channel follower webhooks).
- `source_guild`: The guild of the channel that this webhook is following (for channel follower webhooks).
- `token`: The authentication token of the webhook.
- `type`: The type of the webhook.
- `url`: The webhook's URL.
- `user`: The user who created the webhook.

### Methods
- `clsSyncWebhook.from_url(url, *, session=None, bot_token=None)`: Creates a partial `SyncWebhook` from a webhook URL.
- `clsSyncWebhook.partial(id, token, *, session=None, bot_token=None)`: Creates a partial `SyncWebhook`.
- `delete(*, reason=None, prefer_auth=True)`: Deletes this Webhook.
- `delete_message(message_id)`: Deletes a message sent by this webhook.
- `edit(*, reason=None, name=None, avatar=None, channel=None, prefer_auth=True)`: Edits this Webhook.
- `edit_message(message_id, *, content=None, embeds=None, file=None, files=None, username=None, avatar_url=None, allowed_mentions=None, view=None)`: Edits a message sent by this webhook.
- `fetch(*, prefer_auth=True)`: Fetches the current webhook.
- `fetch_message(message_id)`: Fetches a message sent by this webhook.
- `is_authenticated()`: Checks if the webhook is authenticated.
- `is_partial()`: Checks if the webhook is partial.
- `send(content=None, *, embeds=None, file=None, files=None, username=None, avatar_url=None, tts=False, files=None, allowed_mentions=None, view=None)`: Sends a message to the webhook's channel.
```

--------------------------------

### Get AppInfo Icon URL

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Use AppInfo.icon_url_as() to retrieve the application's icon URL in a specified format. Requires discord.py version 1.4+.

```python
await bot.application_info().icon_url_as(size=1024)
```

--------------------------------

### Registering Client Events via Subclassing

Source: https://discordpy.readthedocs.io/en/latest/api.html

Demonstrates how to register event handlers by subclassing discord.Client and overriding event methods. Ensure all event handlers are defined as coroutines using async def.

```python
import discord

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
```

--------------------------------

### GET /guilds/{guild_id}/threads/active

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of active threads that the client can access.

```APIDOC
## GET /guilds/{guild_id}/threads/active

### Description
Returns a list of active `Thread` objects that the client can access, including both private and public threads.

### Method
GET

### Endpoint
/guilds/{guild_id}/threads/active

### Response
#### Success Response (200)
- **threads** (List[`Thread`]) - The active threads.
```

--------------------------------

### GET /channels/{channel.id}/permissions/resolve

Source: https://discordpy.readthedocs.io/en/latest/api.html

Resolves permission for a given member or role, considering guild owner, roles, channel overrides, and implicit permissions.

```APIDOC
## GET /channels/{channel.id}/permissions/resolve

### Description
Handles permission resolution for the `Member` or `Role`. This function takes into consideration the following cases: Guild owner, Guild roles, Channel overrides, Member overrides, Implicit permissions, Member timeout, User installed app.

If a `Role` is passed, then it checks the permissions someone with that role would have.

Changed in version 2.0: The object passed in can now be a role object.
Changed in version 2.0: `obj` parameter is now positional-only.
Changed in version 2.4: User installed apps are now taken into account.

### Method
GET

### Endpoint
`/channels/{channel.id}/permissions/resolve`

### Parameters
#### Query Parameters
- **obj** (Union[`Member`, `Role`]) - Required - The object to resolve permissions for. This could be either a member or a role. If it’s a role then member overwrites are not computed.

### Response
#### Success Response (200)
- **`Permissions`** - The resolved permissions for the member or role.

#### Response Example
```json
{
  "read_messages": true,
  "send_messages": true,
  "manage_messages": false
}
```
```

--------------------------------

### GET /channels/{channel.id}/permissions/overwrites

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves all permission overwrites for a given channel. The result is a dictionary mapping roles or members to their specific permission overwrites.

```APIDOC
## GET /channels/{channel.id}/permissions/overwrites

### Description
Returns all of the channel’s overwrites. This is returned as a dictionary where the key contains the target which can be either a `Role` or a `Member` and the value is the overwrite as a `PermissionOverwrite`.

Changed in version 2.0: Overwrites can now be type-aware `Object` in case of cache lookup failure.

### Method
GET

### Endpoint
`/channels/{channel.id}/permissions/overwrites`

### Parameters
#### Path Parameters
- **channel.id** (int) - Required - The ID of the channel.

### Response
#### Success Response (200)
- **Dict[Union[`Role`, `Member`, `Object`], `PermissionOverwrite`]** - The channel’s permission overwrites.

#### Response Example
```json
{
  "@everyone": {
    "allow": 104324673,
    "deny": 0
  },
  "123456789012345678": {
    "allow": 8394657,
    "deny": 0
  }
}
```
```

--------------------------------

### Looping Task with a Fixed Count

Source: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

This example shows a task that runs a specific number of times (`count=5`) before automatically exiting. The `after_loop` decorator is used to execute a function once the loop has finished.

```python
from discord.ext import tasks
import discord

@tasks.loop(seconds=5.0, count=5)
async def slow_count():
    print(slow_count.current_loop)

@slow_count.after_loop
async def after_slow_count():
    print('done!')

class MyClient(discord.Client):
    async def setup_hook(self):
        slow_count.start()

```

--------------------------------

### GET /channels/{channel_id}/pins

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves an asynchronous iterator of the pinned messages in the channel.

```APIDOC
## GET /channels/{channel_id}/pins

### Description
Retrieves an asynchronous iterator of the pinned messages in the channel. Requires view_channel and read_message_history permissions.

### Method
GET

### Endpoint
/channels/{channel_id}/pins

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of messages to retrieve. Defaults to 50.
- **before** (Snowflake/datetime) - Optional - Retrieve messages before this date or message.
- **oldest_first** (bool) - Optional - If True, return messages in oldest to newest order.

### Response
#### Success Response (200)
- **Message** (object) - An asynchronous iterator of pinned message objects.
```

--------------------------------

### discord.ext.commands.Command.__call__()

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Details on the __call__ method for commands.Command objects.

```APIDOC
## discord.ext.commands.Command.__call__()

### Description
This method is called when a command is invoked.

### Method
N/A (Internal method)

### Endpoint
N/A

### Parameters
N/A

### Request Example
N/A

### Response
N/A
```

--------------------------------

### GET /channels/{channel_id}/messages/{id}

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a single message from the destination by its ID.

```APIDOC
## GET /channels/{channel_id}/messages/{id}

### Description
Retrieves a single Message from the destination.

### Method
GET

### Endpoint
/channels/{channel_id}/messages/{id}

### Parameters
#### Path Parameters
- **id** (int) - Required - The message ID to look for.

### Response
#### Success Response (200)
- **Message** (object) - The message object retrieved.

### Errors
- **NotFound**: The specified message was not found.
- **Forbidden**: You do not have the permissions required to get a message.
- **HTTPException**: Retrieving the message failed.
```

--------------------------------

### FFmpegOpusAudio Constructor

Source: https://discordpy.readthedocs.io/en/latest/api.html

Instantiate FFmpegOpusAudio directly to create an audio source from FFmpeg. This class produces Opus packets directly, bypassing the need for encoding.

```APIDOC
## FFmpegOpusAudio Constructor

### Description
An audio source from FFmpeg (or AVConv). This launches a sub-process to a specific input file given. However, rather than producing PCM packets like `FFmpegPCMAudio` does that need to be encoded to Opus, this class produces Opus packets, skipping the encoding step done by the library.

### Parameters
#### Path Parameters
- **source** (Union[`str`, `io.BufferedIOBase`]) - Required - The input that ffmpeg will take and convert to Opus bytes. If `pipe` is `True` then this is a file-like object that is passed to the stdin of ffmpeg.
- **bitrate** (`int`) - Optional - The bitrate in kbps to encode the output to. Defaults to `128`.
- **codec** (Optional[`str`]) - Optional - The codec to use to encode the audio data. Normally this would be just `libopus`, but is used by `FFmpegOpusAudio.from_probe()` to opportunistically skip pointlessly re-encoding Opus audio data by passing `copy` as the codec value. Any values other than `copy`, `opus`, or `libopus` will be considered `libopus`. Defaults to `libopus`.
- **executable** (`str`) - Optional - The executable name (and path) to use. Defaults to `ffmpeg`.
- **pipe** (`bool`) - Optional - If `True`, denotes that `source` parameter will be passed to the stdin of ffmpeg. Defaults to `False`.
- **stderr** (Optional[file object]) - Optional - A file-like object to pass to the Popen constructor.
- **before_options** (Optional[`str`]) - Optional - Extra command line arguments to pass to ffmpeg before the `-i` flag.
- **options** (Optional[`str`]) - Optional - Extra command line arguments to pass to ffmpeg after the `-i` flag.

### Raises
- **ClientException** - The subprocess failed to be created.
```

--------------------------------

### Register a Coroutine as a Pre-Invoke Hook

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Use the @before_invoke decorator to register a coroutine that runs before a command is invoked. This is useful for setup tasks and is only called if checks and argument parsing succeed.

```python
@before_invoke
def check_commands(ctx):
    return ctx.command.qualified_name in allowed_commands
```

--------------------------------

### Set Default Permissions for a Command

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Use the `@app_commands.default_permissions` decorator to specify default permissions required to use a command. This example sets `manage_messages` as a required permission.

```python
@app_commands.command()
@app_commands.default_permissions(manage_messages=True)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('You may or may not have manage messages.')
```

--------------------------------

### Slap command with Greedy converter

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Demonstrates using Greedy to accept multiple members in a single command argument.

```python
@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')
```

--------------------------------

### Get Channel by ID

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a channel or thread by its ID. Returns `None` if not found.

```python
get_channel(_id_)
```

--------------------------------

### Hybrid Command with FlagConverter

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Demonstrates how a `FlagConverter` is flattened into individual parameters when used with a hybrid command. This shows the equivalent application command signature.

```python
class BanFlags(commands.FlagConverter):
    member: discord.Member
    reason: str
    days: int = 1


@commands.hybrid_command()
async def ban(ctx, *, flags: BanFlags):
    ...

```

```python
@commands.hybrid_command()
async def ban(ctx, member: discord.Member, reason: str, days: int = 1):
    ...

```

--------------------------------

### Registering a Before-Invoke Hook

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Use the `before_invoke` decorator to register a coroutine that runs before a command is invoked. This can be used for logging or setup tasks across multiple commands or cogs.

```python
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

    @commands.command()
    async def where(self, ctx):
        await ctx.send('on Discord')

    @commands.command()
    async def why(self, ctx):
        await ctx.send('because someone made me')
```

--------------------------------

### POST /commands

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Adds an application command to the local tree.

```APIDOC
## POST /commands

### Description
Adds an application command to the tree. Note that this only adds the command locally; sync() must be called to enable them in the client.

### Method
POST

### Endpoint
/commands

### Parameters
#### Request Body
- **command** (Union[Command, Group]) - Required - The application command or group to add.
- **guild** (Snowflake) - Optional - The guild to add the command to.
- **guilds** (List[Snowflake]) - Optional - A list of guilds to add the command to.
- **override** (bool) - Optional - Whether to override a command with the same name. Defaults to False.
```

--------------------------------

### AppInfo Icon URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of AppInfo.icon_url_as with AppInfo.icon.replace.

```python
AppInfo.icon.replace
```

--------------------------------

### Colour Comparison and Conversion

Source: https://discordpy.readthedocs.io/en/latest/api.html

Illustrates how to compare Colour objects and convert them to different formats.

```APIDOC
## Colour Operations

### Equality Check
```python
colour1 = discord.Colour.red()
colour2 = discord.Colour.from_rgb(255, 0, 0)

print(colour1 == colour2) # Output: True
print(colour1 != colour2) # Output: False
```

### Get RGB Tuple
```python
colour = discord.Colour.blue()
rgb_tuple = colour.to_rgb()
print(rgb_tuple) # Output: (52, 152, 219)
```

### Get Raw Value
```python
colour = discord.Colour.green()
raw_value = int(colour)
print(raw_value) # Output: 4771215
```

### Get Hex String
```python
colour = discord.Colour.purple()
hex_string = str(colour)
print(hex_string) # Output: #9B59B6
```
```

--------------------------------

### Get Channel Messages

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of messages from a channel with various filtering and ordering options.

```APIDOC
## GET /channels/{channel.id}/messages

### Description
Retrieves a list of messages from a channel. All parameters are optional.

### Method
GET

### Endpoint
/channels/{channel.id}/messages

### Parameters
#### Query Parameters
- **limit** (Optional[int]) - The number of messages to retrieve. If `None`, retrieves every message in the channel. Note, however, that this would make it a slow operation.
- **before** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages before this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **after** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages after this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **around** (Optional[Union[Snowflake, datetime.datetime]]) - Retrieve messages around this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time. When using this argument, the maximum limit is 101. Note that if the limit is an even number then this will return at most limit + 1 messages.
- **oldest_first** (Optional[bool]) - If set to `True`, return messages in oldest->newest order. Defaults to `True` if `after` is specified, otherwise `False`.

### Raises
- **Forbidden** - You do not have permissions to get channel message history.
- **HTTPException** - The request to get message history failed.

### Yields
- `Message` - The message with the message data parsed.
```

--------------------------------

### ActionRow Class Overview

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Provides an overview of the ActionRow class and its core functionalities.

```APIDOC
## ActionRow Class

Represents an action row in a Discord UI view, used to group interactive components like buttons and select menus.

### Properties

- **_id** (Optional[int]) - The unique identifier for this component within the view.
- **_children** (List[Item]) - A list of UI items (components) contained within this action row.
- **_parent** (Optional[Item]) - The parent item, if this action row is nested.
- **_view** (Optional[Union[View, LayoutView]]) - The underlying view associated with this action row.

### Methods

- **__init__(*children, id=None)**
  Initializes an ActionRow with optional initial children and an ID.
  Parameters:
    - *children* (Item) – The initial children of this action row.
    - id (Optional[int]) – The ID of this component. This must be unique across the view.

- **content_length() -> int**
  Returns the total length of all text content in this action row.

- **add_item(item: Item)**
  Adds an item to this action row. Returns the instance for chaining.
  Parameters:
    - item (Item) – The item to add to the action row.
  Raises:
    - TypeError – If the provided item is not an `Item`.
    - ValueError – If the maximum number of children (5) is exceeded, or the view's total limit (40) is reached.

- **remove_item(item: Item)**
  Removes an item from this action row. Returns the instance for chaining.
  Parameters:
    - item (Item) – The item to remove from the action row.

- **find_item(id: int) -> Optional[Item]**
  Retrieves an item by its ID. Note: This is not the same as `custom_id`.
  Parameters:
    - id (int) – The ID of the component to find.
  Returns:
    - Optional[Item] – The found item, or `None` if not found.

- **clear_items()**
  Removes all items from this action row. Returns the instance for chaining.

- **_walk_children()**
  An iterator that recursively walks through all children of this action row.
  Yields:
    - Item – An item in the action row.

- **_interaction_check(interaction: Interaction) -> bool**
  A coroutine callback to check if an interaction should be processed by this item. Defaults to returning `True`.
  Parameters:
    - interaction (Interaction) – The interaction that occurred.
  Returns:
    - bool – Whether the callback should be called.

```

--------------------------------

### GET /channels/{channel.id}/pins

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of pinned messages in a channel. All parameters are optional.

```APIDOC
## GET /channels/{channel.id}/pins

### Description
Retrieves a list of pinned messages in a channel.

### Method
GET

### Endpoint
/channels/{channel.id}/pins

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of pinned messages to retrieve. Defaults to 50.
- **before** (datetime or Snowflake) - Optional - Retrieve pinned messages before this time or snowflake.
- **oldest_first** (bool) - Optional - If True, return messages in oldest pin->newest pin order. Defaults to False.

### Raises
- **Forbidden** - You do not have the permission to retrieve pinned messages.
- **HTTPException** - Retrieving the pinned messages failed.

### Yields
- **Message** - The pinned message with `Message.pinned_at` set.
```

--------------------------------

### Fetch Webhook

Source: https://discordpy.readthedocs.io/en/latest/api.html

Fetches the current webhook. This could be used to get a full webhook from a partial webhook. New in version 2.0. When fetching with an unauthenticated webhook, i.e. is_authenticated() returns False, then the returned webhook does not contain any user information.

```APIDOC
## Fetch Webhook

### Description
Fetches the current webhook. This could be used to get a full webhook from a partial webhook.

### Parameters
#### Query Parameters
- **prefer_auth** (bool) - Optional - Whether to use the bot token over the webhook token if available. Defaults to `True`.

### Raises
- **HTTPException** - Could not fetch the webhook
- **NotFound** - Could not find the webhook by this ID
- **ValueError** - This webhook does not have a token associated with it.

### Returns
The fetched webhook.

### Return Type
`Webhook`
```

--------------------------------

### Simplified Late Binding with Built-in Defaults

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Leverage built-in default parameter providers like `commands.Author` for common late binding scenarios, simplifying command definitions.

```python
@bot.command()
async def wave(ctx, to: discord.User = commands.Author):
    await ctx.send(f'Hello {to.mention} :wave:')
```

--------------------------------

### GET /scheduled-events/{event_id}/users

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of users subscribed to the specified scheduled event.

```APIDOC
## GET /scheduled-events/{event_id}/users

### Description
Retrieves all users subscribed to this event. Requires Intents.members.

### Method
GET

### Endpoint
/scheduled-events/{event_id}/users

### Parameters
#### Query Parameters
- **limit** (int) - Optional - Max number of users to return.
- **before** (snowflake) - Optional - Get users before this ID.
- **after** (snowflake) - Optional - Get users after this ID.
- **oldest_first** (bool) - Optional - Sort order.

### Response
#### Success Response (200)
- **users** (List[User]) - List of subscribed users.
```

--------------------------------

### GET /guilds/{guild_id}/bans/{user_id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the ban entry for a specific user in the guild.

```APIDOC
## GET /guilds/{guild_id}/bans/{user_id}

### Description
Retrieves the `BanEntry` for a user. Requires `ban_members` permission.

### Method
GET

### Endpoint
/guilds/{guild_id}/bans/{user_id}

### Parameters
#### Path Parameters
- **user** (`abc.Snowflake`) - Required - The user to get ban information from.

### Response
#### Success Response (200)
- **ban_entry** (`BanEntry`) - The `BanEntry` object for the specified user.
```

--------------------------------

### GET /channels/{channel_id}/messages

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of messages from a channel with optional filtering parameters.

```APIDOC
## GET /channels/{channel_id}/messages

### Description
Retrieves message history from a channel. All parameters are optional.

### Method
GET

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of messages to retrieve.
- **before** (Snowflake/datetime) - Optional - Retrieve messages before this date or message.
- **after** (Snowflake/datetime) - Optional - Retrieve messages after this date or message.
- **around** (Snowflake/datetime) - Optional - Retrieve messages around this date or message.
- **oldest_first** (bool) - Optional - If True, return messages in oldest to newest order.

### Response
- **Message** (List) - A list of message objects.
```

--------------------------------

### Extend existing command checks

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Demonstrates how to wrap an existing check to add custom logic, such as allowing the guild owner to bypass other restrictions.

```python
def owner_or_permissions(**perms):
    original = commands.has_permissions(**perms).predicate
    async def extended_check(ctx):
        if ctx.guild is None:
            return False
        return ctx.guild.owner_id == ctx.author.id or await original(ctx)
    return commands.check(extended_check)
```

--------------------------------

### HelpCommand Methods

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Details the various methods available in the HelpCommand class for customizing help message generation and handling command lookups.

```APIDOC
## HelpCommand Methods

### `add_check(func, /)`

Adds a check to the help command.

Parameters:
- **func** (function) - The function that will be used as a check.

### `asynccommand_callback()`

(Coroutine) The callback for the help command.

### `asyncfilter_commands(cog, commands, /)`

(Coroutine) Filters the commands to be shown.

Parameters:
- **cog** (Cog) - The cog to filter commands for.
- **commands** (List[Command]) - The list of commands to filter.

Returns:
- The filtered list of commands.

### `defcommand_not_found(string, /)`

This function _could be a_ _coroutine_. A method called when a command is not found in the help command. This is useful to override for i18n.

Parameters:
- **string** (str) - The string that contains the invalid command.

Returns:
- The string to use when a command has not been found.

### `defget_bot_mapping()`

Retrieves the bot mapping passed to `send_bot_help()`.

### `defget_command_signature(command, /)`

Retrieves the signature portion of the help page.

Parameters:
- **command** (Command) - The command to get the signature of.

Returns:
- The signature for the command.

### `defget_destination()`

Retrieves the destination to send the help message to.

### `defget_max_size()`

Retrieves the maximum size for the help message.

### `asyncon_help_command_error(ctx, error)`

(Coroutine) Called when an error occurs during the help command invocation.

Parameters:
- **ctx** (Context) - The context of the command invocation.
- **error** (CommandError) - The error that occurred.

### `asyncprepare_help_command(ctx, command)`

(Coroutine) Prepares the help command for invocation.

Parameters:
- **ctx** (Context) - The context of the command invocation.
- **command** (Optional[Command]) - The command to prepare help for.

### `defremove_check(func, /)`

Removes a check from the help command.

Parameters:
- **func** (function) - The function to remove from the checks.

### `defremove_mentions(string, /)`

Removes mentions from the string to prevent abuse.

Parameters:
- **string** (str) - The string with mentions to remove.

Returns:
- The string with mentions removed.

### `asyncsend_bot_help(mapping)`

(Coroutine) Sends the help message for the entire bot.

Parameters:
- **mapping** (Dict[Cog, List[Command]]) - A mapping of cogs to their commands.

### `asyncsend_cog_help(cog)`

(Coroutine) Sends the help message for a specific cog.

Parameters:
- **cog** (Cog) - The cog to send help for.

### `asyncsend_command_help(command)`

(Coroutine) Sends the help message for a specific command.

Parameters:
- **command** (Command) - The command to send help for.

### `asyncsend_error_message(message, /)`

(Coroutine) Sends an error message to the user.

Parameters:
- **message** (str) - The error message to send.

### `asyncsend_group_help(command)`

(Coroutine) Sends the help message for a specific group command.

Parameters:
- **command** (Group) - The group command to send help for.

### `defsubcommand_not_found(command, string, /)`

This function _could be a_ _coroutine_. A method called when a command did not have a subcommand requested in the help command.

Parameters:
- **command** (Command) - The command that was requested.
- **string** (str) - The string that represents the subcommand.

Returns:
- The string to use when a subcommand has not been found.
```

--------------------------------

### Using typing.List for Multiple Flags

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Use `typing.List` in a `FlagConverter` to allow a flag to be passed multiple times. This example shows how to ban multiple members with a single command invocation.

```python
from discord.ext import commands
from typing import List
import discord

class BanFlags(commands.FlagConverter):
    members: List[discord.Member] = commands.flag(name='member')
    reason: str
    days: int = 1

@commands.command()
async def ban(ctx, *, flags: BanFlags):
    for member in flags.members:
        await member.ban(reason=flags.reason, delete_message_days=flags.days)

    members = ', '.join(str(member) for member in flags.members)
    plural = f'{flags.days} days' if flags.days != 1 else f'{flags.days} day'
    await ctx.send(f'Banned {members} for {flags.reason!r} (deleted {plural} worth of messages)')

```

--------------------------------

### Edit Onboarding Configuration

Source: https://discordpy.readthedocs.io/en/latest/api.html

Updates the onboarding configuration for a guild. Requires manage_guild and manage_roles permissions.

```APIDOC
## PATCH /guilds/{guild_id}/onboarding

### Description
Updates the onboarding configuration for a guild. This requires the manage_guild and manage_roles permissions.

### Method
PATCH

### Parameters
#### Request Body
- **prompts** (List[OnboardingPrompt]) - Optional - The prompts that will be shown to new members.
- **default_channels** (List[abc.Snowflake]) - Optional - The channels that will be used as the default channels for new members.
- **enabled** (bool) - Optional - Whether the onboarding configuration is enabled.
- **mode** (OnboardingMode) - Optional - The mode that will be used for the onboarding configuration.
- **reason** (str) - Optional - The reason for editing the onboarding configuration, shown in the audit log.

### Response
#### Success Response (200)
- **onboarding** (Onboarding) - The updated onboarding configuration.
```

--------------------------------

### Define Parameter Choices with app_commands.choices

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Restricts parameter input to a predefined set of choices.

```python
@app_commands.command()
```

--------------------------------

### Create a minimal Discord bot

Source: https://discordpy.readthedocs.io/en/latest/quickstart.html

A basic implementation of a bot that responds to a '$hello' message. Requires the 'message_content' intent to be enabled.

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

### Gateway Intents Configuration

Source: https://discordpy.readthedocs.io/en/latest/api.html

Overview of available intent flags and their associated events and cache mappings.

```APIDOC
## Gateway Intents Configuration

### Description
Intents allow bots to subscribe to specific groups of events. Below are the available boolean flags and their mappings.

### Parameters
#### Request Body
- **integrations** (bool) - Optional - Whether guild integration related events are enabled.
- **webhooks** (bool) - Optional - Whether guild webhook related events are enabled.
- **invites** (bool) - Optional - Whether guild invite related events are enabled.
- **voice_states** (bool) - Optional - Whether guild voice state related events are enabled. Required to connect to voice.
- **presences** (bool) - Optional - Whether guild presence related events are enabled. Requires explicit opt-in in developer portal.
- **messages** (bool) - Optional - Shortcut for both guild_messages and dm_messages.
- **guild_messages** (bool) - Optional - Whether guild message related events are enabled.
- **dm_messages** (bool) - Optional - Whether direct message related events are enabled.
- **reactions** (bool) - Optional - Shortcut for both guild_reactions and dm_reactions.
```

--------------------------------

### Member Avatar Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the replacement of Member.avatar with Member.avatar.key.

```python
Member.avatar.key
```

--------------------------------

### GET /channels/{channel.id}/permissions/overwrites/{obj.id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the channel-specific permission overwrites for a particular member or role.

```APIDOC
## GET /channels/{channel.id}/permissions/overwrites/{obj.id}

### Description
Returns the channel-specific overwrites for a member or a role.

### Method
GET

### Endpoint
`/channels/{channel.id}/permissions/overwrites/{obj.id}`

### Parameters
#### Path Parameters
- **channel.id** (int) - Required - The ID of the channel.
- **obj** (Union[`Role`, `User`, `Object`]) - Required - The role or user denoting whose overwrite to get.

### Response
#### Success Response (200)
- **`PermissionOverwrite`** - The permission overwrites for this object.

#### Response Example
```json
{
  "allow": 8394657,
  "deny": 0
}
```
```

--------------------------------

### GET /channels/{channel.id}/messages/{message.id}

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a single message from the channel. Requires 'read_message_history' permission.

```APIDOC
## GET /channels/{channel.id}/messages/{message.id}

### Description
Retrieves a single `Message` from the destination. You must have `read_message_history` to do this.

### Method
GET

### Endpoint
/channels/{channel.id}/messages/{message.id}

### Parameters
#### Path Parameters
- **id** (int) - Required - The message ID to look for.

### Response
#### Success Response (200)
- **Message** (Message) - The message asked for.

#### Error Response
- **NotFound** - The specified message was not found.
- **Forbidden** - You do not have the permissions required to get a message.
- **HTTPException** - Retrieving the message failed.
```

--------------------------------

### Subclassing Context

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Custom context classes can be defined by inheriting from commands.Context.

```python
class MyContext(commands.Context):
    @property
    def secret(self):
        return 'my secret here'
```

--------------------------------

### Stage Instance Events

Source: https://discordpy.readthedocs.io/en/latest/api.html

Documentation for stage instance creation, update, and deletion events.

```APIDOC
## Stage Instance Events

### Description
Events triggered when a stage instance is started, updated, or ended.

### AuditLogDiff Attributes
- **topic** (String) - The topic of the stage.
- **privacy_level** (Integer) - The privacy level of the stage.
```

--------------------------------

### Get Discord Channel Webhooks

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of webhooks associated with a channel. Requires `manage_webhooks` permission.

```python
await channel.webhooks()
```

--------------------------------

### Get Cog Instance

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a specific cog instance by its name. Returns `None` if the cog is not found.

```python
get_cog(_name_)
```

--------------------------------

### Update Client Execution Pattern

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_async.html

The client run method now handles authentication directly, replacing the separate login and run calls.

```python
client.login('token')
client.run()
```

```python
client.run('token')
```

--------------------------------

### Get Shard Information

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Retrieve information about a specific shard from the AutoShardedClient. Useful for managing individual shards.

```Python
shard_info = await bot.get_shard(0)
```

--------------------------------

### Get Emoji URL

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Use Emoji.url_as() to retrieve the URL for a custom emoji in a specified format and size.

```python
emoji_url = emoji.url_as(format='png', size=128)
```

--------------------------------

### AppCommand Methods

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Details the asynchronous methods available for interacting with application commands, including deletion, editing, and fetching permissions.

```APIDOC
## AppCommand Methods

### `async delete()`

Deletes the application command.

**Raises:**
- **NotFound**: The application command was not found.
- **Forbidden**: You do not have permission to delete this application command.
- **HTTPException**: Deleting the application command failed.
- **MissingApplicationID**: The client does not have an application ID.

### `async edit()`

Edits the application command.

**Parameters:**
- **name** (str): The new name for the application command.
- **description** (str): The new description for the application command.
- **default_member_permissions** (Optional[Permissions]): The new default permissions needed to use this application command. Pass `None` to remove permission requirements.
- **dm_permission** (bool): Indicates if the application command can be used in DMs.
- **options** (List[Union[Argument, AppCommandGroup]]): List of new options for this application command.

**Raises:**
- **NotFound**: The application command was not found.
- **Forbidden**: You do not have permission to edit this application command.
- **HTTPException**: Editing the application command failed.
- **MissingApplicationID**: The client does not have an application ID.

**Returns:**
- `AppCommand`: The newly edited application command.

### `async fetch_permissions(guild)`

Retrieves this command’s permission in the guild.

**Parameters:**
- **guild** (Snowflake): The guild to retrieve the permissions from.

**Raises:**
- **Forbidden**: You do not have permission to fetch the application command’s permissions.
- **HTTPException**: Fetching the application command’s permissions failed.
- **MissingApplicationID**: The client does not have an application ID.
- **NotFound**: The application command’s permissions could not be found or are synced with the guild.

**Returns:**
- `GuildAppCommandPermissions`: An object representing the application command’s permissions in the guild.
```

--------------------------------

### Command and Event Decorators

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Decorators for creating and registering commands and events.

```APIDOC
## Command and Event Decorators

### @command

- **Description**: A shortcut decorator that invokes `command()` and adds the decorated method to the bot's internal command list via `add_command()`.
- **Returns**: A decorator that converts a method into a `Command`, adds it to the bot, and returns it.
- **Return type**: Callable[..., `Command`]

### @event

- **Description**: Decorator for registering event listeners.
```

--------------------------------

### Fetch and send content from URL

Source: https://discordpy.readthedocs.io/en/latest/faq.html

Demonstrates fetching data from an external URL using aiohttp and sending it to a channel.

```python
async with aiohttp.ClientSession() as session:
    async with session.get('http://aws.random.cat/meow') as r:
        if r.status == 200:
            js = await r.json()
            await channel.send(js['file'])
```

--------------------------------

### GET /channels/{channel_id}/webhooks

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of webhooks associated with a specific channel. Requires manage_webhooks permission.

```APIDOC
## GET /channels/{channel_id}/webhooks

### Description
Gets the list of webhooks from this channel. You must have `manage_webhooks` to do this.

### Method
GET

### Endpoint
/channels/{channel_id}/webhooks

### Response
#### Success Response (200)
- **webhooks** (List[Webhook]) - The webhooks for this channel.

### Errors
- **Forbidden** - You don’t have permissions to get the webhooks.
```

--------------------------------

### AppCommand Class Overview

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Provides an overview of the AppCommand class, its attributes, and its purpose in representing Discord application commands.

```APIDOC
## AppCommand Class

Represents an application command, commonly referred to as a “Slash Command” or a “Context Menu Command”.

### Attributes
- **allowed_contexts** (Optional[AppCommandContext]): The contexts that this command is allowed to be used in. Overrides the `dm_permission` attribute.
- **allowed_installs** (Optional[AppInstallationType]): The installation contexts that this command is allowed to be installed in.
- **application_id** (int): The application command’s application’s ID.
- **default_member_permissions** (Optional[Permissions]): The default member permissions that can run this command.
- **description** (str): The application command’s description.
- **description_localizations** (Dict[Locale, str]): The localised descriptions of the application command.
- **dm_permission** (bool): A boolean that indicates whether this command can be run in direct messages.
- **guild** (Optional[Guild]): The guild this command is registered to if it exists.
- **guild_id** (Optional[int]): The ID of the guild this command is registered in. `None` denotes a global command.
- **id** (int): The application command’s ID.
- **mention** (str): A string that allows you to mention the given AppCommand.
- **name** (str): The application command’s name.
- **name_localizations** (Dict[Locale, str]): The localised names of the application command.
- **nsfw** (bool): Whether the command is NSFW and should only work in NSFW channels.
- **options** (List[Union[Argument, AppCommandGroup]]): A list of options for the command.
- **type** (AppCommandType): The application command’s type.

### Equality Comparison
- **x == y**: Checks if two application commands are equal.
- **x != y**: Checks if two application commands are not equal.

### Hashing
- **hash(x)**: Returns the application command’s hash.

### String Representation
- **str(x)**: Returns the application command’s name.
```

--------------------------------

### POST /channels/{channel_id}/invites

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates an instant invite for a specific channel.

```APIDOC
## POST /channels/{channel_id}/invites

### Description
Creates an instant invite for the channel. Requires appropriate permissions.

### Parameters
#### Request Body
- **max_age** (int) - Optional - How long the invite should last in seconds. Defaults to 0 (no expiry).
- **max_uses** (int) - Optional - How many uses the invite could be used for. Defaults to 0 (unlimited).
- **temporary** (bool) - Optional - Denotes that the invite grants temporary membership. Defaults to False.
- **unique** (bool) - Optional - Indicates if a unique invite URL should be created. Defaults to True.
- **reason** (str) - Optional - The reason for creating this invite for the audit log.
- **target_type** (InviteTarget) - Optional - The type of target for the voice channel invite.
- **target_user** (User) - Optional - The user whose stream to display for this invite.
- **target_application_id** (int) - Optional - The id of the embedded application for the invite.
- **guest** (bool) - Optional - Whether the invite is a guest invite.

### Response
#### Success Response (200)
- **Invite** (Invite) - The invite object that was created.

### Errors
- **HTTPException**: Invite creation failed.
- **NotFound**: The channel is a category or invalid.
```

--------------------------------

### Get Emoji URL

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns the URL of the emoji if it is a custom emoji. Returns an empty string if it is not a custom emoji.

```python
_property _url
```

--------------------------------

### Get Audit Logs

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an asynchronous iterator for the guild's audit logs. Requires `view_audit_log` permission.

```APIDOC
## GET /api/guilds/{guild_id}/audit-logs

### Description
Returns an asynchronous iterator that enables receiving the guild’s audit logs.

### Method
GET

### Endpoint
/api/guilds/{guild_id}/audit-logs

### Parameters
#### Query Parameters
- **limit** (integer) - Optional - The number of entries to retrieve. If `None`, retrieve all entries.
- **before** (Snowflake or datetime) - Optional - Retrieve entries before this date or entry. If a datetime is provided, it is recommended to use a UTC aware datetime.
- **after** (Snowflake or datetime) - Optional - Retrieve entries after this date or entry.
- **oldest_first** (boolean) - Optional - If `True`, entries are returned in ascending order (oldest first).
- **user** (Snowflake) - Optional - Filter logs by a specific user.
- **action** (AuditLogAction) - Optional - Filter logs by a specific action type.

### Request Body
(No request body specified)

### Response
#### Success Response (200)
- **AuditLogIterator** (AsyncIterator) - An iterator yielding audit log entries.

#### Error Response
- **Forbidden** - You do not have the proper permissions to view audit logs.
- **HTTPException** - Retrieving audit logs failed.
```

--------------------------------

### Pre-v1.0 Converter Implementation

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Illustrates the older method of defining a converter using a synchronous `convert` method before version 1.0. This approach did not support asynchronous operations directly within the converter.

```python
class MyConverter(commands.Converter):
    def convert(self):
        return self.ctx.message.server.me
```

--------------------------------

### GET /channels/{channel_id}/history

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Returns an asynchronous iterator that enables receiving the destination’s message history.

```APIDOC
## GET /channels/{channel_id}/history

### Description
Returns an asynchronous iterator that enables receiving the destination’s message history. Requires read_message_history permission.

### Method
GET

### Endpoint
/channels/{channel_id}/history

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The number of messages to retrieve. Defaults to 100.
- **before** (Snowflake/datetime) - Optional - Retrieve messages before this date or message.
- **after** (Snowflake/datetime) - Optional - Retrieve messages after this date or message.
- **around** (Snowflake/datetime) - Optional - Retrieve messages around this date or message.
- **oldest_first** (bool) - Optional - If True, return messages in oldest to newest order.

### Response
#### Success Response (200)
- **Message** (object) - An asynchronous iterator of message objects.

### Errors
- **Forbidden**: You do not have permissions to get channel message history.
- **HTTPException**: The request to get message history failed.
```

--------------------------------

### Event Listeners

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Demonstrates how to add event listeners to the bot, both through decorators and direct function calls.

```APIDOC
## Event Listeners

### Description
This section covers methods for registering event listeners for the bot.

### `bot.listen()` decorator

#### Example
```python
@bot.listen('on_message')
async def my_message(message):
    print('two')
```

### `bot.add_listener()` method

#### Description
The non-decorator alternative to `listen()`.

#### Method
`add_listener(func, name=None)`

#### Parameters
*   **func** (coroutine) - The function to call.
*   **name** (str) - The name of the event to listen for. Defaults to `func.__name__`.

#### Request Example
```python
async def on_ready(): pass
async def my_message(message): pass

bot.add_listener(on_ready)
bot.add_listener(my_message, 'on_message')
```

### `bot.add_dynamic_items()` method

#### Description
Registers `DynamicItem` classes for persistent listening.

#### Method
`add_dynamic_items(*items)`

#### Parameters
*   **items** (Type[`DynamicItem`]) - The classes of dynamic items to add.

#### Raises
*   **TypeError** - A class is not a subclass of `DynamicItem`.

### `bot.add_view()` method

#### Description
Registers a `View` for persistent listening.

#### Method
`add_view(view, *, message_id=None)`

#### Parameters
*   **view** (Union[`discord.ui.View`, `discord.ui.LayoutView`]) - The view to register for dispatching.
*   **message_id** (Optional[`int`]) - The message ID that the view is attached to.

#### Raises
*   **TypeError** - A view was not passed.
*   **ValueError** - The view is not persistent or is already finished.

### `bot.add_check()` method

#### Description
Adds a global check to the bot. This is the non-decorator interface to `check()` and `check_once()`.

#### Method
`add_check(_func_, /, *_ , call_once=False)`

#### Parameters
*   **func** - The function that was used as a global check.
*   **call_once** (`bool`) - If the function should only be called once per `invoke()` call.

#### Raises
*   **TypeError** - The function being listened to is not a coroutine.
```

--------------------------------

### Command and Cog Utilities

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Documentation for various functions and classes related to command handling, cogs, and converters in discord.py.

```APIDOC
## Command and Cog Utilities

### Description
This section covers utility functions for retrieving commands, cogs, context, and handling command parameters and signatures.

### Functions and Classes
- **commands.GameConverter**: A converter for game objects.
- **discord.Game**: Represents a game being played by a user.
- **discord.Streaming.game**: The game being streamed.
- **discord.utils.get()**: A general utility function to get an object from an iterable based on criteria.
- **commands.Bot.get_all_channels()**: Gets all channels the bot can see.
- **discord.Client.get_all_channels()**: Gets all channels the bot can see.
- **commands.Bot.get_all_members()**: Gets all members across all guilds the bot is in.
- **discord.Client.get_all_members()**: Gets all members across all guilds the bot is in.
- **discord.Poll.get_answer()**: Retrieves an answer from a poll.
- **commands.Cog.get_app_commands()**: Gets all application commands associated with a cog.
- **commands.HelpCommand.get_bot_mapping()**: Gets a mapping of bots to their cogs for help command generation.
- **discord.Client.get_channel()**: Gets a channel by its ID.
- **commands.Bot.get_channel()**: Gets a channel by its ID.
- **discord.Guild.get_channel()**: Gets a channel within a guild by its ID.
- **discord.Guild.get_channel_or_thread()**: Gets a channel or thread within a guild by its ID.
- **commands.Bot.get_cog()**: Retrieves a cog instance by its name.
- **discord.app_commands.CommandTree.get_command()**: Gets an application command from the command tree by its name.
- **discord.app_commands.Group.get_command()**: Gets a subcommand from a group by its name.
- **commands.Bot.get_command()**: Retrieves a command from the bot by its name.
- **commands.Group.get_command()**: Retrieves a subcommand from a group by its name.
- **commands.GroupMixin.get_command()**: Retrieves a subcommand from a group-like structure.
- **commands.HybridGroup.get_command()**: Retrieves a subcommand from a hybrid group.
- **commands.DefaultHelpCommand.get_command_signature()**: Gets the signature of a command for the default help command.
- **commands.HelpCommand.get_command_signature()**: Gets the signature of a command.
- **commands.MinimalHelpCommand.get_command_signature()**: Gets the signature of a command for the minimal help command.
- **discord.app_commands.CommandTree.get_commands()**: Gets all application commands from the command tree.
- **commands.Cog.get_commands()**: Gets all commands associated with a cog.
- **commands.Bot.get_context()**: Gets the context for a given message.
- **commands.Command.get_cooldown_retry_after()**: Gets the remaining time until a command's cooldown expires.
- **commands.Group.get_cooldown_retry_after()**: Gets the remaining time until a group's cooldown expires.
- **commands.HybridGroup.get_cooldown_retry_after()**: Gets the remaining time until a hybrid group's cooldown expires.
- **commands.Parameter.get_default()**: Gets the default value of a command parameter.
- **commands.DefaultHelpCommand.get_destination()**: Gets the destination for help messages.
- **commands.HelpCommand.get_destination()**: Gets the destination for help messages.
- **commands.MinimalHelpCommand.get_destination()**: Gets the destination for help messages.
- **discord.Client.get_emoji()**: Gets an emoji by its ID.
- **commands.Bot.get_emoji()**: Gets an emoji by its ID.
- **discord.Guild.get_emoji()**: Gets an emoji from a guild by its ID.
- **commands.DefaultHelpCommand.get_ending_note()**: Gets the ending note for the default help command.
- **commands.MinimalHelpCommand.get_ending_note()**: Gets the ending note for the minimal help command.
- **commands.FlagConverter.get_flags()**: Retrieves flags from a converter.
- **discord.Client.get_guild()**: Gets a guild by its ID.
- **commands.Bot.get_guild()**: Gets a guild by its ID.
- **commands.Cog.get_listeners()**: Gets all listener functions associated with a cog.
- **commands.HelpCommand.get_max_size()**: Gets the maximum size for help messages.
- **discord.Guild.get_member()**: Gets a member from a guild by their ID.
- **discord.Guild.get_member_named()**: Gets a member from a guild by their name or ID.
- **commands.MinimalHelpCommand.get_opening_note()**: Gets the opening note for the minimal help command.
- **discord.OnboardingPrompt.get_option()**: Retrieves an option from an onboarding prompt.
- **discord.app_commands.Command.get_parameter()**: Gets a parameter from an application command by its name.
- **discord.DMChannel.get_partial_message()**: Gets a partial message from a DM channel.
- **discord.PartialMessageable.get_partial_message()**: Gets a partial message from a messageable entity.
- **discord.StageChannel.get_partial_message()**: Gets a partial message from a stage channel.
- **discord.TextChannel.get_partial_message()**: Gets a partial message from a text channel.
- **discord.Thread.get_partial_message()**: Gets a partial message from a thread.
- **discord.VoiceChannel.get_partial_message()**: Gets a partial message from a voice channel.
- **discord.Client.get_partial_messageable()**: Gets a partial messageable entity.
- **commands.Bot.get_partial_messageable()**: Gets a partial messageable entity.
- **commands.Bot.get_prefix()**: Gets the prefix for the bot.
- **discord.Onboarding.get_prompt()**: Retrieves a prompt from onboarding settings.
- **discord.app_commands.Cooldown.get_retry_after()**: Gets the remaining time until a cooldown can be retried.
- **discord.Guild.get_role()**: Gets a role from a guild by its ID.
- **discord.Member.get_role()**: Gets a role from a member by its ID.
- **discord.Guild.get_scheduled_event()**: Gets a scheduled event from a guild by its ID.
- **discord.AutoShardedClient.get_shard()**: Gets the shard for the auto-sharded client.
- **discord.Client.get_soundboard_sound()**: Gets a soundboard sound by its ID.
- **commands.Bot.get_soundboard_sound()**: Gets a soundboard sound by its ID.
- **discord.Guild.get_soundboard_sound()**: Gets a soundboard sound from a guild by its ID.
- **discord.Client.get_stage_instance()**: Gets a stage instance by its ID.
- **commands.Bot.get_stage_instance()**: Gets a stage instance by its ID.
- **discord.Guild.get_stage_instance()**: Gets a stage instance from a guild by its ID.
- **discord.Client.get_sticker()**: Gets a sticker by its ID.
- **commands.Bot.get_sticker()**: Gets a sticker by its ID.
- **discord.ForumChannel.get_tag()**: Retrieves a tag from a forum channel.
- **tasks.Loop.get_task()**: Gets the underlying asyncio task for a loop.
- **discord.ForumChannel.get_thread()**: Gets a thread from a forum channel by its ID.
- **discord.Guild.get_thread()**: Gets a thread from a guild by its ID.
- **discord.TextChannel.get_thread()**: Gets a thread from a text channel by its ID.
- **discord.app_commands.Cooldown.get_tokens()**: Gets the number of tokens available for a cooldown.
- **discord.Client.get_user()**: Gets a user by their ID.
- **commands.Bot.get_user()**: Gets a user by their ID.
- **commands.Greedy**: A converter that consumes all remaining arguments.
- **commands.group()**: Decorator to create a command group.
- **commands.Bot.group()**: Creates a command group on the bot.
- **commands.Group.group()**: Creates a subcommand within a group.
- **commands.GroupMixin.group()**: Creates a subcommand within a group-like structure.
- **commands.CogMeta.group_auto_locale_strings**: Whether to automatically generate locale strings for groups.
- **commands.CogMeta.group_description**: The description for a command group.
- **discord.app_commands.TranslationContextLocation.group_description**: Location for group description translations.
- **commands.CogMeta.group_extras**: Extra data for a command group.
- **commands.CogMeta.group_name**: The name of a command group.
- **discord.app_commands.TranslationContextLocation.group_name**: Location for group name translations.
- **commands.CogMeta.group_nsfw**: Whether a command group is NSFW.
- **discord.GroupChannel**: Represents a group DM channel.
- **commands.GroupCog**: A cog that can contain command groups.
- **commands.GroupMixin**: A mixin for creating command groups.
- **discord.app_commands.Group**: Represents a group of application commands.
- **discord.app_commands.AllChannels**: Represents all channel types for application commands.
- **discord.abc.GuildChannel.guild**: The guild this channel belongs to.
- **discord.app_commands.AppCommand.guild**: The guild this application command belongs to.
```

--------------------------------

### Get Nitro Booster Role

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Access Guild.premium_subscriber_role to retrieve the role designated for Nitro boosters, if available on the server.

```python
nitro_role = guild.premium_subscriber_role
```

--------------------------------

### Get Random Colour

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Utilize Colour.random() to generate a random colour instance. This is useful for dynamic colour assignments.

```python
Colour.random()
```

--------------------------------

### Define Command with Variable Arguments (*args)

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Implement a command that accepts an arbitrary number of arguments using the *args syntax. Arguments are joined into a comma-separated string.

```python
@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')
```

--------------------------------

### Sync Integration

Source: https://discordpy.readthedocs.io/en/latest/api.html

Synchronizes a guild integration. Requires 'manage_guild' permission.

```APIDOC
## POST /integrations/{integration.id}/sync

### Description

Syncs the integration. This action requires the `manage_guild` permission.

### Method

POST

### Endpoint

`/integrations/{integration.id}/sync`

### Raises

*   **Forbidden** – You do not have permission to sync the integration.
*   **HTTPException** – Syncing the integration failed.
```

--------------------------------

### Create Context Menus with app_commands.context_menu

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Defines context menu commands for messages or users. The callback must accept an Interaction and a target object (Member, User, or Message).

```python
@app_commands.context_menu()
async def react(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message('Very cool message!', ephemeral=True)

@app_commands.context_menu()
async def ban(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f'Should I actually ban {user}...', ephemeral=True)
```

--------------------------------

### PATCH /edit_welcome_screen

Source: https://discordpy.readthedocs.io/en/latest/api.html

Updates the guild's welcome screen settings.

```APIDOC
## PATCH /edit_welcome_screen

### Description
Updates the welcome screen configuration. Requires 'COMMUNITY' feature and 'manage_guild' permission.

### Parameters
#### Request Body
- **description** (str) - Optional
- **welcome_channels** (list) - Optional
- **enabled** (bool) - Optional
- **reason** (str) - Optional

### Response
#### Success Response (200)
- **welcome_screen** (WelcomeScreen) - The edited welcome screen.
```

--------------------------------

### AppInfo Cover Image URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of AppInfo.cover_image_url_as with AppInfo.cover_image.replace.

```python
AppInfo.cover_image.replace
```

--------------------------------

### Disable Default Logging Configuration

Source: https://discordpy.readthedocs.io/en/latest/logging.html

Prevents the library from applying its default logging setup by passing None to the log_handler parameter.

```python
client.run(token, log_handler=None)
```

--------------------------------

### GET /channels/{channel.id}/pins

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an asynchronous iterator of the pinned messages in the channel. Requires `view_channel` and `read_message_history` permissions.

```APIDOC
## GET /channels/{channel.id}/pins

### Description
Retrieves an asynchronous iterator of the pinned messages in the channel. You must have `view_channel` and `read_message_history` in order to use this.

Changed in version 2.6: Due to a change in Discord’s API, this now returns a paginated iterator instead of a list. For backwards compatibility, you can still retrieve a list of pinned messages by using `await` on the returned object. This is however deprecated.

Note: Due to a limitation with the Discord API, the `Message` object returned by this method does not contain complete `Message.reactions` data.

### Method
GET

### Endpoint
`/channels/{channel.id}/pins`

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The maximum number of messages to retrieve. Defaults to 50.
- **before** (str) - Optional - Get messages before this message ID.
- **oldest_first** (bool) - Optional - If `True`, messages are returned in ascending order (oldest first). Defaults to `False`.

### Response
#### Success Response (200)
- **Iterator[Message]** - An asynchronous iterator of pinned `Message` objects.

#### Response Example (Iterating)
```python
counter = 0
async for message in channel.pins(limit=250):
    counter += 1
    print(f"Message ID: {message.id}")
```

#### Response Example (Flattening to list - deprecated)
```python
messages = [message async for message in channel.pins(limit=50)]
print(f"Found {len(messages)} pinned messages.")
```
```

--------------------------------

### Colour Factory Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

A collection of class methods for generating Colour objects with predefined hex values.

```APIDOC
## Colour Factory Methods

### Description
Factory methods to create `Colour` objects with specific hex values for various themes and colors.

### Methods
- `_dark_red()`: Returns `0x992D22`
- `_lighter_grey()` / `_lighter_gray()`: Returns `0x95A5A6`
- `_dark_grey()` / `_dark_gray()`: Returns `0x607d8b`
- `_light_grey()` / `_light_gray()`: Returns `0x979C9F`
- `_darker_grey()` / `_darker_gray()`: Returns `0x546E7A`
- `_og_blurple()`: Returns `0x7289DA`
- `_blurple()`: Returns `0x5865F2`
- `_greyple()`: Returns `0x99AAB5`
- `_ash_theme()`: Returns `0x2E2E34` (New in 2.6)
- `_dark_theme()`: Returns `0x1A1A1E` (New in 1.5)
- `_onyx_theme()`: Returns `0x070709` (New in 2.6)
- `_light_theme()`: Returns `0xFBFBFB` (New in 2.6)
- `_fuchsia()`: Returns `0xEB459E` (New in 2.0)
- `_yellow()`: Returns `0xFEE75C` (New in 2.0)
- `_ash_embed()`: Returns `0x37373E` (New in 2.6)
- `_dark_embed()`: Returns `0x242429` (New in 2.2)
- `_onyx_embed()`: Returns `0x131416` (New in 2.6)
- `_light_embed()`: Returns `0xFFFFFF` (New in 2.2)
- `_pink()`: Returns `0xEB459F` (New in 2.3)
```

--------------------------------

### CategoryChannel Equality and Hashing

Source: https://discordpy.readthedocs.io/en/latest/api.html

Explains how CategoryChannel objects can be compared for equality and how their hash is determined.

```APIDOC
## CategoryChannel Equality and Hashing

### Equality Check

- **x == y**: Checks if two `CategoryChannel` objects are equal (i.e., they represent the same category).
- **x != y**: Checks if two `CategoryChannel` objects are not equal.

### Hashing

- **hash(x)**: Returns the hash of the `CategoryChannel` object, typically based on its unique ID.
```

--------------------------------

### GET /channels/{channel.id}/messages

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns an asynchronous iterator for the channel's message history. Requires 'read_message_history' permission.

```APIDOC
## GET /channels/{channel.id}/messages

### Description
Returns an asynchronous iterator that enables receiving the destination’s message history. You must have `read_message_history` to do this.

### Method
GET

### Endpoint
/channels/{channel.id}/messages

### Parameters
#### Query Parameters
- **limit** (int) - Optional - Defaults to 100. The maximum number of messages to retrieve.
- **before** (Snowflake) - Optional - Retrieves messages before this date/message ID.
- **after** (Snowflake) - Optional - Retrieves messages after this date/message ID.
- **around** (Snowflake) - Optional - Retrieves messages around this date/message ID.
- **oldest_first** (bool) - Optional - If true, messages are returned in ascending order (oldest first). Otherwise, in descending order (newest first).

### Response
#### Success Response (200)
- **AsyncIterator[Message]** - An asynchronous iterator yielding `Message` objects.

### Request Example
```python
counter = 0
async for message in channel.history(limit=200):
    if message.author == client.user:
        counter += 1
```

### Flattening into a list:
```python
messages = [message async for message in channel.history(limit=123)]
```
```

--------------------------------

### Get Voice Client Latency

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Access the latency information for a voice client connection. This can be used to monitor connection quality.

```Python
latency = voice_client.latency
```

--------------------------------

### Implement Autocomplete for Command Parameters

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

The `app_commands.autocomplete` decorator allows you to provide real-time suggestions for command parameters. The autocomplete callback should return a list of `app_commands.Choice` objects.

```python
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

### Launch Activity

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Responds to an interaction by launching an associated activity. This is only available for applications that have activities enabled.

```APIDOC
## POST /interactions/{interaction.id}/{interaction.token}/callback

### Description
Responds to this interaction by launching the activity associated with the app. Only available for apps with activities enabled.

### Method
POST

### Endpoint
/interactions/{interaction.id}/{interaction.token}/callback

### Raises
- **HTTPException** - Launching the activity failed.
- **InteractionResponded** - This interaction has already been responded to before.

### Returns
- **InteractionCallbackResponse** - The interaction callback data.
```

--------------------------------

### Get Permissions for Object

Source: https://discordpy.readthedocs.io/en/latest/api.html

Resolves permissions for a member or role, considering various factors like guild owner, roles, and overrides.

```APIDOC
## GET /channels/{channel.id}/permissions/{obj_id}

### Description
Resolves permissions for a member or role, considering various factors like guild owner, roles, and overrides.

### Method
GET

### Endpoint
`/channels/{channel.id}/permissions/{obj_id}`

### Parameters
#### Path Parameters
- **obj** (Union[Member, Role]) - Required - The object to resolve permissions for. This could be either a member or a role. If it’s a role then member overwrites are not computed.

### Response
#### Success Response (200)
- **Permissions** - The resolved permissions for the member or role.
```

--------------------------------

### VoiceClient Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods for managing voice connections and audio playback.

```APIDOC
## disconnect

### Description
Disconnects this voice client from voice.

### Method
Coroutine

### Parameters
#### Path Parameters
- **force** (bool) - Optional - Force the disconnection.

## move_to

### Description
Moves the voice client to a different voice channel.

### Method
Coroutine

### Parameters
#### Path Parameters
- **channel** (Optional[abc.Snowflake]) - Required - The channel to move to.
- **timeout** (Optional[float]) - Optional - How long to wait for the move to complete.

## play

### Description
Plays an AudioSource.

### Parameters
- **source** (AudioSource) - Required - The audio source to read from.
- **after** (Callable[[Optional[Exception]], Any]) - Optional - Finalizer called after stream exhaustion.
- **application** (str) - Optional - Encoder application ('audio', 'voip', 'lowdelay').
- **bitrate** (int) - Optional - Encoder bitrate (16-512).
- **fec** (bool) - Optional - Use inband forward error correction.
- **expected_packet_loss** (float) - Optional - Expected packet loss percentage.
- **bandwidth** (str) - Optional - Encoder bandpass ('narrow', 'medium', 'wide', 'superwide', 'full').
- **signal_type** (str) - Optional - Signal type ('auto', 'voice', 'music').
```

--------------------------------

### Get Invocation Context

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Returns the invocation context from a message or interaction. The returned context must be validated using `Context.valid` before invocation.

```python
await _get_context(_origin_ , _/_ , _*_ , _cls =..._)
```

--------------------------------

### FFmpegOpusAudio.probe Class Method

Source: https://discordpy.readthedocs.io/en/latest/api.html

Probes the input source for bitrate and codec information. This is a coroutine method.

```APIDOC
## FFmpegOpusAudio.probe Class Method

### Description
Probes the input source for bitrate and codec information.

### Parameters
#### Path Parameters
- **source** - Required - The input that ffmpeg will take and convert to Opus bytes.
- **method** (Optional[Union[`str`, Callable[`str`, `str`]]]) - Optional - The probing method used to determine bitrate and codec information. As a string, valid values are `native` to use ffprobe (or avprobe) and `fallback` to use ffmpeg (or avconv). As a callable, it must take two string arguments, `source` and `executable`. Both parameters are the same values passed to this factory function. `executable` will default to `ffmpeg` if not provided as a keyword argument.
- **executable** (`str`) - Optional - The executable name (and path) to use. Defaults to `ffmpeg`.
```

--------------------------------

### Get Emojis API

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves the emojis available to the connected client. This property does not include emojis owned by the application; use `fetch_application_emoji()` for those.

```APIDOC
## GET /api/emojis

### Description
Retrieves the emojis available to the connected client. This property does not include emojis owned by the application; use `fetch_application_emoji()` for those.

### Method
GET

### Endpoint
/api/emojis

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
None

### Request Example
None

### Response
#### Success Response (200)
- **emojis** (Sequence[Emoji]) - The emojis that the connected client has.

#### Response Example
```json
[
  {
    "id": "1234567890",
    "name": "custom_emoji",
    "animated": false
  }
]
```
```

--------------------------------

### Get the internal asyncio task

Source: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

Retrieves the internal `asyncio.Task` object associated with the loop. Returns `None` if no task is currently running.

```python
get_task()
```

--------------------------------

### PartialInviteGuild Banner URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of PartialInviteGuild.banner_url_as with PartialInviteGuild.banner.replace.

```python
PartialInviteGuild.banner.replace
```

--------------------------------

### @context_menu Decorator

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

A decorator that creates an application command context menu from a regular function.

```APIDOC
## @context_menu

### Description
A decorator that creates an application command context menu from a regular function directly under this tree.

### Parameters
- **name** (Union[str, locale_str]) - Optional - The name of the context menu command.
- **nsfw** (bool) - Optional - Whether the command is NSFW. Defaults to False.
- **guild** (Optional[Snowflake]) - Optional - The guild to add the command to.
- **guilds** (List[Snowflake]) - Optional - The list of guilds to add the command to.
- **auto_locale_strings** (bool) - Optional - If True, translatable strings will be wrapped into locale_str. Defaults to True.
- **extras** (dict) - Optional - A dictionary to store extraneous data.
```

--------------------------------

### Define a standard command with @discord.ext.commands.command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Use this decorator to transform a function into a `Command`. The command's help text is automatically derived from the function's docstring. Ensure the decorated function is a coroutine.

```Python
@discord.ext.commands.command(_name =..._, _cls =..._, _** attrs_)
```

--------------------------------

### BaseSoundboardSound

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents a generic soundboard sound in Discord.

```APIDOC
## BaseSoundboardSound

### Description
Represents a generic Discord soundboard sound.
New in version 2.5.

### Attributes
- **id** (`int`) - The ID of the sound.
- **volume** (`float`) - The volume of the sound as floating point percentage (e.g. `1.0` for 100%).
- **url** (`str`) - Returns the URL of the sound.

### Methods
- **hash(x)** - Returns the sound’s hash.
- **x == y** - Checks if two sounds are equal.
- **x != y** - Checks if two sounds are not equal.
```

--------------------------------

### Get Guild Vanity URL

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves the guild's special vanity invite URL. Requires `VANITY_URL` feature and `manage_guild` permission.

```APIDOC
## GET /api/guilds/{guild_id}/vanity-url

### Description
Returns the guild’s special vanity invite.

### Method
GET

### Endpoint
/api/guilds/{guild_id}/vanity-invite

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

### Request Body
(No request body specified)

### Response
#### Success Response (200)
- **Invite** (string) - The special vanity invite URL. Returns `None` if no vanity invite is set.

#### Error Response
- **Forbidden** - You do not have the proper permissions to get this.
- **HTTPException** - Retrieving the vanity invite failed.
```

--------------------------------

### Soundboard API

Source: https://discordpy.readthedocs.io/en/latest/api.html

Functions for fetching and creating soundboard sounds.

```APIDOC
## GET /api/guilds/{guild.id}/soundboard/sounds/{sound_id}

### Description
Retrieves a `SoundboardSound` with the specified ID.

### Method
GET

### Endpoint
/api/guilds/{guild.id}/soundboard/sounds/{sound_id}

### Parameters
#### Path Parameters
- **guild.id** (snowflake) - Required - The ID of the guild.
- **sound_id** (snowflake) - Required - The ID of the soundboard sound to retrieve.

### Response
#### Success Response (200)
- **SoundboardSound** - The retrieved sound.

#### Error Response
- **NotFound** - The sound requested could not be found.
- **HTTPException** - Retrieving the sound failed.
```

```APIDOC
## GET /api/guilds/{guild.id}/soundboard/sounds

### Description
Retrieves a list of all soundboard sounds for the guild.

### Method
GET

### Endpoint
/api/guilds/{guild.id}/soundboard/sounds

### Parameters
#### Path Parameters
- **guild.id** (snowflake) - Required - The ID of the guild.

### Response
#### Success Response (200)
- **List[SoundboardSound]** - The retrieved soundboard sounds.

#### Error Response
- **HTTPException** - Retrieving the sounds failed.
```

```APIDOC
## POST /api/guilds/{guild.id}/soundboard/sounds

### Description
Creates a `SoundboardSound` for the guild.

### Method
POST

### Endpoint
/api/guilds/{guild.id}/soundboard/sounds

### Parameters
#### Path Parameters
- **guild.id** (snowflake) - Required - The ID of the guild to create the soundboard sound in.

#### Request Body
- **name** (str) - Required - The name of the sound. Must be between 2 and 32 characters.
- **sound** (bytes) - Required - The bytes-like object representing the sound data. Only MP3 and OGG sound files that don’t exceed the duration of 5.2s are supported.
- **volume** (float) - Optional - The volume of the sound. Must be between 0 and 1. Defaults to `1`.
- **emoji** (Optional[Union[Emoji, PartialEmoji, str]]) - Optional - The emoji of the sound.
- **reason** (Optional[str]) - Optional - The reason for creating the sound. Shows up on the audit log.

### Response
#### Success Response (200)
- **SoundboardSound** - The newly created soundboard sound.

#### Error Response
- **Forbidden** - You do not have permissions to create a soundboard sound.
- **HTTPException** - Creating the soundboard sound failed.
```

--------------------------------

### Handle Multiple Return Values in wait_for

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Shows how to unpack multiple arguments returned by the wait_for event system.

```python
reaction, user = await client.wait_for('reaction_add', check=lambda r, u: u.id == 176995180300206080)

# use user and reaction
```

--------------------------------

### Get Guild Bans

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an asynchronous iterator of users banned from a guild. Requires the `ban_members` permission. This method returns a paginated iterator.

```APIDOC
## GET /guilds/{guild.id}/bans

### Description
Retrieves an asynchronous iterator of the users that are banned from the guild as a `BanEntry`.

### Method
GET

### Endpoint
/guilds/{guild.id}/bans

### Parameters
#### Query Parameters
- **limit** (int) - Optional - The maximum number of bans to retrieve.
- **before** (Snowflake) - Optional - Get bans before this ID.
- **after** (Snowflake) - Optional - Get bans after this ID.

### Request Example
```json
{
  "limit": 1000
}
```

### Response
#### Success Response (200)
- **BanEntry** (iterator) - An iterator yielding `BanEntry` objects.

#### Response Example
```json
[
  {
    "user": {
      "id": "123456789012345678",
      "username": "exampleuser",
      "discriminator": "1234",
      "avatar": "a1b2c3d4e5f67890a1b2c3d4e5f67890"
    },
    "reason": "Violated community guidelines"
  }
]
```

### Error Handling
* **NotFound** – Invalid Channel ID.
* **Forbidden** – You do not have permission to fetch this channel.
```

--------------------------------

### Get element by attributes

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieve the first element from an iterable that matches all specified attributes. Supports nested attribute matching and asynchronous iterables.

```python
member = discord.utils.get(message.guild.members, name='Foo')
```

```python
channel = discord.utils.get(guild.voice_channels, name='Foo', bitrate=64000)
```

```python
channel = discord.utils.get(client.get_all_channels(), guild__name='Cool', name='general')
```

```python
msg = await discord.utils.get(channel.history(), author__name='Dave')
```

--------------------------------

### Guild Discovery Splash URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of Guild.discovery_splash_url_as with Guild.discovery_splash.replace.

```python
Guild.discovery_splash.replace
```

--------------------------------

### POST /create_webhook

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new webhook for the channel.

```APIDOC
## POST /create_webhook

### Description
Creates a webhook for this channel. Requires `manage_webhooks` permission.

### Parameters
#### Request Body
- **name** (str) - Required - The webhook's name.
- **avatar** (bytes) - Optional - Bytes-like object for default avatar.
- **reason** (str) - Optional - Audit log reason.

### Response
#### Success Response (200)
- **webhook** (Webhook) - The created webhook.
```

--------------------------------

### Get Cooldown Retry After Time

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Retrieve the remaining time in seconds before a command's cooldown expires. Returns None if the command is not on cooldown.

```Python
retry_after = commands.Command.get_cooldown_retry_after(command, ctx)
```

--------------------------------

### Bot Configuration Properties

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Properties for configuring bot owner IDs, command prefix behavior, command tree class, and allowed contexts/installs.

```APIDOC
## Bot Configuration Properties

### owner_id

- **Type**: Optional[int]
- **Description**: The user ID that owns the bot. If not set and queried via `is_owner()`, it's fetched automatically using `application_info()`.

### owner_ids

- **Type**: Optional[Collection[int]]
- **Description**: User IDs that own the bot. Similar to `owner_id`. If not set and the application is team-based, it's fetched automatically using `application_info()`. Recommended to use a `set` for performance. Cannot set both `owner_id` and `owner_ids`.
- **New in version**: 1.3

### strip_after_prefix

- **Type**: bool
- **Description**: Whether to strip whitespace characters after encountering the command prefix. Allows for variations in spacing after the prefix. Defaults to `False`.
- **New in version**: 1.7

### tree_cls

- **Type**: Type[CommandTree]
- **Description**: The type of application command tree to use. Defaults to `CommandTree`.
- **New in version**: 2.0

### allowed_contexts

- **Type**: AppCommandContext
- **Description**: The default allowed contexts that apply to all application commands. Can be overridden per command.
- **New in version**: 2.4

### allowed_installs

- **Type**: AppInstallationType
- **Description**: The default allowed install locations that apply to all application commands. Can be overridden per command.
- **New in version**: 2.4
```

--------------------------------

### async with typing()

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns an asynchronous context manager that allows you to send a typing indicator to the destination.

```APIDOC
## async with typing()

### Description
Returns an asynchronous context manager that allows you to send a typing indicator to the destination for an indefinite period of time, or 10 seconds if the context manager is called using await.

### Request Example
```python
async with channel.typing():
    # simulate something heavy
    await asyncio.sleep(20)

await channel.send('Done!')
```
```

--------------------------------

### Create Webhook for Channel

Source: https://discordpy.readthedocs.io/en/latest/api.html

Use this method to create a webhook for the current channel. Requires `manage_webhooks` permission. Available from version 2.0.

--------------------------------

### AudioSource Interface

Source: https://discordpy.readthedocs.io/en/latest/api.html

Interface for creating custom audio streams.

```APIDOC
## AudioSource

### Description
Represents an audio stream. Audio can be Opus encoded or 16-bit 48KHz stereo PCM.

### Methods
- **read()**: Reads 20ms worth of audio. Returns bytes.
- **is_opus()**: Checks if the audio source is already encoded in Opus.
- **cleanup()**: Called when clean-up is needed (e.g., clearing buffers).
```

--------------------------------

### Event Registration

Source: https://discordpy.readthedocs.io/en/latest/api.html

Decorator for registering event listeners.

```APIDOC
## Event Registration

### Description
A decorator used to register coroutine functions as event listeners for the client.

### Method
`@client.event`

### Parameters
- **coro** (coroutine function) - The coroutine function to register as an event listener.

### Raises
- **TypeError** - If the provided function is not a coroutine.

### Example
```python
@client.event
async def on_ready():
    print('Ready!')
```

*Note: The `coro` parameter is positional-only since version 2.0.*
```

--------------------------------

### Get Thread

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns a thread with the given ID. Note: This does not always retrieve archived threads, as they are not retained in the internal cache. Use Guild.fetch_channel() instead.

```APIDOC
## GET /channels/{channel.id}/threads/{thread.id}

### Description
Returns a thread with the given ID.

### Method
GET

### Endpoint
`/channels/{channel.id}/threads/{thread.id}`

### Parameters
#### Path Parameters
- **channel.id** (int) - Required - The ID of the channel the thread is in.
- **thread.id** (int) - Required - The ID of the thread to retrieve.

### Request Example
None (This is a GET request with path parameters only)

### Response
#### Success Response (200)
- **thread** (Thread) - The returned thread or `None` if not found.

#### Response Example
```json
{
  "id": "123456789012345678",
  "name": "My Awesome Thread",
  "type": 10
}
```
```

--------------------------------

### Context Methods

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Methods available on the Context object for interacting with commands.

```APIDOC
## Context Methods

### Description
Methods available on the Context object for interacting with commands.

### Methods
#### `_from_interaction(_interaction_)`
This function is a _coroutine_.
Creates a context from a `discord.Interaction`. This only works on application command based interactions, such as slash commands or context menus.

Parameters
- **interaction** (`discord.Interaction`) – The interaction to create a context with.

Raises
- **ValueError** – The interaction does not have a valid command.
- **TypeError** – The interaction client is not derived from `Bot` or `AutoShardedBot`.

#### `_invoke(_command_, *args, **kwargs)`
This function is a _coroutine_.
Calls a command with the arguments given. This is useful if you want to just call the callback that a `Command` holds internally.
Note: This does not handle converters, checks, cooldowns, pre-invoke, or after-invoke hooks in any matter. It calls the internal callback directly as-if it was a regular function. You must take care in passing the proper arguments when using this function.

Parameters
- **command** (`Command`) – The command that is going to be called.
- ***args** – The arguments to use.
- ****kwargs** – The keyword arguments to use.

Raises
- **TypeError** – The command argument to invoke is missing.

#### `_reinvoke(*, call_hooks=False, restart=True)`
This function is a _coroutine_.
Calls the command again. This is similar to `invoke()` except that it bypasses checks, cooldowns, and error handlers.
Note: If you want to bypass `UserInputError` derived exceptions, it is recommended to use the regular `invoke()` as it will work more naturally.

Parameters
- **call_hooks** (`bool`) – Whether to call the before and after invoke hooks.
- **restart** (`bool`) – Whether to start the call chain from the very beginning or where we left off (i.e. the command that caused the error). The default is to start where we left off.

Raises
- **ValueError** – The context to reinvoke is not valid.
```

--------------------------------

### Get Partial Message

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a PartialMessage from the message ID. This is useful if you only have the message ID and want to work with the message without an unnecessary API call.

```APIDOC
## GET /channels/{channel.id}/messages/{message.id}/partial

### Description
Creates a `PartialMessage` from the message ID.

### Method
GET

### Endpoint
`/channels/{channel.id}/messages/{message.id}/partial`

### Parameters
#### Path Parameters
- **channel.id** (int) - Required - The ID of the channel the message is in.
- **message.id** (int) - Required - The ID of the message to create a partial message for.

### Request Example
None (This is a GET request with path parameters only)

### Response
#### Success Response (200)
- **partial_message** (PartialMessage) - The partial message.

#### Response Example
```json
{
  "id": "123456789012345678"
}
```
```

--------------------------------

### Client Configuration Options

Source: https://discordpy.readthedocs.io/en/latest/api.html

Configuration options for the discord.py client, affecting performance and event handling.

```APIDOC
## Client Configuration Options

### Description
Configuration options that can be passed during client initialization to control various aspects of the library's behavior, including event dispatching, rate limit handling, and HTTP tracing.

### Parameters
#### Initialization Parameters
- **enable_raw_events** (`bool`) - Optional - Defaults to `False`. If `True`, enables `on_socket_raw_receive()` and `on_socket_raw_send()` events. Set to `True` for performance considerations.
- **enable_raw_presences** (`bool`) - Optional - Defaults to `True` only when `Intents.presences` is enabled and `Intents.members` is disabled, otherwise `False`. Manually enables or disables the `on_raw_presence_update()` event. Requires `Intents.presences` to be enabled.
- **http_trace** (`aiohttp.TraceConfig`) - Optional - The trace configuration for tracking HTTP requests made by the library using `aiohttp`. See aiohttp documentation for more details.
- **max_ratelimit_timeout** (Optional[`float`]) - Optional - The maximum number of seconds to wait for non-global rate limits. If a request requires sleeping longer than this, `RateLimited` will be raised. Minimum value is `30.0` seconds. Defaults to no timeout limit.
- **connector** (Optional[`aiohttp.BaseConnector`]) - Optional - The `aiohttp` connector to use for the client. Allows control over underlying `aiohttp` behavior, such as DNS resolvers or SSL contexts.
```

--------------------------------

### Get Emoji Creation Time

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns the emoji's creation time in UTC. Returns None if it is a Unicode emoji. Available from version 1.6.

```python
_property _created_at
```

--------------------------------

### Get creation time from snowflake ID

Source: https://discordpy.readthedocs.io/en/latest/api.html

Converts a Discord snowflake ID into its creation timestamp. The returned value is an aware datetime object in UTC.

```python
# Example usage is not provided in the source, but the function signature is:
def snowflake_time(id): ...
```

--------------------------------

### PartialWebhookGuild and PartialWebhookChannel

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents partial guild and channel objects used for webhooks.

```APIDOC
## PartialWebhookGuild

### Description
Represents a partial guild for webhooks, typically given for channel follower webhooks.

### Attributes
- **id** (int) - The partial guild’s ID.
- **name** (str) - The partial guild’s name.
- **icon** (Optional[Asset]) - The guild’s icon asset, if available.

## PartialWebhookChannel

### Description
Represents a partial channel for webhooks, typically given for channel follower webhooks.

### Attributes
- **id** (int) - The partial channel’s ID.
- **name** (str) - The partial channel’s name.
- **mention** (str) - The string that allows you to mention the channel.
```

--------------------------------

### Implement Autocomplete Choice Filtering

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Use this pattern to return a list of app_commands.Choice objects based on a user's current input string.

```python
fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
return [
    app_commands.Choice(name=fruit, value=fruit)
    for fruit in fruits if current.lower() in fruit.lower()
]
```

--------------------------------

### Version Information

Source: https://discordpy.readthedocs.io/en/latest/api.html

Accessing library version details using discord.version_info and discord.__version__.

```APIDOC
## Version Information

### Description
Provides access to the library version information using a named tuple or a string representation.

### Attributes
- **discord.version_info** (named tuple) - Similar to sys.version_info, containing major, minor, micro, releaselevel, and serial.
- **discord.__version__** (string) - A string representation of the version based on PEP 440 (e.g., '1.0.0rc1').
```

--------------------------------

### Fetch Soundboard Default Sounds

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves all default soundboard sounds.

```APIDOC
## GET /soundboard/sounds/default

### Description
Retrieves all default soundboard sounds.

### Method
GET

### Endpoint
/soundboard/sounds/default

### Raises
- **HTTPException** - Retrieving the default soundboard sounds failed.

### Returns
- **List[SoundboardDefaultSound]** - All default soundboard sounds.
```

--------------------------------

### Define a hybrid command with @discord.ext.commands.hybrid_command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Use this decorator to create a `HybridCommand` that functions as both a regular command and an application command. The callback must be representable as an application command callback. Checks and error handlers use `Context`.

```Python
@discord.ext.commands.hybrid_command(_name =..._, _*_ , _with_app_command =True_, _** attrs_)
```

--------------------------------

### Positional Flag with Default Boolean

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Example of a positional flag with a default boolean value. The flag converter syntax is inspired by Discord's search bar.

```python
# Hello there --bold True
class Greeting(commands.FlagConverter):
    text: str = commands.flag(positional=True)
    bold: bool = False

```

--------------------------------

### Flattening Channel History to a List

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Shows how to fetch all messages from a channel's history and store them in a list. Use this when you need all messages at once, but be mindful of memory usage for large histories.

```python
messages = await channel.history().flatten()
for message in messages:
    print(message)
```

--------------------------------

### Configure Custom Sharding

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Advanced configuration for controlling shard counts and specific shard IDs.

```python
# launch 10 shards regardless
client = discord.AutoShardedClient(shard_count=10)

# launch specific shard IDs in this process
client = discord.AutoShardedClient(shard_count=10, shard_ids=(1, 2, 5, 6))
```

--------------------------------

### POST create_forum

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new forum channel within the guild.

```APIDOC
## POST create_forum

### Description
Creates a new ForumChannel. This is a coroutine.

### Parameters
#### Request Body
- **name** (str) - Required - The channel name.
- **topic** (str) - Optional - The channel topic.
- **category** (CategoryChannel) - Optional - The category to place the channel under.
- **position** (int) - Optional - Position in the channel list.
- **nsfw** (bool) - Optional - Whether the channel is NSFW.
- **slowmode_delay** (int) - Optional - Slowmode rate limit in seconds.
- **reason** (str) - Optional - Reason for audit log.
- **available_tags** (Sequence[ForumTag]) - Optional - Tags for the forum.
- **media** (bool) - Optional - Whether to create a media forum channel.

### Response
#### Success Response (200)
- **ForumChannel** (object) - The created forum channel object.
```

--------------------------------

### SystemChannelFlags Class Overview

Source: https://discordpy.readthedocs.io/en/latest/api.html

Details the SystemChannelFlags class, its constructor, and general usage for managing system channel flags.

```APIDOC
## SystemChannelFlags

### Description
Wraps up a Discord system channel flag value. Similar to `Permissions`, the properties provided are two way. You can set and retrieve individual bits using the properties as if they were regular bools. This allows you to edit the system flags easily. To construct an object you can pass keyword arguments denoting the flags to enable or disable.

### Class
`discord.SystemChannelFlags`

### Constructor
`__init__(**kwargs)`

### Operations
- `x == y`: Checks if two flags are equal.
- `x != y`: Checks if two flags are not equal.
- `x | y`, `x |= y`: Returns a `SystemChannelFlags` instance with all enabled flags from both x and y. (New in version 2.0)
- `x & y`, `x &= y`: Returns a `SystemChannelFlags` instance with only flags enabled on both x and y. (New in version 2.0)
- `x ^ y`, `x ^= y`: Returns a `SystemChannelFlags` instance with only flags enabled on only one of x or y, not on both. (New in version 2.0)
- `~x`: Returns a `SystemChannelFlags` instance with all flags inverted from x. (New in version 2.0)
- `hash(x)`: Return the flag’s hash.
- `iter(x)`: Returns an iterator of `(name, value)` pairs. This allows it to be, for example, constructed as a dict or a list of pairs. (New in version 2.0)
- `bool(b)`: Returns whether any flag is set to `True`. (New in version 2.0)
```

--------------------------------

### Member Default Avatar Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates the replacement of Member.default_avatar with Member.default_avatar.key.

```python
Member.default_avatar.key
```

--------------------------------

### Create command groups and subcommands

Source: https://discordpy.readthedocs.io/en/latest/faq.html

Uses the group decorator to nest commands under a parent command.

```python
@bot.group()
async def git(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid git command passed...')

@git.command()
async def push(ctx, remote: str, branch: str):
    await ctx.send(f'Pushing to {remote} {branch}')
```

--------------------------------

### Guild Splash URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of Guild.splash_url_as with Guild.splash.replace.

```python
Guild.splash.replace
```

--------------------------------

### Using built-in owner check

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Demonstrates the use of the library-provided is_owner check.

```python
@bot.command(name='eval')
@commands.is_owner()
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))
```

--------------------------------

### AppInfo Cover Image Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of AppInfo.cover_image with AppInfo.cover_image.key.

```python
AppInfo.cover_image.key
```

--------------------------------

### PCMAudio

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents raw 16-bit 48KHz stereo PCM audio source.

```APIDOC
## PCMAudio

### Description
Represents raw 16-bit 48KHz stereo PCM audio source.

### Attributes
- **stream** (file object) - A file-like object that reads byte data representing raw PCM.

### Methods
- **read()**
  Reads 20ms worth of audio. Subclasses must implement this. If the audio is complete, then returning an empty bytes-like object to signal this is the way to do so. If `is_opus()` method returns `True`, then it must return 20ms worth of Opus encoded audio. Otherwise, it must be 20ms worth of 16-bit 48KHz stereo PCM, which is about 3,840 bytes per frame (20ms worth of audio).
  Returns: A bytes like object that represents the PCM or Opus data.
  Return type: `bytes`
```

--------------------------------

### get_destination

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Returns the `Messageable` where the help command will be output. This method can be overridden to customize behavior. By default, it returns the context's channel.

```APIDOC
## get_destination

### Description
Returns the `Messageable` where the help command will be output.

### Method
This is a method that can be overridden.

### Returns
- **Messageable** - The destination where the help command will be output.
```

--------------------------------

### Fetch Guild Preview

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a preview of a Guild by its ID. This is useful for discoverable guilds even if you are not a member.

```python
await _fetch_guild_preview(_guild_id_)
```

--------------------------------

### Permissions Handling

Source: https://discordpy.readthedocs.io/en/latest/api.html

Explains how permissions are resolved for a user, especially in direct messages.

```APIDOC
## permissions_for(_obj_ , _/_)

### Description
Handles permission resolution for a `User`. This function is there for compatibility with other channel types. Actual direct messages do not really have the concept of permissions. This returns all the Text related permissions set to `True` except for TTS messages, managing messages, and thread-related permissions. It also checks the `kick_members` permission if the user is the owner.

### Parameters
* **obj** (`Snowflake`) – The user to check permissions for. (Positional-only)

### Returns
* The resolved permissions for the user.

### Return type
* `Permissions`

### Changed in version 2.0
* `obj` parameter is now positional-only.

### Changed in version 2.1
* Thread related permissions are now set to `False`.
```

--------------------------------

### discord.IntegrationApplication

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents an application for a bot integration, including its description, icon, and name.

```APIDOC
## discord.IntegrationApplication

### Description
Represents an application for a bot integration.
New in version 2.0.

### Attributes
- **description** (`str`) - The application’s description. Can be an empty string.
- **icon** (`Optional[str]`) - The application’s icon hash.
- **id** (`int`) - The ID for this application.
- **name** (`str`) - The application’s name.
- **summary** (`str`) - The summary of the application. Can be an empty string.
- **user** (`Optional[User]`) - The bot user on this application.
```

--------------------------------

### Get Guild Audit Log Entries

Source: https://discordpy.readthedocs.io/en/latest/api.html

Iterate through guild audit log entries. You need the 'view_audit_log' permission. You can filter by limit, before/after a date or entry, oldest_first, user, or action type.

```python
async for entry in guild.audit_logs(limit=100):
    print(f'{entry.user} did {entry.action} to {entry.target}')
```

```python
async for entry in guild.audit_logs(action=discord.AuditLogAction.ban):
    print(f'{entry.user} banned {entry.target}')
```

```python
entries = [entry async for entry in guild.audit_logs(limit=None, user=guild.me)]
await channel.send(f'I made {len(entries)} moderation actions.')
```

--------------------------------

### Getting a Single Element from History

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Demonstrates using `AsyncIterator.get()` to retrieve a single message matching specific criteria, such as messages authored by the client user. This is efficient for finding one specific item.

```python
my_last_message = await channel.history().get(author=client.user)
```

--------------------------------

### Perform HTTP Requests with ClientSession

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Replaces deprecated aiohttp helper functions with the recommended ClientSession context manager.

```python
async with aiohttp.ClientSession() as sess:
    async with sess.get('url') as resp:
        # work with resp
```

--------------------------------

### Create Role with Integer Colour

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

The Guild.create_role() method now accepts an integer value for the 'colour' parameter, in addition to Colour objects.

```python
await guild.create_role(name='New Role', colour=0x3498db)
```

--------------------------------

### Guild Discovery Splash URL Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of Guild.discovery_splash_url with Guild.discovery_splash.

```python
Guild.discovery_splash
```

--------------------------------

### Create a custom application command check

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Use a predicate function to define custom logic for command access. If the predicate returns a false-like value, a CheckFailure exception is raised.

```python
def check_if_it_is_me(interaction: discord.Interaction) -> bool:
    return interaction.user.id == 85309593344815104

@tree.command()
@app_commands.check(check_if_it_is_me)
async def only_for_me(interaction: discord.Interaction):
    await interaction.response.send_message('I know you!', ephemeral=True)
```

```python
def is_me():
    def predicate(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 85309593344815104
    return app_commands.check(predicate)

@tree.command()
@is_me()
async def only_me(interaction: discord.Interaction):
    await interaction.response.send_message('Only you!')
```

--------------------------------

### fetch_template

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Fetches a Template object from a discord.new URL or code.

```APIDOC
## fetch_template

### Description
Gets a Template from a discord.new URL or code.

### Parameters
#### Request Body
- **code** (Union[Template, str]) - Required - The Discord Template Code or URL.

### Response
#### Success Response (200)
- **Template** (Object) - The template from the URL/code.
```

--------------------------------

### Getting a Command Programmatically

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieve a Command object from the internal list by its name. This method can also be used to retrieve aliases. For nested commands, use a fully qualified name like 'foo bar'. Returns None if the command is not found.

```python
get_command(name)
```

--------------------------------

### Guild Splash URL Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of Guild.splash_url with Guild.splash.

```python
Guild.splash
```

--------------------------------

### format_help_command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

A utility function to format the non-indented block of commands and groups. The `command` parameter is now positional-only since version 2.0. `add_command_arguments()` is now called if `show_parameter_descriptions` is `True`.

```APIDOC
## format_help_command

### Description
A utility function to format the non-indented block of commands and groups.

### Parameters
#### Path Parameters
- **command** (Command) - Required - The command to format.

### Notes
- Changed in version 2.0: `command` parameter is now positional-only.
- Changed in version 2.0: `add_command_arguments()` is now called if `show_parameter_descriptions` is `True`.
```

--------------------------------

### Reinvoke a Command, Bypassing Checks

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Calls the command again, bypassing checks, cooldowns, and error handlers. Set `call_hooks` to `True` to include before and after invoke hooks. `restart` determines if the call chain starts from the beginning or resumes from where it left off. Raises `ValueError` if the context is invalid.

```python
await ctx._reinvoke(_*, call_hooks=False, restart=True)
```

--------------------------------

### Iterating Over Channel History

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Demonstrates how to iterate over a channel's message history using an asynchronous iterator. This is the standard way to fetch messages sequentially.

```python
async for message in channel.history():
    print(message)
```

--------------------------------

### TextChannel Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

This section details the methods available for interacting with a TextChannel object, such as sending messages, creating threads, and managing permissions.

```APIDOC
## TextChannel Methods

### Description
Methods available for a `TextChannel` object.

### Methods
- **archived_threads(private: bool = False, limit: int = 100)**: Returns an asynchronous iterator yielding `Thread` objects representing archived threads.
- **clone()**: Creates a new channel with the same details as this channel.
- **create_invite(max_age: int = 86400, max_uses: int = 0, temporary: bool = False, unique: bool = False, reason: Optional[str] = None)**: Creates an invite to the channel.
- **create_thread(name: str, auto_archive_duration: Union[int, timedelta] = MISSING, slowmode_delay: Optional[int] = None, type: Optional[ThreadType] = None, start_message: Optional[Message] = None, reason: Optional[str] = None)**: Creates a public or private thread associated with this channel.
- **create_webhook(name: str, avatar: Optional[bytes] = None, reason: Optional[str] = None)**: Creates a webhook for this channel.
- **delete_messages(messages: Iterable[Snowflake])**: Bulk deletes messages from the channel.
- **edit(name: Optional[str] = None, topic: Optional[str] = None, position: Optional[int] = None, nsfw: Optional[bool] = None, slowmode_delay: Optional[int] = None, default_auto_archive_duration: Optional[int] = None, default_thread_slowmode_delay: Optional[int] = None, reason: Optional[str] = None)**: Edits the channel.
- **fetch_message(id: int)**: Fetches a single message from the channel by its ID.
- **follow(channel: TextChannel, reason: Optional[str] = None)**: Creates a webhook that mirrors messages from this channel to the target channel.
- **get_partial_message(id: int)**: Gets a partial message object from the channel by its ID.
- **get_thread(thread_id: int)**: Fetches a thread from the channel by its ID.
- **history(limit: int = 100, before: Optional[Snowflake] = None, after: Optional[Snowflake] = None, around: Optional[Snowflake] = None)**: Returns an asynchronous iterator yielding `Message` objects from the channel's history.
- **invites()**: Returns a list of invites to the channel.
- **is_news()**: Returns `True` if the channel is a news channel.
- **is_nsfw()**: Returns `True` if the channel is marked as NSFW.
- **move(members: Iterable[Member], *, channel: TextChannel, limit: int = 1000, reason: Optional[str] = None)**: Moves members to this channel.
- **overwrites_for(obj: Union[Role, Member, User])**: Returns the `PermissionOverwrite` object for the given role or member.
- **permissions_for(obj: Union[Role, Member, User])**: Returns a `Permissions` object representing the permissions of the given role or member in this channel.
- **pins()**: Returns a list of pinned messages in the channel.
- **purge(limit: int = 100, check: Callable[[Message], bool] = None, before: Optional[Snowflake] = None, after: Optional[Snowflake] = None, around: Optional[Snowflake] = None)**: Deletes messages from the channel.
- **send(content: Optional[str] = None, *, tts: bool = False, embed: Optional[Embed] = None, file: Optional[File] = None, files: Optional[List[File]] = None, delete_after: Optional[float] = None, nonce: Optional[str] = None, allowed_mentions: Optional[AllowedMentions] = None, reference: Optional[MessageReference] = None, mention_author: bool = True)**: Sends a message to the channel.
- **set_permissions(target: Union[Role, Member, User], *, allow: Optional[Permissions] = None, deny: Optional[Permissions] = None, reason: Optional[str] = None)**: Sets the permissions for a given role or member in this channel.
- **typing()**: Returns an asynchronous context manager that allows you to send a typing indicator to the destination for an indefinite period of time, or 10 seconds if the context manager is called using `await`.
```

--------------------------------

### Button Configuration

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Parameters available for configuring a button component.

```APIDOC
## Button Parameters

### Parameters
#### Request Body
- **disabled** (bool) - Whether the button is disabled or not. Defaults to `False`.
- **emoji** (Optional[Union[`str`, `Emoji`, `PartialEmoji`]]) - The emoji of the button. This can be in string form or a `PartialEmoji` or a full `Emoji`.
- **row** (Optional[`int`]) - The relative row this button belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to `None`, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).
Note
This parameter is ignored when used in a `ActionRow` or v2 component.
- **id** (Optional[`int`]) - The ID of this component. This must be unique across the view.
New in version 2.6.
```

--------------------------------

### Waiting for Events

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Demonstrates how to use `client.wait_for` to asynchronously wait for specific events with optional checks and timeouts.

```APIDOC
## wait_for

### Description
Asynchronously wait for a specific event to occur.

### Method
`await client.wait_for(event, *, check=None, timeout=None)`

### Parameters
#### Event Name
- **event** (`str`) – The name of the event to wait for (e.g., 'reaction_add').
#### Check Predicate
- **check** (Optional[Callable[…, `bool`]]) – A function that returns `True` if the event meets the criteria.
#### Timeout
- **timeout** (Optional[`float`]) – The maximum time in seconds to wait for the event.

### Raises
- **asyncio.TimeoutError** – If the timeout is reached before the event occurs.

### Returns
- Returns arguments passed to the event, mirroring its parameters.

### Example
```python
async def check(reaction, user):
    return user == message.author and str(reaction.emoji) == '👍'

try:
    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
except asyncio.TimeoutError:
    await channel.send('👎')
else:
    await channel.send('👍')
```

**Note:** The `event` parameter is positional-only since version 2.0.
```

--------------------------------

### Set Logging Level via Client.run

Source: https://discordpy.readthedocs.io/en/latest/logging.html

Adjusts the verbosity of the library logs by specifying a log level alongside the handler.

```python
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Assume client refers to a discord.Client subclass...
client.run(token, log_handler=handler, log_level=logging.DEBUG)
```

--------------------------------

### locale_str Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Marks a string as ready for translation. Translation is handled lazily by the CommandTree.sync() method.

```APIDOC
## locale_str Class

### Description
Marks a string as ready for translation. This is done lazily and is not actually translated until `CommandTree.sync()` is called. The sync method then ultimately defers the responsibility of translating to the `Translator` instance used by the `CommandTree`.

### Attributes
- **extras** (dict) - A dict of user provided extras to attach to the translated string. This can be used to add more context, information, or any metadata necessary to aid in actually translating the string. Since these are passed via keyword arguments, the keys are strings.
- **message** (str) - The message being translated. Once set, this cannot be changed. This must be the default “message” that you send to Discord. Discord sends this message back to the library and the library uses it to access the data in order to dispatch commands. For example, in a command name context, if the command name is `foo` then the message _must_ also be `foo`. For other translation systems that require a message ID such as Fluent, consider using a keyword argument to pass it in.

### Methods
- **str(x)** - Returns the message passed to the string.
- **x == y** - Checks if the string is equal to another string.
- **x != y** - Checks if the string is not equal to another string.
- **hash(x)** - Returns the hash of the string. (New in version 2.0)
```

--------------------------------

### Fetch SKUs

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves the bot’s available SKUs.

```APIDOC
## GET /skus

### Description
Retrieves the bot’s available SKUs.

### Method
GET

### Endpoint
/skus

### Raises
- **MissingApplicationID** - The application ID could not be found.
- **HTTPException** - Retrieving the SKUs failed.

### Returns
- **List[SKU]** - The bot’s available SKUs.
```

--------------------------------

### Command Management

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Information on adding commands to the bot.

```APIDOC
## Command Management

### `bot.add_command()` method

#### Description
Adds a `Command` into the internal list of commands. This is usually not called directly; the `command()` or `group()` shortcut decorators are used instead.

#### Method
`add_command(command, /)`

#### Parameters
*   **command** (`Command`) - The command to add.

#### Raises
*   **CommandRegistrationError** - If the command or its alias is already registered by a different command.
*   **TypeError** - If the command passed is not a subclass of `Command`.
```

--------------------------------

### @discord.app_commands.command

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Creates an application command from a regular function.

```APIDOC
## @discord.app_commands.command

### Description
Creates an application command from a regular function.

### Parameters
- **name** (str) - Optional - The name of the application command. Defaults to lower-case callback name.
- **description** (str) - Optional - The description of the command. Defaults to the first line of the docstring.
- **nsfw** (bool) - Optional - Whether the command is NSFW. Defaults to False.
- **auto_locale_strings** (bool) - Optional - If True, translatable strings are wrapped into locale_str. Defaults to True.
- **extras** (dict) - Optional - A dictionary to store extraneous data.
```

--------------------------------

### AppCommandContext

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Wraps up the Discord Command execution context.

```APIDOC
## AppCommandContext

### Description
Wraps up the Discord `Command` execution context.
New in version 2.4.

### Parameters
- **guild** (`Optional[bool]`) – Whether the context allows usage in a guild.
- **dm_channel** (`Optional[bool]`) – Whether the context allows usage in a DM channel.
- **private_channel** (`Optional[bool]`) – Whether the context allows usage in a DM or a GDM channel.

### Properties
- **guild** (`bool`) - Whether the context allows usage in a guild.
- **dm_channel** (`bool`) - Whether the context allows usage in a DM channel.
- **private_channel** (`bool`) - Whether the context allows usage in a DM or a GDM channel.
```

--------------------------------

### PartialAppInfo Model

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents partial application information returned by methods like create_invite().

```APIDOC
## PartialAppInfo

### Description
Represents a partial AppInfo object containing metadata about a Discord application.

### Attributes
- **id** (int) - The application ID.
- **name** (str) - The application name.
- **description** (str) - The application description.
- **rpc_origins** (Optional[List[str]]) - A list of RPC origin URLs.
- **verify_key** (str) - The hex encoded key for verification.
- **terms_of_service_url** (Optional[str]) - The application’s terms of service URL.
- **privacy_policy_url** (Optional[str]) - The application’s privacy policy URL.
- **approximate_guild_count** (int) - The approximate count of the guilds the bot was added to.
- **redirect_uris** (List[str]) - A list of authentication redirect URIs.
- **interactions_endpoint_url** (Optional[str]) - The interactions endpoint URL.
- **role_connections_verification_url** (Optional[str]) - The application’s connection verification URL.
- **icon** (Optional[Asset]) - The application’s icon asset.
- **cover_image** (Optional[Asset]) - The cover image of the application’s default rich presence.
- **flags** (ApplicationFlags) - The application’s flags.
```

--------------------------------

### Asset Handling

Source: https://discordpy.readthedocs.io/en/latest/api.html

Provides methods for reading, saving, and converting assets.

```APIDOC
## Asset Methods

### `_await _read()`

#### Description
This function is a coroutine. Retrieves the content of this asset as a `bytes` object.

#### Returns
- The content of the asset (`bytes`).

#### Raises
- **DiscordException** – There was no internal connection state.
- **HTTPException** – Downloading the asset failed.
- **NotFound** – The asset was deleted.

### `_await _save(_fp_ , _*_ , _seek_begin =True_)`

#### Description
This function is a coroutine. Saves this asset into a file-like object.

#### Parameters
- **fp** (Union[`io.BufferedIOBase`, `os.PathLike`]) – The file-like object to save this asset to or the filename to use. If a filename is passed then a file is created with that filename and used instead.
- **seek_begin** (`bool`) – Whether to seek to the beginning of the file after saving is successfully done.

#### Returns
- The number of bytes written (`int`).

#### Raises
- **DiscordException** – There was no internal connection state.
- **HTTPException** – Downloading the asset failed.
- **NotFound** – The asset was deleted.

### `_await _to_file(_*_ , _filename =..._, _description =None_, _spoiler =False_)`

#### Description
This function is a coroutine. Converts the asset into a `File` suitable for sending via `abc.Messageable.send()`.

#### Parameters
- **filename** (Optional[`str`]) – The filename of the file. If not provided, then the filename from the asset’s URL is used.
- **description** (Optional[`str`]) – The description for the file.
- **spoiler** (`bool`) – Whether the file is a spoiler.

#### Returns
- The asset as a file suitable for sending (`File`).

#### Raises
- **DiscordException** – The asset does not have an associated state.
- **ValueError** – The asset is a unicode emoji.
- **TypeError** – The asset is a sticker with lottie type.
- **HTTPException** – Downloading the asset failed.
- **NotFound** – The asset was deleted.
```

--------------------------------

### discord.ext.tasks.Loop.__call__()

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Details on the __call__ method for tasks.Loop objects.

```APIDOC
## discord.ext.tasks.Loop.__call__()

### Description
This method is called to start or manage a loop task.

### Method
N/A (Internal method)

### Endpoint
N/A

### Parameters
N/A

### Request Example
N/A

### Response
N/A
```

--------------------------------

### Define a basic command

Source: https://discordpy.readthedocs.io/en/latest/faq.html

A standard command definition where arguments are parsed individually.

```python
@bot.command()
async def echo(ctx, message: str):
    await ctx.send(message)
```

--------------------------------

### POST /guild/stickers

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a sticker for the guild. Requires manage_emojis_and_stickers permission.

```APIDOC
## POST /guild/stickers

### Description
Creates a sticker for the guild. Requires manage_emojis_and_stickers permission.

### Parameters
#### Request Body
- **name** (str) - Required - The sticker name.
- **description** (str) - Optional - The sticker’s description.
- **emoji** (str) - Required - The emoji tag associated with the sticker.
- **file** (File) - Required - The file of the sticker to upload.
- **reason** (str) - Optional - The reason for creating this sticker.

### Response
- **GuildSticker** - The created sticker.
```

--------------------------------

### PartialEmoji.to_file

Source: https://discordpy.readthedocs.io/en/latest/api.html

Converts the asset into a File object suitable for sending via messageable channels.

```APIDOC
## [ASYNC] to_file

### Description
Converts the asset into a File suitable for sending via abc.Messageable.send().

### Parameters
#### Request Body
- **filename** (Optional[str]) - Optional - The filename of the file. If not provided, then the filename from the asset’s URL is used.
- **description** (Optional[str]) - Optional - The description for the file.
- **spoiler** (bool) - Optional - Whether the file is a spoiler.

### Response
#### Success Response (200)
- **File** (File) - The asset as a file suitable for sending.
```

--------------------------------

### Webhook.partial

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a partial Webhook object using an ID and token, allowing for subsequent API interactions.

```APIDOC
## Webhook.partial

### Description
Creates a partial Webhook object. A partial webhook is a webhook object containing only an ID and a token.

### Parameters
#### Path Parameters
- **id** (int) - Required - The ID of the webhook.
- **token** (str) - Required - The authentication token of the webhook.

#### Request Body
- **session** (aiohttp.ClientSession) - Optional - The session to use for requests.
- **client** (Client) - Optional - The client to initialize this webhook with.
- **bot_token** (Optional[str]) - Optional - The bot authentication token for authenticated requests.

### Response
- **Webhook** (Object) - A partial Webhook instance.
```

--------------------------------

### Asset I/O Operations

Source: https://discordpy.readthedocs.io/en/latest/api.html

Covers asynchronous methods for reading, saving, and converting assets.

```APIDOC
## Asset I/O Operations

### `async read()`

- **Description**: Retrieves the content of this asset as a `bytes` object.
- **Raises**:
  - **DiscordException**: There was no internal connection state.
  - **HTTPException**: Downloading the asset failed.
  - **NotFound**: The asset was deleted.
- **Returns**: The content of the asset (`bytes`).

### `async save(fp, *_, seek_begin=True)`

- **Description**: Saves this asset into a file-like object.
- **Parameters**:
  - **fp** (Union[`io.BufferedIOBase`, `os.PathLike`]) - The file-like object to save this asset to or the filename to use. If a filename is passed then a file is created with that filename and used instead.
  - **seek_begin** (`bool`) - Whether to seek to the beginning of the file after saving is successfully done.
- **Raises**:
  - **DiscordException**: There was no internal connection state.
  - **HTTPException**: Downloading the asset failed.
  - **NotFound**: The asset was deleted.
- **Returns**: The number of bytes written (`int`).

### `async to_file(*_, filename=None, description=None, spoiler=False)`

- **Description**: Converts the asset into a `File` suitable for sending via `abc.Messageable.send()`.
- **Parameters**:
  - **filename** (Optional[`str`]) - The filename of the file. If not provided, then the filename from the asset’s URL is used.
  - **description** (Optional[`str`]) - The description for the file.
  - **spoiler** (`bool`) - Whether the file is a spoiler.
- **Raises**:
  - **DiscordException**: The asset does not have an associated state.
  - **ValueError**: The asset is a unicode emoji.
  - **TypeError**: The asset is a sticker with lottie type.
  - **HTTPException**: Downloading the asset failed.
  - **NotFound**: The asset was deleted.
- **Returns**: The asset as a file suitable for sending (`File`).
```

--------------------------------

### Send Typing Indicator

Source: https://discordpy.readthedocs.io/en/latest/api.html

Demonstrates the usage of the typing context manager to show a typing indicator for 10 seconds.

```python
# Do some computational magic for about 10 seconds
await channel.send('Done!')
```

--------------------------------

### Create Invite

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new invite for a channel with various options for expiration, usage limits, and temporary membership.

```APIDOC
## POST /channels/{channel.id}/invites

### Description
Creates a new invite for the specified channel.

### Method
POST

### Endpoint
/channels/{channel.id}/invites

### Parameters
#### Query Parameters
- **max_age** (int) - Optional - How long the invite should last in seconds. If it’s 0 then the invite doesn’t expire. Defaults to `0`.
- **max_uses** (int) - Optional - How many uses the invite could be used for. If it’s 0 then there are unlimited uses. Defaults to `0`.
- **temporary** (bool) - Optional - Denotes that the invite grants temporary membership (i.e. they get kicked after they disconnect). Defaults to `False`.
- **unique** (bool) - Optional - Indicates if a unique invite URL should be created. Defaults to True. If this is set to `False` then it will return a previously created invite.
- **reason** (str) - Optional - The reason for creating this invite. Shows up on the audit log.
- **target_type** (InviteTarget) - Optional - The type of target for the voice channel invite, if any.
- **target_user** (User) - Optional - The user whose stream to display for this invite, required if `target_type` is `InviteTarget.stream`. The user must be streaming in the channel.
- **target_application_id** (int) - Optional - The id of the embedded application for the invite, required if `target_type` is `InviteTarget.embedded_application`.
- **guest** (bool) - Optional - Whether the invite is a guest invite.

### Raises
- **HTTPException** – Invite creation failed.
- **NotFound** – The channel that was passed is a category or an invalid channel.

### Returns
- **Invite** (Invite) - The invite that was created.
```

--------------------------------

### Create a Custom ActionRow with Buttons

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Demonstrates subclassing ActionRow to add custom buttons using decorators. This is useful for creating reusable UI elements with predefined interactions.

```python
import discord
from discord import ui

# you can subclass it and add components with the decorators
class MyActionRow(ui.ActionRow):
    @ui.button(label='Click Me!')
    async def click_me(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You clicked me!')

```

--------------------------------

### discord.ext.tasks.Loop Methods

Source: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

Methods for controlling the lifecycle of the background task.

```APIDOC
## start(*args, **kwargs)

### Description
Starts the internal task in the event loop.

### Parameters
- ***args** (any) - Optional - The arguments to use.
- ****kwargs** (any) - Optional - The keyword arguments to use.

### Raises
- **RuntimeError** - A task has already been launched and is running.

### Response
- **asyncio.Task** - The task that has been created.

## stop()

### Description
Gracefully stops the task from running, allowing it to finish its current iteration.

## cancel()

### Description
Cancels the internal task, if it is running.

## restart(*args, **kwargs)

### Description
A convenience method to restart the internal task.

### Parameters
- ***args** (any) - Optional - The arguments to use.
- ****kwargs** (any) - Optional - The keyword arguments to use.
```

--------------------------------

### discord.Webhook.partial()

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Creates a partial webhook object, useful when you only have the webhook ID and token.

```APIDOC
## discord.Webhook.partial()

### Description
Creates a partial webhook object.

### Parameters
*   **id** (int) - Required - The ID of the webhook.
*   **token** (str) - Required - The token of the webhook.
```

--------------------------------

### GroupMixin Class

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

The GroupMixin class provides functionality for managing commands, including adding, removing, and retrieving them. It also handles command registration through decorators.

```APIDOC
## GroupMixin

### Description
A mixin that implements common functionality for classes that behave similar to `Group` and are allowed to register commands.

### Attributes
- **all_commands** (dict) - A mapping of command name to `Command` objects.
- **case_insensitive** (bool) - Whether the commands should be case insensitive. Defaults to `False`.
- **commands** (Set[Command]) - A unique set of commands without aliases that are registered.

### Methods
- **add_command(command: Command, /)**: Adds a `Command` into the internal list of commands. This is usually not called directly; the `command()` or `group()` shortcut decorators are used instead.
  - **Parameters**:
    - **command** (Command) - The command to add.
  - **Raises**:
    - CommandRegistrationError: If the command or its alias is already registered by a different command.
    - TypeError: If the command passed is not a subclass of `Command`.
- **remove_command(name: str, /)**: Removes a `Command` from the internal list of commands. This can also be used to remove aliases.
  - **Parameters**:
    - **name** (str) - The name of the command to remove.
  - **Returns**:
    - Optional[Command] - The command that was removed. Returns `None` if the name is not valid.
- **get_command(name: str, /)**: Gets a `Command` from the internal list of commands. This can also be used to get aliases. The name can be fully qualified (e.g. `'foo bar'`) to get a subcommand.
  - **Parameters**:
    - **name** (str) - The name of the command to get.
  - **Returns**:
    - Optional[Command] - The command that was requested. Returns `None` if not found.
- **walk_commands()**: An iterator that recursively walks through all commands and subcommands.
  - **Yields**:
    - Union[Command, Group] - A command or group from the internal list of commands.

### Decorators
- **@command(\*args, \*\*kwargs)**: A shortcut decorator that invokes `command()` and adds it to the internal command list via `add_command()`. Converts the provided method into a `Command`.
- **@group(\*args, \*\*kwargs)**: A shortcut decorator that invokes `group()` and adds it to the internal command list via `add_command()`. Converts the provided method into a `Group`.
```

--------------------------------

### HybridGroup Decorators

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Explains the various decorators available for HybridGroup, including post-invoke, pre-invoke, autocomplete, error handling, and command/group creation.

```APIDOC
### HybridGroup Decorators

#### @after_invoke

_decorator_ @after_invoke(_coro_)

A decorator that registers a coroutine as a post-invoke hook. A post-invoke hook is called directly after the command is called. This makes it a useful function to clean-up database connections or any type of clean up required.

**Parameters**

- **coro** (coroutine) – The coroutine to register as the post-invoke hook.

**Raises**

- **TypeError** – The coroutine passed is not actually a coroutine.

*See `Bot.after_invoke()` for more info.*

*Changed in version 2.0: `coro` parameter is now positional-only.*

#### @autocomplete

_decorator_ @autocomplete(_name_)

A decorator that registers a coroutine as an autocomplete prompt for a parameter. This is the same as `autocomplete()`. It is only applicable for the application command and doesn’t do anything if the command is a regular command.

**Note**

This is only available if the group has a fallback application command registered.
Similar to the `autocomplete()` method, this takes `Interaction` as a parameter rather than a `Context`.

**Parameters**

- **name** (`str`) – The parameter name to register as autocomplete.

**Raises**

- **TypeError** – The coroutine passed is not actually a coroutine or the parameter is not found or of an invalid type.

#### @before_invoke

_decorator_ @before_invoke(_coro_)

A decorator that registers a coroutine as a pre-invoke hook. A pre-invoke hook is called directly before the command is called. This makes it a useful function to set up database connections or any type of set up required.

**Parameters**

- **coro** (coroutine) – The coroutine to register as the pre-invoke hook.

**Raises**

- **TypeError** – The coroutine passed is not actually a coroutine.

*See `Bot.before_invoke()` for more info.*

*Changed in version 2.0: `coro` parameter is now positional-only.*

#### @command

_decorator_ @command(**args, **kwargs)

A shortcut decorator that invokes `hybrid_command()` and adds it to the internal command list via `add_command()`.

**Returns**

A decorator that converts the provided method into a Command, adds it to the bot, then returns it.

**Return type**

Callable[…, `HybridCommand`]

#### @error

_decorator_ @error(_coro_)

A decorator that registers a coroutine as a local error handler. A local error handler is an `on_command_error()` event limited to a single command. However, the `on_command_error()` is still invoked afterwards as the catch-all.

**Parameters**

- **coro** (coroutine) – The coroutine to register as the local error handler.

**Raises**

- **TypeError** – The coroutine passed is not actually a coroutine.

*Changed in version 2.0: `coro` parameter is now positional-only.*

#### @group

_decorator_ @group(**args, **kwargs)

A shortcut decorator that invokes `hybrid_group()` and adds it to the internal command list via `add_command()`.

**Returns**

A decorator that converts the provided method into a Group, adds it to the bot, then returns it.

**Return type**

Callable[…, `HybridGroup`]
```

--------------------------------

### Add Cog Description

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

The commands.Cog class now accepts a 'description' keyword argument for providing a description to the cog.

```python
class MyCog(commands.Cog, name='My Cog'):
    def __init__(self, bot):
        self.bot = bot

    # ... cog commands ...

    __init__.description = 'This is a description for MyCog.'
```

--------------------------------

### POST /channels/webhooks

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new webhook for the channel.

```APIDOC
## POST /channels/webhooks

### Description
Creates a webhook for this channel. Requires `manage_webhooks` permission.

### Parameters
#### Request Body
- **name** (str) - Required - The webhook's name.
- **avatar** (bytes) - Optional - Bytes-like object for the default avatar.
- **reason** (str) - Optional - The reason for creating this webhook.
```

--------------------------------

### Updating Event Signatures

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_async.html

Several update events now provide both 'before' and 'after' states instead of a single object.

```python
def on_channel_update(channel): pass
def on_member_update(member): pass
def on_status(member): pass
def on_server_role_update(role): pass
def on_voice_state_update(member): pass
def on_socket_raw_send(payload, is_binary): pass
```

```python
def on_channel_update(before, after): pass
def on_member_update(before, after): pass
def on_server_role_update(before, after): pass
def on_voice_state_update(before, after): pass
def on_socket_raw_send(payload): pass
```

--------------------------------

### Per-Command Before and After Invocation Hooks

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Defines specific before and after invocation hooks for a particular command named 'foo'.

```python
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

### InteractionCallbackActivityInstance Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents an activity instance launched as an interaction response.

```APIDOC
## InteractionCallbackActivityInstance

### Description
Represents an activity instance launched as an interaction response. Introduced in version 2.5.

### Attributes
- **id** (str) - The activity instance ID.
```

--------------------------------

### discord.Asset Class Overview

Source: https://discordpy.readthedocs.io/en/latest/api.html

Provides an overview of the discord.Asset class, its attributes, and basic operations.

```APIDOC
## discord.Asset Class

Represents a CDN asset on Discord.

### Attributes
- **key** (`str`) - Returns the identifying key of the asset.
- **url** (`str`) - Returns the URL of the CDN asset.

### Basic Operations
- `str(asset)`: Returns the URL of the CDN asset.
- `len(asset)`: Returns the length of the CDN asset’s URL.
- `asset == other`: Checks if the asset is equal to another asset.
- `asset != other`: Checks if the asset is not equal to another asset.
- `hash(asset)`: Returns the hash of the asset.
```

--------------------------------

### POST /create_voice_channel

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new VoiceChannel in the guild.

```APIDOC
## POST /create_voice_channel

### Description
Creates a new VoiceChannel. This is a coroutine.

### Method
POST

### Parameters
#### Request Body
- **name** (str) - Required - The channel's name.
- **overwrites** (Dict) - Optional - A dict of target to PermissionOverwrite.
- **category** (CategoryChannel) - Optional - The category to place the channel under.
- **position** (int) - Optional - The position in the channel list.
- **bitrate** (int) - Optional - Preferred audio bitrate.
- **user_limit** (int) - Optional - Member limit for the channel.
- **rtc_region** (str) - Optional - Voice region for communication.
- **video_quality_mode** (VideoQualityMode) - Optional - Camera video quality.
- **nsfw** (bool) - Optional - NSFW status.
- **reason** (str) - Optional - Reason for audit log.

### Response
#### Success Response (200)
- **channel** (VoiceChannel) - The channel that was just created.
```

--------------------------------

### Flatten reaction users into a list

Source: https://discordpy.readthedocs.io/en/latest/api.html

Shows how to collect all users who reacted into a list using an asynchronous list comprehension.

```python
users = [user async for user in reaction.users()]
# users is now a list of User...
winner = random.choice(users)
await channel.send(f'{winner} has won the raffle.')
```

--------------------------------

### @command Decorator

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

A decorator that creates an application command from a regular function directly under the CommandTree.

```APIDOC
## @command

### Description
A decorator that creates an application command from a regular function directly under this tree.

### Parameters
- **name** (Union[str, locale_str]) - Optional - The name of the application command.
- **description** (Union[str, locale_str]) - Optional - The description of the application command.
- **nsfw** (bool) - Optional - Whether the command is NSFW. Defaults to False.
- **guild** (Optional[Snowflake]) - Optional - The guild to add the command to.
- **guilds** (List[Snowflake]) - Optional - The list of guilds to add the command to.
- **auto_locale_strings** (bool) - Optional - If True, translatable strings will be wrapped into locale_str. Defaults to True.
- **extras** (dict) - Optional - A dictionary to store extraneous data.
```

--------------------------------

### FFmpegPCMAudio

Source: https://discordpy.readthedocs.io/en/latest/api.html

An audio source from FFmpeg (or AVConv). This launches a sub-process to a specific input file given.

```APIDOC
## FFmpegPCMAudio

### Description
An audio source from FFmpeg (or AVConv). This launches a sub-process to a specific input file given.
Warning: You must have the ffmpeg or avconv executable in your path environment variable in order for this to work.

### Parameters
- **source** (Union[`str`, `io.BufferedIOBase`]) - The input that ffmpeg will take and convert to PCM bytes. If `pipe` is `True` then this is a file-like object that is passed to the stdin of ffmpeg.
- **executable** (`str`) - The executable name (and path) to use. Defaults to `ffmpeg`. Warning: Since this class spawns a subprocess, care should be taken to not pass in an arbitrary executable name when using this parameter.
- **pipe** (`bool`) - If `True`, denotes that `source` parameter will be passed to the stdin of ffmpeg. Defaults to `False`.
- **stderr** (Optional[file object]) - A file-like object to pass to the Popen constructor.
- **before_options** (Optional[`str`]) - Extra command line arguments to pass to ffmpeg before the `-i` flag.
- **options** (Optional[`str`]) - Extra command line arguments to pass to ffmpeg after the `-i` flag.

### Raises
- **ClientException** - The subprocess failed to be created.

### Methods
- **is_opus()**
  Checks if the audio source is already encoded in Opus.
- **read()**
  Reads 20ms worth of audio. Subclasses must implement this. If the audio is complete, then returning an empty bytes-like object to signal this is the way to do so. If `is_opus()` method returns `True`, then it must return 20ms worth of Opus encoded audio. Otherwise, it must be 20ms worth of 16-bit 48KHz stereo PCM, which is about 3,840 bytes per frame (20ms worth of audio).
  Returns: A bytes like object that represents the PCM or Opus data.
  Return type: `bytes`
```

--------------------------------

### Member Avatar URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of Member.avatar_url_as with Member.avatar.replace.

```python
Member.avatar.replace
```

--------------------------------

### @app_commands.autocomplete

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Associates a parameter with an autocomplete callback function to provide dynamic suggestions.

```APIDOC
## @app_commands.autocomplete

### Description
Registers a callback function that provides dynamic suggestions for a command parameter as the user types.

### Parameters
#### Parameters
- **parameters** (Callable) - Required - The parameters to mark as autocomplete.

### Request Example
@app_commands.autocomplete(fruit=fruit_autocomplete)
async def fruits(interaction: discord.Interaction, fruit: str):
    ...
```

--------------------------------

### Set channel permissions using keyword arguments

Source: https://discordpy.readthedocs.io/en/latest/api.html

Sets specific permission flags directly via keyword arguments. This approach cannot be combined with the overwrite parameter.

```python
await message.channel.set_permissions(message.author, read_messages=True,
                                                      send_messages=False)
```

--------------------------------

### CommandTree Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents a container that holds application command information and manages command registration.

```APIDOC
## CommandTree

### Description
Represents a container that holds application command information.

### Parameters
- **client** (Client) - Required - The client instance to get application command information from.
- **fallback_to_global** (bool) - Optional - If a guild-specific command is not found, try falling back to a global command. Defaults to True.
- **allowed_contexts** (AppCommandContext) - Optional - The default allowed contexts that applies to all commands in this tree.
- **allowed_installs** (AppInstallationType) - Optional - The default allowed install locations that apply to all commands in this tree.
```

--------------------------------

### Use check_any for logical OR conditions

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Combines multiple checks so that the command executes if any one of the provided checks passes.

```python
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

### DynamicItem Methods

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Instance methods available for the DynamicItem class.

```APIDOC
## DynamicItem Callback and Interaction Check Methods

### Description
Methods that handle the callback and interaction check for DynamicItem.

### Methods

* **`await _callback(_interaction_)`**
  The callback associated with this UI item. This can be overridden by subclasses.

  ### Parameters
  * **interaction** (`Interaction`) – The interaction that triggered this UI item.

* **`await _interaction_check(_interaction_ , _/_)`**
  A callback that is called when an interaction happens within this item that checks whether the callback should be processed. This is useful to override if, for example, you want to ensure that the interaction author is a given user. The default implementation of this returns `True`.

  **Note**: If an exception occurs within the body then the check is considered a failure and `View.on_error()` (or `LayoutView.on_error()`) is called. For `DynamicItem` this does not call the `on_error` handler.
  New in version 2.4.

  ### Parameters
  * **interaction** (`Interaction`) – The interaction that occurred.

  ### Returns
  Whether the callback should be called.

  ### Return type
  `bool`
```

--------------------------------

### Create a basic command check

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Shows a simple predicate function used to restrict a command to a specific user ID.

```python
def check_if_it_is_me(ctx):
    return ctx.message.author.id == 85309593344815104

@bot.command()
@commands.check(check_if_it_is_me)
async def only_for_me(ctx):
    await ctx.send('I know you!')
```

--------------------------------

### Exception Hierarchy Overview

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

A structural overview of the exception classes available in discord.py.

```APIDOC
## Exception Hierarchy

### Description
The discord.py library uses a hierarchical exception system to handle various error states during command processing, extension loading, and client operations.

### Base Exceptions
- **DiscordException**: The base class for all exceptions in the library.
- **CommandError**: Base class for all command-related errors.
- **ExtensionError**: Base class for all extension-related errors.
- **ClientException**: Base class for client-specific errors.

### Key Subclasses
- **UserInputError**: Errors occurring due to invalid user input (e.g., MissingRequiredArgument, BadArgument).
- **CheckFailure**: Errors occurring when command checks fail (e.g., MissingPermissions, NotOwner).
- **ExtensionError**: Errors occurring during extension management (e.g., ExtensionNotFound, ExtensionFailed).
```

--------------------------------

### Discord Resource Creation Methods

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

A collection of methods used to create various resources within a Discord guild or client context.

```APIDOC
## Resource Creation Methods

### Description
These methods allow for the creation of various Discord entities such as channels, threads, webhooks, and guild-specific resources.

### Methods
- `create_application_emoji()`: Creates an application emoji.
- `create_automod_rule()`: Creates an auto-moderation rule in a guild.
- `create_category()` / `create_category_channel()`: Creates a category channel.
- `create_custom_emoji()`: Creates a custom emoji in a guild.
- `create_dm()`: Creates a direct message channel.
- `create_entitlement()`: Creates an entitlement.
- `create_forum()`: Creates a forum channel.
- `create_guild()`: Creates a new guild.
- `create_instance()`: Creates a stage instance.
- `create_integration()`: Creates a guild integration.
- `create_invite()`: Creates an invite for a channel.
- `create_role()`: Creates a new role in a guild.
- `create_scheduled_event()`: Creates a scheduled event.
- `create_soundboard_sound()`: Creates a soundboard sound.
- `create_stage_channel()`: Creates a stage channel.
- `create_sticker()`: Creates a sticker.
- `create_tag()`: Creates a tag in a forum channel.
- `create_template()`: Creates a guild template.
- `create_text_channel()`: Creates a text channel.
- `create_thread()`: Creates a thread from a message or channel.
- `create_voice_channel()`: Creates a voice channel.
- `create_webhook()`: Creates a webhook for a channel.
```

--------------------------------

### Group Configuration Options

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Configuration options for a Group.

```APIDOC
## Group Configuration Options

### auto_locale_strings

(`bool`) – If this is set to `True`, then all translatable strings will implicitly be wrapped into `locale_str` rather than `str`. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to `True`.

### extras

(`dict`) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.
```

--------------------------------

### @group

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Shortcut decorator to create and register a command group.

```APIDOC
## @group

### Description
A shortcut decorator that invokes group() and adds it to the internal command list via add_command().

### Returns
- **Callable[..., Group]** - A decorator that converts the method into a Group and adds it to the bot.
```

--------------------------------

### Subclassing discord.ui.Container with a Button

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Demonstrates how to subclass discord.ui.Container and add interactive components like buttons. The button is defined using a decorator and handles interaction responses.

```Python
import discord
from discord import ui

# you can subclass it and add components as you would add them
# in a LayoutView
class MyContainer(ui.Container):
    action_row = ui.ActionRow()

    @action_row.button(label='A button in a container!')
    async def a_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You clicked a button!')

```

--------------------------------

### Create Category with Position

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Create a new category in a guild and specify its position in the channel list. Positions are zero-indexed.

```Python
category = await guild.create_category('New Category', position=0)
```

--------------------------------

### discord.ext.commands.command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Transforms a function into a Command. Automatically extracts help text from the docstring.

```APIDOC
## @discord.ext.commands.command

### Description
A decorator that transforms a function into a `Command` or if called with `group()`, `Group`. By default the `help` attribute is received automatically from the docstring of the function and is cleaned up with the use of `inspect.cleandoc`. If the docstring is `bytes`, then it is decoded into `str` using utf-8 encoding. All checks added using the `check()` & co. decorators are added into the function. There is no way to supply your own checks through this decorator.

### Parameters
- **name** (str) - The name to create the command with. By default this uses the function name unchanged.
- **cls** - The class to construct with. By default this is `Command`. You usually do not change this.
- **attrs** - Keyword arguments to pass into the construction of the class denoted by `cls`.

### Raises
- **TypeError** - If the function is not a coroutine or is already a command.
```

--------------------------------

### Iterate Over SKU Subscriptions

Source: https://discordpy.readthedocs.io/en/latest/api.html

Use an asynchronous for loop to retrieve subscriptions for a given SKU. You can specify a limit and filter by user. This is useful for iterating through multiple subscriptions.

```python
async for subscription in sku.subscriptions(limit=100, user=user):
    print(subscription.user_id, subscription.current_period_end)
```

--------------------------------

### Construct MessageReference

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

MessageReference can now be constructed by users, providing more control over message referencing.

```python
message_reference = MessageReference(message_id=1234567890, channel_id=9876543210)
```

--------------------------------

### UI View Management

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods for registering and removing persistent UI components.

```APIDOC
## POST /views/dynamic-items

### Description
Registers DynamicItem classes for persistent listening.

## DELETE /views/dynamic-items

### Description
Removes DynamicItem classes from persistent listening.

## POST /views

### Description
Registers a View for persistent listening.

### Parameters
#### Request Body
- **view** (Union[discord.ui.View, discord.ui.LayoutView]) - Required - The view to register.
- **message_id** (int) - Optional - The message ID that the view is attached to.
```

--------------------------------

### PartialInviteGuild Banner URL Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of PartialInviteGuild.banner_url with PartialInviteGuild.banner.

```python
PartialInviteGuild.banner
```

--------------------------------

### @listen

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Registers a function as an external event listener.

```APIDOC
## @listen

### Description
A decorator that registers another function as an external event listener, allowing multiple listeners for the same event.

### Parameters
- **name** (str) - Optional - The name of the event to listen to.

### Request Example
```python
@bot.listen()
async def on_message(message):
    print('one')
```
```

--------------------------------

### Command Cogs and Metadata

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Details on Cogs, their lifecycle methods, and related metadata.

```APIDOC
## Command Cogs and Metadata

### Description
This section explains the concept of Cogs in discord.py for organizing commands, including methods for loading, unloading, and managing Cogs, as well as accessing Cog-related information.

### Cog Classes
- `commands.Cog`
- `commands.CogMeta`

### Cog Management
- `commands.Bot.cogs`
- `commands.Cog.cog_after_invoke()`
- `commands.Cog.cog_app_command_error()`
- `commands.Cog.cog_before_invoke()`
- `commands.Cog.cog_check()`
- `commands.Cog.cog_command_error()`
- `commands.Cog.cog_load()`
- `commands.Cog.cog_unload()`

### Cog Metadata
- `commands.Command.cog`
- `commands.Context.cog`
- `commands.HelpCommand.cog`
- `commands.Command.cog_name`
- `commands.Group.cog_name`
- `commands.HybridGroup.cog_name`
```

--------------------------------

### FFmpegAudio

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents an FFmpeg (or AVConv) based AudioSource.

```APIDOC
## FFmpegAudio

### Description
Represents an FFmpeg (or AVConv) based AudioSource. User created AudioSources using FFmpeg differently from how `FFmpegPCMAudio` and `FFmpegOpusAudio` work should subclass this.
New in version 1.3.

### Methods
- **cleanup()**
  Called when clean-up is needed to be done. Useful for clearing buffer data or processes after it is done playing audio.
```

--------------------------------

### Fix CustomActivity createdAt Uninitialized

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Corrects an issue where CustomActivity.created_at might be uninitialized.

```python
# No specific code example provided, but fixes uninitialized CustomActivity.created_at.
```

--------------------------------

### AppInfo Cover Image URL Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of AppInfo.cover_image_url with AppInfo.cover_image.

```python
AppInfo.cover_image
```

--------------------------------

### discord.on_shard_ready(_shard_id_)

Source: https://discordpy.readthedocs.io/en/latest/api.html

Used by `AutoShardedClient` to indicate when a specific shard has become ready.

```APIDOC
## discord.on_shard_ready(_shard_id_)

### Description
Similar to `on_ready()` except used by `AutoShardedClient` to denote when a particular shard ID has become ready.

### Method
Event

### Endpoint
N/A (Internal Event)

### Parameters
#### Path Parameters
- **shard_id** (`int`) - Required - The shard ID that is ready.

### Request Example
N/A

### Response
N/A

#### Success Response (N/A)
N/A

#### Response Example
N/A
```

--------------------------------

### discord.SKUType

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents the type of a SKU.

```APIDOC
## Class: discord.SKUType

### Description
Represents the type of a SKU.

### Members
- **durable**: The SKU is a durable one-time purchase.
- **consumable**: The SKU is a consumable one-time purchase.
- **subscription**: The SKU is a recurring subscription.
- **subscription_group**: The SKU is a system-generated group.

### Version
New in version 2.4.
```

--------------------------------

### BaseActivity Class

Source: https://discordpy.readthedocs.io/en/latest/api.html

The base class for all user-settable activities in discord.py.

```APIDOC
## class discord.BaseActivity

### Description
The base activity that all user-settable activities inherit from. Used in `Client.change_presence()`.

### Attributes
- **created_at** (Optional[datetime.datetime]) - When the user started doing this activity in UTC. (New in 1.3)
```

--------------------------------

### HybridGroup Class Overview

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Provides an overview of the HybridGroup class, its purpose, and how it functions as both a text and application command group.

```APIDOC
## HybridGroup Class

### Description
A class that is both an application command group and a regular text group. It doubles as an application command group, with the callback only being called if it's not invoked as an application command. Hybrid groups always have `Group.invoke_without_command` set to `True`.

New in version 2.0.

### Attributes
- **clean_params** - Parameters cleaned for use.
- **cog_name** - The name of the cog this command belongs to.
- **commands** - A dictionary of commands in this group.
- **cooldown** - The cooldown applied to this command.
- **fallback** - The command name to use as a fallback for the application command.
- **fallback_locale** - The fallback command name's locale string, if available.
- **full_parent_name** - The full parent name of the command.
- **parents** - A list of parent groups.
- **qualified_name** - The qualified name of the command.
- **root_parent** - The root parent of the command.
- **short_doc** - The short documentation string for the command.
- **signature** - The signature of the command.

### Methods
- **add_check(predicate)**: Adds a check to the command.
- **add_command(command)**: Adds a command to this group.
- **@after_invoke(coro)**: Registers a coroutine as a post-invoke hook.
- **@autocomplete(_name_)**: Registers a coroutine as an autocomplete prompt for a parameter.
- **@before_invoke(coro)**: Registers a coroutine as a pre-invoke hook.
- **can_run(ctx)**: Checks if the command can be executed.
- **@command(**args, **kwargs)**: A shortcut decorator that invokes `hybrid_command()`.
- **copy()**: Creates a copy of the command.
- **@error(coro)**: Registers a coroutine as a local error handler.
- **get_command(name)**: Gets a command from this group by name.
- **get_cooldown_retry_after(ctx)**: Gets the remaining cooldown time for the command.
- **@group(**args, **kwargs)**: A shortcut decorator that invokes `hybrid_group()`.
- **has_error_handler()**: Checks if the command has a local error handler.
- **is_on_cooldown(ctx)**: Checks if the command is currently on cooldown.
- **remove_check(predicate)**: Removes a check from the command.
- **remove_command(name)**: Removes a command from this group.
- **reset_cooldown(ctx)**: Resets the cooldown for the command.
- **update(**kwargs)**: Updates the command with new keyword arguments.
- **walk_commands()**: Returns an iterator of all commands in this group.
```

--------------------------------

### Accessing Guild Icon with Asset Object

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Demonstrates how to access the Guild icon using the new Asset object, replacing older methods like Guild.icon_url.

```python
guild.icon
```

--------------------------------

### Bot Execution

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Function to run the bot with a given token, handling connection and logging.

```APIDOC
## run

### Description
A blocking call that abstracts away the event loop initialisation from you. If you want more control over the event loop then this function should not be used. Use `start()` coroutine or `connect()` + `login()`.
This function also sets up the logging library to make it easier for beginners to know what is going on with the library. For more advanced users, this can be disabled by passing `None` to the `log_handler` parameter.

**Warning**: This function must be the last function to call due to the fact that it is blocking. That means that registration of events or anything being called after this function call will not execute until it returns.

### Method
run

### Parameters
#### Path Parameters
- **token** (str) - Required - The authentication token. Do not prefix this token with anything as the library will do it for you.
- **reconnect** (bool) - Optional - If we should attempt reconnecting, either due to internet failure or a specific failure on Discord’s part. Certain disconnects that lead to bad state will not be handled (such as invalid sharding payloads or bad tokens).
- **log_handler** (Optional[logging.Handler]) - Optional - The log handler to use for the library’s logger. If this is `None` then the library will not set up anything logging related. Logging will still work if `None` is passed, though it is your responsibility to set it up. The default log handler if not provided is `logging.StreamHandler`.
- **log_formatter** (logging.Formatter) - Optional - The formatter to use with the given log handler. If not provided then it defaults to a colour based logging formatter (if available).
- **log_level** (int) - Optional - The default log level for the library’s logger. This is only applied if the `log_handler` parameter is not `None`. Defaults to `logging.INFO`.
- **root_logger** (bool) - Optional - 
```

--------------------------------

### Thread and Channel Actions

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Methods and properties for interacting with threads and channels.

```APIDOC
## discord.Thread.join()

### Description
Joins the thread.

### Method
ASYNC

## discord.abc.GuildChannel.jump_url

### Description
Returns the URL to jump to the channel.

### Type
property
```

--------------------------------

### Fetch Guild Integrations

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Retrieve a list of all integrations associated with a specific guild. Integrations can include bots, webhooks, etc.

```Python
integrations = await guild.integrations()
```

--------------------------------

### Guild Banner URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of Guild.banner_url_as with Guild.banner.replace.

```python
Guild.banner.replace
```

--------------------------------

### commands.param() alias

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

An alias for the commands.parameter() function.

```APIDOC
## Function discord.ext.commands.param

### Description
An alias for `parameter()`.

### Parameters
- **converter** (Any) - The converter to use for this parameter.
- **default** (Any) - The default value for the parameter.
- **description** (str) - The description of this parameter.
- **displayed_default** (str) - The displayed default in `Command.signature`.
- **displayed_name** (str) - The name that is displayed to the user.
```

--------------------------------

### Adding Asset Helper Methods

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Highlights the addition of helper methods to the Asset object for customizing size and format.

```python
Asset.with_size()
```

```python
Asset.with_format()
```

```python
Asset.with_static_format()
```

--------------------------------

### SelectMenu Component

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents a select menu from the Discord Bot UI Kit.

```APIDOC
## SelectMenu

### Description
Represents a select menu from the Discord Bot UI Kit. A select menu is functionally the same as a dropdown.

### Attributes
- **type** (ComponentType) - The type of component.
- **custom_id** (Optional[str]) - The ID of the select menu that gets received during an interaction.
- **placeholder** (Optional[str]) - The placeholder text that is shown if nothing is selected.
- **min_values** (int) - The minimum number of items that must be chosen.
- **max_values** (int) - The maximum number of items that must be chosen.
- **options** (List[SelectOption]) - A list of options that can be selected.
- **disabled** (bool) - Whether the select is disabled or not.
- **channel_types** (List[ChannelType]) - A list of channel types that are allowed to be chosen.
- **id** (Optional[int]) - The ID of this component.
- **required** (bool) - Whether the select is required.
```

--------------------------------

### Custom Converter with Parameter Metadata

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Use `commands.parameter` to specify a custom converter for a command parameter, resolving type checker warnings.

```python
class SomeType:
    foo: int

class MyVeryCoolConverter(commands.Converter[SomeType]):
    ...

@bot.command()
async def bar(ctx, cool_value: SomeType = commands.parameter(converter=MyVeryCoolConverter)):
    cool_value.foo  # no error (hurray)
```

--------------------------------

### POST /channels/{channel_id}/voice-connect

Source: https://discordpy.readthedocs.io/en/latest/api.html

Connects to a voice channel and creates a VoiceClient.

```APIDOC
## POST /channels/{channel_id}/voice-connect

### Description
Connects to voice and creates a VoiceClient to establish your connection to the voice server.

### Parameters
#### Request Body
- **timeout** (float) - Optional - The timeout in seconds to wait the connection to complete.
- **reconnect** (bool) - Optional - Whether the bot should automatically attempt a reconnect.
- **cls** (Type[VoiceProtocol]) - Optional - A type that subclasses VoiceProtocol to connect with.
- **self_mute** (bool) - Optional - Indicates if the client should be self-muted.
- **self_deaf** (bool) - Optional - Indicates if the client should be self-deafened.

### Response
#### Success Response (200)
- **voice_client** (VoiceProtocol) - A voice client that is fully connected to the voice server.
```

--------------------------------

### POST /channels/{channel.id}/webhooks

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a webhook for the current channel. Requires 'manage_webhooks' permission. New in version 2.0.

```APIDOC
## POST /channels/{channel.id}/webhooks

### Description
Creates a webhook for this channel. You must have `manage_webhooks` to do this. New in version 2.0.

### Method
POST

### Endpoint
/channels/{channel.id}/webhooks

### Parameters
#### Query Parameters
- **name** (str) - Required - The webhook’s name.
- **avatar** (Optional[bytes]) - Optional - A bytes-like object representing the webhook’s default avatar. This operates similarly to `edit()`.
- **reason** (Optional[str]) - Optional - The reason for creating this webhook. Shows up in the audit logs.

### Response
#### Success Response (200)
- **Webhook** (Webhook) - The created webhook.

#### Error Response
- **HTTPException** - Creating the webhook failed.
- **Forbidden** - You do not have permissions to create a webhook.
```

--------------------------------

### Member Default Avatar URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of Member.default_avatar_url_as with Member.default_avatar.replace.

```python
Member.default_avatar.replace
```

--------------------------------

### POST /entitlement

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Creates a test Entitlement for the application.

```APIDOC
## POST /entitlement

### Description
Creates a test Entitlement for the application.

### Method
POST

### Parameters
#### Request Body
- **sku** (Snowflake) - Required - The SKU to create the entitlement for.
- **owner** (Snowflake) - Required - The ID of the owner.
- **owner_type** (EntitlementOwnerType) - Required - The type of the owner.
```

--------------------------------

### Guild Invites API

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a list of all active instant invites from the guild. Requires `manage_guild` permission.

```APIDOC
## GET /guilds/{guild.id}/invites

### Description
Returns a list of all active instant invites from the guild. Requires `manage_guild` permission.

### Method
GET

### Endpoint
`/guilds/{guild.id}/invites`

### Raises
- **Forbidden** - You do not have proper permissions to get the information.
- **HTTPException** - An error occurred while fetching the information.

### Returns
- List[Invite] - The list of invites that are currently active.
```

--------------------------------

### Decorators for Adding Components

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Details on using decorators to easily add buttons and select menus to an ActionRow.

```APIDOC
## Component Decorators

### `button()` Decorator

A decorator to attach a button to the action row. The decorated function acts as the button's callback.

```python
@row.button(label='A button!', custom_id='my_button')
async def row_button(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message('Button clicked!')
```

Parameters:
  - label (Optional[str]) – The label of the button (max 80 characters).
  - custom_id (Optional[str]) – The ID of the button for interaction events (max 100 characters). Recommended to leave unset.
  - style (ButtonStyle) – The visual style of the button. Defaults to `ButtonStyle.secondary`.
  - disabled (bool) – Whether the button is disabled. Defaults to `False`.
  - emoji (Optional[Union[str, Emoji, PartialEmoji]]) – An emoji to display on the button.
  - id (Optional[int]) – The unique ID of the component within the view. New in version 2.6.

Note: URL or SKU buttons cannot be created with this decorator; use `ActionRow.add_item()` with a manually created `discord.ui.Button` instead.

### `select()` Decorator

A decorator to attach a select menu to the action row. The decorated function acts as the select menu's callback.

```python
@row.select(
    placeholder='Choose an option!',
    options=[
        discord.SelectOption(label='Option 1', value='1'),
        discord.SelectOption(label='Option 2', value='2'),
    ]
)
async def row_select(self, interaction: discord.Interaction, select: discord.ui.Select):
    await interaction.response.send_message(f'You selected: {select.values[0]}')
```

Parameters:
  - cls (Type[Select]) – The select menu class to use. Defaults to `discord.ui.select.Select`.
  - options (List[SelectOption]) – The options available in the select menu.
  - channel_types (Optional[List[ChannelType]]) – List of channel types the select menu is valid in.
  - placeholder (Optional[str]) – Text shown when no options are selected.
  - custom_id (Optional[str]) – The ID for the select menu interaction.
  - min_values (int) – The minimum number of options a user must select. Defaults to 1.
  - max_values (int) – The maximum number of options a user can select. Defaults to 1.
  - disabled (bool) – Whether the select menu is disabled. Defaults to `False`.
  - default_values (Optional[List[SelectDefaultValue]]) – Pre-selected options.
  - id (Optional[int]) – The unique ID of the component within the view. New in version 2.6.

```

--------------------------------

### Create Guild Integration

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Create a new integration for a guild. This typically involves providing integration type and relevant data.

```Python
integration = await guild.create_integration(type='twitch', id=1234567890)
```

--------------------------------

### GroupChannel Icon URL As Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of GroupChannel.icon_url_as with GroupChannel.icon.replace.

```python
GroupChannel.icon.replace
```

--------------------------------

### ContextMenu Error Handling

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Registering a local error handler for a ContextMenu command.

```APIDOC
## @error(coro)

### Description
A decorator that registers a coroutine as a local error handler for the context menu command.

### Parameters
- **coro** (coroutine) - Required - The coroutine to register as the local error handler. Must accept (interaction, error) parameters.

### Raises
- **TypeError** - If the provided object is not a coroutine.
```

--------------------------------

### Invite Management

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Methods for retrieving and managing server invites.

```APIDOC
## Invite Management Methods

### Description
Methods to retrieve lists of invites for various channel types and guild objects.

### Methods
- `discord.Guild.invites()`
- `discord.TextChannel.invites()`
- `discord.VoiceChannel.invites()`
- `discord.CategoryChannel.invites()`
- `discord.ForumChannel.invites()`
- `discord.StageChannel.invites()`
```

--------------------------------

### Send a basic message

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Use `channel.send()` to send messages. This replaces the older `client.send_message()` method.

```python
await channel.send('Hello')
```

--------------------------------

### Cog Method for Before and After Invocation Hooks

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_v1.html

Implements before and after invocation hooks within a Cog class, demonstrating how to set cog-specific data and log command completion.

```python
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

### GroupChannel Icon Key

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of GroupChannel.icon with GroupChannel.icon.key.

```python
GroupChannel.icon.key
```

--------------------------------

### run_converters Utility

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

A utility function to manually run converters for a given context, converter, argument, and parameter.

```APIDOC
## `discord.ext.commands.run_converters` Utility

### Description
This coroutine function manually runs converters for a given converter, argument, and parameter within a specified context. It replicates the library's internal conversion process.

### Parameters
- `ctx` (Context) - The invocation context.
- `converter` (Any) - The converter to use (e.g., a type hint or a converter class).
- `argument` (str) - The argument string to convert.
- `param` (Parameter) - The parameter object, primarily used for error reporting.

### Raises
- `CommandError` - If the converter fails during execution.

### Returns
- `Any` - The successfully converted value.
```

--------------------------------

### get_destination

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves the destination for help command output.

```APIDOC
## get_destination

### Description
Returns the Messageable where the help command will be output. Defaults to the context's channel.

### Response
- **abc.Messageable** - The destination where the help command will be output.
```

--------------------------------

### POST /reply

Source: https://discordpy.readthedocs.io/en/latest/api.html

A shortcut method to reply to a message.

```APIDOC
## POST /reply

### Description
A shortcut method to `abc.Messageable.send()` to reply to the `Message`.

### Method
POST

### Parameters
#### Request Body
- **content** (str) - Optional - The content of the reply.
- **kwargs** (dict) - Optional - Additional arguments for sending the message.

### Response
#### Success Response (200)
- **message** (Message) - The message that was sent.

### Error Handling
- **HTTPException**: Sending the message failed.
- **Forbidden**: You do not have the proper permissions to send the message.
- **ValueError**: The `files` list is not of the appropriate size.
- **TypeError**: You specified both `file` and `files`.
```

--------------------------------

### Voice Control Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods for managing audio playback state and sending audio data.

```APIDOC
## pause()

### Description
Pauses the audio playing.

## resume()

### Description
Resumes the audio playing.

## send_audio_packet(data, encode=True)

### Description
Sends an audio packet composed of the data. You must be connected to play audio.

### Parameters
#### Request Body
- **data** (bytes) - Required - The bytes-like object denoting PCM or Opus voice data.
- **encode** (bool) - Optional - Indicates if data should be encoded into Opus.

### Errors
- **ClientException**: You are not connected.
- **opus.OpusError**: Encoding the data failed.
```

--------------------------------

### Autocomplete Functionality

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Details on how to implement and use autocomplete features for application commands.

```APIDOC
## discord.app_commands.Argument.autocomplete

### Description
Attribute related to autocomplete for command arguments.

### Endpoint
N/A (Attribute of an object)

## discord.app_commands.Parameter.autocomplete

### Description
Attribute related to autocomplete for command parameters.

### Endpoint
N/A (Attribute of an object)

## discord.InteractionType.autocomplete

### Description
Represents the interaction type for autocomplete requests.

### Endpoint
N/A (Enum value)

## discord.app_commands.Command.autocomplete()

### Description
Method to define or handle autocomplete for a command.

### Endpoint
N/A (Method of an object)

## discord.app_commands.Transformer.autocomplete()

### Description
Method to define or handle autocomplete for a transformer.

### Endpoint
N/A (Method of an object)

## commands.HybridCommand.autocomplete()

### Description
Method to define or handle autocomplete for a hybrid command.

### Endpoint
N/A (Method of an object)

## commands.HybridGroup.autocomplete()

### Description
Method to define or handle autocomplete for a hybrid command group.

### Endpoint
N/A (Method of an object)

## discord.InteractionResponse.autocomplete()

### Description
Method to respond to an autocomplete interaction.

### Endpoint
N/A (Method of an object)

## discord.app_commands.autocomplete()

### Description
Decorator or function to register an autocomplete callback.

### Endpoint
N/A (Function/Decorator)

## discord.InteractionResponseType.autocomplete_result

### Description
Represents the response type for autocomplete results.

### Endpoint
N/A (Enum value)
```

--------------------------------

### POST /channels/{channel_id}/stage-instances

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new stage instance for the specified stage channel.

```APIDOC
## POST /channels/{channel_id}/stage-instances

### Description
Creates a stage instance for the stage channel. Requires `manage_channels` permission.

### Method
POST

### Endpoint
/channels/{channel_id}/stage-instances

### Parameters
#### Request Body
- **topic** (str) - Required - The stage instance’s topic.
- **privacy_level** (PrivacyLevel) - Optional - The stage instance’s privacy level. Defaults to `PrivacyLevel.guild_only`.
- **send_start_notification** (bool) - Optional - Whether to send a start notification. Defaults to `False`.
- **scheduled_event** (Snowflake) - Optional - The guild scheduled event associated with the stage instance.
- **reason** (str) - Optional - The reason the stage instance was created for the audit log.

### Response
#### Success Response (200)
- **instance** (StageInstance) - The newly created stage instance.

### Errors
- **TypeError**: If the `privacy_level` parameter is not the proper type.
- **Forbidden**: You do not have permissions to create a stage instance.
- **HTTPException**: Creating a stage instance failed.
```

--------------------------------

### @hybrid_command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Shortcut decorator to create and register a hybrid command.

```APIDOC
## @hybrid_command

### Description
A shortcut decorator that invokes hybrid_command() and adds it to the internal command list via add_command().

### Parameters
- **name** (str) - Optional - Name of the command.
- **with_app_command** (bool) - Optional - Whether to include an app command (default: True).

### Returns
- **Callable[..., HybridCommand]** - A decorator that converts the method into a Command and adds it to the bot.
```

--------------------------------

### Create Discord Channel Webhook

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new webhook for a channel. Requires `manage_webhooks` permission. An optional avatar can be provided.

```python
await channel.create_webhook(name='MyWebhook', avatar=webhook_avatar_bytes, reason='Creating a new webhook')
```

--------------------------------

### POST /guild/integrations

Source: https://discordpy.readthedocs.io/en/latest/api.html

Attaches an integration to the guild. Requires manage_guild permission.

```APIDOC
## POST /guild/integrations

### Description
Attaches an integration to the guild. Requires manage_guild permission.

### Parameters
#### Request Body
- **type** (str) - Required - The integration type (e.g. Twitch).
- **id** (int) - Required - The integration ID.
```

--------------------------------

### AppInfo Icon URL Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Shows the replacement of AppInfo.icon_url with AppInfo.icon.

```python
AppInfo.icon
```

--------------------------------

### Soundboard and DM API

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods for retrieving soundboard sounds and managing DM channels.

```APIDOC
## GET /soundboard/default

### Description
Retrieves all default soundboard sounds.

## POST /users/{user}/dm

### Description
Creates a DMChannel with the specified user.

### Parameters
#### Path Parameters
- **user** (Snowflake) - Required - The user to create a DM with.
```

--------------------------------

### Webhook.fetch

Source: https://discordpy.readthedocs.io/en/latest/api.html

Fetches the latest information about the webhook from Discord.

```APIDOC
## Webhook.fetch

### Description
This is a coroutine that fetches the current state of the webhook from the Discord API.

### Parameters
#### Query Parameters
- **prefer_auth** (bool) - Optional - Whether to prefer using authentication when fetching the webhook.
```

--------------------------------

### ContextMenu Check Management

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Methods for managing command execution checks.

```APIDOC
## add_check(func)

### Description
Adds a check to the command to determine if the callback should be executed.

### Parameters
- **func** (function) - Required - The predicate function to add.

## remove_check(func)

### Description
Removes a check from the command. This method is idempotent.

### Parameters
- **func** (function) - Required - The function to remove.
```

--------------------------------

### Follow Channel with Webhook

Source: https://discordpy.readthedocs.io/en/latest/api.html

Follows a channel using a webhook. This is only applicable to news channels. The returned webhook will not have a token for actions.

```APIDOC
## POST /channels/{channel.id}/followers

### Description
Follows a channel using a webhook. Only news channels can be followed.

### Method
POST

### Endpoint
`/channels/{channel.id}/followers`

### Parameters
#### Path Parameters
- **channel.id** (int) - Required - The ID of the channel to follow from.

#### Query Parameters
None

#### Request Body
- **webhook_channel_id** (int) - Required - The ID of the webhook channel to follow.
- **webhook_id** (int) - Required - The ID of the webhook to follow.

### Request Example
```json
{
  "webhook_channel_id": 123456789012345678,
  "webhook_id": 987654321098765432
}
```

### Response
#### Success Response (200)
- **webhook** (Webhook) - The created webhook.

#### Response Example
```json
{
  "id": "123456789012345678",
  "type": 1,
  "name": "My Awesome Webhook"
}
```

### Raises
- **Forbidden** – You do not have permissions to create a webhook.
- **HTTPException** – Following the channel failed.
- **ClientException** – The channel is not a news channel.
- **TypeError** – The destination channel is not a text channel.
```

--------------------------------

### POST /create_category

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new CategoryChannel in the guild.

```APIDOC
## POST /create_category

### Description
Creates a new CategoryChannel. This is a coroutine.

### Method
POST

### Parameters
#### Request Body
- **name** (str) - Required - The channel's name.
- **overwrites** (Dict) - Optional - A dict of target to PermissionOverwrite.
- **reason** (str) - Optional - Reason for audit log.
- **position** (int) - Optional - The position in the channel list.

### Response
#### Success Response (200)
- **channel** (CategoryChannel) - The channel that was just created.
```

--------------------------------

### Create Thread

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a thread in this text channel. To create a public thread, you must have `create_public_threads`. For a private thread, `create_private_threads` is needed instead.

```APIDOC
## POST /channels/{channel.id}/threads

### Description
Creates a thread in this text channel.

### Method
POST

### Endpoint
`/channels/{channel.id}/threads`

### Parameters
#### Path Parameters
- **channel.id** (int) - Required - The ID of the channel to create the thread in.

#### Query Parameters
None

#### Request Body
- **name** (str) - Required - The name of the thread.
- **message_id** (int) - Optional - A snowflake representing the message to create the thread with. If `None` is passed then a private thread is created.
- **auto_archive_duration** (int) - Optional - The duration in minutes before a thread is automatically hidden from the channel list. Must be one of `60`, `1440`, `4320`, or `10080`.
- **type** (ChannelType) - Optional - The type of thread to create. Ignored if `message_id` is provided.
- **reason** (str) - Optional - The reason for creating a new thread. Shows up on the audit log.
- **invitable** (bool) - Optional - Whether non-moderators can add users to the thread. Only applicable to private threads.
- **slowmode_delay** (int) - Optional - Specifies the slowmode rate limit for user in this channel, in seconds. Maximum value is `21600`.

### Request Example
```json
{
  "name": "My New Thread",
  "auto_archive_duration": 1440,
  "reason": "Creating a thread for discussion"
}
```

### Response
#### Success Response (200)
- **thread** (Thread) - The created thread.

#### Response Example
```json
{
  "id": "123456789012345678",
  "name": "My New Thread",
  "type": 11
}
```

### Raises
- **Forbidden** – You do not have permissions to create a thread.
- **HTTPException** – Starting the thread failed.
```

--------------------------------

### POST /application_emoji

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Create an emoji for the current application.

```APIDOC
## POST /application_emoji

### Description
Create an emoji for the current application.

### Method
POST

### Parameters
#### Request Body
- **name** (str) - Required - The emoji name (2-32 characters).
- **image** (bytes) - Required - The bytes-like object representing the image data (JPG, PNG, or GIF).

### Response
#### Success Response (200)
- **Emoji** (object) - The emoji that was created.
```

--------------------------------

### Permissions and Flags

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Details on permission-related flags and general permissions.

```APIDOC
## Permissions and Flags

### Description
Information on permission-related flags and general permission methods.

### Items
- **discord.Permissions.general()**: A method related to general permissions (details not provided).
- **discord.ApplicationFlags.gateway_guild_members**: Enables the Gateway Guild Members intent.
- **discord.ApplicationFlags.gateway_guild_members_limited**: Enables a limited version of the Gateway Guild Members intent.
- **discord.ApplicationFlags.gateway_message_content**: Enables the Gateway Message Content intent.
- **discord.ApplicationFlags.gateway_message_content_limited**: Enables a limited version of the Gateway Message Content intent.
- **discord.ApplicationFlags.gateway_presence**: Enables the Gateway Presence intent.
- **discord.ApplicationFlags.gateway_presence_limited**: Enables a limited version of the Gateway Presence intent.
- **discord.MemberFlags.guest**: Indicates if a member is a guest.
```

--------------------------------

### Walk Commands

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

An iterator that recursively walks through all commands and subcommands.

```APIDOC
## GET /walk_commands

### Description
An iterator that recursively walks through all commands and subcommands. Duplicates due to aliases are no longer returned.

### Method
GET

### Endpoint
/walk_commands

### Parameters
None

### Response
#### Success Response (200)
- **commands** (list) - A list of `Command` or `Group` objects.

#### Response Example
```json
{
  "commands": [
    {
      "name": "command1",
      "type": "Command"
    },
    {
      "name": "subgroup",
      "type": "Group"
    }
  ]
}
```
```

--------------------------------

### discord.ui.Select Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents a UI select menu with a list of custom options, displayed as a dropdown to the user.

```APIDOC
## discord.ui.Select

### Description
Represents a UI select menu with a list of custom options. This is represented to the user as a dropdown menu.

### Parameters
- **custom_id** (str) - Optional - The ID of the select menu that gets received during an interaction.
- **placeholder** (str) - Optional - The placeholder text that is shown if nothing is selected.
- **min_values** (int) - Optional - The minimum number of items that must be chosen (0-25).
- **max_values** (int) - Optional - The maximum number of items that must be chosen (1-25).
- **options** (List[discord.SelectOption]) - Optional - A list of options that can be selected.
- **disabled** (bool) - Optional - Whether the select is disabled.
- **required** (bool) - Optional - Whether the select is required (only for modals).
- **row** (int) - Optional - The relative row this select menu belongs to (0-4).
- **id** (int) - Optional - The unique ID of the component.

### Methods
- **add_option(label, value=..., description=None, emoji=None, default=False)**: Adds an option to the select menu.
- **append_option(option)**: Appends a pre-existing discord.SelectOption to the menu.
- **callback(interaction)**: Coroutine. The callback associated with this UI item.
- **interaction_check(interaction)**: Coroutine. Checks whether the callback should be processed.
```

--------------------------------

### Webhook.from_url

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a partial Webhook object from a provided Discord webhook URL.

```APIDOC
## Webhook.from_url

### Description
Creates a partial Webhook object from a webhook URL.

### Parameters
#### Request Body
- **url** (str) - Required - The URL of the webhook.
- **session** (aiohttp.ClientSession) - Optional - The session to use for requests.
- **client** (Client) - Optional - The client to initialize this webhook with.
- **bot_token** (Optional[str]) - Optional - The bot authentication token for authenticated requests.

### Response
- **Webhook** (Object) - A partial Webhook instance.
```

--------------------------------

### Application Info API

Source: https://discordpy.readthedocs.io/en/latest/api.html

Provides information about the application.

```APIDOC
## Application Info API

### Description
Retrieves information related to the Discord application.

### Method
GET

### Endpoint
/oauth2/applications/@me (assumed)

### Parameters
None

### Response
#### Success Response (200)
- **id** (int) - The application ID.
- **name** (string) - The application name.
- **description** (string) - The application description.
- **rpc_origins** (array of strings) - List of RPC origins.

#### Response Example
```json
{
  "id": 1234567890,
  "name": "My Discord Bot",
  "description": "A bot that does cool things.",
  "rpc_origins": []
}
```
```

--------------------------------

### Invite Create Event

Source: https://discordpy.readthedocs.io/en/latest/api.html

Details about the event when an invite is created.

```APIDOC
## Invite Create Event

### Description

An invite was created.

### Method

Not Applicable (Event-driven)

### Endpoint

Not Applicable (Event-driven)

### Parameters

#### Target
- **target** (Invite) - The invite that was created.

#### Audit Log Diff Attributes
- **max_age** (integer) - The duration in seconds the invite is valid for.
- **code** (string) - The unique invite code.
- **temporary** (boolean) - Whether the invite grants temporary membership.
- **inviter** (User) - The user who created the invite.
- **channel** (Channel) - The channel the invite is for.
- **uses** (integer) - The current number of uses.
- **max_uses** (integer) - The maximum number of uses.
- **flags** (integer) - Invite flags.

### Request Example

```json
{
  "action": "invite_create",
  "target": {
    "code": "AbCdEf",
    "inviter": {
      "id": "123456789012345678",
      "username": "InviterUser",
      "discriminator": "1111"
    },
    "channel": {
      "id": "987654321098765432",
      "name": "general"
    },
    "max_age": 86400,
    "max_uses": 0
  }
}
```

### Response

This is an event, not an API call with a direct response. The data is provided within the event payload.
```

--------------------------------

### Thread Actions

Source: https://discordpy.readthedocs.io/en/latest/api.html

Documentation for thread creation, update, and deletion audit log actions.

```APIDOC
## Audit Log Actions: thread_create, thread_update, thread_delete

### Description
These actions represent the creation, update, or deletion of a thread.

### Target
- **target**: Thread or Object (ID of the thread)

### AuditLogDiff Attributes
- name
- archived
- locked
- auto_archive_duration
- invitable
```

--------------------------------

### Query Members by User IDs

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Fetch specific members from a guild by providing a list of their user IDs. This is more efficient than fetching all members.

```Python
members = await guild.query_members(user_ids=[1234567890, 9876543210])
```

--------------------------------

### Select Menu Properties

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Properties defining the behavior and state of select menu items.

```APIDOC
## Select Menu Properties

### Properties
- **min_values** (int) - The minimum number of items that must be chosen for this select menu.
- **max_values** (int) - The maximum number of items that can be chosen for this select menu.
- **parent** (Optional[Item]) - This item’s parent, if applicable. Only available on items with children. (New in version 2.6)
- **placeholder** (Optional[str]) - The placeholder text that is shown if nothing is selected, if any.
- **required** (bool) - Whether the select is required or not. Only supported in modals. (New in version 2.6)
- **view** (Optional[Union[View, LayoutView]]) - The underlying view for this item.
```

--------------------------------

### Define Command with Positional Arguments

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Create a command that accepts and sends two positional arguments. Users can pass arguments directly, or quote multi-word arguments.

```python
@bot.command()
async def test(ctx, arg1, arg2):
    await ctx.send(f'You passed {arg1} and {arg2}')
```

--------------------------------

### Guild Banner URL Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of Guild.banner_url with Guild.banner.

```python
Guild.banner
```

--------------------------------

### Fetch All Premium Sticker Packs

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves all available premium sticker packs.

```APIDOC
## GET /sticker-packs

### Description
Retrieves all available premium sticker packs.

### Method
GET

### Endpoint
/sticker-packs

### Raises
- **HTTPException** - Retrieving the sticker packs failed.

### Returns
- **List[StickerPack]** - All available premium sticker packs.
```

--------------------------------

### Commands and Command Invocation

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Information on command objects, their invocation, and related errors.

```APIDOC
## Commands and Command Invocation

### Description
This section details the `Command` object in discord.py, including how commands are invoked, associated errors, and how they relate to command trees and groups.

### Command Objects
- `discord.app_commands.Command`
- `commands.Command`

### Command Invocation and Errors
- `discord.app_commands.CommandInvokeError.command`
- `discord.app_commands.CommandSignatureMismatch.command`
- `discord.app_commands.GuildAppCommandPermissions.command`
- `discord.app_commands.Parameter.command`
- `commands.Context.command`
- `discord.Interaction.command`

### Command Registration
- `discord.app_commands.CommandTree.command()`
- `discord.app_commands.Group.command()`
- `commands.Bot.command()`
- `commands.Group.command()`
- `commands.GroupMixin.command()`
- `commands.HybridGroup.command()`
```

--------------------------------

### POST create_text_channel

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new text channel within the guild.

```APIDOC
## POST create_text_channel

### Description
Creates a TextChannel for the guild. Requires manage_channels permission.

### Parameters
#### Request Body
- **name** (str) - Required - The channel name.
- **reason** (Optional[str]) - Optional - Reason for audit log.
- **category** (Optional[CategoryChannel]) - Optional - Category to place channel under.
- **news** (bool) - Optional - Whether to create as a news channel.
- **position** (int) - Optional - Position in channel list.
- **topic** (str) - Optional - Channel topic.
- **slowmode_delay** (int) - Optional - Slowmode rate limit in seconds.
- **nsfw** (bool) - Optional - NSFW status.
- **overwrites** (Dict) - Optional - Permission overwrites.
- **default_auto_archive_duration** (int) - Optional - Default thread archive duration.
- **default_thread_slowmode_delay** (int) - Optional - Default thread slowmode delay.

### Response
#### Success Response (200)
- **channel** (TextChannel) - The created text channel object.
```

--------------------------------

### Error Handling and Copying

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Methods for checking if a command has an error handler and for creating a copy of a command group.

```APIDOC
## GET /commands/has_error_handler

### Description
Checks whether the command has an error handler registered.

### Method
GET

### Endpoint
/commands/has_error_handler

### Response
#### Success Response (200)
- **has_error_handler** (bool) - True if the command has an error handler, False otherwise.

## POST /commands/copy

### Description
Creates a copy of this `Group`.

### Method
POST

### Endpoint
/commands/copy

### Response
#### Success Response (200)
- **new_instance** (Group) - A new instance of this group.
```

--------------------------------

### Fetch Invite

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an Invite object from a Discord invite URL or code. If the invite is for a guild the user has not joined, guild and channel attributes will be partial.

```python
await _fetch_invite(_url_ , _*_ , _with_counts =True_, _with_expiration =True_, _scheduled_event_id =None_)
```

--------------------------------

### Save Asset to File

Source: https://discordpy.readthedocs.io/en/latest/api.html

Saves an asset to a file-like object or a specified filename. The `seek_begin` parameter controls whether to seek to the beginning of the file after saving. This method can raise `DiscordException`, `HTTPException`, or `NotFound`.

```python
await asset.save(fp, seek_begin=True)
```

--------------------------------

### Cooldown and Concurrency

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Configuration for command cooldowns and maximum concurrency.

```APIDOC
## Cooldown and Concurrency

### Description
Configuration for command cooldowns and concurrency.

### Classes
*   **discord.app_commands.Cooldown.per**: Specifies the period for a cooldown.
*   **commands.MaxConcurrencyReached.per**: Specifies the period for maximum concurrency.
```

--------------------------------

### AppCommandGroup Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents an application command subcommand, including its name, description, and options.

```APIDOC
## AppCommandGroup Class

### Description
Represents an application command subcommand.

### Attributes
- **name** (str) - The name of the subcommand.
- **description** (str) - The description of the subcommand.
- **name_localizations** (Dict[Locale, str]) - The localised names of the subcommand.
- **description_localizations** (Dict[Locale, str]) - The localised descriptions of the subcommand.
- **options** (List[Union[Argument, AppCommandGroup]]) - A list of options.
- **parent** (Union[AppCommand, AppCommandGroup]) - The parent application command.
- **qualified_name** (str) - The fully qualified command name.
- **mention** (str) - A string that allows you to mention the given AppCommandGroup.
- **type** (AppCommandOptionType) - The type of subcommand.
```

--------------------------------

### Client Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods for checking client status and handling errors.

```APIDOC
## Client Methods

### Description
Methods available on the client for checking its operational status and managing error handling.

### Methods
- **is_ws_ratelimited()** -> `bool`
  Returns `True` if the websocket is currently rate limited, `False` otherwise. Useful for deciding between HTTP and gateway queries for members.
  New in version 1.6.
- **is_ready()** -> `bool`
  Specifies if the client's internal cache is ready for use.
- **_on_error(_event_method_, _/_ , _*args_, _**kwargs_)** -> `coroutine`
  The default error handler provided by the client. By default, it logs errors to the library logger. This method can be overridden for custom error handling. See `on_error()` for more details.
```

--------------------------------

### discord.SelectMenu.placeholder

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

The placeholder text displayed on a select menu when no option is selected.

```APIDOC
## discord.SelectMenu.placeholder

### Description
The placeholder text for a select menu.

### Type
str | None
```

--------------------------------

### Context and Author

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Details on accessing author information within a command context.

```APIDOC
## commands.Context.author

### Description
Represents the author of the message that invoked the command.

### Endpoint
N/A (Attribute of an object)
```

--------------------------------

### GroupChannel Icon URL Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of GroupChannel.icon_url with GroupChannel.icon.

```python
GroupChannel.icon
```

--------------------------------

### Provide Autocomplete Choices

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Responds to an interaction by providing a list of choices for the user's autocomplete input. This is used in slash commands with autocomplete options.

```APIDOC
## POST /interactions/{interaction.id}/{interaction.token}/callback

### Description
Responds to this interaction by giving the user the choices they can use.

### Method
POST

### Endpoint
/interactions/{interaction.id}/{interaction.token}/callback

### Parameters
#### Request Body
- **choices** (List[Choice]) - The list of new choices as the user is typing.

### Raises
- **HTTPException** - Sending the choices failed.
- **ValueError** - This interaction cannot respond with autocomplete.
- **InteractionResponded** - This interaction has already been responded to before.
```

--------------------------------

### Define a basic hybrid command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Use the @bot.hybrid_command() decorator to create a command that can be invoked via text or slash interface.

```python
@bot.hybrid_command()
async def test(ctx):
    await ctx.send("This is a hybrid command!")
```

--------------------------------

### Member.create_dm

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a DMChannel with the user.

```APIDOC
## [COROUTINE] create_dm()

### Description
Creates a DMChannel with this user. This should be rarely called, as this is done transparently for most people.

### Returns
- **DMChannel** - The channel that was created.
```

--------------------------------

### Argument

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents an application command argument.

```APIDOC
## Argument

### Description
Represents an application command argument.
New in version 2.0.

### Attributes
- **type** (`AppCommandOptionType`) - The type of argument.
- **name** (`str`) - The name of the argument.
- **description** (`str`) - The description of the argument.
- **name_localizations** (Dict[`Locale`, `str`]) - The localised names of the argument. Used for display purposes.
- **description_localizations** (Dict[`Locale`, `str`]) - The localised descriptions of the argument. Used for display purposes.
- **required** (`bool`) - Whether the argument is required.
- **choices** (List[`Choice`]) - A list of choices for the command to choose from for this argument.
- **parent** (Union[`AppCommand`, `AppCommandGroup`]) - The parent application command that has this argument.
- **channel_types** (List[`ChannelType`]) - The channel types that are allowed for this parameter.
- **min_value** (Optional[Union[`int`, `float`]]) - The minimum supported value for this parameter.
- **max_value** (Optional[Union[`int`, `float`]]) - The maximum supported value for this parameter.
- **min_length** (Optional[`int`]) - The minimum allowed length for this parameter.
- **max_length** (Optional[`int`]) - The maximum allowed length for this parameter.
- **autocomplete** (`bool`) - Whether the argument has autocomplete.
```

--------------------------------

### User Equality and Hashing

Source: https://discordpy.readthedocs.io/en/latest/api.html

Details on how User objects are compared and hashed.

```APIDOC
## User Equality and Hashing

### Description
Defines how User objects are compared for equality and how their hash is computed.

### Operations
- **x == y**
  Checks if two users are equal (based on their IDs).

- **x != y**
  Checks if two users are not equal.

- **hash(x)**
  Returns the user's hash value.
```

--------------------------------

### discord.ext.tasks.Loop Decorators

Source: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

Lifecycle decorators for managing task execution flow.

```APIDOC
## @after_loop

### Description
A decorator that registers a coroutine to be called after the loop finishes running.

### Parameters
- **coro** (coroutine) - Required - The coroutine to register after the loop finishes.

### Raises
- **TypeError** - The function was not a coroutine.

## @before_loop

### Description
A decorator that registers a coroutine to be called before the loop starts running.

### Parameters
- **coro** (coroutine) - Required - The coroutine to register before the loop runs.

### Raises
- **TypeError** - The function was not a coroutine.

## @error

### Description
A decorator that registers a coroutine to be called if the task encounters an unhandled exception.

### Parameters
- **coro** (coroutine) - Required - The coroutine to register in the event of an unhandled exception.

### Raises
- **TypeError** - The function was not a coroutine.
```

--------------------------------

### POST /create_role

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new role for the guild with optional parameters for permissions, colors, and icons.

```APIDOC
## POST /create_role

### Description
Creates a new Role for the guild. Requires 'manage_roles' permission.

### Parameters
#### Request Body
- **name** (str) - Optional - The role name. Defaults to 'new role'.
- **permissions** (Permissions) - Optional - The permissions to have.
- **colour** (Union[Colour, int]) - Optional - The colour for the role.
- **secondary_colour** (Optional[Union[Colour, int]]) - Optional - The secondary colour for the role.
- **tertiary_colour** (Optional[Union[Colour, int]]) - Optional - The tertiary colour for the role.
- **hoist** (bool) - Optional - Indicates if the role should be shown separately.
- **display_icon** (Union[bytes, str]) - Optional - Icon bytes or unicode emoji string.
- **mentionable** (bool) - Optional - Indicates if the role is mentionable.
- **reason** (Optional[str]) - Optional - Reason for audit log.

### Response
#### Success Response (200)
- **role** (Role) - The newly created role.
```

--------------------------------

### Initiate Typing Indicator

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Initiates a typing indicator in the channel. This is a simpler way to show the bot is 'typing' without using the context manager.

```python
await channel.typing()
```

--------------------------------

### Send Typing Indicator in Channel

Source: https://discordpy.readthedocs.io/en/latest/api.html

Use the typing context manager to indicate activity in a channel. Requires async with for indefinite duration or await for a 10-second duration.

```python
async with channel.typing():
    # simulate something heavy
    await asyncio.sleep(20)

await channel.send('Done!')
```

```python
await channel.typing()
# Do some computational magic for about 10 seconds
await channel.send('Done!')
```

--------------------------------

### Ban command with Greedy and Optional

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Combines Greedy and Optional to handle multiple members and an optional delete_days parameter.

```python
import typing

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

### Applying multiple checks to a command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

When multiple checks are applied, all must return True for the command to execute.

```python
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

### Fetch Template

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves a Template object using a Discord Template Code or URL. The URL must be a discord.new URL.

```python
_await _fetch_template(_code_)
```

--------------------------------

### UserConverter Fetches API

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

In discord.ext.commands, UserConverter now fetches the API if a user ID is provided and the user is not already cached.

```python
# No specific code example provided, but describes UserConverter's enhanced behavior.
```

--------------------------------

### Discord.py Enumerations

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Reference documentation for core discord.py enumerations used in interactions and UI components.

```APIDOC
## Enumerations

### InteractionType
Specifies the type of Interaction (New in 2.0).
- ping: Discord pinging.
- application_command: Slash command.
- component: UI Kit component.
- autocomplete: Auto complete.
- modal_submit: Modal submission.

### InteractionResponseType
Specifies the response type for the interaction (New in 2.0).
- pong: Pong the interaction.
- channel_message: Respond with a message.
- deferred_channel_message: Respond with a message later.
- deferred_message_update: Acknowledge component interaction.
- message_update: Edit the message.
- autocomplete_result: Suggested choices.
- modal: Respond with a modal.

### ComponentType
Represents the component type (New in 2.0/2.6/2.7).
- action_row, button, text_input, select, string_select, user_select, role_select, mentionable_select, channel_select, section, text_display, thumbnail, media_gallery, file, separator, container, label, file_upload, radio_group, checkbox_group, checkbox.

### ButtonStyle
Represents the style of the button component (New in 2.0/2.4).
- primary (blurple), secondary (grey/gray), success (green), danger (red), link (url), premium.

### TextStyle
Represents the style of the text box component (New in 2.0).
- short, paragraph (long).

### AppCommandOptionType
Application command option type (New in 2.0).
- subcommand, subcommand_group, string, integer, boolean, user, channel, role, mentionable, number, attachment.

### AppCommandType
Type of application command (New in 2.0).
- chat_input, user, message.
```

--------------------------------

### HybridCommand Class Methods

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

API documentation for the HybridCommand class methods and decorators.

```APIDOC
## @after_invoke

### Description
A decorator that registers a coroutine as a post-invoke hook, called directly after the command is executed.

### Parameters
- **coro** (coroutine) - Required - The coroutine to register as the post-invoke hook.

### Errors
- **TypeError** - Raised if the provided object is not a coroutine.

---

## @autocomplete(name)

### Description
A decorator that registers a coroutine as an autocomplete prompt for a specific parameter in an application command.

### Parameters
- **name** (str) - Required - The parameter name to register as autocomplete.

### Errors
- **TypeError** - Raised if the coroutine is invalid or the parameter is not found.

---

## @before_invoke

### Description
A decorator that registers a coroutine as a pre-invoke hook, called directly before the command is executed.

### Parameters
- **coro** (coroutine) - Required - The coroutine to register as the pre-invoke hook.

### Errors
- **TypeError** - Raised if the provided object is not a coroutine.

---

## @error

### Description
A decorator that registers a coroutine as a local error handler for the command.

### Parameters
- **coro** (coroutine) - Required - The coroutine to register as the local error handler.

### Errors
- **TypeError** - Raised if the provided object is not a coroutine.

---

## await can_run(ctx)

### Description
Checks if the command can be executed by evaluating all predicates in the checks attribute and verifying if the command is disabled.

### Parameters
- **ctx** (Context) - Required - The context of the command currently being invoked.

### Response
- **bool** - Returns True if the command can be invoked, False otherwise.

### Errors
- **CommandError** - Propagates any error raised during check execution.
```

--------------------------------

### Webhook Support

Source: https://discordpy.readthedocs.io/en/latest/api.html

Overview of the Webhook class capabilities in discord.py for managing and executing webhooks.

```APIDOC
## Webhook Support

### Description
discord.py offers support for creating, editing, and executing webhooks through the `Webhook` class.
```

--------------------------------

### discord.ui.MediaGallery

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents a UI media gallery. Can contain up to 10 `MediaGalleryItem`s. This is a top-level layout component that can only be used on `LayoutView`.

```APIDOC
## discord.ui.MediaGallery

### Description
Represents a UI media gallery. Can contain up to 10 `MediaGalleryItem`s. This is a top-level layout component that can only be used on `LayoutView`.

### Attributes
- `id` (Optional[int]): The ID of this component. This must be unique across the view.
- `items` (List[MediaGalleryItem]): Returns a read-only list of this gallery’s items.
- `parent` (Optional[Item]): This item’s parent, if applicable. Only available on items with children.
- `view` (Optional[Union[View, LayoutView]]): The underlying view for this item.

### Methods
- `add_item(media, description=None, spoiler=False)`: Adds an item to this gallery.
- `append_item(item)`: Appends an item to this gallery.
- `clear_items()`: Removes all items from the gallery.
- `insert_item_at(index, media, description=None, spoiler=False)`: Inserts an item before a specified index to the media gallery.
- `remove_item(item)`: Removes an item from the gallery.

### Parameters
- `items` (MediaGalleryItem): The initial items of this gallery.
- `id` (Optional[int]): The ID of this component. This must be unique across the view.

### Parameters for `add_item` and `insert_item_at`
- `media` (Union[str, discord.File, UnfurledMediaItem]): The media item data. This can be a string representing a local file uploaded as an attachment in the message, which can be accessed using the `attachment://<filename>` format, or an arbitrary url.
- `description` (Optional[str]): The description to show within this item. Up to 256 characters. Defaults to `None`.
- `spoiler` (bool): Whether this item should be flagged as a spoiler. Defaults to `False`.

### Parameters for `append_item`
- `item` (MediaGalleryItem): The item to add to the gallery.

### Parameters for `remove_item`
- `item` (MediaGalleryItem): The item to remove from the gallery.

### Raises
- `ValueError`: Maximum number of items has been exceeded (10).
- `TypeError`: A `MediaGalleryItem` was not passed (for `append_item`).
```

--------------------------------

### commands.parameter() decorator

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

A decorator to assign custom metadata for a Command's parameter.

```APIDOC
## Function discord.ext.commands.parameter

### Description
A way to assign custom metadata for a `Command`'s parameter.

### Parameters
- **converter** (Any) - The converter to use for this parameter.
- **default** (Any) - The default value for the parameter. If callable or coroutine, it's called with a `Context` argument.
- **description** (str) - The description of this parameter.
- **displayed_default** (str) - The displayed default in `Command.signature`.
- **displayed_name** (str) - The name that is displayed to the user.

### Example
```python
@bot.command()
async def wave(ctx, to: discord.User = commands.parameter(default=lambda ctx: ctx.author)):
    await ctx.send(f'Hello {to.mention} :wave:')
```
```

--------------------------------

### Client, Connection, and Status

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Information about the Discord client, connection status, and user client status.

```APIDOC
## Client, Connection, and Status

### Description
This section covers core client-related classes and attributes, including the main client object, connection status, and user presence information.

### Client Objects
- `discord.Client`
- `discord.Interaction.client`
- `discord.ClientException`
- `discord.ClientUser`

### Client Status
- `discord.Member.client_status`
- `discord.RawPresenceUpdateEvent.client_status`
- `discord.ClientStatus`
```

--------------------------------

### VoiceChannel Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

This section details the methods available for the VoiceChannel object, including editing, connecting, and managing channel properties.

```APIDOC
## VoiceChannel Methods

### Edit Channel

#### Description
Edits the voice channel's properties. You must have `manage_channels` permissions to perform this action.

#### Method
`async` `edit`

#### Parameters
- **name** (str) - The new channel name.
- **bitrate** (int) - The new channel's bitrate.
- **nsfw** (bool) - To mark the channel as NSFW or not.
- **user_limit** (int) - The new channel's user limit.
- **position** (int) - The new channel's position.
- **sync_permissions** (bool) - Whether to sync permissions with the channel's new or pre-existing category. Defaults to `False`.
- **category** (Optional[CategoryChannel]) - The new category for this channel. Can be `None` to remove the category.
- **slowmode_delay** (int) - Specifies the slowmode rate limit for users in this channel, in seconds. A value of `0` disables slowmode. The maximum value is `21600`.
- **reason** (Optional[str]) - The reason for editing this channel. Shows up on the audit log.
- **overwrites** (Mapping) - A `Mapping` of target (either a role or a member) to `PermissionOverwrite` to apply to the channel.
- **rtc_region** (Optional[str]) - The new region for the voice channel's voice communication. A value of `None` indicates automatic voice region detection.
- **video_quality_mode** (VideoQualityMode) - The camera video quality for the voice channel's participants.
- **status** (Optional[str]) - The new voice channel status. It can be up to 500 characters. Can be `None` to remove the status.

#### Raises
- **TypeError** - If the permission overwrite information is not in proper form.
- **Forbidden** - You do not have permissions to edit the channel.
- **HTTPException** - Editing the channel failed.

#### Returns
- The newly edited voice channel. If the edit was only positional then `None` is returned instead.

### Other Methods
- **async clone()**: Clones the voice channel.
- **async connect()**: Connects to the voice channel.
- **async create_invite()**: Creates an invite to the voice channel.
- **async create_webhook()**: Creates a webhook for the voice channel.
- **async delete()**: Deletes the voice channel.
- **async delete_messages()**: Deletes messages from the voice channel.
- **async fetch_message(id)**: Fetches a message from the voice channel by its ID.
- **def get_partial_message(id)**: Gets a partial message object from the voice channel by its ID.
- **async history(**
  `limit=None`,
  `before=None`,
  `after=None`,
  `around=None`
**)**: Returns the message history for the voice channel.
- **async invites()**: Returns a list of all invites to the voice channel.
- **def is_nsfw()**: Returns `True` if the channel is NSFW, `False` otherwise.
- **async move(members, *, channel=None, flush=None, reason=None)**: Moves voice channel members to a different channel.
- **def overwrites_for(object)**: Returns the permission overwrites for a given object (member or role).
- **def permissions_for(object)**: Returns the calculated permissions for a given object (member or role).
- **def pins()**: Returns a list of all messages pinned to the voice channel.
- **async purge(limit=100, *, check=None, before=None, after=None)**: Bulk deletes messages from the voice channel.
- **async send(content, *, tts=False, embed=None, files=None, delete_after=None, nonce=None, **kwargs)**: Sends a message to the voice channel.
- **async send_sound(path)**: Sends an audio file to the voice channel.
- **async set_permissions(role_or_member, **perms)**: Sets the permissions for a given role or member.
- **def typing()**: Returns an async iterator that yields context managers.
- **async webhooks()**: Returns a list of all webhooks for the voice channel.
```

--------------------------------

### Command Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents an application command. These are typically created using decorators like `command()`.

```APIDOC
## Class discord.app_commands.Command

Implements an application command.

### Parameters

* **name** (Union[`str`, `locale_str`]) - The name of the application command.
* **description** (Union[`str`, `locale_str`]) - The description of the application command. This shows up in the UI to describe the application command.
* **callback** (coroutine) - The coroutine that is executed when the command is called.
* **auto_locale_strings** (`bool`) - If this is set to `True`, then all translatable strings will implicitly be wrapped into `locale_str` rather than `str`. Defaults to `True`.
* **nsfw** (`bool`) - Whether the command is NSFW and should only work in NSFW channels. Defaults to `False`. Due to a Discord limitation, this does not work on subcommands.
* **parent** (Optional[`Group`]) - The parent application command. `None` if there isn’t one.
* **guild_ids** (Optional[List[`int`]]) - A list of guild IDs where this command should be registered. If `None`, the command is global.
* **allowed_contexts** (Optional[`AppCommandContext`]) - The contexts that the command is allowed to be used in. Overrides `guild_only` if this is set. New in version 2.4.
* **allowed_installs** (Optional[`AppInstallationType`]) - The installation contexts that the command is allowed to be installed on. New in version 2.4.
* **extras** (`dict`) - A dictionary that can be used to store extraneous data.

### Attributes

* **allowed_contexts**
* **allowed_installs**
* **callback**
* **checks**
* **default_permissions**
* **description**
* **extras**
* **guild_only**
* **name**
* **nsfw**
* **parameters**
* **parent**
* **qualified_name**
* **root_parent**

### Methods

* **add_check**(_check_)
* **autocomplete**(_name_)
* **error**(_coro_)
* **get_parameter**(_name_)
* **remove_check**(_check_)
```

--------------------------------

### StickerItem.fetch

Source: https://discordpy.readthedocs.io/en/latest/api.html

Attempts to retrieve the full sticker data of the sticker item.

```APIDOC
## async StickerItem.fetch

### Description
Attempts to retrieve the full sticker data of the sticker item.

### Response
#### Success Response (200)
- **Sticker** (Union[StandardSticker, GuildSticker]) - The retrieved sticker.

#### Error Handling
- **HTTPException** - Raised if retrieving the sticker failed.
```

--------------------------------

### Widget.fetch_invite

Source: https://discordpy.readthedocs.io/en/latest/api.html

Retrieves an Invite object from the widget's invite URL.

```APIDOC
## async Widget.fetch_invite

### Description
Retrieves an Invite from the widget’s invite URL. This is the same as Client.fetch_invite(); the invite code is abstracted away.

### Parameters
#### Query Parameters
- **with_counts** (bool) - Optional - Whether to include count information in the invite. Defaults to True.

### Response
#### Success Response (200)
- **Invite** (Optional[Invite]) - The invite from the widget’s invite URL, if available.
```

--------------------------------

### Create Test Entitlement

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Creates a test entitlement for an application's SKU. This is useful for testing purposes. Ensure the SKU and owner exist and the owner type is correct. Requires the application ID.

```python
await client._create_entitlement(sku, owner, owner_type)
```

--------------------------------

### POST /create_stage_channel

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new StageChannel in the guild.

```APIDOC
## POST /create_stage_channel

### Description
Creates a new StageChannel. This is a coroutine.

### Method
POST

### Parameters
#### Request Body
- **name** (str) - Required - The channel's name.
- **overwrites** (Dict) - Optional - A dict of target to PermissionOverwrite.
- **category** (CategoryChannel) - Optional - The category to place the channel under.
- **position** (int) - Optional - The position in the channel list.
- **bitrate** (int) - Optional - Preferred audio bitrate.
- **user_limit** (int) - Optional - Member limit for the channel.
- **rtc_region** (str) - Optional - Voice region for communication.
- **video_quality_mode** (VideoQualityMode) - Optional - Camera video quality.
- **nsfw** (bool) - Optional - NSFW status.
- **reason** (str) - Optional - Reason for audit log.

### Response
#### Success Response (200)
- **channel** (StageChannel) - The channel that was just created.
```

--------------------------------

### View Interaction Methods

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Methods for managing the lifecycle and traversal of UI views.

```APIDOC
## await wait()

### Description
Waits until the view has finished interacting. A view is considered finished when stop() is called or it times out.

### Response
- **bool** - Returns True if the view timed out, False if it finished normally.

## for ... in walk_children()

### Description
An iterator that recursively walks through all the children of this view and its children, if applicable.

### Yields
- **Item** - An item in the view.
```

--------------------------------

### Send Message with Reference

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

The abc.Messageable.send() method can now accept a MessageReference object, allowing for more complex message interactions, such as replies.

```python
await channel.send(reference=message_reference, content='Another message with a reference.')
```

--------------------------------

### Create a Discord UI Modal

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Inherit from discord.ui.Modal to create a custom modal. Define input fields using ui.Label and ui.TextInput. The on_submit method handles the user's input.

```python
import discord
from discord import ui

class Questionnaire(ui.Modal, title='Questionnaire Response'):
    name = ui.Label(text='Name', component=ui.TextInput())
    answer = ui.Label(text='Answer', component=ui.TextInput(style=discord.TextStyle.paragraph))

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {self.name.component.value}!', ephemeral=True)
```

--------------------------------

### ForumChannel Equality and Hashing

Source: https://discordpy.readthedocs.io/en/latest/api.html

Checks for equality and calculates the hash for ForumChannel objects.

```APIDOC
## ForumChannel Equality and Hashing

### Description
Checks for equality and calculates the hash for ForumChannel objects.

### Operations
- **x == y**: Checks if two forums are equal.
- **x != y**: Checks if two forums are not equal.
- **hash(x)**: Returns the forum’s hash.
```

--------------------------------

### Registering an Event Listener

Source: https://discordpy.readthedocs.io/en/latest/api.html

Use the `@client.event` decorator to register asynchronous functions as event listeners. The decorated function must be a coroutine. This is essential for handling events like `on_ready`.

```python
@client.event
async def on_ready():
    print('Ready!')
```

--------------------------------

### CategoryChannel Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Details the methods available for interacting with a CategoryChannel object.

```APIDOC
## CategoryChannel Methods

### clone()

- **Description**: Clones this channel. Creates a new channel with the same properties. Requires `manage_channels` permission.
- **Method**: `async clone()`
- **Parameters**:
  - **name** (`str`, Optional): The name for the new channel. Defaults to the current channel name.
  - **category** (`CategoryChannel`, Optional): The category for the new channel. Ignored if cloning a category channel.
  - **reason** (`str`, Optional): The reason for cloning, shown in the audit log.
- **Raises**:
  - `Forbidden`: If the user lacks `manage_channels` permission.
  - `HTTPException`: If the channel creation fails.
- **Returns**: The newly created channel.

### create_forum()

- **Description**: Creates a new forum channel within this category. Requires `manage_channels` permission.
- **Method**: `async create_forum()`
- **Parameters**: (Refer to `discord.abc.GuildChannel.create_forum` for detailed parameters)
- **Returns**: The created `ForumChannel`.

### create_invite()

- **Description**: Creates an invite to this channel. Requires `create_instant_invite` permission.
- **Method**: `async create_invite()`
- **Parameters**: (Refer to `discord.abc.GuildChannel.create_invite` for detailed parameters)
- **Returns**: The created `Invite`.

### create_stage_channel()

- **Description**: Creates a new stage channel within this category. Requires `manage_channels` permission.
- **Method**: `async create_stage_channel()`
- **Parameters**: (Refer to `discord.abc.GuildChannel.create_stage_channel` for detailed parameters)
- **Returns**: The created `StageChannel`.

### create_text_channel()

- **Description**: Creates a new text channel within this category. Requires `manage_channels` permission.
- **Method**: `async create_text_channel()`
- **Parameters**: (Refer to `discord.abc.GuildChannel.create_text_channel` for detailed parameters)
- **Returns**: The created `TextChannel`.

### create_voice_channel()

- **Description**: Creates a new voice channel within this category. Requires `manage_channels` permission.
- **Method**: `async create_voice_channel()`
- **Parameters**: (Refer to `discord.abc.GuildChannel.create_voice_channel` for detailed parameters)
- **Returns**: The created `VoiceChannel`.

### delete()

- **Description**: Deletes the category. Requires `manage_channels` permission.
- **Method**: `async delete()`
- **Parameters**: None.
- **Raises**:
  - `Forbidden`: If the user lacks `manage_channels` permission.
  - `HTTPException`: If the category deletion fails.

### edit()

- **Description**: Edits the category. Requires `manage_channels` permission. Returns the edited category.
- **Method**: `async edit()`
- **Parameters**:
  - **name** (`str`): The new name for the category.
  - **position** (`int`): The new position for the category.
  - **nsfw** (`bool`): Whether to mark the category as NSFW.
  - **reason** (`str`, Optional): The reason for the edit, shown in the audit log.
  - **overwrites** (`Mapping`): A mapping of targets (roles or members) to `PermissionOverwrite` objects.
- **Raises**:
  - `ValueError`: If position is invalid.
  - `TypeError`: If overwrite information is malformed.
  - `Forbidden`: If the user lacks `manage_channels` permission.
  - `HTTPException`: If the category edit fails.
- **Returns**: The edited `CategoryChannel` or `None` if only position was edited.

### invites()

- **Description**: Returns a list of invites for this channel.
- **Method**: `async invites()`
- **Parameters**: None.
- **Returns**: A list of `Invite` objects.

### is_nsfw()

- **Description**: Checks if the category is NSFW.
- **Method**: `def is_nsfw()`
- **Returns**: `bool`: True if the category is NSFW, False otherwise.

### move()

- **Description**: Moves the channel relative to other channels. Requires `manage_channels` permission.
- **Method**: `async move()`
- **Parameters**:
  - **beginning** (`bool`): Move to the beginning of the list.
  - **end** (`bool`): Move to the end of the list.
  - **before** (`Snowflake`): Move before the specified channel.
  - **after** (`Snowflake`): Move after the specified channel.
- **Raises**:
  - `TypeError` or `ValueError`: If parameters are invalid or conflicting.
  - `Forbidden`: If the user lacks `manage_channels` permission.
  - `HTTPException`: If the move operation fails.

### set_permissions()

- **Description**: Sets the permission overwrites for a target (role or member) in this category. Requires `manage_channels` permission.
- **Method**: `async set_permissions()`
- **Parameters**: (Refer to `discord.abc.GuildChannel.set_permissions` for detailed parameters)
- **Raises**:
  - `Forbidden`: If the user lacks `manage_channels` permission.
  - `HTTPException`: If setting permissions fails.
```

--------------------------------

### User Input and Lookup Exceptions

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Exceptions related to invalid user input or failure to locate resources.

```APIDOC
## UserInputError
### Description
The base exception type for errors that involve errors regarding user input.

## TooManyArguments
### Description
Exception raised when the command was passed too many arguments and its Command.ignore_extra attribute was not set to True.

## MessageNotFound
### Description
Exception raised when the message provided was not found in the channel.
- **argument** (str) - The message supplied by the caller that was not found.

## MemberNotFound
### Description
Exception raised when the member provided was not found in the bot’s cache.
- **argument** (str) - The member supplied by the caller that was not found.

## GuildNotFound
### Description
Exception raised when the guild provided was not found in the bot’s cache.
- **argument** (str) - The guild supplied by the called that was not found.

## UserNotFound
### Description
Exception raised when the user provided was not found in the bot’s cache.
- **argument** (str) - The user supplied by the caller that was not found.

## ChannelNotFound
### Description
Exception raised when the bot can not find the channel.
- **argument** (Union[int, str]) - The channel supplied by the caller that was not found.

## ChannelNotReadable
### Description
Exception raised when the bot does not have permission to read messages in the channel.
- **argument** (Union[abc.GuildChannel, Thread]) - The channel supplied by the caller that was not readable.

## ThreadNotFound
### Description
Exception raised when the bot can not find the thread.
- **argument** (str) - The thread supplied by the caller that was not found.

## BadColourArgument
### Description
Exception raised when the colour is not valid.
- **argument** (str) - The colour supplied by the caller that was not valid.

## RoleNotFound
### Description
Exception raised when the bot can not find the role.
- **argument** (str) - The role supplied by the caller that was not found.

## BadInviteArgument
### Description
Exception raised when the invite is invalid or expired.
```

--------------------------------

### Define a Simple Command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Use the @bot.command() decorator to define a command that echoes a single argument. Ensure the message_content intent is enabled.

```python
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)
```

--------------------------------

### coroutine Command.can_run(ctx)

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Checks if the command can be executed by evaluating all predicates and the disabled status.

```APIDOC
## coroutine Command.can_run(ctx)

### Description
Checks if the command can be executed by checking all the predicates inside the `checks` attribute. This also checks whether the command is disabled.

### Parameters
#### Path Parameters
- **ctx** (Context) - Required - The ctx of the command currently being invoked.

### Returns
- **bool** - A boolean indicating if the command can be invoked.

### Raises
- **CommandError** - Any command error that was raised during a check call will be propagated by this function.
```

--------------------------------

### discord.ext.commands.Group Class

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Overview of the Group class and its primary configuration attributes.

```APIDOC
## Group Class

### Description
A class that implements a grouping protocol for commands to be executed as subcommands. It is a subclass of `Command`.

### Attributes
- **invoke_without_command** (bool) - Indicates if the group callback should begin parsing only if no subcommand was found. Defaults to False.
- **case_insensitive** (bool) - Indicates if the group's commands should be case insensitive. Defaults to False.
```

--------------------------------

### discord.utils.get

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns the first element in an iterable that matches all provided attributes.

```APIDOC
## discord.utils.get

### Description
A helper that returns the first element in the iterable that meets all the traits passed in attrs. Attributes are checked using logical AND.

### Parameters
- **iterable** (Union[collections.abc.Iterable, collections.abc.AsyncIterable]) - Required - The iterable to search through.
- **attrs** (dict) - Optional - Keyword arguments that denote attributes to search with.
```

--------------------------------

### Color and Style Enums

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Enumerations for colors and button styles.

```APIDOC
## Color and Style Enums

### Description
Enumerations for defining colors and button styles.

### Enums
- **discord.Colour.g**: Represents the color green.
- **discord.Colour.gold()**: Returns a gold color.
- **discord.Colour.green()**: Returns a green color.
- **discord.Colour.greyple()**: Returns a greyple color.
- **discord.ButtonStyle.gray**: Represents a gray button style.
- **discord.ButtonStyle.green**: Represents a green button style.
- **discord.ButtonStyle.grey**: Represents a grey button style.
- **discord.DefaultAvatar.gray**: Represents the default gray avatar.
- **discord.DefaultAvatar.green**: Represents the default green avatar.
- **discord.DefaultAvatar.grey**: Represents the default grey avatar.
```

--------------------------------

### Discord UI Kit Components

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Overview of internal component classes representing UI elements in the Discord Bot UI Kit.

```APIDOC
## LabelComponent

### Description
Represents a label component from the Discord Bot UI Kit.

### Attributes
- **label** (str) - The label text to display.
- **description** (Optional[str]) - The description text to display below the label.
- **component** (Component) - The component that this label is associated with.
- **id** (Optional[int]) - The ID of this component.
- **type** (ComponentType) - The type of component.

## SectionComponent

### Description
Represents a section from the Discord Bot UI Kit.

### Attributes
- **children** (List[TextDisplay]) - The components on this section.
- **accessory** (Component) - The section accessory.
- **id** (Optional[int]) - The ID of this component.
- **type** (ComponentType) - The type of component.

## ThumbnailComponent

### Description
Represents a Thumbnail from the Discord Bot UI Kit.

### Attributes
- **media** (UnfurledMediaItem) - The media for this thumbnail.
- **description** (Optional[str]) - The description shown within this thumbnail.
- **spoiler** (bool) - Whether this thumbnail is flagged as a spoiler.
- **id** (Optional[int]) - The ID of this component.
- **type** (ComponentType) - The type of component.

## TextDisplay

### Description
Represents a text display from the Discord Bot UI Kit.

### Attributes
- **content** (str) - The content that this display shows.
- **id** (Optional[int]) - The ID of this component.
- **type** (ComponentType) - The type of component.

## MediaGalleryComponent

### Description
Represents a Media Gallery component from the Discord Bot UI Kit.

### Attributes
- **items** (List[MediaGalleryItem]) - The items this gallery has.
- **id** (Optional[int]) - The ID of this component.
- **type** (ComponentType) - The type of component.

## FileComponent

### Description
Represents a File component from the Discord Bot UI Kit.

### Attributes
- **media** (UnfurledMediaItem) - The unfurled attachment contents of the file.
- **spoiler** (bool) - Whether this file is flagged as a spoiler.
- **id** (Optional[int]) - The ID of this component.
- **name** (Optional[str]) - The displayed file name.
- **size** (Optional[int]) - The file size in MiB.
- **type** (ComponentType) - The type of component.

## SeparatorComponent

### Description
Represents a Separator from the Discord Bot UI Kit.

### Attributes
- **spacing** (SeparatorSpacing) - The spacing size of the separator.
- **visible** (bool) - Whether this separator is visible.
- **id** (Optional[int]) - The ID of this component.
- **type** (ComponentType) - The type of component.
```

--------------------------------

### SoundboardDefaultSound

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents a default soundboard sound provided by Discord.

```APIDOC
## SoundboardDefaultSound

### Description
Represents a Discord soundboard default sound.
New in version 2.5.

### Attributes
- **emoji** (`PartialEmoji`) - The emoji of the sound.
- **id** (`int`) - The ID of the sound.
- **name** (`str`) - The name of the sound.
- **volume** (`float`) - The volume of the sound as floating point percentage (e.g. `1.0` for 100%).

### Methods
- **hash(x)** - Returns the sound’s hash.
- **x == y** - Checks if two sounds are equal.
- **x != y** - Checks if two sounds are not equal.
```

--------------------------------

### discord.utils.find

Source: https://discordpy.readthedocs.io/en/latest/api.html

Returns the first element in a sequence that meets a predicate.

```APIDOC
## discord.utils.find

### Description
A helper to return the first element found in the sequence that meets the predicate. If an entry is not found, then None is returned.

### Parameters
- **predicate** (Callable) - Required - A function that returns a boolean-like result.
- **iterable** (Union[collections.abc.Iterable, collections.abc.AsyncIterable]) - Required - The iterable to search through.
```

--------------------------------

### Registering a Command with @command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Use the @command decorator to convert a method into a command and automatically add it to the bot's command list. This is a shortcut for manually calling command() and add_command().

```python
@command()
def example(ctx):
    pass
```

--------------------------------

### @app_commands.choices

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Defines a set of choices for a command parameter, allowing users to select from a predefined list.

```APIDOC
## @app_commands.choices

### Description
Limits the input of a command parameter to a specific set of choices defined by the developer.

### Parameters
#### Parameters
- **fruits** (Choice[int]) - Required - The choices of the parameters.

### Request Example
@app_commands.choices(fruits=[Choice(name='apple', value=1), Choice(name='banana', value=2)])
async def fruit(interaction: discord.Interaction, fruits: Choice[int]):
    ...
```

--------------------------------

### Create a Hybrid Command with @hybrid_command

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

A shortcut decorator that invokes hybrid_command() and adds it to the internal command list via add_command(). It converts the provided method into a Command, adds it to the bot, and returns it.

```python
@hybrid_command(_name =..._, _with_app_command =True_, _* args_, _** kwargs_)

```

--------------------------------

### Implement a static command cooldown

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Applies a fixed cooldown of one use per 5 seconds per member using a lambda key function.

```python
@tree.command()
@app_commands.checks.cooldown(1, 5.0, key=lambda i: (i.guild_id, i.user.id))
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('Hello')

@test.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(str(error), ephemeral=True)
```

--------------------------------

### Webhook Utility Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Provides utility methods for webhook objects.

```APIDOC
## Webhook Utility Methods

### Description
Provides utility methods for webhook objects.

### Methods
- **is_authenticated()** (`bool`) - Returns `True` if the webhook is authenticated with a bot token, `False` otherwise. New in version 2.0.
- **is_partial()** (`bool`) - Returns `True` if the webhook is a partial webhook, `False` otherwise. New in version 2.0.
```

--------------------------------

### Define an application command group

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Subclass discord.app_commands.Group to create a command group, applying decorators to set constraints like guild-only access.

```python
from discord import app_commands

@app_commands.guild_only()
class MyGroup(app_commands.Group):
    pass
```

--------------------------------

### Role Comparison and Operations

Source: https://discordpy.readthedocs.io/en/latest/api.html

Details on how Role objects can be compared and used in operations.

```APIDOC
## Role Comparison and Operations

### Description
Defines how Role objects can be compared with each other and used in standard Python operations.

### Operators
- **==**: Checks if two roles are equal.
- **!=**: Checks if two roles are not equal.
- **>**: Checks if a role is higher than another in the hierarchy.
- **<**: Checks if a role is lower than another in the hierarchy.
- **>=**: Checks if a role is higher than or equal to another in the hierarchy.
- **<=**: Checks if a role is lower than or equal to another in the hierarchy.

### Built-in Functions
- **hash(role)**: Returns the role's hash.
- **str(role)**: Returns the role's name.
```

--------------------------------

### Fetch Guild Template

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Fetch information about a guild template using its code. This requires appropriate permissions and is currently restricted for bot accounts.

```Python
template = await client.fetch_template('template_code')
```

--------------------------------

### Command Registration and Hybrid Command Errors

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Exceptions related to command registration conflicts and errors during hybrid command execution.

```APIDOC
## discord.ext.commands.CommandRegistrationError(_name_ , _*_, _alias_conflict =False_)

### Description
An exception raised when the command can’t be added because the name is already taken by a different command.
This inherits from `discord.ClientException`.
New in version 1.4.

### Parameters
#### Attributes
- **name** (str) - The command name that had the error.
- **alias_conflict** (bool) - Whether the name that conflicts is an alias of the command we try to add.

## discord.ext.commands.HybridCommandError(_original_)

### Description
An exception raised when a `HybridCommand` raises an `AppCommandError` derived exception that could not be sufficiently converted to an equivalent `CommandError` exception.
New in version 2.0.

### Parameters
#### Attributes
- **original** (AppCommandError) - The original exception that was raised. You can also get this via the `__cause__` attribute.
```

--------------------------------

### Define Command with Keyword-Only Argument (*)

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Use a keyword-only argument (*) to capture all remaining input as a single string, simplifying the handling of multi-word arguments without requiring quotes. Only one keyword-only argument is permitted.

```python
@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)
```

--------------------------------

### Manage Event Loop Manually

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_async.html

Use this pattern to maintain control over the event loop instead of using the blocking client.run method.

```python
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

### Component Types and Components

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Details on different component types like checkboxes and their associated classes.

```APIDOC
## Component Types and Components

### Description
This section covers various component types available in discord.py, such as checkboxes, and their corresponding classes for UI elements.

### Component Types
- `discord.ComponentType.checkbox`
- `discord.ComponentType.checkbox_group`

### Components
- `discord.CheckboxComponent`
- `discord.ui.CheckboxGroup`
- `discord.CheckboxGroupComponent`
- `discord.CheckboxGroupOption`
```

--------------------------------

### Embed Class Initialization

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents a Discord embed. For ease of use, all parameters that expect a `str` are implicitly casted to `str` for you. `Embed.Empty` has been removed in favour of `None`.

```APIDOC
## Embed Class

### Description
Represents a Discord embed. Useful for creating rich messages.

### Parameters
- **colour** (Optional[Union[Colour, int]]) - The colour code of the embed. Aliased to `color` as well.
- **color** (Optional[Union[Colour, int]]) - Alias for `colour`.
- **title** (Optional[str]) - The title of the embed. Can only be up to 256 characters.
- **type** (str) - The type of embed. Usually "rich". Possible strings can be found on discord’s api docs.
- **url** (Optional[str]) - The URL of the embed.
- **description** (Optional[str]) - The description of the embed. Can only be up to 4096 characters.
- **timestamp** (Optional[datetime.datetime]) - The timestamp of the embed content. If a naive datetime is passed, it is converted to an aware datetime with the local timezone.

### Request Example
```python
import discord

embed = discord.Embed(
    title="My Embed Title",
    description="This is the embed description.",
    color=discord.Color.blue()
)
```
```

--------------------------------

### User Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods available on the User object for performing actions or retrieving related information.

```APIDOC
## User Methods

### Description
Provides functionality to interact with or get more information about a Discord user.

### Methods
- **asynccreate_dm()**
  Asynchronously creates a direct message channel with the user.

- **asyncfetch_message(id: int)**
  Asynchronously fetches a message from a shared channel with the user.

- **async forhistory(limit: int, before: Snowflake, after: Snowflake, around: Snowflake)**
  Asynchronously retrieves message history from a shared channel with the user.

- **mentioned_in(message: Message)**
  Checks if the user is mentioned in the specified message.
  - **Parameters**:
    - **message** (Message) - The message to check.
  - **Returns**:
    - bool - True if the user is mentioned, False otherwise.

- **pins()**
  Returns a list of pinned messages in a shared channel with the user.

- **async send(content: Optional[str], *, tts: bool, embed: Optional[Embed], file: Optional[File], files: Optional[List[File]], nonce: Optional[str], delete_after: float, group: Optional[str], reference: Optional[MessageReference], mention_author: bool)**
  Asynchronously sends a message to the user.

- **async typing()**
  Returns an asynchronous context manager that sends a typing indicator.
```

--------------------------------

### load_extension

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Loads a Python module extension containing commands, cogs, or listeners.

```APIDOC
## load_extension(name, *, package=None)

### Description
Loads an extension. An extension is a python module that contains commands, cogs, or listeners. This function is a coroutine.

### Parameters
#### Arguments
- **name** (str) - Required - The extension name to load (dot separated).
- **package** (str) - Optional - The package name to resolve relative imports with.

### Errors
- **ExtensionNotFound**: Extension could not be imported.
- **ExtensionAlreadyLoaded**: Extension is already loaded.
- **NoEntryPointError**: Extension lacks a setup function.
- **ExtensionFailed**: Execution error in setup function.
```

--------------------------------

### Awaiting Coroutines

Source: https://discordpy.readthedocs.io/en/latest/migrating_to_async.html

Client functions are now coroutines and must be awaited or yielded from.

```python
client.send_message(message.channel, 'Hello')
```

```python
yield from client.send_message(message.channel, 'Hello')

# or in python 3.5+
await client.send_message(message.channel, 'Hello')
```

--------------------------------

### POST /send

Source: https://discordpy.readthedocs.io/en/latest/api.html

Sends a new message to the channel with optional content, embeds, files, and other configurations.

```APIDOC
## POST /send

### Description
Sends a message to the destination. If content is None, an embed must be provided.

### Method
POST

### Parameters
#### Request Body
- **content** (str) - Optional - The content of the message.
- **tts** (bool) - Optional - Whether to use text-to-speech.
- **embed** (Embed) - Optional - A single rich embed.
- **embeds** (List[Embed]) - Optional - A list of up to 10 embeds.
- **file** (File) - Optional - A single file to upload.
- **files** (List[File]) - Optional - A list of files to upload.
- **nonce** (int) - Optional - The nonce for the message.
- **delete_after** (float) - Optional - Seconds to wait before deleting the message.
- **allowed_mentions** (AllowedMentions) - Optional - Controls mention processing.
- **reference** (Message/MessageReference) - Optional - Reference to a message to reply to.
- **mention_author** (bool) - Optional - Overrides reply mention behavior.
- **view** (View) - Optional - Discord UI View.
- **stickers** (Sequence) - Optional - List of up to 3 stickers.
- **suppress_embeds** (bool) - Optional - Whether to suppress embeds.
- **silent** (bool) - Optional - Whether to suppress notifications.
- **poll** (Poll) - Optional - A poll to send.
```

--------------------------------

### async with typing()

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Sends a typing indicator to the destination. In interaction-based contexts, this acts as a defer call.

```APIDOC
## async with typing(ephemeral=False)

### Description
Returns an asynchronous context manager that allows you to send a typing indicator to the destination for an indefinite period of time, or 10 seconds if the context manager is called using await.

### Parameters
#### Request Body
- **ephemeral** (bool) - Optional - Whether the typing indicator is ephemeral (interaction-based contexts only).

### Request Example
```python
async with context.typing():
    await asyncio.sleep(20)
```
```

--------------------------------

### discord.Guild.widget

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Accesses the guild widget information.

```APIDOC
## discord.Guild.widget

### Description
Retrieves the widget information for a guild, including enabled status and channel settings.

### Attributes
- **widget_enabled** (bool) - Whether the guild widget is enabled.
- **widget_channel** (discord.WidgetChannel) - The channel associated with the guild widget.
```

--------------------------------

### Persistent Views

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Manages persistent UI views across bot restarts.

```APIDOC
## Persistent Views

### Description
Manages persistent UI views.

### Attributes
*   **discord.Client.persistent_views**: A collection of persistent views for the client.
*   **commands.Bot.persistent_views**: A collection of persistent views for the bot.
```

--------------------------------

### Command Choices with Enum Annotation

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Using an `enum.Enum` is another ergonomic way to define command choices. This approach is useful for more complex or structured choice sets.

```python
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

### PartialInviteGuild

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents a partial guild associated with an invite.

```APIDOC
### PartialInviteGuild

Represents a “partial” invite guild. This model will be given when the user is not part of the guild the `Invite` resolves to.

#### Attributes
* **banner** - Guild banner asset.
* **created_at** (`datetime.datetime`) - The guild’s creation time in UTC.
* **description** (`Optional[str]`) - The partial guild’s description.
* **features** (`List[str]`) - A list of features the guild has.
* **icon** (`Optional[Asset]`) - The guild’s icon asset.
* **id** (`int`) - The partial guild’s ID.
* **name** (`str`) - The partial guild’s name.
* **nsfw_level** (`NSFWLevel`) - The partial guild’s NSFW level.
* **premium_subscription_count** (`int`) - The number of “boosts” the partial guild currently has.
* **splash** (`Optional[Asset]`) - The guild’s invite splash asset.
* **vanity_url** (`Optional[str]`) - The Discord vanity invite URL for this partial guild, if available.
* **vanity_url_code** (`Optional[str]`) - The partial guild’s vanity URL code, if available.
* **verification_level** (`VerificationLevel`) - The partial guild’s verification level.

#### Methods
* **x == y**: Checks if two partial guilds are the same.
* **x != y**: Checks if two partial guilds are not the same.
* **hash(x)**: Return the partial guild’s hash.
* **str(x)**: Returns the partial guild’s name.
```

--------------------------------

### Allowed Contexts Command

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

The `allowed_contexts()` decorator specifies the valid contexts (guilds, DMs, private channels) in which a command can be used.

```APIDOC
## @discord.app_commands.allowed_contexts()

### Description
A decorator that indicates this command can only be used in certain contexts. Valid contexts are guilds, DMs and private channels. This is not implemented as a `check()`, and is instead verified by Discord server side. Due to a Discord limitation, this decorator does nothing in subcommands and is ignored. New in version 2.4.

### Method
APPLY DECORATOR

### Endpoint
N/A (Decorator)

### Parameters
#### Query Parameters
- **guilds** (boolean) - Whether the command is allowed in guilds.
- **dms** (boolean) - Whether the command is allowed in DMs.
- **private_channels** (boolean) - Whether the command is allowed in private channels.

### Request Example
```python
@app_commands.command()
@app_commands.allowed_contexts(guilds=True, dms=False, private_channels=True)
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am only available in guilds and private channels!')
```

### Response
N/A (Decorator)
```

--------------------------------

### Fetch Discord Template

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Retrieves a `Template` object from a Discord invite code or URL. Requires the template to be valid and accessible.

```python
await _fetch_template(_code_)
```

--------------------------------

### Member Avatar URL Replacement

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of Member.avatar_url with Member.avatar.

```python
Member.avatar
```

--------------------------------

### Permissions Factory Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Factory methods to create Permissions objects with predefined sets of permissions based on the official Discord UI categories.

```APIDOC
## Permissions Factory Methods

### Description
These class methods create a `Permissions` object with specific sets of permissions enabled.

### Methods
- `_general()`: Creates a Permissions object with all "General" permissions.
- `_membership()`: Creates a Permissions object with all "Membership" permissions.
- `_text()`: Creates a Permissions object with all "Text" permissions.
- `_voice()`: Creates a Permissions object with all "Voice" permissions.
- `_stage()`: Creates a Permissions object with all "Stage Channel" permissions.
- `_stage_moderator()`: Creates a Permissions object with all permissions for stage moderators.
- `_elevated()`: Creates a Permissions object with all permissions that require 2FA.
- `_apps()`: Creates a Permissions object with all "Apps" permissions.
- `_events()`: Creates a Permissions object with all "Events" permissions.
- `_advanced()`: Creates a Permissions object with all "Advanced" permissions.
```

--------------------------------

### AppCommandPermissions

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents the permissions for an application command.

```APIDOC
## AppCommandPermissions

### Description
Represents the permissions for an application command.
New in version 2.0.

### Attributes
- **guild** (`Guild`) - The guild associated with this permission.
- **id** (`int`) - The ID of the permission target, such as a role, channel, or guild. The special `guild_id - 1` sentinel is used to represent “all channels”.
- **target** (Any) - The role, user, or channel associated with this permission. This could also be the `AllChannels` sentinel type. Falls back to `Object` if the target could not be found in the cache.
- **type** (`AppCommandPermissionType`) - The type of permission.
- **permission** (`bool`) - The permission value. `True` for allow, `False` for deny.
```

--------------------------------

### AllChannels Data Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents all channels for application command permissions.

```APIDOC
## AllChannels

### Description
Represents all channels for application command permissions. New in version 2.0.

### Attributes
- **guild** (Guild) - The guild the application command permission is for.
- **id** (int) - The ID sentinel used to represent all channels.
```

--------------------------------

### Handling check failures

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Demonstrates catching CheckFailure exceptions in a command error handler.

```python
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

### PartialEmoji URL as String Type

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Notes that PartialEmoji.url is now a string, and PartialEmoji.url_as has been removed.

```python
PartialEmoji.url
```

--------------------------------

### Configure allowed command contexts

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Use this decorator to explicitly define which contexts (guilds, DMs, private channels) a command can be used in.

```python
@app_commands.command()
@app_commands.allowed_contexts(guilds=True, dms=False, private_channels=True)
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am only available in guilds and private channels!')
```

--------------------------------

### POST /create_thread

Source: https://discordpy.readthedocs.io/en/latest/api.html

Creates a new public thread in a forum channel with an initial message.

```APIDOC
## POST /create_thread

### Description
Creates a thread in a forum channel. Requires `send_messages` permission. At least one of `content`, `embed`, `embeds`, `file`, `files`, or `view` must be provided.

### Parameters
#### Request Body
- **name** (str) - Required - The name of the thread.
- **auto_archive_duration** (int) - Optional - Duration in minutes (60, 1440, 4320, 10080).
- **slowmode_delay** (int) - Optional - Slowmode rate limit in seconds.
- **content** (str) - Optional - Message content.
- **tts** (bool) - Optional - Whether to use text-to-speech.
- **embed** (Embed) - Optional - Rich embed.
- **embeds** (List[Embed]) - Optional - List of embeds (max 10).
- **file** (File) - Optional - File to upload.
- **files** (List[File]) - Optional - List of files (max 10).
- **allowed_mentions** (AllowedMentions) - Optional - Mentions processing.
- **mention_author** (bool) - Optional - Override replied_user attribute.
- **applied_tags** (List[discord.ForumTag]) - Optional - Tags to apply.
- **view** (Union[discord.ui.View, discord.ui.LayoutView]) - Optional - UI View.
- **stickers** (Sequence) - Optional - Stickers to upload (max 3).
- **suppress_embeds** (bool) - Optional - Whether to suppress embeds.
- **silent** (bool) - Optional - Whether to suppress notifications.
- **reason** (str) - Optional - Audit log reason.

### Response
#### Success Response (200)
- **thread** (Thread) - The created thread.
- **message** (Message) - The initial message.
```

--------------------------------

### ForumChannel Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods available for a ForumChannel object.

```APIDOC
## ForumChannel Methods

### Description
Methods available for a ForumChannel object.

### Methods
- **archived_threads(type: ThreadArchiveDuration, limit: int = 100, before: Snowflake = None)** - Fetches archived threads.
- **clone()** - Creates a copy of the channel.
- **create_invite(max_age: int = 86400, max_uses: int = 0, unique: bool = False, reason: Optional[str] = None)** - Creates an invite to the channel.
- **create_tag(name: str, emoji: Optional[Union[str, PartialEmoji]] = None, moderated: bool = False)** - Creates a new tag for the forum.
- **create_thread(name: str, content: Optional[str] = None, *, auto_archive_duration: Union[int, ThreadArchiveDuration] = MISSING, slowmode_delay: Optional[int] = None, reason: Optional[str] = None, suppress_embeds: bool = False, files: Optional[List[File]] = None, attachments: Optional[List[Attachment]] = None, embed: Optional[Embed] = None, view_only: bool = False, rate_limit_per_user: Optional[int] = None)** - Creates a new thread in the forum.
- **create_webhook(name: str, avatar: Optional[bytes] = None, reason: Optional[str] = None)** - Creates a webhook for the channel.
- **delete(reason: Optional[str] = None)** - Deletes the channel.
- **edit(name: Optional[str] = None, position: Optional[int] = None, topic: Optional[str] = None, nsfw: Optional[bool] = None, default_auto_archive_duration: Optional[Union[int, ThreadArchiveDuration]] = None, default_thread_slowmode_delay: Optional[int] = None, default_reaction_emoji: Optional[Union[str, PartialEmoji]] = None, default_layout: Optional[ForumLayoutType] = None, default_sort_order: Optional[ForumOrderType] = None, reason: Optional[str] = None)** - Edits the channel.
- **get_tag(tag_id: int)** - Retrieves a tag by its ID.
- **get_thread(thread_id: int)** - Retrieves a thread by its ID.
- **invites()** - Returns a list of invites to the channel.
- **is_media()** - Checks if the channel is a media channel.
- **is_nsfw()** - Checks if the channel is NSFW.
- **move(category: Optional[CategoryChannel] = None, sibling: Optional[BaseChannel] = None, offset: int = 0, reason: Optional[str] = None)** - Moves the channel to a new position or category.
- **overwrites_for(obj: Union[Member, Role])** - Gets permission overwrites for a member or role.
- **permissions_for(obj: Union[Member, Role])** - Resolves permissions for a member or role.
- **set_permissions(target: Union[Member, Role], allow: int = 0, deny: int = 0, reason: Optional[str] = None)** - Sets permissions for a member or role.
- **webhooks()** - Returns a list of webhooks for the channel.
```

--------------------------------

### Walk Cog Commands

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html

Use walk_commands to retrieve all commands including subcommands recursively.

```python
>>> print([c.qualified_name for c in cog.walk_commands()])
```

--------------------------------

### POST /channels/clone

Source: https://discordpy.readthedocs.io/en/latest/api.html

Clones a channel, creating a new one with the same properties.

```APIDOC
## POST /channels/clone

### Description
Clones this channel. This creates a channel with the same properties as this channel. Requires `manage_channels` permission.

### Parameters
#### Request Body
- **name** (str) - Optional - The name of the new channel.
- **category** (CategoryChannel) - Optional - The category the new channel belongs to.
- **reason** (str) - Optional - The reason for cloning this channel.

### Response
#### Success Response (200)
- **channel** (abc.GuildChannel) - The channel that was created.
```

--------------------------------

### @client.event

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Registers a coroutine as an event listener.

```APIDOC
## @client.event

### Description
A decorator that registers an event to listen to. The function must be a coroutine.

### Parameters
- **coro** (coroutine) - Required - The coroutine to register.

### Request Example
```python
@client.event
async def on_ready():
    print('Ready!')
```

### Response
- **Raises** (TypeError) - Raised if the passed function is not a coroutine.
```

--------------------------------

### discord.TeamMember Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods available for a TeamMember object.

```APIDOC
## TeamMember Methods

### `mentioned_in(message)`

Checks if the user is mentioned in the specified message.

Parameters:
  * **message** (`Message`) - The message to check if you’re mentioned in.

Returns:
  Indicates if the user is mentioned in the message.
Return type:
  `bool`
```

--------------------------------

### Upload command with multiple attachments

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Processes multiple attachments where the second one is optional.

```python
import typing
import discord

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

### Exception Handling Settings

Source: https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html

Methods to configure which exceptions are handled by the task's reconnect logic.

```APIDOC
## Exception Handling Settings

### add_exception_type(*exceptions)

### Description
Adds exception types to be handled during the reconnect logic. By default, the exception types handled are those handled by `discord.Client.connect()`, which includes a lot of internet disconnection errors. This function is useful if you’re interacting with a 3rd party library that raises its own set of exceptions.

### Parameters
- **exceptions** (Type[BaseException]) - An argument list of exception classes to handle.

### Raises
- **TypeError** - An exception passed is either not a class or not inherited from `BaseException`.

### clear_exception_types()

### Description
Removes all exception types that are handled. Note: This operation obviously cannot be undone!

### remove_exception_type(*exceptions)

### Parameters
- **exceptions** (Type[BaseException]) - An argument list of exception classes to handle.

### Returns
- bool - Whether all exceptions were successfully removed.
```

--------------------------------

### LayoutView Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents a layout view for components. This object must be inherited to create a UI within Discord. It supports all component types and uses v2 components.

```APIDOC
## discord.ui.LayoutView

### Description
Represents a layout view for components. This object must be inherited to create a UI within Discord. This differs from a `View` in that it supports all component types and uses what Discord refers to as “v2 components”.

### Parameters
- **timeout** (Optional[float]) - Timeout in seconds from last interaction with the UI before no longer accepting input. If `None` then there is no timeout.

### Attributes
- **children** (List[Item]) - The list of children attached to this view.
- **timeout** (float) - Timeout in seconds from last interaction with the UI before no longer accepting input.
- **total_children_count** (int) - The total number of children in the view.
```

--------------------------------

### Locale and Choices

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Details on locale settings, specifically Chinese, and the use of choices for command arguments and parameters.

```APIDOC
## Locale and Choices

### Description
This section covers locale information, including Chinese language support, and the definition and usage of choices for command arguments.

### Locale
- `discord.Locale.chinese`

### Choices
- `discord.app_commands.Choice`
- `discord.app_commands.TranslationContextLocation.choice_name`
- `discord.app_commands.Argument.choices`
- `discord.app_commands.Parameter.choices`
- `discord.app_commands.Transformer.choices`
- `discord.app_commands.choices()`
```

--------------------------------

### Audio Source

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Represents an audio source for playback.

```APIDOC
## discord.AudioSource

### Description
Abstract base class for audio sources.

### Endpoint
N/A (Class)
```

--------------------------------

### Create a Command Group with @group

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

A shortcut decorator that invokes group() and adds it to the internal command list via add_command(). It converts the provided method into a Group and adds it to the bot.

```python
@group(_* args_, _** kwargs_)

```

--------------------------------

### Replacing Guild Icon URL Method

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Illustrates the replacement of Guild.icon_url_as with the Asset object's replace method for handling icon formats.

```python
guild.icon.replace
```

--------------------------------

### Define a command with consume-rest behavior

Source: https://discordpy.readthedocs.io/en/latest/faq.html

Uses the asterisk operator to capture all remaining input as a single argument, avoiding the need for quotes.

```python
@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)
```

--------------------------------

### Custom asynchronous converter with Converter interface

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

Implement a custom asynchronous converter by inheriting from `commands.Converter` and overriding the `convert` method. This allows access to the context and asynchronous operations.

```python
import random
from discord.ext import commands

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f'{ctx.author} slapped {to_slap} because *{argument}*'

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

```

--------------------------------

### Save Asset to File-like Object

Source: https://discordpy.readthedocs.io/en/latest/api.html

Saves an asset to a file-like object or a specified filename. Raises DiscordException if there's no internal connection state, HTTPException for download failures, or NotFound if the asset was deleted.

```python
_await _save(_fp_ , _*_ , _seek_begin =True_)
```

--------------------------------

### LayoutView Class Methods

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Methods available for the LayoutView class, including creating views from messages, adding/removing items, and handling interactions.

```APIDOC
## LayoutView Class Methods

### `classmethod from_message(message, /, *, timeout=180.0)`

#### Description
Converts a message’s components into a `View` or `LayoutView`. If the message has any v2 components, then you must use `LayoutView` in order for them to be converted into their respective items. `View` does not support v2 components.

#### Parameters
- **message** (discord.Message) - The message with components to convert into a view.
- **timeout** (Optional[float]) - The timeout of the converted view.

#### Returns
- Union[View, LayoutView] - The converted view. This will always return one of `View` or `LayoutView`, and not one of its subclasses.

### `add_item(item)`

#### Description
Adds an item to the view. This function returns the class instance to allow for fluent-style chaining.

#### Parameters
- **item** (Item) - The item to add to the view.

#### Raises
- TypeError - An `Item` was not passed.
- ValueError - Maximum number of children has been exceeded, the row the item is trying to be added to is full or the item you tried to add is not allowed in this View.

### `clear_items()`

#### Description
Removes all items from the view. This function returns the class instance to allow for fluent-style chaining.

### `content_length()`

#### Description
Returns the total length of all text content in the view’s items. A view is allowed to have a maximum of 4000 display characters across all its items.

#### Returns
- int - The total length of all text content in the view’s items.

### `find_item(id, /)`

#### Description
Gets an item with `Item.id` set as `id`, or `None` if not found. This is not the same as `custom_id`.

#### Parameters
- **id** (int) - The ID of the component.

#### Returns
- Optional[Item] - The item found, or `None`.

### `interaction_check(interaction, /)`

#### Description
A callback that is called when an interaction happens within the view that checks whether the view should process item callbacks for the interaction. This is useful to override if, for example, you want to ensure that the interaction author is a given user. The default implementation of this returns `True`.

#### Parameters
- **interaction** (Interaction) - The interaction that occurred.

#### Returns
- bool - Whether the view children’s callbacks should be called.

### `is_dispatching()`

#### Description
Checks if the view has been added for dispatching purposes.

#### Returns
- bool - True if the view is dispatching, False otherwise.

### `is_finished()`

#### Description
Checks if the view has finished interacting.

#### Returns
- bool - True if the view is finished, False otherwise.

### `is_persistent()`

#### Description
Checks if the view is set up as persistent. A persistent view has all their components with a set `custom_id` and a `timeout` set to `None`.

#### Returns
- bool - True if the view is persistent, False otherwise.

### `on_error(interaction, error, item, /)`

#### Description
A callback that is called when an item’s callback or `interaction_check()` fails with an error. The default implementation logs to the library logger.

#### Parameters
- **interaction** (Interaction) - The interaction that led to the failure.
- **error** (Exception) - The exception that was raised.
- **item** (Item) - The item that failed the dispatch.

### `on_timeout()`

#### Description
A callback that is called when a view’s timeout elapses without being explicitly stopped.

### `remove_item(item)`

#### Description
Removes an item from the view. This function returns the class instance to allow for fluent-style chaining.

#### Parameters
- **item** (Item) - The item to remove from the view.

### `stop()`

#### Description
Stops listening to interaction events from this view. This operation cannot be undone.
```

--------------------------------

### Bot Properties

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Accessors for various bot configurations and states.

```APIDOC
## Bot Properties

### `_property _activity`

#### Description
The activity being used upon logging in.

#### Type
Optional[`BaseActivity`]

### `_property _allowed_mentions`

#### Description
The allowed mention configuration.

#### Type
Optional[`AllowedMentions`]

### `_property _application`

#### Description
The client’s application info. This is retrieved on `login()` and is not updated afterwards.

#### Type
Optional[`ApplicationInfo`]
```

--------------------------------

### Send Sound

Source: https://discordpy.readthedocs.io/en/latest/api.html

Sends a soundboard sound to a voice channel. Requires 'speak' and 'use_soundboard' permissions. 'use_external_sounds' is needed for sounds from different guilds.

```APIDOC
## _await _send_sound(_sound_ , _/_) 

### Description
Sends a soundboard sound for this channel. You must have `speak` and `use_soundboard` to do this. Additionally, you must have `use_external_sounds` if the sound is from a different guild.

### Parameters
- **sound** (Union[`SoundboardSound`, `SoundboardDefaultSound`]) – The sound to send for this channel.

### Raises
- **Forbidden** – You do not have permissions to send a sound for this channel.
- **HTTPException** – Sending the sound failed.
```

--------------------------------

### discord.ui.Thumbnail

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents a UI Thumbnail. This currently can only be used as a `Section`’s accessory.

```APIDOC
## discord.ui.Thumbnail

### Description
Represents a UI Thumbnail. This currently can only be used as a `Section`’s accessory.

### Parameters
#### Parameters
- **media** (Union[str, discord.File, discord.UnfurledMediaItem]) - The media of the thumbnail. This can be a URL or a reference to an attachment that matches the `attachment://filename.extension` structure.
- **description** (Optional[str]) - The description of this thumbnail. Up to 256 characters.
- **spoiler** (bool) - Whether to flag this thumbnail as a spoiler.
- **id** (Optional[int]) - The ID of this component. This must be unique across the view.

### Attributes
- **id** (Optional[int]) - The ID of this component.
- **media** (discord.UnfurledMediaItem) - This thumbnail unfurled media data.
- **parent** (Optional[Item]) - This item’s parent, if applicable. Only available on items with children.
- **view** (Optional[Union[View, LayoutView]]) - The underlying view for this item.
```

--------------------------------

### HybridGroup can_run Method

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Documentation for the `can_run` asynchronous method of the HybridGroup class, which checks if a command can be executed.

```APIDOC
### HybridGroup Methods

#### can_run

_await_ can_run(_ctx_ , _/_)

This function is a _coroutine_.
Checks if the command can be executed by checking all the predicates inside the `checks` attribute. This also checks whether the command is disabled.

**Parameters**

- **ctx** - The invocation context.

*Changed in version 1.3: Checks whether the command is disabled or not*
*Changed in version 2.0: `ctx` parameter is now positional-only.*
```

--------------------------------

### Migrate AsyncIterator.get() to discord.utils.get()

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Use discord.utils.get() for fetching a single item from an asynchronous iterator, similar to how it was used with AsyncIterator.get().

```Python
# before
msg = await channel.history().get(author__name='Dave')
```

```Python
# after
msg = await discord.utils.get(channel.history(), author__name='Dave')
```

--------------------------------

### Send a typing indicator for 10 seconds

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Use `async with` to send a typing indicator for a specified duration. This functionality was added in version 2.0.

```python
await channel.send('Done!')
```

--------------------------------

### Intents Configuration

Source: https://discordpy.readthedocs.io/en/latest/api.html

Configuration settings for enabling or disabling specific event categories in discord.py.

```APIDOC
## Intent Configuration Fields

### Description
These boolean fields control the reception of specific events. Enabling these allows the bot to receive corresponding gateway events and cache relevant data.

### Parameters
#### Request Body
- **guild_reactions** (bool) - Optional - Enables reaction events for guilds.
- **dm_reactions** (bool) - Optional - Enables reaction events for DMs.
- **typing** (bool) - Optional - Enables typing events for both guilds and DMs.
- **guild_typing** (bool) - Optional - Enables typing events for guilds.
- **dm_typing** (bool) - Optional - Enables typing events for DMs.
- **message_content** (bool) - Optional - Enables access to message content, attachments, and embeds.
- **guild_scheduled_events** (bool) - Optional - Enables scheduled event related events.
- **auto_moderation** (bool) - Optional - Enables auto moderation configuration and execution events.
- **auto_moderation_configuration** (bool) - Optional - Enables auto moderation rule events.
- **auto_moderation_execution** (bool) - Optional - Enables auto moderation action events.
- **polls** (bool) - Optional - Enables poll vote events for both guilds and DMs.
- **guild_polls** (bool) - Optional - Enables poll vote events for guilds.
```

--------------------------------

### Event Reference for Commands Extension

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Details custom events provided by the commands extension for monitoring command lifecycle.

```APIDOC
## Event Reference

### `on_command_error(ctx, error)`

An error handler called when an error occurs during command invocation.

**Parameters**
- **ctx** (`Context`) – The invocation context.
- **error** (`CommandError` derived) – The error that was raised.

### `on_command(ctx)`

An event called when a command is found and is about to be invoked.

**Parameters**
- **ctx** (`Context`) – The invocation context.

### `on_command_completion(ctx)`

An event called when a command has successfully completed its invocation.

**Parameters**
- **ctx** (`Context`) – The invocation context.
```

--------------------------------

### State and Status Checking

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Utility methods to check the state of various objects like connections, permissions, and flags.

```APIDOC
## State Checking Methods

### Description
Methods used to verify the current status or properties of objects such as connections, roles, and messages.

### Methods
- `discord.Client.is_closed()`
- `discord.VoiceClient.is_connected()`
- `discord.Role.is_assignable()`
- `discord.Interaction.is_expired()`
- `discord.TextChannel.is_nsfw()`
```

--------------------------------

### Subscription Class

Source: https://discordpy.readthedocs.io/en/latest/api.html

Represents a user subscription in Discord.

```APIDOC
## Subscription

### Description
Represents a Discord subscription.

### Attributes
- **id** (int) - The subscription’s ID.
- **user_id** (int) - The ID of the user that is subscribed.
- **sku_ids** (List[int]) - The IDs of the SKUs that the user subscribed to.
- **entitlement_ids** (List[int]) - The IDs of the entitlements granted for this subscription.
- **current_period_start** (datetime.datetime) - When the current billing period started.
- **current_period_end** (datetime.datetime) - When the current billing period ends.
- **status** (SubscriptionStatus) - The status of the subscription.
- **canceled_at** (Optional[datetime.datetime]) - When the subscription was canceled.
```

--------------------------------

### Method: edit

Source: https://discordpy.readthedocs.io/en/latest/api.html

Edits the application info using an asynchronous coroutine.

```APIDOC
## Await edit(reason=..., custom_install_url=..., description=..., role_connections_verification_url=..., install_params_scopes=..., install_params_permissions=..., flags=..., icon=..., cover_image=..., interactions_endpoint_url=..., tags=..., guild_install_scopes=..., guild_install_permissions=..., user_install_scopes=..., user_install_permissions=...)

### Description
This function is a coroutine that edits the application info.

### Method
ASYNC COROUTINE

### Parameters
- **reason** (str) - Optional - The reason for the edit.
- **custom_install_url** (str) - Optional - The custom authorization URL for the application.
- **description** (str) - Optional - The application description.
- **role_connections_verification_url** (str) - Optional - The application's connection verification URL.
- **install_params_scopes** (List[str]) - Optional - The scopes for custom authorization.
- **install_params_permissions** (Permissions) - Optional - The permissions for custom authorization.
- **flags** (ApplicationFlags) - Optional - The application's flags.
- **icon** (bytes) - Optional - The application's icon asset.
- **cover_image** (bytes) - Optional - The cover image on a store embed.
- **interactions_endpoint_url** (str) - Optional - The interactions endpoint URL.
- **tags** (List[str]) - Optional - The list of tags describing the functionality.
- **guild_install_scopes** (List[str]) - Optional - Scopes for guild installation.
- **guild_install_permissions** (Permissions) - Optional - Permissions for guild installation.
- **user_install_scopes** (List[str]) - Optional - Scopes for user installation.
- **user_install_permissions** (Permissions) - Optional - Permissions for user installation.
```

--------------------------------

### POST /send

Source: https://discordpy.readthedocs.io/en/latest/api.html

Sends a message to the channel with optional content, embeds, and files.

```APIDOC
## POST /send

### Description
Sends a message to the destination with the content given.

### Parameters
#### Request Body
- **content** (str) - Optional - The content of the message.
- **tts** (bool) - Optional - Indicates if the message should be sent using text-to-speech.
- **embed** (Embed) - Optional - The rich embed for the content.
- **embeds** (List[Embed]) - Optional - A list of embeds to upload (max 10).
- **file** (File) - Optional - The file to upload.
- **files** (List[File]) - Optional - A list of files to upload (max 10).
- **nonce** (int) - Optional - The nonce to use for sending this message.
```

--------------------------------

### discord.ui.ChannelSelect Class

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Represents a UI select menu with a list of predefined options containing the current channels in the guild.

```APIDOC
## discord.ui.ChannelSelect

### Description
Represents a UI select menu with a list of predefined options with the current channels in the guild. Note that if used in a private message, no channels will be displayed.

### Parameters
- **custom_id** (str) - Optional - The ID of the select menu received during an interaction (max 100 chars).
- **channel_types** (List[ChannelType]) - Optional - The types of channels to show in the select menu.
- **placeholder** (Optional[str]) - Optional - The placeholder text shown if nothing is selected (max 150 chars).
- **min_values** (int) - Optional - The minimum number of items that must be chosen (0-25, default 1).
- **max_values** (int) - Optional - The maximum number of items that must be chosen (1-25, default 1).
- **disabled** (bool) - Optional - Whether the select is disabled.
- **required** (bool) - Optional - Whether the select is required (only for modals).
- **default_values** (Sequence[Snowflake]) - Optional - A list of objects representing channels selected by default.
- **row** (Optional[int]) - Optional - The relative row this select menu belongs to (0-4).
- **id** (Optional[int]) - Optional - The unique ID of the component.

### Methods
- **callback(interaction)**: The coroutine triggered when the UI item is interacted with.
- **interaction_check(interaction)**: A coroutine that checks if the callback should be processed.
```

--------------------------------

### Template Methods

Source: https://discordpy.readthedocs.io/en/latest/api.html

Methods available for interacting with and managing Discord templates.

```APIDOC
## Template Methods

### Description
Provides methods to create, edit, delete, and synchronize Discord templates.

### Methods

#### `async create_guild(name: str, icon: bytes = None) -> Guild`

Creates a `Guild` using the template.

**Parameters**
- **name** (str) - The name of the guild.
- **icon** (bytes) - The bytes-like object representing the icon. See `ClientUser.edit()` for more details on what is expected.

**Raises**
- **HTTPException** - Guild creation failed.
- **ValueError** - Invalid icon image format given. Must be PNG or JPG.

**Returns**
- The guild created. This is not the same guild that is added to cache.

**Note**: Bot accounts in more than 10 guilds are not allowed to create guilds. Changed in version 2.0: The `region` parameter has been removed. Changed in version 2.0: This function will now raise `ValueError` instead of `InvalidArgument`. Deprecated since version 2.6: This function is deprecated and will be removed in a future version.

#### `async sync() -> Template`

Sync the template to the guild’s current state.

**Raises**
- **HTTPException** - Editing the template failed.
- **Forbidden** - You don’t have permissions to edit the template.
- **NotFound** - This template does not exist.

**Returns**
- The newly edited template.

**Note**: You must have `manage_guild` in the source guild to do this. New in version 1.7. Changed in version 2.0: The template is no longer edited in-place, instead it is returned.

#### `async edit(name: str = None, description: str = None) -> Template`

Edit the template metadata.

**Parameters**
- **name** (str) - The template’s new name.
- **description** (Optional[str]) - The template’s new description.

**Raises**
- **HTTPException** - Editing the template failed.
- **Forbidden** - You don’t have permissions to edit the template.
- **NotFound** - This template does not exist.

**Returns**
- The newly edited template.

**Note**: You must have `manage_guild` in the source guild to do this. New in version 1.7. Changed in version 2.0: The template is no longer edited in-place, instead it is returned.

#### `async delete()`

Delete the template.

**Raises**
- **HTTPException** - Editing the template failed.
- **Forbidden** - You don’t have permissions to edit the template.
- **NotFound** - This template does not exist.

**Note**: You must have `manage_guild` in the source guild to do this. New in version 1.7.

#### `url` (property)

The template url.

**Type**
`str`
New in version 2.0.
```

--------------------------------

### Set channel permissions using PermissionOverwrite

Source: https://discordpy.readthedocs.io/en/latest/api.html

Applies a pre-configured PermissionOverwrite object to a target.

```python
overwrite = discord.PermissionOverwrite()
overwrite.send_messages = False
overwrite.read_messages = True
await channel.set_permissions(member, overwrite=overwrite)
```

--------------------------------

### Group Methods

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Methods for managing commands within a Group.

```APIDOC
## Group Methods

### add_command

Adds a command or group to this group’s internal list of commands.

Parameters:
  * **command** (Union[`Command`, `Group`]) – The command or group to add.
  * **override** (`bool`) – Whether to override a pre-existing command or group with the same name. If `False` then an exception is raised.

Raises:
  * **CommandAlreadyRegistered** – The command or group is already registered. Note that the `CommandAlreadyRegistered.guild_id` attribute will always be `None` in this case.
  * **ValueError** – There are too many commands already registered or the group is too deeply nested.
  * **TypeError** – The wrong command type was passed.

### remove_command

Removes a command or group from the internal list of commands.

Parameters:
  * **name** (`str`) – The name of the command or group to remove.

Returns:
  The command that was removed. If nothing was removed then `None` is returned instead.

Return type: Optional[Union[`Command`, `Group`]]

### get_command

Retrieves a command or group from its name.

Parameters:
  * **name** (`str`) – The name of the command or group to retrieve.

Returns:
  The command or group that was retrieved. If nothing was found then `None` is returned instead.

Return type: Optional[Union[`Command`, `Group`]]
```

--------------------------------

### User Avatars and Decorations

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Information on retrieving user avatars and avatar decorations.

```APIDOC
## discord.abc.User.avatar

### Description
Represents the avatar URL of a user.

### Endpoint
N/A (Attribute of an object)

## discord.AuditLogDiff.avatar

### Description
Represents the change in a user's avatar in the audit log.

### Endpoint
N/A (Attribute of an object)

## discord.ClientUser.avatar

### Description
Represents the avatar URL of the client user.

### Endpoint
N/A (Attribute of an object)

## discord.Member.avatar

### Description
Represents the avatar URL of a guild member.

### Endpoint
N/A (Attribute of an object)

## discord.SyncWebhook.avatar

### Description
Represents the avatar URL of a synchronized webhook.

### Endpoint
N/A (Attribute of an object)

## discord.TeamMember.avatar

### Description
Represents the avatar URL of a team member.

### Endpoint
N/A (Attribute of an object)

## discord.User.avatar

### Description
Represents the avatar URL of a user.

### Endpoint
N/A (Attribute of an object)

## discord.Webhook.avatar

### Description
Represents the avatar URL of a webhook.

### Endpoint
N/A (Attribute of an object)

## discord.WidgetMember.avatar

### Description
Represents the avatar URL of a widget member.

### Endpoint
N/A (Attribute of an object)

## discord.abc.User.avatar_decoration

### Description
Represents the avatar decoration of a user.

### Endpoint
N/A (Attribute of an object)

## discord.ClientUser.avatar_decoration

### Description
Represents the avatar decoration of the client user.

### Endpoint
N/A (Attribute of an object)

## discord.Member.avatar_decoration

### Description
Represents the avatar decoration of a guild member.

### Endpoint
N/A (Attribute of an object)

## discord.TeamMember.avatar_decoration

### Description
Represents the avatar decoration of a team member.

### Endpoint
N/A (Attribute of an object)

## discord.User.avatar_decoration

### Description
Represents the avatar decoration of a user.

### Endpoint
N/A (Attribute of an object)

## discord.WidgetMember.avatar_decoration

### Description
Represents the avatar decoration of a widget member.

### Endpoint
N/A (Attribute of an object)

## discord.abc.User.avatar_decoration_sku_id

### Description
Represents the SKU ID of a user's avatar decoration.

### Endpoint
N/A (Attribute of an object)

## discord.ClientUser.avatar_decoration_sku_id

### Description
Represents the SKU ID of the client user's avatar decoration.

### Endpoint
N/A (Attribute of an object)

## discord.Member.avatar_decoration_sku_id

### Description
Represents the SKU ID of a guild member's avatar decoration.

### Endpoint
N/A (Attribute of an object)

## discord.TeamMember.avatar_decoration_sku_id

### Description
Represents the SKU ID of a team member's avatar decoration.

### Endpoint
N/A (Attribute of an object)

## discord.User.avatar_decoration_sku_id

### Description
Represents the SKU ID of a user's avatar decoration.

### Endpoint
N/A (Attribute of an object)

## discord.WidgetMember.avatar_decoration_sku_id

### Description
Represents the SKU ID of a widget member's avatar decoration.

### Endpoint
N/A (Attribute of an object)
```

--------------------------------

### Asset Object String Representation

Source: https://discordpy.readthedocs.io/en/latest/migrating.html

Explains that str(Asset) will no longer return an empty string.

```python
str(x)
```

--------------------------------

### Partial Objects

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Represents partial or incomplete versions of Discord objects, often used for efficiency when full object data is not required.

```APIDOC
## Partial Objects

### Description
Represents partial or incomplete versions of Discord objects.

### Classes
*   **discord.PartialAppInfo**: Represents partial application information.
*   **discord.PartialEmoji**: Represents a partial emoji object.
*   **commands.PartialEmojiConversionFailure**: Exception raised when partial emoji conversion fails.
*   **commands.PartialEmojiConverter**: Converter for partial emoji objects.
*   **discord.PartialIntegration**: Represents a partial integration.
*   **discord.PartialInviteChannel**: Represents a partial channel in an invite.
*   **discord.PartialInviteGuild**: Represents a partial guild in an invite.
*   **discord.PartialMessage**: Represents a partial message object.
*   **discord.PartialMessageable**: Represents a partial messageable entity.
*   **commands.PartialMessageConverter**: Converter for partial message objects.
*   **discord.PartialWebhookChannel**: Represents a partial channel in a webhook.
*   **discord.PartialWebhookGuild**: Represents a partial guild in a webhook.
```

--------------------------------

### AppCommand Exceptions

Source: https://discordpy.readthedocs.io/en/latest/interactions/api.html

Exceptions related to application command lifecycle and synchronization errors.

```APIDOC
## Exception: CommandAlreadyRegistered

### Description
Raised when an application command is already registered.

### Parameters
- **name** (str) - The name of the command already registered.
- **guild_id** (Optional[int]) - The guild ID this command was registered at, or None if global.

## Exception: CommandSignatureMismatch

### Description
Raised when an application command from Discord has a different signature from the one provided in the code.

### Parameters
- **command** (Union[Command, ContextMenu, Group]) - The command that had the signature mismatch.

## Exception: CommandNotFound

### Description
Raised when an application command could not be found.

### Parameters
- **name** (str) - The name of the application command not found.
- **parents** (List[str]) - A list of parent command names found prior to the error.
- **type** (AppCommandType) - The type of command that was not found.

## Exception: CommandSyncFailure

### Description
Raised when CommandTree.sync() fails, providing details on the failure.

### Parameters
- **child** (Any) - The child command or object involved in the failure.
- **commands** (Any) - The list of commands involved in the sync failure.
```

--------------------------------

### Query Members with Presences

Source: https://discordpy.readthedocs.io/en/latest/whats_new.html

Use Guild.query_members() with the 'presences' parameter set to True to include presence information when fetching members.

```python
members = await guild.query_members(limit=100, presences=True)
```

--------------------------------

### Check Decorators

Source: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

Decorators for adding global checks to the bot that run before command execution.

```APIDOC
## Check Decorators

### @check

- **Description**: Adds a global check to the bot that runs before any command checks. Applies to all commands. Can be a regular function or a coroutine. Takes a `Context` parameter and can raise `CommandError` exceptions.
- **Example**:
```python
@bot.check
def check_commands(ctx):
    return ctx.command.qualified_name in allowed_commands
```
- **Changed in version**: 2.0: `func` parameter is now positional-only.

### @check_once

- **Description**: Adds a "call once" global check. Called only once per `invoke()` call, even for the default help command. Can be a regular function or a coroutine. Takes a `Context` parameter and can raise `CommandError` exceptions.
- **Note**: May only parse the parent command for group subcommands due to being invoked once per `Bot.invoke()`.
- **Example**:
```python
@bot.check_once
def whitelist(ctx):
    return ctx.message.author.id in my_whitelist
```
- **Changed in version**: 2.0: `func` parameter is now positional-only.
```

--------------------------------

### POST /channels/{channel_id}/clone

Source: https://discordpy.readthedocs.io/en/latest/api.html

Clones an existing forum channel, creating a new channel with the same properties.

```APIDOC
## POST /channels/{channel_id}/clone

### Description
Clones this channel. This creates a channel with the same properties as this channel. Requires `manage_channels` permission.

### Method
POST

### Endpoint
/channels/{channel_id}/clone

### Parameters
#### Request Body
- **name** (str) - Optional - The name of the new channel.
- **category** (CategoryChannel) - Optional - The category the new channel belongs to.
- **reason** (str) - Optional - The reason for cloning this channel for the audit log.

### Response
#### Success Response (200)
- **channel** (abc.GuildChannel) - The channel that was created.
```

--------------------------------

### discord.TextStyle

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Defines the text style for input fields in components.

```APIDOC
## discord.TextStyle

### Description
Defines the text style for input fields.

### Enum Members
*   **paragraph**: Represents a paragraph text style.
```

--------------------------------

### discord.app_commands.Command.parameters

Source: https://discordpy.readthedocs.io/en/latest/genindex.html

Accesses the parameters of an application command.

```APIDOC
## discord.app_commands.Command.parameters

### Description
Accesses the parameters of an application command.
```