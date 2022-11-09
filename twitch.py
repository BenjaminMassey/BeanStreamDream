# https://twitchio.dev/en/latest/quickstart.html

# --- LIRARIES ---

from twitchio.ext import commands

# --- CODE ---

class Bot(commands.Bot):

    def __init__(self, xdata):
        result = self.get_data(xdata)
        super().__init__(
            token=result[0],
            prefix='!',
            initial_channels=[result[1]]
        )
        
    def get_data(self, xdata):
        oauth_file = open(xdata.oauth_path, 'r')
        oauth = oauth_file.read()
        oauth = xdata.fdecrypt(oauth)
        oauth_file.close()
        chat_file = open(xdata.chat_path, 'r')
        chat = chat_file.read()
        chat_file.close()
        return (oauth, chat)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return

        print(message.content)
        
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')