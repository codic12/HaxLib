class embeds:
    def create_embed(description="", title="", footer=None)
        embed = {
          "title":title,
          "description":description
          }
        if footer != None:
            temp = {
            "footer":{
              "text":footer
              }
            }
            embed.update(temp)
            del(temp)
          return embed
          