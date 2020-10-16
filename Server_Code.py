if message.content == ".서버" or message.content == ".서버정보" or message.content == ".서버 정보" or message.content == ".server":

    i = 0
    guild_emoji = ""
    while len(message.guild.emojis) > i:
        guild_emoji = guild_emoji + " " + str(message.guild.emojis[i])
        i = i + 1

    i = 1
    guild_role = ""
    while len(message.guild.roles) > i:
        guild_role = guild_role + " " + str(message.guild.roles[i].mention)
        i = i + 1

    print(guild_emoji)

    if json_data[userid] == "kr":

        if len(message.guild.roles) < 30 and len(message.guild.emojis) < 30:
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name=message.guild.name + " 서버 정보", value="""

            ⚪ | 서버 이름: {}
            🔖 | 서버 주인: {}

            🔑 | 서버 아이디: {}

            👩 | 서버 멤버: {}명

            🔴 | 서버 부스트 레벨: {} 레벨
            🔴 | 부스트 개수: {}개

            📢 | 규칙 채널: {}
            🛠 | 시스템 채널: {}

            💬 | 텍스트 채널: {}개
            🔊 | 음성 채널: {}개
            """.format(message.guild.name, message.guild.owner.name, message.guild.id, len(message.guild.members), message.guild.premium_tier, message.guild.premium_subscription_count, message.guild.rules_channel, message.guild.system_channel, len(message.guild.text_channels), len(message.guild.voice_channels)), inline=True)
            embed.add_field(name="서버 전용 이모지/역활", value="""
            😀 | 전용 이모지: {}
            😉 | 역활: {}""".format(guild_emoji, guild_role), inline=False)
            embed.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name=message.guild.name + " 서버 정보", value="""

            ⚪ | 서버 이름: {}
            🔖 | 서버 주인: {}

            🔑 | 서버 아이디: {}

            👩 | 서버 멤버: {}명

            🔴 | 서버 부스트 레벨: {} 레벨
            🔴 | 부스트 개수: {}개

            📢 | 규칙 채널: {}
            🛠 | 시스템 채널: {}

            💬 | 텍스트 채널: {}개
            🔊 | 음성 채널: {}개

            서버 전용 이모지 또는 역활이 너무 많아서
            표시할 수 없어요.""".format(message.guild.name, message.guild.owner.name, message.guild.id, len(message.guild.members), message.guild.premium_tier, message.guild.premium_subscription_count, message.guild.rules_channel, message.guild.system_channel, len(message.guild.text_channels), len(message.guild.voice_channels)), inline=True)
            embed.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(embed=embed)

    else:

        if len(message.guild.roles) < 30 and len(message.guild.emojis) < 30:
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name=message.guild.name + " Server Information", value="""

            ⚪ | Server name: {}
            🔖 | Server owner: {}

            🔑 | Server id: {}

            👩 | Server member: {}

            🔴 | Server boost level: {} 
            🔴 | Number of boosts: {}

            📢 | Rule channel: {}
            🛠 | System channel: {}

            💬 | Text channel: {}
            🔊 | Voice channel: {}
            """.format(message.guild.name, message.guild.owner.name, message.guild.id, len(message.guild.members), message.guild.premium_tier, message.guild.premium_subscription_count, message.guild.rules_channel, message.guild.system_channel, len(message.guild.text_channels), len(message.guild.voice_channels)), inline=True)
            embed.add_field(name="Server Role/Emoji", value="""
            😀 | Emoji: {}
            😉 | Role: {}""".format(guild_emoji, guild_role), inline=False)
            embed.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name=message.guild.name + " Server Information", value="""

            ⚪ | Server name: {}
            🔖 | Server owner: {}

            🔑 | Server id: {}

            👩 | Server member: {}

            🔴 | Server boost level: {} 
            🔴 | Number of boosts: {}

            📢 | Rule channel: {}
            🛠 | System channel: {}

            💬 | Text channel: {}
            🔊 | Voice channel: {}

            There are too many server emojis or roles,
            I can't display it.""".format(message.guild.name, message.guild.owner.name, message.guild.id, len(message.guild.members), message.guild.premium_tier, message.guild.premium_subscription_count, message.guild.rules_channel, message.guild.system_channel, len(message.guild.text_channels), len(message.guild.voice_channels)), inline=True)
            embed.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(embed=embed)
