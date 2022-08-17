import discord as dc


class Dino:
    def __init__(self, title, color, description, variablen_name, picture_url, field_name, field_value):
        self.title = title
        self.color = color
        self.description = description
        self.picture_url = picture_url
        self.field_name = field_name
        self.field_value = field_value
        self.variablen_name = variablen_name

    def embed(self):
        embed = dc.Embed(title=self.title, colour=dc.Colour(self.color),
                         description=self.description)
        embed.set_image(url=self.picture_url)
        embed.add_field(name=self.field_name, value=self.field_value)

        return embed

