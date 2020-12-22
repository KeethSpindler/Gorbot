from discord import Embed

class Embedder():
        def __init__(self):
                self.colors = {
                    'DEFAULT': 0,
                    'AQUA': 1752220,
                    'GREEN': 3066993,
                    'BLUE': 3447003,
                    'PURPLE': 10181046,
                    'GOLD': 15844367,
                    'ORANGE': 15105570,
                    'RED': 15158332,
                    'GREY': 9807270,
                    'DARKER_GREY': 8359053,
                    'NAVY': 3426654,
                    'DARK_AQUA': 1146986,
                    'DARK_GREEN': 2067276,
                    'DARK_BLUE': 2123412,
                    'DARK_PURPLE': 7419530,
                    'DARK_GOLD': 12745742,
                    'DARK_ORANGE': 11027200,
                    'DARK_RED': 10038562,
                    'DARK_GREY': 9936031,
                    'LIGHT_GREY': 12370112,
                    'DARK_NAVY': 2899536,
                    'LUMINOUS_VIVID_PINK': 16580705,
                    'DARK_VIVID_PINK': 12320855
                }

class UserColorEmbedder(Embedder):
    def __init__(self):
        Embedder.__init__(self)
        self.user_colors = {
                    #Brady - Gold
                    178851504076095488: 15844367,
                    #Carlie - Purple
                    323968599687430145: 10181046,
                    #James - Grey
                    191384926321508353: 9807270,
                    #Derick - Blue
                    179051738354024449: 3447003,
                    #Keeth - Red
                    636724139922554893: 15158332,
                    #Rob - Orange
                    209101464944115713: 15105570,
                    #Robbot - Luminous Vivid Pink
                    422470851435298818: 16580705
                }

class DrinkEmbedder(Embedder):

    def __init__(self, drink):
        self.drink = drink
        Embedder.__init__(self)
        embed = Embed(title=self.drink.name, description='A drink for you, good Bud.', color=self.colors.get('DARK_NAVY'))
        self.embed = self.embed_drink(embed)
        
    def embed_drink(self, embed):
        embed.set_image(url=self.drink.img)
        embed.add_field(name="Name", value=self.drink.name)
        embed.add_field(name="Category", value=self.drink.category)
        embed.add_field(name="\u200b", value='\u200b')
        embed.add_field(name="Alcoholic?", value=self.drink.alcoholic)
        embed.add_field(name="Glass Type", value=self.drink.glass)
        embed.add_field(name="\u200b", value='\u200b')
        ingredient_string = ""
        for string in self.drink.ingredients:
            ingredient_string += string + '\n'
        embed.add_field(name="Ingredients", value=self.drink.ingredients, inline=False)
        embed.add_field(name="Instructions", value=self.drink.instructions, inline=False)
        embed.set_footer(text="Have ideas for additional functionality? Throw them in #robbot_discussion!")
        return embed

class PinEmbedder(UserColorEmbedder):
    def __init__(self, pin):
        self.pin = pin
        UserColorEmbedder.__init__(self)
        embed = Embed(title=self.pin.author, description=f'Posted on {self.pin.posted_date}', color=self.user_colors.get(self.pin.id))
        self.embed = self.embed_pin(embed)

    def embed_pin(self, embed):
        pin_embed = embed
        pin_embed.set_thumbnail(url=self.pin.avatar)
        pin_embed.add_field(name="Channel", value=self.pin.channel, inline=False)
        pin_embed.add_field(name="Message", value=f'[{self.pin.content}]({self.pin.url})', inline=False)
        return pin_embed