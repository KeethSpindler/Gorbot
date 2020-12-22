'''
@author: Keeth S.
@dependencies: discord, datetime
@desc: Creates a Pin object from the reply message served from robbot.py
@retunrs: async message back to channel confirming message was pinned
# TODO Make JSON file to save colors for users
       Allow users to customize their pin color 
'''
import datetime

class Pin:
    def __init__(self, message, embedder):
        self.author = message.author.display_name
        self.id = message.author.id
        self.avatar = message.author.avatar_url
        self.channel = message.channel.name
        formated_date = datetime.date.strftime(message.created_at, "%m/%d/%Y")
        self.posted_date = formated_date
        self.content = message.content
        self.url = message.jump_url
        self.embed = embedder(self).embed

