# https://twitchio.dev/en/latest/quickstart.html

# --- LIRARIES ---

from twitchio.ext import commands
from enum import Enum

# --- CODE ---

class Bot(commands.Bot):

    class Mode(Enum):
        normal = 0
        poll = 1

    mode = Mode.normal
    
    usernames = []
    
    poll_values = dict()

    def __init__(self, xdata):
        result = self.get_data(xdata)
        super().__init__(
            token=result[0],
            prefix='?',
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
        
    def start_poll(self):
        self.usernames = []
        self.poll_values = dict()
        self.mode = self.Mode.poll
        
    def stop_poll(self):
        self.mode = self.Mode.normal

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        
        user = str(message.author.name)
        msg = str(message.content)
        
        print(user + " says '" + msg + "'.")
        
        if (self.mode == self.Mode.poll):
            if user not in self.usernames and msg.startswith("!vote"):
                self.usernames.append(message.author.name)
                vote = msg.lower()
                for filter in ["!vote", " ", "-", "_", "/"]:
                    vote = vote.replace(filter, "")
                if vote in self.poll_values.keys():
                    self.poll_values[vote] += 1
                else:
                    self.poll_values[vote] = 1
        
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')