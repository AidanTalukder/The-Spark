import discord
from discord.ext import commands

async def getAllMembers(guild, blacklist):
    '''Gets all members' public data on a server. Allows for
    blacklisted list of users
    
    Input: server, blacklisted users
    Output: list of all members'''

    members = [member for member in guild.members if member.id not in blacklist and not member.bot]

    return members

async def getAllUIDs(guild, blacklist):
    '''Gets all UIDs of users on a server. Allows for
    blacklisted list of users'''

    UIDs = [member.id for member in guild.members if member.id not in blacklist and not member.bot]
    print(f"User IDs in this server: {UIDs}")
    return UIDs